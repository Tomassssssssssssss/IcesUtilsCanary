import discord
from discord.ext import commands
from datetime import datetime
import os
from modules import dev

s = os.path.basename(__file__)

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, ctx):
        dev.log(s, f"message received: {ctx.content}")
        chatlog = open("chatlog.txt", "a")
        dev.log(s, "open chatlog.txt")
        chatlog.write(f"{str(datetime.now())} [{str(ctx.author)}][{str(ctx.channel)}] >>> {str(ctx.content)}\n")
        dev.log(s, f" write {datetime.now()} [{ctx.author}][{ctx.channel}] >>> {ctx.content} \\n")
        chatlog.close()
        dev.log(s, f"close chatlog.txt")
        return

    ############################################################## CHATLOG COMMAND BEGIN
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def chatlog(self, ctx):
        dev.log(s, f"chatlog command called\ncheck for admin permission")
        dev.log(s, f"admin permission true\ngot all required arguments\n begin chatlog command execution")
        dm = await ctx.author.create_dm()
        dev.log(s, f"create dm with {ctx.author}")
        filesentembeddm = discord.Embed(
            title="Here you go!",
            description="Here's the chat log file you requested.",
            color=discord.Color.green()
        )
        dev.log(s, f"create filesentembeddm")

        await dm.send(embed=filesentembeddm)

        dev.log(s, f"send embed to dm")

        await dm.send(file=discord.File('chatlog.txt'))

        dev.log(s, f"upload file chatlog.txt")

        filesentembed = discord.Embed(
            title="Log File Ready!",
            description="I have sent you a DM containing `chatlog.txt`",
            color=discord.Color.green()
        )
        dev.log(s, f"create filesentembed")
        await ctx.channel.send(embed=filesentembed)
        dev.log(s, f"send embed to dm\nend chatlog command execution")

    ############################################################## CHATLOG COMMAND END

    ############################################################## ANNOUNCEDM COMMAND BEGIN
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def announcedm(self, ctx, *, announcement: str):
        dev.log(s, f"chatlog command called\ncheck for admin permission")
        dev.log(s, f"admin permission true\ngot all required arguments\n begin chatlog command execution")
        dmallembed1 = discord.Embed(
            title="AnnounceDM Started",
            description="I have started sending out DMs. This might take some time depending on the number of members in the server.",
            color=discord.Color.green()
        )
        dev.log(s, f"create dmallembed1")
        dmallembed2 = discord.Embed(
            title="AnnounceDM Successful",
            description=f"Successfully sent the announcement to all server members.",
            color=discord.Color.green()
        )
        dev.log(s, f"create dmallembed2")
        await ctx.channel.send(embed=dmallembed1)

        for member in ctx.guild.members:
            announcementdm = await member.create_dm()
            dev.log(s, f"create dm with {member}")

            announcementdmembed = discord.Embed(
                title=f"**{ctx.guild.name} Announcement**",
                description=f"{announcement}",
                color=discord.Color.green()
            )
            dev.log(s, f"create announcementdmembed")
            await announcementdm.send(embed=announcementdmembed)
            dev.log(s, f"create send announcementdmembed to dm")


        await ctx.channel.send(embed = dmallembed2)
        dev.log(s, f"send dmallembed2 to {ctx.channel}")

############################################################## ANNOUNCEDM COMMAND END

    @commands.command()
    async def calculate(self, ctx, num1 : float, operation : str, num2 : float):
        try:
            valid_operations = ["+", "-", "/", "*"]
            if operation in valid_operations:

                if operation == '-':
                    await ctx.channel.send(num1 - num2)
                elif operation == '+':
                    await ctx.channel.send(num1 + num2)
                elif operation == '/':
                    await ctx.channel.send(num1 / num2)
                elif operation == '*':
                    await ctx.channel.send(num1 * num2)

                return True
            else:
                await ctx.channel.send(f"The operation you entered is not valid! You can enter {valid_operations}")
                return None
        except ZeroDivisionError:
            await ctx.channel.send("You can not divide by zero!")
            return None



def setup(client):
    client.add_cog(Misc(client))
