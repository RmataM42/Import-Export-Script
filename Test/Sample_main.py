import csv

#import Xytech.txt
Xytech_file_path = "Test/Sample_Xytech.txt"
xytech_folders = []

try:
    with open(Xytech_file_path, 'r') as read_xytech_file:
        # Filter out only line that contains "/" append in xytech_folders list
        for line in read_xytech_file:
            if "/" in line:
                # If "/" is found, append the line to xytech_folders list
                xytech_folders.append(line)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")


# Debug: See if xytech_folders[] comes out correctly
# for x, folder in enumerate(xytech_folders, start=1):
#     print(x, folder.strip())

# print(xytech_folders)
#import Baselight_export.txt
Baselight_file_path = "Test/Sample_Baselight_export.txt"
try:
    with open(Baselight_file_path, 'r') as baselight_file: 
        n = 1 
        for line in baselight_file:
            # Split baselight txt into list w/ whitespace as delimeter
            # Able to: seperate file path and frame 
            line_split = line.split(" ")
                # debug line_split
            # print (n, line_split)
            # n+=1

            # Pop 1st element in list which is always file path
            line_pop = line_split.pop(0)
                # debug line_pop
            # print(n, line_pop)
            # n+=1

            # Replace "/baselightfilesystem1" w/ "" in 1st element of line_pop
            line_replace = line_pop.replace("/baselightfilesystem1","")
                # debug line_replace
            # print(n, line_replace)
            # n+=1

            # Compare Baselight.txt w/ Xytech.txt to find matching txt
            # new_location = ""
            # for xytech_check in xytech_folders:
            #     if line_replace in xytech_check:
            #         new_location = xytech_check.strip()
                    # print(new_location)
except FileNotFoundError:
    print("Baselight_export.txt file not found.")
except PermissionError:
    print("Permission denied.")