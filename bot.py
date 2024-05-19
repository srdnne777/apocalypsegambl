import discord
from discord import app_commands
from discord.ext import commands
import os
import json
import random
import asyncio

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())

@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Game('?guide for help!'))
   print("let's get bottle cap gambling")

@bot.command()
async def start(ctx, member:discord.Member=None):
    if member is not ctx.author:
        member = ctx.author

    with open("cogs/data.json", "r") as f:
        user_eco = json.load(f)

    if str(member.id) not in user_eco:
        user_eco[str(member.id)] = {}
        user_eco[str(member.id)]["Green_Caps"] = 1
        user_eco[str(member.id)]["Blue_Caps"] = 4
        user_eco[str(member.id)]["Total_Caps"] = 8

        with open("cogs/data.json", "w") as f:
            json.dump(user_eco, f, indent=4)   
        await ctx.reply(f"Congratulations {member.display_name} you have successfully initiated your crippling bottle cap gambling addiction!")
    elif str(ctx.id) in user_eco:
        await ctx.reply(f"{member.display_name} you already have a gambling addiction bud.")

@bot.command()
async def beg(ctx, member:discord.Member=None):
    if member is not ctx.author:
        member = ctx.author
    
    chance1 = random.randint(1,100)
    chance2 = random.randint(1,100)
    blue = random.randint(1,20)
    green = random.randint(1,4)

    with open("cogs/data.json", "r") as f:
        user_eco = json.load(f)

        if str(member.id) in user_eco:
            if chance1 < 75:
                if chance2 < 45:
                    determine  = random.randint(1,2)

                    if determine == 1:
                        await ctx.reply(f"You have been donated {blue} 🔵 Caps!")
                        user_eco[str(member.id)]["Blue_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + blue
                        user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                        with open("cogs/data.json", "w") as f:
                            json.dump(user_eco, f, indent=4) 
                    else:
                        await ctx.reply(f"You have been donated {green} 🟢 Caps!")
                        user_eco[str(member.id)]["Green_Caps"] = user_eco[str(member.id)]["Green_Caps"] + green
                        user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                        with open("cogs/data.json", "w") as f:
                            json.dump(user_eco, f, indent=4)
                else:
                   await ctx.reply(f"{member.display_name}, you have been caught trying to beg! Stupid zombie peasant ass!!! 🤣") 
            else:
                await ctx.reply(f"{member.display_name}, you have been caught trying to beg! Stupid zombie peasant ass!!! 🤣")
        else:
            await ctx.reply(f"{member.display_name} has yet to start their bottle cap gambling legacy!")
    
@bot.command(aliases=['bal'])
async def balance(ctx, member:discord.Member=None):
    with open("cogs/data.json", "r") as f:
        user_eco = json.load(f)

    if member is None:
        member = ctx.author
        if str(member.id) in user_eco:
            g_caps = user_eco[str(member.id)]["Green_Caps"]
            b_caps = user_eco[str(member.id)]["Blue_Caps"]
            total = user_eco[str(member.id)]["Total_Caps"]
            balance = discord.Embed(title=f"{member.display_name}'s balance", description="Viewing this user's balance", color=discord.Color.random())
            balance.set_author(name=f"{member}", icon_url=f"{member.avatar}")
            balance.add_field(name="🟢 Caps:", value=f"{g_caps}", inline=False)
            balance.add_field(name="🔵 Caps:", value=f"{b_caps}", inline=False)
            balance.add_field(name="Total Caps:", value=f"{total}", inline=False)
            await ctx.reply(embed = balance)
        else:
            await ctx.reply(f"You have yet to start your bottle cap gambling legacy! Use **?start** to begin.")
    elif member is not None:
        member = member
        if str(member.id) in user_eco:
            g_caps = user_eco[str(member.id)]["Green_Caps"]
            b_caps = user_eco[str(member.id)]["Blue_Caps"]
            total = user_eco[str(member.id)]["Total_Caps"]
            balance = discord.Embed(title=f"{member.display_name}'s balance", description="Viewing this user's balance", color=discord.Color.random())
            balance.set_author(name=f"{member}", icon_url=f"{member.avatar}")
            balance.add_field(name="🟢 Caps:", value=f"{g_caps}", inline=False)
            balance.add_field(name="🔵 Caps:", value=f"{b_caps}", inline=False)
            balance.add_field(name="Total Caps:", value=f"{total}", inline=False)
            await ctx.reply(embed = balance)
        else:
            await ctx.reply(f"{member.display_name} has yet to start their bottle cap gambling legacy!")

@bot.command(aliases=['flipacoin','coinf','cf'])
async def coinflip(ctx, type=None, amount=None, flipinp=None, member: discord.Member=None):
    if member is not ctx.author:
        member = ctx.author

    with open("cogs/data.json", "r") as f:
        user_eco = json.load(f)

    flip = random.randint(1,2)
    green_bonus = random.randint(2,4)
    blue_bonus = random.randint(2,8)

    if (str(member.id)) in user_eco:
        if type is None or type == "":
            await ctx.reply("Please enter either 'green' or 'blue' bottle caps to bet!")
            return
        elif type.lower() == "green":
            if amount is None or amount == "":
                await ctx.reply("Please specify an amount of bottle caps to bet!")
                return
            elif int(amount) > int(user_eco[str(member.id)]["Green_Caps"]):
                await ctx.reply(f"You cannot bet more green caps than what you have!")
                return
            else:
                if flipinp is None or flipinp == "":
                    await ctx.reply("Please specify either heads or tails to bet on!")
                    return
                
                if flipinp.lower() == "heads" and flip == 1:
                    reward = int(amount)*green_bonus
                    user_eco[str(member.id)]["Green_Caps"] -= int(amount)
                    user_eco[str(member.id)]["Green_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4) 
                    await ctx.reply(f"The coin showed heads, and you chose heads! You won {green_bonus}x your green caps! ({reward} 🟢 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return

                if flipinp.lower() == "tails" and flip == 2:
                    reward = int(amount)*green_bonus
                    user_eco[str(member.id)]["Green_Caps"] -= int(amount)
                    user_eco[str(member.id)]["Green_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"The coin showed tails, and you chose tails! You won {green_bonus}x your green caps! ({reward} 🟢 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if flipinp.lower() == "heads" and flip == 2:
                    user_eco[str(member.id)]["Green_Caps"] -= int(amount)
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply("The coin showed tails, but you chose heads! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if flipinp.lower() == "tails" and flip == 1:
                    user_eco[str(member.id)]["Green_Caps"] -= int(amount)
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply("The coin showed heads, but you chose tails! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
        elif type.lower() == "blue":
            if amount is None or amount == "":
                await ctx.reply("Please specify an amount of bottle caps to bet!")
                return
            elif int(amount) > int(user_eco[str(member.id)]["Blue_Caps"]):
                await ctx.reply(f"You cannot bet more Blue caps than what you have!")
                return
            else:
                if flipinp is None or flipinp == "":
                    await ctx.reply("Please specify either heads or tails to bet on!")
                    return
                
                if flipinp.lower() == "heads" and flip == 1:
                    reward = int(amount)*blue_bonus
                    user_eco[str(member.id)]["Blue_Caps"] -= int(amount)
                    user_eco[str(member.id)]["Blue_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4) 
                    await ctx.reply(f"The coin showed heads, and you chose heads! You won {blue_bonus}x your green caps! ({reward} 🔵 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return

                if flipinp.lower() == "tails" and flip == 2:
                    reward = int(amount)*blue_bonus
                    user_eco[str(member.id)]["Blue_Caps"] -= int(amount)
                    user_eco[str(member.id)]["Blue_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"The coin showed tails, and you chose tails! You won {blue_bonus}x your green caps! ({reward} 🔵 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if flipinp.lower() == "heads" and flip == 2:
                    user_eco[str(member.id)]["Blue_Caps"] -= int(amount)
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply("The coin showed tails, but you chose heads! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if flipinp.lower() == "tails" and flip == 1:
                    user_eco[str(member.id)]["Blue_Caps"] -= int(amount)
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply("The coin showed heads, but you chose tails! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
    else:
        await ctx.reply(f"{member.display_name} has yet to start their bottle cap gambling legacy!")

@bot.command(aliases=['dice','dr'])
async def diceroll(ctx, type=None, amount=None, sideinp=None, member: discord.Member=None):
    if member is not ctx.author:
        member = ctx.author

    with open("cogs/data.json", "r") as f:
        user_eco = json.load(f)

    side = random.randint(1,6)
    blue_bonus = random.randint(4,10)
    green_bonus = random.randint(1,6)

    if (str(member.id)) in user_eco:
        if type is None or type == "":
            await ctx.reply("Please enter either 'green' or 'blue' bottle caps to bet!")
            return
        elif type.lower() == "green":
            if amount is None or amount == "":
                await ctx.reply("Please enter an amount of bottle caps to bet!")
                return
            elif int(amount) > int(user_eco[str(member.id)]["Green_Caps"]):
                await ctx.reply("You cannot bet more Green caps than what you have!")
                return
            else:
                if sideinp == 1 and side == 1:
                    reward = int(amount)*green_bonus
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Green_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {green_bonus}x your bottle caps! ({reward} 🟢 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 1 and side != 1:
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if sideinp == 2 and side == 2:
                    reward = int(amount)*green_bonus
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Green_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {green_bonus}x your bottle caps! ({reward} 🟢 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 2 and side != 2:
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if sideinp == 3 and side == 3:
                    reward = int(amount)*green_bonus
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Green_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {green_bonus}x your bottle caps! ({reward} 🟢 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 3 and side != 3:
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if sideinp == 4 and side == 4:
                    reward = int(amount)*green_bonus
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Green_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {green_bonus}x your bottle caps! ({reward} 🟢 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 4 and side != 4:
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if sideinp == 5 and side == 5:
                    reward = int(amount)*green_bonus
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Green_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {green_bonus}x your bottle caps! ({reward} 🟢 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 5 and side != 5:
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if sideinp == 6 and side == 6:
                    reward = int(amount)*green_bonus
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Green_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {green_bonus}x your bottle caps! ({reward} 🟢 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 6 and side != 6:
                    user_eco[str(member.id)]["Green_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
        elif type.lower() == "blue":
            if amount is None or amount == "":
                await ctx.reply("Please enter an amount of bottle caps to bet!")
                return
            elif int(amount) > int(user_eco[str(member.id)]["Blue_Caps"]):
                await ctx.reply("You cannot bet more Blue caps than what you have!")
                return
            else:
                if sideinp == 1 and side == 1:
                    reward = int(amount)*blue_bonus
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Blue_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {blue_bonus}x your bottle caps! ({reward} 🔵 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 1 and side != 1:
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if sideinp == 2 and side == 2:
                    reward = int(amount)*blue_bonus
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Blue_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {blue_bonus}x your bottle caps! ({reward} 🔵 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 2 and side != 2:
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if sideinp == 3 and side == 3:
                    reward = int(amount)*blue_bonus
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Blue_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {blue_bonus}x your bottle caps! ({reward} 🔵 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 3 and side != 3:
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if sideinp == 4 and side == 4:
                    reward = int(amount)*blue_bonus
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Blue_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {blue_bonus}x your bottle caps! ({reward} 🔵 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 4 and side != 4:
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if sideinp == 5 and side == 5:
                    reward = int(amount)*blue_bonus
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Blue_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {blue_bonus}x your bottle caps! ({reward} 🔵 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 5 and side != 5:
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                
                if sideinp == 6 and side == 6:
                    reward = int(amount)*blue_bonus
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Blue_Caps"] += reward
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} and the dice rolled a {side}! Congrats, you won {blue_bonus}x your bottle caps! ({reward} 🔵 Caps)")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                elif sideinp == 6 and side != 6:
                    user_eco[str(member.id)]["Blue_Caps"] -= amount
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"You chose {sideinp} but the dice rolled a {side}! Better luck next time!")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
    else:
        await ctx.reply(f"{member.display_name} has yet to start their bottle cap gambling legacy!")

@bot.command(aliases=['conv'])
async def convert(ctx, type=None, amount=None, member: discord.Member=None):
    if member is not ctx.author:
        member = ctx.author

    with open("cogs/data.json", "r") as f:
        user_eco = json.load(f)

    if (str(member.id)) in user_eco:
        if type is None or type == "":
            await ctx.reply("Please enter either 'green' or 'blue' bottle caps to convert. Entering 'green' means you will convert existing blue caps to green caps, and entering 'blue' means you will convert existing green caps to blue caps.")
            return
        elif type == "green":
            if amount is None or amount == "":
                await ctx.reply("Please specify an amount of blue bottle caps to convert to green bottle caps! (Multiples of 4)")
            elif int(amount) > int(user_eco[str(member.id)]["Blue_Caps"]):
                await ctx.reply("You cannot convert more blue caps than you have!")
            elif int(amount) <= int(user_eco[str(member.id)]["Blue_Caps"]):
                if (int(amount) % 4) == 0:
                    user_eco[str(member.id)]["Blue_Caps"] -= int(amount)
                    user_eco[str(member.id)]["Green_Caps"] += int(amount) // 4
                    user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                    await ctx.reply(f"{member.display_name}, successfully converted {amount} 🔵 Caps into {int(amount) // 4} 🟢 Caps.")
                    with open("cogs/data.json", "w") as f:
                        json.dump(user_eco, f, indent=4)
                    return
                else:
                    await ctx.reply(f"Cannot convert {amount} 🔵 Caps into 🟢 Caps! (Each green cap is worth 4 blue caps!)")
        elif type == "blue":
            if amount is None or amount == "":
                await ctx.reply("Please specify an amount of green bottle caps to convert to blue bottle caps!")
            elif int(amount) > int(user_eco[str(member.id)]["Green_Caps"]):
                await ctx.reply("You cannot convert more green caps than you have!")
            elif int(amount) <= int(user_eco[str(member.id)]["Green_Caps"]):
                user_eco[str(member.id)]["Green_Caps"] -= int(amount)
                user_eco[str(member.id)]["Blue_Caps"] += int(amount) * 4
                user_eco[str(member.id)]["Total_Caps"] = user_eco[str(member.id)]["Blue_Caps"] + (user_eco[str(member.id)]["Green_Caps"] * 4)
                await ctx.reply(f"{member.display_name}, successfully converted {amount} 🟢 Caps into {int(amount) * 4} 🔵 Caps.")
                with open("cogs/data.json", "w") as f:
                    json.dump(user_eco, f, indent=4)
                return
    else:
        await ctx.reply(f"{member.display_name} has yet to start their bottle cap gambling legacy!")    

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start('MTI0MTQ2NjY1OTk4Njg2NjM0MA.GxgUpP.NouLMpO5irbvL5qQDKwAP8-fakefakefake')

asyncio.run(main())
