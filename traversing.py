# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:23:27 2019

@author: pablo
"""

import request
import time


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

token = "Token "

# api-endpoint
init        = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/"
move        = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/"
take        = "https://lambda-treasure-hunt.herokuapp.com/api/adv/take/"
changeName  = "https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/"
sale        = "https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/"
examineItem = "https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/"



#####TODO#####
#json object that contains room information

#inplement graph traversal and building

#account visited room path

#reverse direction incase needs to go back.

#account cooldown time.

#request to the server
##############