# _*_ coding:utf-8 _*_

from google.appengine.ext import db


class FirstClass(db.Model):
    fuckingTextFunction = db.StringProperty()
    fuckingLike = db.IntegerProperty()
    def setText(self, text):
        self.fuckingTextFunction = text

    def getText(self):
        return self.fuckingTextFunction

    def setLike(self, like):
    	self.fuckingLike = like

    def getLike(self):
    	return self.fuckingLike

    def 