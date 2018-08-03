import sys
sys.path.insert(0, '/Users/demouser/Desktop/cssi-project/Debater/')
from models import contentmodels, genfunc, adminmodels
import random

def querytopic(topic_category="", fieldval = ""):
    outval = genfunc.queryfield(contentmodels.Topics, topic_category, str(fieldval)) #"" is user input category
    outputdict = {"topic": outval}
    return outputdict

def querytopicrand(topic_category="", fieldval = ""):
    outval = genfunc.queryfield(contentmodels.Topics, topic_category, str(fieldval))
    random.shuffle(outval)
    outputdict = {"topic": outval}
    return outputdict

def exfield(modeltype, modprop, contentfilt="", shuffle=False):
    outval = genfunc.excludefield(modeltype, modprop, contentfilt)
    if shuffle:
        random.shuffle(outval)
    outputdict = {"topic": outval}
    return outputdict

def gettopic(roundnum, indexnum, sessionid):
    outval = genfunc.queryfield(adminmodels.Sessions, "sessid", int(sessionid))[0]
    print(outval)
    questions = eval("outval.topic_"+str(roundnum))
    maintopic = questions[0]
    stance = questions[int(indexnum)]
    return maintopic,stance

def getroundnum(sessid):
    outval = genfunc.queryfield(adminmodels.Sessions, "sessid", int(sessid))[0]
    return outval.round_num