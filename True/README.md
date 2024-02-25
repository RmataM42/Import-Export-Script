# Import/Export Script

Project 1: import/export script​

Import file created from baselight (Baselight_export.txt)​
Import xytech work order (Xytech.txt)​
Script will parse data ​
Computation done to match shareholder request, to replace file system from local baselight to facility storage (remember color correcter's prefer local storage for bandwidth issues)​
Remember we are dealing with 3rd party data, so some errors in the data might occur and you have to deal with it (i.e <null> <err>)​
Export CSV file ('/' indicates columns): ​
Line 1: Producer / Operator / job /notes​
Line 4: show location / frames to fix​
Frames and frame ranges processed in consecutive/numerical order shown (from baselight_export.txt) as either:
ranges (i.e /filesystem/Dune2/PartA/1920x1080  32-35) 
individually (i.e  /filesystem/Dune2/PartA/1920x1080   41)​
Frames shown need to reflect their proper location and not mix with ranges from another location

Grading:

10% - does in import files correctly?

15% - does it parse the data correctly

25% - Correct file name swapping

35% - Correct frame ranges

15% - correct export to CSV with correct data
 
