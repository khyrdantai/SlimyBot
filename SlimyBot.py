import discord
from datetime import *
from discord.ext import tasks


# the slimy bot client itself
class SlimyBot(discord.Client):

    # this will store all of our external files and objects needed by the bot
    loader = None

    def __init__(self, loader):
        # import the Loader object created by Main
        self.loader = loader

        # connect to discord
        super().__init__()

        # start the background date check task
        self.daily_check.start()

    # this is how the bot can respond to stuff
    async def on_message(self, message):
        # do not let the bot reply to itself
        if message.author.id == self.user.id:
            return
        # used to make sure the bot lives
        if message.content.startswith('!hello'):
            await message.reply('Hello!')
        # to add a birthday to the list
        if message.content.startswith('!add'):
            add_date = str(message.content).replace('!add ', '')
            user_id = str(message.author.id)
            if add_date.isnumeric:
                self.loader.add_birthday(add_date, user_id)
                await message.reply('I did my best~')
            else:
                await message.reply('Try again in this format: DDMM')

    # main loop to check for birthday
    @tasks.loop(hours=1)
    async def daily_check(self):

        await self.wait_until_ready()

        if datetime.now().strftime("%H") != "10":
            print('Not the time.')
            return

        now = datetime.today()
        today = now.strftime("%d%m")

        for person in self.loader.list_of_people:
            if today in person.birth_date:
                channel = await self.fetch_channel(self.loader.channel_id)
                name = await self.fetch_user(person.discord_id)
                if name is not None:
                    await channel.send("Happy birthday <@!" + person.discord_id + "> !!!")
                else:
                    print("Does not exist.")
            else:
                print("No birthday today.")

    @daily_check.before_loop
    async def before_check(self):
        await self.wait_until_ready()
