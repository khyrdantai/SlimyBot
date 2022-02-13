from SlimyBot import SlimyBot
from Loader import Loader


# load all the files up
loader = Loader()

# start the bot with the files and run it
client = SlimyBot(loader)
client.run(loader.token)
