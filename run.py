from dowClient import dowClient
import os

client = dowClient()

TOKUN = os.environ['DISCORD_BOT_TOKEN']

client.run(TOKUN)
