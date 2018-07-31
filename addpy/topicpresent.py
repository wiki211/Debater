"""
import sys
sys.path.insert(0, '/Users/demouser/Desktop/cssi-project/Debater/')
from models import contentmodels, genfunc
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
"""
