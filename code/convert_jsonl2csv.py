import csv, json, sys
#if you are not using utf-8 files, remove the next line
#sys.setdefaultencoding("UTF-8") #set the encode to utf8
#check if you pass the input file and output file

if sys.argv[1] is not None and sys.argv[2] is not None:
    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]
    inputFile = open(fileInput, 'r') #open json file
    outputFile = open(fileOutput, 'w') #load csv file
    tweets = []
    flag = 0

    for line in inputFile:
        tweets.append(json.loads(line))

    for tweet in tweets:
        if(flag==0):
            output = csv.writer(outputFile) #create a csv.write
            output.writerow(tweet.keys())  # header row
            flag = 1
        output.writerow(tweet.values()) #values row

    inputFile.close() #close the input file
    outputFile.close()
