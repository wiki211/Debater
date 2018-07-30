import csv
import sys
import os
sys.path.insert(0, '/Users/demouser/Desktop/cssi-project/Debater/')
#these are necessary to change the syspath
from models import contentmodels,adminmodels

def getdata(pathtofile):
    fullpath = os.path.expanduser(str(pathtofile))
    with open(str(pathtofile), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        nn = [r for r in spamreader]
    return nn

def importdata(impdata):
    n = 0 #number of filled data entries 
    for r in impdata:
        dd = contentmodels.Topics(topic_content=r[0],topic_category=r[1],
        topic_option_1=r[2],topic_option_2=r[3],topic_id=r[4])
        dd.put()
        if r[0] != "": #check to see if the topic is empty
            n+=1
    return n

#data = getdata("/Users/demouser/Desktop/cssi-project/Debater/data/topics_cssi.csv")

