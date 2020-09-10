# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import urllib.request
import datetime
import logging
import argparse
import sys

LOG_FILENAME = "errors.log"
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)
assignment2 = logging.getLogger("assignment2")
# assignment2.debug('This message should go to the log file')

def downloadData(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    return text

def processData(data):
    result = {}
    c = data.split("\n")
    for i in range(1, len(c) - 1):
        r = c[i].split(",")
        key = r[0]
        try:
            birthday = datetime.datetime.strptime(r[2], '%d/%m/%Y')
        except:
            assignment2.debug("Error processing line #%s for ID #%s", i, r[0])
            birthday = datetime.datetime.strptime("01/01/2000", '%d/%m/%Y')
        val = (r[1], birthday)
        result[key] = val
    return result

def displayPerson(id, personData):
    if str(id) in personData.keys():
        print("Person #" + str(id) + " is " + personData[str(id)][0] + " with a birthday of " + personData[str(id)][
            1].strftime("%Y-%m-%d"))
    else:
        print("No user found with that id")

def main(url):

    try:
        csvData = downloadData(url)

    except:
        print("Failed to connect to the file through the url")
        sys.exit()
    personData = processData(csvData)
    userID = input("Please enter a userID: ")
    while int(userID)>0:
        displayPerson(userID, personData)
        userID = input("Please enter a userID: ")
    sys.exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='File Url')
    parser.add_argument('url', help='the url of the file, please enter it')
    args = parser.parse_args()
    main(args.url)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
