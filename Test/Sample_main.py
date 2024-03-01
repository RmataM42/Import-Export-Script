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
    #     print(folder.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

#import Baselight_export.txt
Baselight_file_path = "Test/Sample_Baselight_export.txt"
try:
    with open(Baselight_file_path, 'r') as baselight_file: 
        for line in baselight_file:
            # Split baselight txt into list w/ whitespace as delimeter
            # Able to: seperate file path and frame 
            line_split = line.split() 
            # Pop 1st element in list which is always file path
            line_pop = line_split.pop(0)

except FileNotFoundError:
    print("Baselight_export.txt file not found.")
except PermissionError:
    print("Permission denied.")