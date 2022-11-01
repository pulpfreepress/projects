"""Implements Team Roster Operations"""

import json

class Roster(object):
    """Implements Team Roster Operations"""
    def __init__(self):
        self.roster = {}

    def load_roster(self):
        filename = input("Enter filepath and name: ")
        with open(filename, 'r', encoding='UTF-8') as f:
            self.roster = json.loads(f.read())
            print(self.roster['members'][0])
            # print(self.roster)

    def print_roster(self):
        print(json.dumps(self.roster))

    def add_members(self):
        keep_going = 'y'
        while keep_going == 'y':
            member_name = input("Enter team member name: ")
            member_age = int(input("Enter team member age: "))
            self.roster['members'].append({'name': member_name, 'age': member_age})
            keep_going = input("Add another? (y/n)")
            



