credits="""

ADD ME ON DISCORD a404#8596 if you need help
"""







print(credits)
import discord,json,os,random
from discord.ext import commands
import time  
from datetime import datetime
from discord.ext.commands import cooldown, BucketType

with open("config.json") as file: 
    info = json.load(file)
    token = info["token"]
    prefix = info["prefix"]

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Bot Running!")
@bot.command()
async def stock(ctx):
    stockmenu = discord.Embed(title="Account Stock",description="",color=0x9208ea,)
    for filename in os.listdir("Accounts"):
        with open("Accounts\\"+filename) as f:
            ammount = len(f.read().splitlines())
            name = (filename[0].upper() + filename[1:].lower()).replace(".txt","")
            stockmenu.description += f"*{name}* - {ammount}\n"
    await ctx.send(embed=stockmenu)

@bot.event
async def on_command_error (ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Cooldown!",description=f"Try again in {error.retry_after:.2f}s.",color=0x9208ea,timestamp = datetime.utcnow())
            await ctx.send(embed=em)


@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def gen(ctx,name=None):
    if name == None:
        lol = discord.Embed(title="Specify the account you want!",description="",color=0x9208ea,timestamp = datetime.utcnow())
        await ctx.send(embed=lol)
    else:
        name = name.lower()+".txt" 
        if name not in os.listdir("Accounts"):
            lol1 = discord.Embed(title=f"Account does not exist. `{prefix}stock`",description="",color=0x9208ea,timestamp = datetime.utcnow()) 
            await ctx.send(embed=lol1)
        else:
            with open("Accounts\\"+name) as file:
                lines = file.read().splitlines()
            if len(lines) == 0:
                lol2 = discord.Embed(title="These accounts are out of stock",description="",color=0x9208ea,timestamp = datetime.utcnow())
                await ctx.send(embed=lol2)
                
                
            else:
                with open("Accounts\\"+name) as file:
                    account = random.choice(lines)
                try:
                    lol3 = discord.Embed(title=f"{str(account)}",description="Here your account",color=0x9208ea,timestamp = datetime.utcnow())
                    lol3.set_footer(text="by zabtxd#2000 & xhze#1325")
                    lol3.set_thumbnail(url='https://cdn.discordapp.com/attachments/916248485379055656/927998700729565234/CE22A7D4-905C-40A8-96E4-00BFCC3E3A52.gif')
                    await ctx.author.send(embed=lol3)
                except:
                    lol4 = discord.Embed(title="Failed to send! Turn on ur direct messages",color=0x9208ea)
                    await ctx.author.send(embed=lol4)
                else:
                    embed = discord.Embed(
                    title="Account Generated!",
                    description="""Check your DMs\n 
                    Remember, sometimes the Account wont work""",
                    color=0x9208ea,
                    timestamp = datetime.utcnow()
                    )
                    embed.set_footer(text="by zabtxd#2000 & xhze#1325")
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/916248485379055656/927998700729565234/CE22A7D4-905C-40A8-96E4-00BFCC3E3A52.gif')
                    await ctx.send(embed = embed)
                    with open("Accounts\\"+name,"w") as file:
                        file.write("")
                    with open("Accounts\\"+name,"a") as file:
                        for line in lines:
                            if line != account:
                                file.write(line+"\n")
bot.run(token)
