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

""""
    def get_coins(self):
      # Want this to do 3 things:
      # Function to go to the wishing well and examine
      # Function to go to where the wishing well says
      # Function to mine coin at specified location
      # Could include if clause to go transmog coins

      coins = 0
      # variable for proof?
      while coins < 1000:
        # Go to wishing well
        print('Going to the Wishing Well.')
        self.wishing_well()
        # Examine well
        self.action('examine')
        # Go to where it says
        self.go_to_room('hinted location/room')
        # Mine Coin
        print('Getting proof...')
        response = request.post(f'https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/', headers=self.headers)
        new_proof = proof_of_work(data.get('proof'), data.get('difficulty'))
        time.sleep(self.wait)
        # Need to send new_proof in the mine request json
        response = request.post(f'https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/', headers=self.headers, json={"proof":''})
        print('You got a coin!')
        coins += 1
        time.sleep(self.wait)

""""