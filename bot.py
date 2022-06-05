import discord
import os
import requests
import json
import random
import time

text = "some text"


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event

async def on_ready():
  print('We have logd in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello') 

  if message.content.startswith('$senddm'):
    await message.author.send("test")


@client.event
async def on_member_join(member):
  print("Member joined")

  print(member)
  print (text)
  await member.send(text)

f = open("token.txt","r")


mytoken = f.read()

my_secret = mytoken

client.run(my_secret)

print("running")