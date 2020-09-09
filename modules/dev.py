import discord
from discord.ext import commands
from datetime import datetime
import os
import traceback

s = os.path.basename(__file__)

class dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def debuglog(self, ctx,):
        log(s, f"debuglog command called\ncheck for admin permission")
        log(s, f"admin permission true\ngot all required arguments\n begin debuglog command execution")
        dm = await ctx.author.create_dm()
        log(s, f"create dm with {ctx.author}")
        filesentembeddm = discord.Embed(
            title="Here you go!",
            description="Here's the dev log file you requested.",
            color=discord.Color.green()
        )
        log(s, f"create filesentembeddm")

        await dm.send(embed=filesentembeddm)

        log(s, f"send embed to dm")

        await dm.send(file=discord.File('devlog.txt'))

        log(s, f"upload file devlog.txt")

        filesentembed = discord.Embed(
            title="dev File Ready!",
            description="I have sent you a DM containing `devlog.txt`",
            color=discord.Color.green()
        )
        log(s, f"create filesentembed")
        await ctx.channel.send(embed=filesentembed)
        log(s, f"send embed to dm\nend getlog command execution")
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def stacktrace(self, ctx):
        log(s, f"stacktrace command called\ncheck for admin permission")
        log(s, f"admin permission true\ngot all required arguments\n begin stacktrace command execution")
        stacktraceembed = discord.Embed(
            title="Developer Stacktrace",
            description=f"```py"
                        f"{traceback.extract_stack(f=None)}"
                        f"```",
            color=discord.Color.green()
        )
        log(s, f"create stacktracembed")
        log(s, f"get stacktrace {traceback.extract_stack(f=None)}")
        log(s, f"send stacktrace to channel")
        await ctx.channel.send(embed = stacktraceembed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def forcewrite(self, ctx, filename : str, content : str):
        log(s, f"forcewrite command called\ncheck for admin permission")
        log(s, f"admin permission true\ngot all required arguments\n begin forcewrite command execution")
        try:
            writefile = open(filename, "w+")

            log(s, f"open {filename} in read/write mode")
            log(s, f"erased all file contents")

            writefile.write(content)

            log(s, f"write {content} to {filename}")

            currentfilecontentsembed = discord.Embed(
                title = "ForceWrite Successful",
                description = f"New file content: ```{str(writefile.read())}```",
                color = discord.Color.green()
            )
            log(s, f"create currentfilecontentsembed")
            await ctx.channel.send(embed = currentfilecontentsembed)
            log(s, f"send currrentfilecontentsembed to {ctx.channel}")
            writefile.close()
            log(s, f"close {filename}")
            return

        except FileNotFoundError:
            log(s, f"raise file not found error")
            filenotfoundembed = discord.Embed(
                title = f"ForceWrite Error",
                description = f"`{filename}` is not a valid file.",
                color = discord.Color.red()
            )

            log(s, f"create filenotfoundembed")

            await ctx.channel.send(embed = filenotfoundembed)

            log(s, f"send filenotfoundembed to {ctx.channel}")
            return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def forceread(self, ctx, filename: str):
        log(s, f"forceread command called\ncheck for admin permission")
        log(s, f"admin permission true\ngot all required arguments\n begin forceread command execution")
        try:
            readfile = open(filename, "r")

            log(s, f"open {filename} in read only mode")

            content = readfile.read()

            log(s, f"read {content} from {filename}")

            filecontentsembed = discord.Embed(
                title="ForceRead Successful",
                description=f"File content: `{content}`",
                color=discord.Color.green()
            )
            log(s, f"create filecontentsembed")
            await ctx.channel.send(embed=filecontentsembed)
            log(s, f"send filecontentsembed to {ctx.channel}")
            readfile.close()
            log(s, f"close {filename}")
            return

        except FileNotFoundError:
            log(s, f"raise file not found error")
            filenotfoundembed = discord.Embed(
                title=f"ForceRead Error",
                description=f"`{filename}` is not a valid file.",
                color=discord.Color.red()
            )

            log(s, f"create filenotfoundembed")

            await ctx.channel.send(embed=filenotfoundembed)

            log(s, f"send filenotfoundembed to {ctx.channel}")
            return







def log(scriptname : str, log:str):
    dl = open("devlog.txt", "a")
    dl.write(f"{datetime.now()}[{scriptname}] >>> {log}\n")
    print(f"{datetime.now()}[{scriptname}] >>> {log}")
    dl.close()



def setup(client):
    client.add_cog(dev(client))
