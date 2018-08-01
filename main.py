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
            "./data/topics_cssi.csv"))

class WelcomeHandler(webapp2.RequestHandler):
    #This is the welcome page 
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")

        self.response.write(jinja_template.render())

class SessionProvideHandler(webapp2.RequestHandler):
    #This is the session code providing area 
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/classcode.html")
        sessionid = sessionprovide.getsessionid()
        self.response.set_cookie(key="sessionid", value=str(sessionid))
        val = {"session_id":sessionid}
        self.response.write(jinja_template.render(val))

class SessionSelectHandler(webapp2.RequestHandler):
    #This handler is made to have teams select their rooms
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/sessionselect.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))
    """
    def post(self):
        jinja_template = jinja_current_dir.get_template("/templates/sessionselect.html")
        #this is where the function call would go
        
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))
    """

class TeamSelectHandler(webapp2.RequestHandler):
    #This handler is made to manage the selection of teams
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/teamselect.html")
        #NEED TO DEFINE TOPIC_CATEGORY
        self.response.write(jinja_template.render(  # this is where the dictionary files would be pushed
        ))
    def post(self): #this is after session mgmt
        sessioncode = self.request.cookies.get("sessionid")        


class TeamDisplayHandler(webapp2.RequestHandler):
    #This handler is made to 
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/teamdisplay.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class TopicPresentHandler(webapp2.RequestHandler):
    #This handler is made to present the debate topic
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/topicpresent.html")
        #this is where the function call would go
        topicval = topicpresent.exfield("Topics","topic_category","",shuffle=True)
        self.response.write(jinja_template.render(topicval))

class StancePresentHandler(webapp2.RequestHandler):
    #This handler is made to present the debate stance - immediately follows TopicPresentHandler
    """
    000.099 is Food
    100.199 is Miscellaneous
    200.299 is Memes
    300.399 is Pop Culture
    400.499 is Technology
    """
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/stancepresent.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class VoteHandler(webapp2.RequestHandler):
    #This handler is made to handle the votes
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/voting.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class TimerPresentHandler(webapp2.RequestHandler):
    #This handler is made to present the timer - potential to be merged with StancePresentHandler or given only to judges
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/timer.html")
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
        jinja_template = jinja_current_dir.get_template("/templates/end.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/Aboutus.html")
        self.response.write(jinja_template.render())

class SessionChecker(webapp2.RequestHandler): #returns TRUE if the sessid exists, otherwise returns FALSE
    def get(self):
        usersessid = int(self.request.get('input_text'))
        if (sessionselect.checksessionid(usersessid)):
            self.response.set_cookie(key="sessionid", value=str(usersessid))
            self.response.write("True")
        else:
            self.response.write("False")

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/begin', SessionProvideHandler),
    ('/sess', SessionSelectHandler),
    ('/teamselect', TeamSelectHandler),
    ('/teamdisplay', TeamDisplayHandler),
    ('/topic', TopicPresentHandler),
    ('/vote', VoteHandler),
    ('/timer', TimerPresentHandler),
    ('/continue', ContinueHandler),
    ('/end', EndHandler),
    ('/seed', SeedHandler),
    ('/aboutus', AboutUsHandler),
    ('/check/session.*', SessionChecker),
], debug=True)
