import csv

#import Xytech.txt
Xytech_file_path = "Test/Sample_Xytech.txt"
xytech_folders = []

try:
    with open(Xytech_file_path, 'r') as read_xytech_file:  
        # Iterate over each line in the file
        for line in read_xytech_file:
            # Check if the line contains "/"
            if "/" in line:
                # If "/" is found, append the line to xytech_folders list
                xytech_folders.append(line)
    # Test to see if xytech_folders[] comes out correctly
    # for folder in xytech_folders:
    #     print(folder.strip())  # strip() removes leading/trailing whitespace, if any
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

#import Baselight_export.txt
Baselight_file_path = "/Test/Sample_Baselight_export.txt"
