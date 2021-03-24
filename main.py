import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)


@client.event
async def on_ready():
  print('Bot is ready')
  general = client.get_channel(824067463264075809)
  await general.send(input("Send:"))



@client.event
async def on_member_join(member):
  print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
  print(f'{member} has left the server.')

@client.event
async def on_message(message):
  print(f'{message.author.name} has written in the chat:{message.content}')
  #if not message.author.name == "Joe Bidome":
  general = client.get_channel(824067463264075809)
  bots = client.get_channel(824067509807742986)
  tofu = client.get_user(743958088968831117)
  chch = input("1 = General, 2 = Bots, 3 = Tofu,\n4 = jod\nChannel:")
  chch = int(chch)
  if chch == 1:
    await general.send(input("Send:"))
  elif chch == 2:
    await bots.send(input("Send:"))
  elif chch == 3:
    await tofu.send(input("Send:"))

client.run("ODI0MDYyODY4OTcwMDEyNzIy.YFp6Wg.KZ87qrc66GJNaHPtYP9edZ16DaY")