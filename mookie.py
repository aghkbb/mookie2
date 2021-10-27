from discord.ext import commands
from dotenv import load_dotenv
from foaas import foaas
from dict_api import get_meaning
import ast
import os
import re

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
USER_LOOKUP = ast.literal_eval(os.getenv("USER_LOOKUP"))

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print(f"{bot.user} is connected")

@bot.command()
async def players(ctx, *args):
    print("Entered .players command")

    arg_length = len(args)

    if arg_length == 0:
        await ctx.send("Please enter at least 1 argument\nPlease refer to .help")
        return
    
    if args[0] == "list":
        print("Listing all players")
        return
    
    if args[0] == "add":

        print("Adding player")

        if arg_length == 1:
            await ctx.send("Please enter a player to be added")
            return

        response_list = []

        for n in range(1, arg_length):
            print("in for loop: " + str(n))
            response_list.append(f"{args[n]} has been added")

        await ctx.send("\n".join(response_list))
        return
    
    if args[0] == "remove":
        print("Removing player")
        if arg_length == 1:
            await ctx.send("Please enter a player to be removed")
            return
            
        response_list = []

        for n in range(1, arg_length):
            print("in for loop: " + str(n))
            response_list.append(f"{args[n]} has been removed")

        await ctx.send("\n".join(response_list))
        return
    
    await ctx.send("Unknown command entered\nPlease refer to .help")
    return

@bot.command()
async def greet(ctx):
    print("Entered .greet command")
    await ctx.send(foaas(str(ctx.author)))

@bot.event
async def on_message(message):

    if "mook" in message.content.lower() or "mookie" in message.content.lower():

        if "what is a" in message.content.lower():
            m = re.search("what is (a|an) ([A-Za-z]*)\?", message.content.lower())
            searched_word = m.group(2)
            meaning = get_meaning(searched_word)
            if meaning:
                if searched_word[0] in ["a","e","i","o","u"]:
                    await message.channel.send("An " + searched_word + " is " + meaning)
                else:
                    await message.channel.send("A " + searched_word + " is " + meaning)
            else:
                await message.channel.send("A what?")

        else:
            name = USER_LOOKUP.get(str(message.author))
            await message.channel.send(foaas(name))
    
    await bot.process_commands(message)

bot.run(TOKEN)