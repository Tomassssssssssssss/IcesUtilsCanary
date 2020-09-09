import discord
from discord.ext import commands
import os
from modules import dev

s = os.path.basename(__file__)

class ErrorHandler(commands.Cog): #setup the module
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #same thing as client.event decorator
    async def on_command_error(self, ctx, error): #ctx is context of the command
        if isinstance(error, commands.MissingPermissions): #If the command executor does not have permission to run the command

            missingpermissionembed = discord.Embed( #discord embed method
                title = "Insufficient Permission!",
                description = "You do not have permission to execute this command.",
                color = discord.Color.red()
            )
            dev.log(s, f"user attempted to execute command but does not have permission")
            dev.log(s, f"{error}")

            await ctx.send(embed = missingpermissionembed)
        elif isinstance(error, commands.MissingRequiredArgument):

            missingargumentembed = discord.Embed(
                title="Invalid Arguments!",
                description="One or more of the command arguments you provided were invalid. Did you type out the command correctly? Do ?help to see a list of commands.",
                color = discord.Color.red()
            )
            dev.log(s, f"user attempted to execute command but the arguments provided were not valid")

            await ctx.send(embed=missingargumentembed)

        elif isinstance(error, commands.CommandNotFound):

            invalidcommandembed = discord.Embed(
                title="Invalid Command!",
                description="The command you entered is not a valid command. Run ?help to view a list of commands.",
                color = discord.Color.red()
            )
            dev.log(s, f"user attempted to execute command but it does not exist")
            dev.log(s, f"{error}")
            await ctx.send(embed=invalidcommandembed)

        elif isinstance(error, commands.NoPrivateMessage):
            return
#            botmissingpermsembed = discord.Embed(
#                title="I can't run this command!",
#                description="Due to the way you have configured my permissions, I am not allowed to run this command. Try dragging my role up in the role hierarchy!",
#                color = discord.Color.red()
#            )
#
#            await ctx.send(embed=botmissingpermsembed)


        else:


            unknownerrorembed = discord.Embed(

                title="Uh Oh! Something went wrong! :/",

                description=f"An unknown error has occured. If this keeps happening, contact an admin or developer and give them this info: `{error}`",

                color=discord.Color.red()

            )

            await ctx.send(embed=unknownerrorembed)

            dev.log(s, f"an unknown error occured")
            dev.log(s, f"{error}")

            errorlog = open("errors.log", "w+")

            errorlog.write(str(error))

            print (str(error))

            errorlog.close()


def setup(client):
    client.add_cog(ErrorHandler(client))