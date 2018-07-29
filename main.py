#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import os
import jinja2

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#The following Handlers are made to 
#the specification detailed in "Game Design" under User Design

class WelcomeHandler(webapp2.RequestHandler):
    #This is the welcome page 
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/question.html")
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
