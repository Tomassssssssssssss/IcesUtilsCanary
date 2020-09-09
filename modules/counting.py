import discord
from discord.ext import commands
import os
from modules import dev

s = os.path.basename(__file__)
"""CANARY BUILD"""
#Hello there this is a git test

class Counting(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #on message edit event
    async def on_message_edit(self, before, after):
        dev.log(s, f"message was edited from '{before}' to '{after}'")
        if after.channel.id == 703460208940417064: #counting channel
            dev.log(s, f"message is in counting channel")
            await after.delete() #delete the message
            dev.log(s, f"deleted the message")
            messageeditembeddm = discord.Embed(
                title = "You are not allowed to edit messages!",
                description = "You cannot edit messages in this channel! Please refrain from doing this as it makes it difficult to count.",
                colour = discord.Color.red(),
            )
            dev.log(s, f"create messageeditembeddm")
            dm = await after.author.create_dm()

            dev.log(s, f"create a dm with {after.author}")
            await dm.send(embed = messageeditembeddm)
            dev.log(s, f"send embed to dm and return")
            return
        else:
            dev.log(s, f"message is in a different channel, return")
            return None #message is in a different channel

    @commands.Cog.listener()  #on message event
    async def on_message(self, ctx):
        if ctx.channel.id == 703460208940417064: #canary counting channel

            pa = open("author.txt", "r")



            dev.log(s, f"open author.txt in read only mode")

            prev_author = str(pa.read())



            pa.close()

            dev.log(s, f"prev author is {prev_author} and current author is {ctx.author}")

            if prev_author == str(ctx.author):
                dev.log(s, f"prev author matches current author")
                dev.log(s, f"deleting message and return")
                await ctx.delete()
                return

            current_author = str(ctx.author)

            dev.log(s, f"current author is {current_author}")

            pa = open("author.txt", "w")

            dev.log(s, f"open author.txt in write mode")



            pa.write(current_author)



            pa.close()

            dev.log(s, f"closing author.txt")

            dev.log(s, f"open counting.txt in read only mode")

            numfile = open("counting.txt", "r")



            prevnum = int(numfile.read())

            dev.log(s, f"read counting.txt prevnum is {prevnum}")



            numfile.close()
            nextnum = prevnum + 1

            numfilenew = open("counting.txt", "w+")



            dev.log(s, f"next number will be {nextnum}")
            if ctx.content == str(nextnum):
                dev.log(s, f"hit {ctx.content}")
                numfilenew.write(str(nextnum))
                dev.log(s, f"write {nextnum} to counting.txt")
                dev.log(s, f"closing counting.txt and return")
                nextnum = int(nextnum)

                await ctx.channel.edit(topic=f"The next number will be {nextnum+1}")
                dev.log(s, f"new contents of counting.txt are {numfilenew.read()}")

                numfile.close()
                return

            else:
                dev.log(s, f"miss {ctx.content}")
                numfilenew.write(str(prevnum))
                dev.log(s, f"write {prevnum} to counting.txt")

                await ctx.delete()
                pa = open("author.txt", "w")

                pa.close()
                dev.log(s, f"deleting message closing counting.txt and return")
                numfile.close()
                return



############################################################## COUNTING END

def setup(client):
    client.add_cog(Counting(client))