
import discord

import random

data = {
    "greetings" : {
        "cause" : ["Hi","hi","hiu"],
        "response" : ["Hello ", "Hiu","Hello Peasant"],

        },
    "gavin" : {
        "cause" : ["Gavin","gavin"],
        "response" : ["Gavin...","No one likes Gavin","Gavin you are a shrimp"],

        },
    
    "questions" : {
        "cause" : ["why","Why"],
        "response" : ["Cause reasons", "I dunno","Yes","No"],

        },
    "questions2" : {
        "cause" : ["?","are","Are","is","Is"],
        "response" : ["I dunno","Yes","No","Probrably"],

        },
     "summon" : {
        "cause" : ["Shrimpington","shrimpington"],
        "response" : ["Oh hi","YOU HAVE SUMMONED THE FINE FELLOW","https://tenor.com/view/shrimp-dancing-beer-shrimp-party-gif-15700991"],

        },
    "gif" : {
        "cause" : ["gif","Gif"],
        "response" : ["https://tenor.com/view/shrimp-dancing-beer-shrimp-party-gif-15700991","https://tenor.com/view/rage-angry-samuel-l-jackson-animated-glitch-gif-5638725","https://images-ext-2.discordapp.net/external/H3_mP8OUCHk4tWM6SNFtL8jaJiUkxbMI3b5HMusFKoA/https/media.discordapp.net/attachments/808009398081421322/911859809983270912/Load-the-fish-cannon.gif","https://images-ext-1.discordapp.net/external/U4GTiyPL1_2pGkQD9E1dal_G7LqyaV6auJF4a__K-bE/https/media.discordapp.net/attachments/722486772789018624/770805817486082068/image0.gif",],
        }
    
    }
    

def get_cause(message):
    #Greetings
    message = message.content
    if data["summon"]["cause"][0] in message or data["summon"]["cause"][1] in message:
        response = random.choice(data["summon"]["response"])
    
    if data["greetings"]["cause"][0] in message or data["greetings"]["cause"][1] in message or data["greetings"]["cause"][2] in message:
        response = random.choice(data["greetings"]["response"])

    if data["questions"]["cause"][0] in message or data["questions"]["cause"][1] in message:
        response = random.choice(data["questions"]["response"])

    if data["questions2"]["cause"][0] in message or data["questions2"]["cause"][1] in message or data["questions2"]["cause"][2] in message or data["questions2"]["cause"][3] in message or data["questions2"]["cause"][4] in message:
        response = random.choice(data["questions2"]["response"])

    if "snazzy" in message or "Snazzy" in message:
        response = "Yes I am the most snazzy shrimp"

    if data["gavin"]["cause"][0] in message or data["gavin"]["cause"][1] in message:
        response = random.choice(data["gavin"]["response"])
        
    if data["gif"]["cause"][0] in message or data["gif"]["cause"][1] in message:
        response = random.choice(data["gif"]["response"])    
        
    return response
#run bot

client = discord.Client()

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.content.startswith("$"):
    response = "None"
    response = get_cause(message)
    await message.channel.send(response)

client.run("OTUxMjIwMjc0NjEzODcwNjAz.YikS6g.mqFUG3UqBjdpfHdesfqF_xsnlTg")
