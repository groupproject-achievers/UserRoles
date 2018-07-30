import os

import datetime
#  


class Users(object):

    def __init__(self):
        self.users = []
        self.single_user_holder = dict()
    def add_user(self, username, email, password, role):
        print("creating user ...")
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
                now = datetime.datetime.now()
                date_logged = now.strftime("%Y-%m-%d %H:%M")
                user["last_login"] = date_logged
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

    def add_comment(self, message, author):
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
    def modify_comment(self, id, message):
    	acomment = dict()
    	if message:
            for i in self.comments:
                counter += 1
                if id == counter:
                	i['message'] = message
		            

    def all_comments(self):
        return self.comments

if __name__=="__main__":
	user_obj= Users()
	comment_obj = comments()
	current_user = None
	while True:
		command= input("#- ")
		if command == ("exit"):
			break
		elif command == "add_user":
			username = input ("username: ")
			email = input ("email: ")
			password  = input("password: ")
			role = input("role(admin/norm/mod): ")
			while not (role == "mod" or role == "admin" or role == "norm"):
				role = input("enter a valid role \n role(admin/norm/mod): ")
			user_obj.add_user(username, email, password, role)
			print("user created")

		elif command == "login":
			username = input ("username: ")
			password  = input("password: ")
			if user_obj.login(username, password):
				current_user = username 
				print ("logged in")

			else:
				print("wrong username or password")

		elif command == "add_comment":
			if current_user:
				message = input ("message: ")
				comment_obj.add_comment(message, current_user)
			else:
				print("you have to login first")
		elif command == "all_users":
			print(user_obj.all_users())
		elif command == "all_comments":
			print(comment_obj.all_comments())

		else:
			print ("enter valid command")

