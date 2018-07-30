#!/usr/bin/python

import webapp2
import os
import jinja2
#import addpy.sessionselect
#addpy.sessionselect.test()
from addpy import * 
from models import *

#this imports all modules under the addpy folder
#please update the __all__ = [] with specified module names

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#The following Handlers are made to 
#the specification detailed in "Game Design" under User Design

#Data seeding is provided by the following functions:
#dataimport.importdata(dataimport.getdata("/Users/demouser/Desktop/cssi-project/Debater/data/topics_cssi.csv"))

class SeedHandler(webapp2.RequestHandler):
    def get(self):
        dataimport.importdata(dataimport.getdata(
            "/Users/demouser/Desktop/cssi-project/Debater/data/topics_cssi.csv"))

class WelcomeHandler(webapp2.RequestHandler):
    #This is the welcome page 
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        self.response.write(jinja_template.render())

class SessionSelectHandler(webapp2.RequestHandler):
    #This handler is made to have teams select their rooms
    def get(self):
        pass

class TeamSelectHandler(webapp2.RequestHandler):
    #This handler is made to manage the selection of teams
    def get(self):
        pass

class TeamDisplayHandler(webapp2.RequestHandler):
    #This handler is made to 
    def get(self):
        pass

class TopicPresentHandler(webapp2.RequestHandler):
    #This handler is made to present the debate topic
    def get(self):
        pass

class VoteHandler(webapp2.RequestHandler):
    #This handler is made to handle the votes
    def get(self):
        pass

class TimerPresentHandler(webapp2.RequestHandler):
    #This handler is made to 
    def get(self):
        pass

class ContinueHandler(webapp2.RequestHandler):
    #This handler is made to 
    def get(self):
        pass

class EndHandler(webapp2.RequestHandler):
    #This handler is made to 
    def get(self):
        pass


app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/sess', SessionSelectHandler),
    ('/teamselect', TeamSelectHandler),
    ('/teamdisplay', TeamDisplayHandler),
    ('/topic', TopicPresentHandler),
    ('/vote', VoteHandler),
    ('/timer', TimerPresentHandler),
    ('/continue', ContinueHandler),
    ('/end', EndHandler),
], debug=True)
