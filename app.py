import , sys

import datetime
#  

args = str(sys.argv)
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
            self.users.append(self.single_user_holder)
            # return true
            return 1

        # on failure to add return false
        return 0

    def login(self, username, password):
        '''login an existing user'''
        for user in self.users:
            if username in user['username'] and password in user['password']:
                return True
            else:
                return False
        

