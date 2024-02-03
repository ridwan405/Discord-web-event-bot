import os

import discord

TOKEN = os.environ['WEBEVENT_BOT_TOKEN']
intents = discord.Intents.default() 
intents.message_content = True

client= discord.Client(intents= intents)

#bot online notif
@client.event
async def on_ready():
  print(f"{client.user} is now online")



#test bot

@client.event
async def on_message(message):

  print(message.content)

  if message.author == client.user:
      return  
  # # lower case message
  # message_content = message.content.lower()  

  if message.content.startswith('$hello'):
    await message.channel.send('hello')



#run bot
client.run(TOKEN)