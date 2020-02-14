# InstaScraper
Takes an image file and csv of instagram urls as parameters. Visits each url and check the last three posts and compares image. 
Returns csv of true/false for each url.

Uses Chrome driver (included in directory) so make sure to download the Chrome browser and in CheckInstaPics.py file 
lines 17 and 35 set the executable_path to the ABSOLUTE path of the chrome driver file in your own project directory.

How to use:
1. Add instagram URLs to the 'CenterInstagramList.csv' file with name as first column and URL as second column.
2. Add the image file to be compared to the instagram post images for each URL as 'ogImg.jpg' in the root directory.
3. Run the Main.py function.
4. After the script finished running without errors, check 'CenterHasPost.csv'.
5. Profit(?).

Confirms working in MacOS as of 2/14/2020. Feel free to use it for personal use @^_^@
