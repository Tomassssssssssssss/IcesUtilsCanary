import discord
from discord.ext import commands
import os
from modules import dev

s = os.path.basename(__file__)

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


############################################################## BAN COMMAND BEGIN
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason = "unspecified"):
        dev.log(s, f"ban command called\ncheck for ban members permission")
        dev.log(s, f"ban members permission true\ngot all required arguments\n begin ban command execution")
        banembed = discord.Embed(
            title = "Member Banned",
            description = f"{member.mention} was banned from the server by {ctx.author.mention}. Reason: `{reason}`.",
            color = discord.Color.dark_red()
        )
        dev.log(s, f"create banembed")


        await ctx.send(embed = banembed)

        dev.log(s, f"send embed to chat")

        dm = await member.create_dm()

        dev.log(s, f"create dm with {member}")

        dmbanembed = discord.Embed(
            title = f"You have been banned!",
            description = f"You have been banned from `{ctx.guild.name}` by `{ctx.author}`. Reason: `{reason}`. If you feel the ban was unjustified, or you deserve a second chance, join this server and submit a ban appeal. https://discord.gg/N86JzKM",
            color = discord.Color.red()
        )
        dev.log(s, f"create banenbeddm")

        await dm.send(embed = dmbanembed)

        dev.log(s, f"send banembeddm to dm")

        await member.ban(reason = reason)

        dev.log(s, f"ban {member} for {reason}")
        dev.log(s, f"end ban command execution")
############################################################## BAN COMMAND END

############################################################## CLEARCHAT COMMAND BEGIN
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def clearchat(self, ctx, amount):
        dev.log(s, f"clearchat command called\ncheck for ban members permission")
        dev.log(s, f"ban members permission true\ngot all required arguments\n begin ban command execution")
        await ctx.channel.purge(limit = int(amount)+1)
        dev.log(s, f"purge {ctx.channel} with limit {amount}")
        clearchatembed = discord.Embed(
            title="Chat Cleared",
            description=f"The last `{amount}` messages were removed from the channel by {ctx.author.mention}.",
            color=discord.Color.green()
        )
        dev.log(s, f"create clearchatembed")
        await ctx.send(embed=clearchatembed)
        dev.log(s, f"send clearchatembed")
        dev.log(s, f"end clearchat command execution")
############################################################## CLEARCHAT COMMAND END

############################################################## UNBAN COMMAND BEGIN
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member, reason = "unspecified"):
        dev.log(s, f"unban command called\ncheck for ban members permission")
        dev.log(s, f"unban members permission true\ngot all required arguments\n begin unban command execution")

        ban_list = await ctx.guild.bans()

        dev.log(s, f"get ban list in guild")

        member_name, member_discriminator = member.split("#")

        dev.log(s, f"target is {member_name}#{member_discriminator}")

        for ban in ban_list:

            user = ban.user

            dev.log(s, f"get ban {user}")

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                dev.log(s, f"hit\nunban{member_name}#{member_discriminator}")
                unbanembed = discord.Embed(
                    title="Member Unbanned",
                    description=f"{member} was unbanned from the server by {ctx.author.mention}. Reason: `{reason}`.",
                    color=discord.Color.green()
                )
                dev.log(s, f"create unbanembed")
                await ctx.send(embed=unbanembed)
                dev.log(s, f"send unbanembed")
                dev.log(s, f"end unban command execution")
                return
############################################################## UNBAN COMMAND END

############################################################## KICK COMMAND BEGIN
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason = "unspecified"):
        dev.log(s, f"kick command called\ncheck for kick members permission")
        dev.log(s, f"kick members permission true\ngot all required arguments\n begin kick command execution")
        kickembed = discord.Embed(
            title = "Member Kicked",
            description = f"{member.mention} was kicked from the server by {ctx.author.mention}. Reason: `{reason}`.",
            color = discord.Color.red()
        )

        dev.log(s, f"create kickembed")

        await ctx.send(embed = kickembed)

        dev.log(s, f"send kickembed")

        dm = await member.create_dm()

        dev.log(s, f"create dm with {member}")

        dmkickembed = discord.Embed(
            title = f"You have been kicked!",
            description = f"You have been kicked from `{ctx.guild.name}` by `{ctx.author}`. Reason: `{reason}`.",
            color = discord.Color.red()
        )

        dev.log(s, f"create dmkickembed")

        await dm.send(embed = dmkickembed)

        dev.log(s, f"send dmkickembed to dm")

        await member.kick(reason = reason)

        dev.log(s, f"kick {member} for {reason}")
        dev.log(s, f"end kick command execution")
############################################################## KICK COMMAND END

############################################################## HIST COMMAND BEGIN

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def hist(self, ctx, user):
        dev.log(s, f"hist command called\ncheck for ban members permission")
        dev.log(s, f"hist members permission true\ngot all required arguments\n begin hist command execution")


############################################################## HIST COMMAND END

def setup(client):
    client.add_cog(Moderation(client))