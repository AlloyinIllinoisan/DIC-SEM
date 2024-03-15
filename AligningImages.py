import cv2
import numpy as np
import os
import csv
import time
tic = time.time()

Step0_folder = 'G:/FGM_30416_B/step0'
Step1_folder = 'G:/FGM_30416_B/step6'
output_folder = 'I:/Test/Aligned'
csv_file = 'I:/Test/displacements.csv'
non_zero_step = 6

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
roi_x, roi_y, roi_width, roi_height = 2000, 1152, 2136, 1692
# Open CSV file for writing
with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = ['Image Pair', 'X Displacement', 'Y Displacement']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate through each image in the Step0_folder
    for filename in os.listdir(Step0_folder):
        if filename.endswith(".tif"):  # check for TIFF files
            print(f"Processing {filename}...")
            step0_img_path = os.path.join(Step0_folder, filename)
            step1_img_name = f"step{non_zero_step}{filename[5:]}"  # Extract image name and construct Step1 filename
            step1_img_path = os.path.join(Step1_folder, step1_img_name)

            # Check if the image file exists in the Step1 folder
            if not os.path.isfile(step1_img_path):
                print(f"Error: {step1_img_name} not found in Step1 folder.")
                continue  # Skip to the next iteration

            # Load images
            step0_img = cv2.imread(step0_img_path, 0)
            step1_img = cv2.imread(step1_img_path, 0)

            if step0_img is None or step1_img is None:
                print(f"Error: Could not read {filename}.")
                continue  # Skip to the next iteration

            # Extract ROI from the Step1 image
            roi = step1_img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]

            # Template matching to find translation
            res = cv2.matchTemplate(step0_img, roi, cv2.TM_CCOEFF_NORMED)
            _, _, _, max_loc = cv2.minMaxLoc(res)
            dx, dy = max_loc
            print(f"Translation for {filename}: dx={dx}, dy={dy}")

            # Write to CSV file
            writer.writerow({'Image Pair': filename,
                             'X Displacement': dx - roi_x,
                             'Y Displacement': dy - roi_y})

            # Apply translation to the entire Step1 image
            translation_matrix = np.float32([[1, 0, dx - roi_x], [0, 1, dy - roi_y]])
            aligned_img = cv2.warpAffine(step1_img, translation_matrix, step0_img.shape[::-1])

            # Extract step number from filename
            step_number = int(filename.split('_')[1])

            # Save the aligned image with step number
            output_filename = f"{step1_img_name}.tif"
            output_path = os.path.join(output_folder, output_filename)
            cv2.imwrite(output_path, aligned_img)
            print(f"Saved aligned image to {output_path}")

print("Alignment and saving completed.")
toc = time.time()
print(toc-tic, 'seconds elapsed')