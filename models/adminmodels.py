from google.appengine.ext import ndb

class boolstore(ndb.Model):
    propname = ndb.StringProperty(required=True)
    boolval = ndb.BooleanProperty(required=True)

def modifyndb(typeclass, inpname, selectvalue):
    if typeclass.query().filter(typeclass.propname == inpname).fetch() == []:
        dd = typeclass(propname = inpname, boolval = selectvalue)
        dd.put()
    else:
        dd = typeclass.query().filter(typeclass.propname == inpname).fetch()[0]
        dd.boolval = selectvalue
        dd.put()
 
