from google.appengine.ext import ndb
"""
def cleartype(modeltype):
    db.delete(modeltype)
"""

def cleartype(modeltype):
    ndb.delete_multi(modeltype.query().fetch(keys_only=True))

def queryfield(modeltype, modprop, contentfilt="", typefilter=True):
    if typefilter:
        return modeltype.query().filter(modeltype.modprop==str(contentfilt)).fetch()
    else:
        return modeltype.query().order(modeltype.modprop).fetch()

