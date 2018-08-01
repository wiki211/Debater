from google.appengine.ext import ndb
"""
def cleartype(modeltype):
    db.delete(modeltype)
"""
from models import contentmodels

def cleartype(modeltype):
    ndb.delete_multi(modeltype.query().fetch(keys_only=True))

def queryfield(modeltype, modprop="", contentfilt="", typefilter=True):
    if (modprop==""):
        return (modeltype.query().fetch())
    elif typefilter:
        return modeltype.query().filter(eval("modeltype."+modprop)==(contentfilt)).fetch()
    else:
        return modeltype.query().order(eval("modeltype."+modprop)).fetch()

def excludefield(modeltype, modprop, contentfilt=""):
    prefix = eval("contentmodels."+modeltype)
    #print(prefix.query().filter(eval("contentmodels." +modeltype+"."+modprop) != str(contentfilt)).fetch())
    return prefix.query().filter(eval("contentmodels."+modeltype+"."+modprop) != str(contentfilt)).fetch()
