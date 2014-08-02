from google.appengine.ext import db


class Member(db.Model):
    userId = db.StringProperty()
    userPassword = db.StringProperty()

    def __init__(self):
        self.userId = ""
        self.userPassword = ""

    def getId(self):
        return self.userId

    def getPassword(self):
        return self.userPassword

    def setId(self, userId):
        self.userId = userId

    def setPassword(self, userPassword):
        self.userPassword = userPassword

    def getInfo(self):
        result = {}
        result['userId'] = self.getId()
        result['userPassword'] = self.getPassword()
        return result
