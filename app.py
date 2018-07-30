import os, sys

import datetime
#  


class Users(object):

    def __init__(self):
        self.users = []
        self.single_user_holder = dict()
    def adduser(self, username, email, password, role):
        if username and email and password:
            now = datetime.datetime.now()
            date_created = now.strftime("%Y-%m-%d %H:%M")

            # entry id
            user_id = 1
            for i in self.users:
                user_id += 1
                if i['id'] == user_id:
                    user_id += 1
            self.single_user_holder = dict()
            self.single_user_holder['id'] = user_id
            self.single_user_holder['username'] = username
            self.single_user_holder['email'] = email
            self.single_user_holder['password'] = password
            self.single_user_holder['created'] = str(date_created)
            self.single_user_holder['role'] = role
            self.single_user_holder['last_login'] = None
            self.users.append(self.single_user_holder)
            # return true
            return 1

        # on failure to add return false
        return 0

    def login(self, username, password):
        """login an existing user"""
        for user in self.users:
            if username in user['username'] and password in user['password']:
                return True
        else:
            return False

    def all_users(self):
        return self.users

class comments(object):
    """keep user's comments"""

    # constructor
    def __init__(self):
        # placeholder for comments
        self.comments = []

    def addrecipe(self, message, date_created, author):
        """add a new recipe"""
        acomment = dict()
        if message:
            now = datetime.datetime.now()
            date_created = now.strftime("%Y-%m-%d %H:%M")
            counter = 1
            for i in self.comments:
                counter += 1
                if i['id'] == counter:
                    counter += 1
            acomment['message'] = message
            acomment['id'] = counter
            acomment['author'] = author
            acomment['date_create'] = date_created
            self.comments.append(acomment)
            # return true
            return 1
        else:
            # return false
            return 0

    def all_comments(self):
        return self.comments

if __name__=="__main__":
	args = str(sys.argv)
	if args[1] == "adduser":
		user_obj= Users()
		user_obj.adduser(args[2], args[3], args[4], args[5])


