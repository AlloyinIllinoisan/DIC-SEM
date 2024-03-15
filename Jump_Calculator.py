# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 08:34:17 2024

@author: rlb8
"""

import cv2
import numpy as np
import csv
import glob
import re
import time
import math
import matplotlib.pyplot as plt
import os

tic = time.time()

def find_discontinuities(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Find contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate the bounding box for each contour
    discontinuities = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        discontinuities.append((w, h))

    return discontinuities

def extract_step_numbers(image_path):
    # Extract the last two numbers before the .tif extension
    match = re.search(r'step\d+_(\d+)_(\d+)\.tif$', image_path)
    if match:
        return f"{match.group(1)}_{match.group(2)}"
    else:
        return ""

def plot_histogram(values, title, xlabel, ylabel, save_path=None, save_directory=None):
    plt.hist(values, bins=50, color='blue', edgecolor='black', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if save_path:
        plt.savefig(save_path)
    elif save_directory:
        plt.savefig(f'{save_directory}/{title.replace(" ", "_").lower()}.png')
    else:
        plt.show()
    plt.close()

def calculate_statistics(discontinuities):
    if not discontinuities:
        return 0, 0, 0, 0, 0, 0

    widths, heights = zip(*discontinuities)

    avg_width = np.mean(widths)
    avg_height = np.mean(heights)
    stdev_width = np.std(widths)
    stdev_height = np.std(heights)
    max_width = np.max(widths)
    max_height = np.max(heights)

    return avg_width, avg_height, stdev_width, stdev_height, max_width, max_height

def process_image(image_path, rectangles_list, save_histograms=True, save_directory=None):
    # Read the image
    image = cv2.imread(image_path)

    # Print a message indicating a new image is loaded
    print(f"Processing image: {image_path}")

    all_discontinuities = []

    for x, y, width, height in rectangles_list:
        # Extract the region of interest (ROI) from the image
        roi = image[y:y + height, x:x + width]

        # Find discontinuities in the ROI
        discontinuities = find_discontinuities(roi)

        all_discontinuities.extend(discontinuities)

    # Extract the step numbers from the image path
    step_numbers = extract_step_numbers(image_path)

    # Plot histograms before calculating statistics
    if save_histograms:
        widths, heights = zip(*all_discontinuities)
        plot_histogram(widths, f'Distribution of Widths - {step_numbers}', 'Width', 'Frequency', save_directory=save_directory)
        plot_histogram(heights, f'Distribution of Heights - {step_numbers}', 'Height', 'Frequency', save_directory=save_directory)

    # Calculate statistics for discontinuities across all small rectangles
    avg_width, avg_height, stdev_width, stdev_height, max_width, max_height = calculate_statistics(all_discontinuities)

    # Calculate nearest rounded-up values
    rounded_avg_width = math.ceil(avg_width)
    rounded_avg_height = math.ceil(avg_height)

    # Return a single set of values for each image
    return step_numbers, avg_width, avg_height, stdev_width, stdev_height, max_width, max_height, rounded_avg_width, rounded_avg_height

def save_to_csv(results, csv_filename, mode='a'):
    with open(csv_filename, mode, newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        if mode == 'w':
            csv_writer.writerow(['Step_Numbers', 'Avg_Width', 'Avg_Height', 'Stdev_Width', 'Stdev_Height', 'Max_Width', 'Max_Height', 'Rounded_Avg_Width', 'Rounded_Avg_Height'])

        if results:  # Check if the results list is not empty
            csv_writer.writerow(results)


if __name__ == "__main__":
    directory_path = "I:/DARPA/C001S1A/AlignedImages_step4/"  # Replace with the actual path to your image
    csv_output_path = "I:/DARPA/C001S1A/step4_jump.csv"

    main_rect_x, main_rect_y = 307, 205
    main_rect_width, main_rect_height = 5630, 3686
    small_rect_width, small_rect_height = 35,35

    # Calculate the coordinates of the small rectangles
    rectangles_list = [(x, y, small_rect_width, small_rect_height)
                       for y in range(main_rect_y, main_rect_y + main_rect_height, small_rect_height)
                       for x in range(main_rect_x, main_rect_x + main_rect_width, small_rect_width)]

    # Manually define the step number
    step_number = 4

    histogram_directory = 'I:/DARPA/C001S1A//Histograms'
    if not os.path.exists(histogram_directory):
        os.makedirs(histogram_directory)
    save_to_csv([], csv_output_path, mode='w')

    for image_path in glob.glob(f"{directory_path}/step{step_number}*.tif"):
        toc1 = time.time()
        results = process_image(image_path, rectangles_list, save_directory=histogram_directory)
        save_to_csv(results, csv_output_path)
        toc2 = time.time()
        print(toc2 - toc1, 'seconds elapsed')

toc = time.time()
print(toc - tic, 'seconds elapsed')