import discord
import asyncio
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, MissingPermissions, MissingRequiredArgument
import sqlite3
import sys
import traceback
bot = commands.Bot(command_prefix= "xp!")
#bot.remove_command('help')
@bot.event
async def on_ready():
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS userconfiguration(
        user_id TEXT,
        api_token TEXT
        )
        ''')
    print("Bot Ready")
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(bot.user.id))
    change_status.start()

initial_extension = ['cogs.admin',
                     'cogs.pterylink',
                     'cogs.info',]
if __name__ == '__main__':
    for extension in initial_extension:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed To Load {extension}",file=sys.stderr)
            traceback.print_exc()
@tasks.loop()
async def change_status():
    emmem=bot.guilds
    sum1=0
    for s in emmem:
        sum1+=len(s.members)
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Plethonode Pterodactyl Panel | v0.7"))
    await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Activity(name=f"{len(bot.guilds)} servers | {sum1} Users", type=discord.ActivityType.watching))
    


bot.run('BOT_TOKEN')
