import csv
import sys
import os
sys.path.insert(0, '../')
#these are necessary to change the syspath
<<<<<<< HEAD
from models import adminmodels, contentmodels, genfunc
=======
from models import contentmodels, genfunc
>>>>>>> Michelle

def getdata(pathtofile):
    fullpath = os.path.expanduser(str(pathtofile))
    with open(str(pathtofile)) as csvfile:  # this used to have , newline=''
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        nn = [r for r in spamreader]
    nn = nn[1:]
    return nn

def importdata(impdata):
    n = 0 #number of filled data entries
    genfunc.cleartype(contentmodels.Topics)
    for r in impdata:
        dd = contentmodels.Topics(topic_content=r[0],topic_category=r[1],
        topic_option_1=r[2],topic_option_2=r[3],topic_id=r[4])
        dd.put()
        if r[0] != "": #check to see if the topic is empty
            n+=1
    return n


#data = getdata("/Users/demouser/Desktop/cssi-project/Debater/data/topics_cssi.csv")
