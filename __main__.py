import json
import discord #Allows access to the discord API
from discord.ext import commands, tasks #Pre-built command handler
import os #For interacting with files
from modules import dev #A script I wrote to log commands and help with devging. Takes 2 arguments: scriptname (s), log.
import urllib.request
s = os.path.basename(__file__) #scriptname (arg1)

""" THIS IS A CANARY BUILD """

client = commands.Bot(command_prefix = "$") #All commands start with $


@tasks.loop(hours = 24)  #Fact of the day
async def postfact():
    dev.log(s, f"running postfact")
    factcount = open("factcount.txt", "r")
    dev.log(s, f"opened factcount.txt")
    currentfact = int(factcount.read())
    dev.log(s, f"read {currentfact}")
    nextfact = currentfact + 1

    dev.log(s, f"next fact will be {nextfact}")

    factcount.close()
    dev.log(s, f"closing factcount")
    factcount = open("factcount.txt", "w")
    dev.log(s, f"open factcount in write mode")
    factcount.write(str(nextfact))
    dev.log(s, f"write {nextfact} to factcount.txt")
    factcount.close()

    fotd_channel = client.get_channel(703463111155253329)
    dev.log(s, f"got channel")

    raw_fact = urllib.request.urlopen("https://uselessfacts.jsph.pl/random.json?language=en")
    dev.log(s, f"requested url")
    fact = json.loads(raw_fact.read())
    dev.log(s, f"read {fact}")
    await fotd_channel.send(f'[**Fact #{str(currentfact)}**] {fact["text"]}')
    dev.log(s, f"send {fact['text']}")


@client.event #event decorator, makes event handling a lot easier
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="Version c3.2.3")
    ) #set the bot's playing status
    dev.log(s, f"logged in as {client.user.name}#{client.user.discriminator} with latency {round(client.latency*1000)}ms. THIS IS A CANARY BUILD!")
    dev.log(s, f"bot running in {__file__}") #get the directory the bot is running in
    postfact.start()

for filename in os.listdir('./modules'): #Get all files in current directory
    dev.log(s, f"detected {filename}")
    if filename.endswith(".py"): #Check if python file
        client.load_extension(f"modules.{filename[:-3]}") #Load the module (/modules/ folder)
        dev.log(s, f"successfully loaded module {filename}")



client.run("NzAzNDU4MzczMzAzMTQwNDAy.XqO44Q.uPPBr9JPUY0FcGTyaKnFQOV3CVQ") #Login to discord API

