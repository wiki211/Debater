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
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class TeamSelectHandler(webapp2.RequestHandler):
    #This handler is made to manage the selection of teams
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class TeamDisplayHandler(webapp2.RequestHandler):
    #This handler is made to 
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class TopicPresentHandler(webapp2.RequestHandler):
    #This handler is made to present the debate topic
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class StancePresentHandler(webapp2.RequestHandler):
    #This handler is made to present the debate stance - immediately follows TopicPresentHandler
    """
    000 – 099 is Food
    100 – 199 is Miscellaneous
    200 – 299 is Memes
    300 – 399 is Pop Culture
    400 – 499 is Technology
    """
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class VoteHandler(webapp2.RequestHandler):
    #This handler is made to handle the votes
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class TimerPresentHandler(webapp2.RequestHandler):
    #This handler is made to present the timer - potential to be merged with StancePresentHandler or given only to judges
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class ContinueHandler(webapp2.RequestHandler):
    #This handler is made to redirect to next page
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class EndHandler(webapp2.RequestHandler):
    #This handler is made to display end statistics
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))


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
    ('/seed', SeedHandler),
], debug=True)
