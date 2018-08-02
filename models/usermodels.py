from google.appengine.ext import ndb

class User(ndb.Model):
    user_id = ndb.IntegerProperty(required=True)
    sessions = ndb.IntegerProperty(repeated=True)

