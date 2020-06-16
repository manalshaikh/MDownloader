import requests
import io
import re
import signal
import sys

#CTRLC handling
def signal_handler(signal, frame):
    print("Thank you for using CRON!")
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def grab(string, start, end):
    match = re.search(r'%s[^<]*%s' % (start, end), string)
    if match:
        return match.group().split(start)[1][:-len(end)]
    else:
        return False

url = []

file = open("urls.txt", "r")

for i in file:
    i = i.replace("\n", "")
    url.append(i)

for i in url:
    # String - Start - End
    # Example filename = grab(i, 'geos/', '.html') 
    # It will be grab the word between that goes/ and html
    start = 'geos/' 
    end = '.html'
    filename = grab(i, start, end) 
    res = requests.get(i)
    type(res)
    fname = filename + ".html"
    fname = "data/" + fname
    with io.open(fname, "w", encoding="utf-8") as f:
        f.write(res.text)
        f.close()
        print(filename + ".html is downloaded.")
print("All file(s) are downloaded!")