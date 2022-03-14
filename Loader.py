from User import User
import json


class Loader:

    # used for turning some text files into usable objects
    server_id = None
    bot_id = None
    bot_token = None
    # the object-form list of people
    list_of_users = []

    def __init__(self):
        self.init = 'Initializer'
        self.operations()
        self.generate_list()

    def operations(self):
        # open file and populate parameters then close file
        file = open('config.json')
        data = json.load(file)
        self.server_id = data["server_id"]
        self.bot_id = data["bot_id"]
        self.bot_token = data["bot_token"]
        file.close()

    def generate_list(self):
        # open file, load in objects, and close file
        file = open('discord_users.json')
        discord_users = json.load(file)
        for key in enumerate(discord_users):
            discord_id = discord_users[key, "discord_id"]
            day = discord_users[key, "day"]
            month = discord_users[key, "month"]
            self.list_of_users.append(User(discord_id, month, day))
        file.close()

    # not yet fully implemented
    def add_user(self, discord_id, month, day):
        # add to object list of people
        self.list_of_users.append(User(discord_id, month, day))
        # to-implement: write to file

    def remove_user(self, user):
        self.list_of_users.remove(user)
