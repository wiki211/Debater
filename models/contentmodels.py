#!/usr/bin/python

from google.appengine.ext import ndb

class Topics(ndb.Model):
  topic_content = ndb.StringProperty(required=True)
  topic_category = ndb.StringProperty(required=True)
  topic_id = ndb.StringProperty(required=True)
  topic_option_1 = ndb.StringProperty(required=True)
  topic_option_2 = ndb.StringProperty(required=True)
  

      
    


            
