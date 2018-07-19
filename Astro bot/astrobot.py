#Astrobot by Astedroid

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord.voice_client import VoiceClient

startup_extensions = ["Music"]
bot = commands.Bot(command_prefix='/')

class Main_Commands():
    def __init__(self, bot) :
        self.bot = bot

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{} : {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

@bot.event
async def on_member_join(member):
    channel = discord.Object("405440715510775808")
    msg = "{0}, wellcome to **{1}!**".format(member.mention, member.server.name)
    await bot.send_message(channel, msg)

@bot.event
async def on_member_remove(member):
    channel = discord.Object("405440715510775808")
    msg = "**{0}** has leaved **{1}**. Bye bye. We'll miss you...".format(member.name, member.server.name)
    await bot.send_message(channel, msg)

@bot.event
async def on_ready():
    print ("Ready when you are. I am so glad to help ya!")
    print ("I am runing on:" + bot.user.name)
    print ("with the ID:" + bot.user.id)

@bot.command (pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!")
    print ("User has pinged!")

@bot.command(pass_context=True)
async def info (ctx, user: discord.Member):
    await bot.say("The username is: {}".format(user.name))
    await bot.say("The user's ID is: {}".format(user.id))
    await bot.say("The user's status is: {}".format(user.status))
    await bot.say("The user's highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}" .format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya looser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Newer come back!".format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
async def embedtest(ctx):
    embed = discord.Embed(title="test", description="My name is Jeff.",color=0x00ff00)
    embed.set_image(url="https://assets.materialup.com/uploads/5c9b5df3-df44-4172-aa01-057c9280665b/preview")
    embed.set_footer(text="This is a footer")
    embed.set_author(name="Astedroid")
    embed.add_field(name="This is a field", value = "no it isn't", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(title="Invite", description="There's the link to invite me, into your server! :wink:",color=0x4bdda2)
    embed.add_field(name="https://discordapp.com/api/oauth2/authorize?client_id=453108353095303189&permissions=8&scope=bot", value = "link", inline=True)
    await bot.say(embed=embed)

@bot.command (pass_context=True)
async def zoom(ctx):
    await bot.say("**You zoomed in, and now you realize that it didn't bring you any further. You stop zooming.**")

@bot.command (pass_context=True)
async def call(ctx):
    await bot.say("**:iphone: You try to call a random number. You hear a quiet voice saying: ``Hello?`` and ask that person how their day was. You only hear an awkward silence and you end the conversation.**")

bot.run("NDUzMTA4MzUzMDk1MzAzMTg5.DfaQ4g.3H5Fx0-EiTROIZjJa0-xy-6I7ps")