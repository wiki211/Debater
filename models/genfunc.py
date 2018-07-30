from google.appengine.ext import ndb
"""
def cleartype(modeltype):
    db.delete(modeltype)
"""

def cleartype(modeltype):
    ndb.delete_multi(modeltype.query().fetch(keys_only=True))
