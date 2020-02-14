from CheckInstaPics import check_insta_pics
import csv

imagetocompare = 'ogImg.jpg'
originalcsv = open('CenterInstagramList.csv', 'r')
finalcsv = open('CenterHasPost.csv', 'w')

reader = csv.reader(originalcsv)
writer = csv.writer(finalcsv)
writer.writerow(['Center Name', 'Has post?'])

for row in reader:
    print(row[0])
    try:
        trueorfalse = check_insta_pics(row[1],imagetocompare)
        writer.writerow([row[0],trueorfalse])
        print(trueorfalse)
    except IndexError:
        print("Done!")
