from google.appengine.ext import ndb

class Otherdatastore(ndb.Model):
    propname = ndb.StringProperty(required=True)
    genval = ndb.IntegerProperty(repeated=True)
    #otherdatastore is a kind of heuristics, like unavailable sessids, etc. 

"""
def modifyndb(typeclass, inpname, selectvalue):
    if typeclass.query().filter(typeclass.propname == inpname).fetch() == []:
        dd = typeclass(propname = inpname, boolval = selectvalue)
        dd.put()
    else:
        dd = typeclass.query().filter(typeclass.propname == inpname).fetch()[0]
        dd.boolval = selectvalue
        dd.put()
"""

class Sessions(ndb.Model):
    sessid = ndb.IntegerProperty(required=True) #8 digit number that allows room entrance
    playernames  = ndb.IntegerProperty(repeated=True) #list of player names
    #list of votes for and against a team. Structured as a 3x3 matrix,
    #where each row represents a game and each column a team
    #structure is nested lists, stored a string before input
    vote_game = ndb.StringProperty(required=True)
