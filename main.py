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
jinja_current_dir = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],autoescape=True)

""" INFO PAGES """

class WelcomeHandler(webapp2.RequestHandler):
    #This is the welcome page
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        self.response.write(jinja_template.render())

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/Aboutus.html")
        self.response.write(jinja_template.render())

""" UTILITY SITES """

class SeedHandler(webapp2.RequestHandler):
    def get(self):
        dataimport.importdata(dataimport.getdata(
            "./data/topics_cssi.csv"))

class LoadingHandler(webapp2.RequestHandler):
    #Before : 
    #After : 
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/loading.html")
        self.response.write(jinja_template.render())

    def post(self):
        self.response.write(jinja_template.render())

class MinTimer(webapp2.RequestHandler):
    #This is the Loading page for round one
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/min.timer.html")
        self.response.write(jinja_template.render())
class Timer(webapp2.RequestHandler):
    #This is the Loading page for round one
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/timer.html")
        self.response.write(jinja_template.render())

class TimerPresentHandler(webapp2.RequestHandler):
    #This handler is made to present the timer - potential to be merged with StancePresentHandler or given only to judges
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/timer.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

class SessionChecker(webapp2.RequestHandler): #returns TRUE if the sessid exists, otherwise returns FALSE
    def get(self):
        try:
            usersessid = int(self.request.get('input_text'))
            if (sessionselect.checksessionid(usersessid)):
                self.response.set_cookie(key="sessionid", value=str(usersessid))
                self.response.write("True")
            else:
                self.response.write("False")
        except:
            self.response.write("False")

""" STARTPOINT SITES """

class SessionProvideHandler(webapp2.RequestHandler): #/BEGIN - PROVIDES ID
    #This is the session code providing area
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/classcode.html")
        sessionid = sessionprovide.getsessionid()
        self.response.set_cookie(key="sessionid", value=str(sessionid))
        try:
            cookieid = int(self.request.cookies.get("userid"))
            print('THIS IS THE COOKIE ID')
            print(cookieid)
            user_id = sessionprovide.usertoken(cookieid,int(sessionid)) # get the user id and append the session to them
            print("did you make it")
        except:
            print("except is happening ")
            user_id = sessionprovide.usertoken("",int(sessionid)) # get the user id and append the session to them
        self.response.set_cookie(key="userid", value=str(user_id))
        val = {"session_id":sessionid}
        self.response.write(jinja_template.render(val))

class SessionSelectHandler(webapp2.RequestHandler):
    #This handler is made to have teams select their rooms
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/sessionselect.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

""" DATA PROCESSING SITES """

class RedirectOrganizeHandler(webapp2.RequestHandler): #sets roundnum cookie, teamnum cookie, 
    def get(self):
        sessionid = int(self.request.cookies.get("sessionid"))
        self.response.set_cookie(key="teamnum", value=str(2))
        try:
            cookieid = int(self.request.cookies.get("userid"))
            user_id = sessionprovide.usertoken(cookieid,int(sessionid)) # get the user id and append the session to them
        except:
            user_id = sessionprovide.usertoken("",int(sessionid)) # get the user id and append the session to them
        self.response.set_cookie(key="userid", value=str(user_id))
        self.redirect("/preptopic")

class StancePresentHandler(webapp2.RequestHandler):
    #This handler is made to present the debate stance
    """
    000.099 is Food
    100.199 is Miscellaneous
    200.299 is Memes
    300.399 is Pop Culture
    400.499 is Technology
    """
    def get(self):
        conversionmatrix = [[0,1,2],[2,0,1],[1,2,0]]
        jinja_template = jinja_current_dir.get_template("/templates/topicpresent.html")
        #this is where the function call would go
        teamnum = int(self.request.cookies.get("teamnum"))
        print(teamnum)
        sessioncode = self.request.cookies.get("sessionid")
        roundnum = topicpresent.getroundnum(sessioncode)
        print("This is roundnum %d" % roundnum)
        self.response.set_cookie(key="roundnum",value=str(roundnum+1))
        if conversionmatrix[roundnum-1][teamnum-1] == 0:
            self.response.set_cookie(key="index", value=str(0))
            self.redirect("/judge") #REDIRECT TO JUDGE
        else:
            self.response.set_cookie(key="index", value=str(conversionmatrix[roundnum-1][teamnum-1]))
            self.redirect("/topic")

""" INTERMEDIATE SITES """
class Round1Handler(webapp2.RequestHandler):
    #This is the Loading page for round one
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/round1.html")
        self.response.write(jinja_template.render())

class TopicPresentHandler(webapp2.RequestHandler):
    #This handler is made to present the debate topic
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/topicpresent.html")
        #this is where the function call would go
        # topicval = topicpresent.exfield("Topics","topic_category","",shuffle=True)
        # print(topicval)
        #self.response.set_cookie(key="topicindex",value=)
        index = self.request.cookies.get("index")
        sessioncode = self.request.cookies.get("sessionid")
        roundnum = topicpresent.getroundnum(sessioncode)
        topic, stance = topicpresent.gettopic(roundnum, index, sessioncode)
        print(stance)
        topicval = {"topic":topic, "stance":stance}
        self.response.write(jinja_template.render(topicval))

class VoteHandler(webapp2.RequestHandler):
    #This handler is made to handle the votes
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/teamjudge.html")
        #this is where the function call would go
        #WE NEED THIS TO UPDATE SO THE ROUND MOVES ON !!!!! 
        sessid = self.request.cookies.get("sessionid")
        cur_round = votehandler.updateroundnum(sessid)
        self.response.write(jinja_template.render({"cur_round" : cur_round}))

class ContinueHandler(webapp2.RequestHandler):
    #This handler is made to redirect to next page
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/welcome.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

""" ENDPOINT SITES """

class EndHandler(webapp2.RequestHandler):
    #This handler is made to display end statistics
    def get(self):
        jinja_template = jinja_current_dir.get_template("/templates/end.html")
        #this is where the function call would go
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

""" DEPRECATED OR UNUSED """
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
        addpy.teamdisplay()
        self.response.write(jinja_template.render(#this is where the dictionary files would be pushed
        ))

"""

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/loading',LoadingHandler),
    ('/begin', SessionProvideHandler), 
    ('/round1', Round1Handler),
    ('/mintimer', MinTimer),
    ('/timer', Timer),
    ('/organize', RedirectOrganizeHandler),
    ('/sess', SessionSelectHandler),
    #('/teamselect', TeamSelectHandler),
    #('/teamdisplay', TeamDisplayHandler),
    ('/topic', TopicPresentHandler),
    ('/preptopic', StancePresentHandler),
    ('/judge', VoteHandler),
    ('/timer', TimerPresentHandler),
    ('/continue', ContinueHandler),
    ('/end', EndHandler),
    ('/seed', SeedHandler),
    ('/aboutus', AboutUsHandler),
    ('/check/session.*', SessionChecker),
], debug=True)
