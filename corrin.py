import discord
import json
import os
from discord.ext import commands

TOKEN = 'NTIxNDYzNDc1MDg4Nzg1NDA4.Du8yjg.MedNBM84XG1ZISyL6mJbOpISiy8'
client = commands.Bot(command_prefix = '.')
os.chdir(r'C:\Users\tammy\Desktop\corrin')

@client.event
async def on_ready():
    print('Bot Online')

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    with open('users.json', 'w') as f:
        json.dump(users, f)
        
@client.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)

    #Code

    
     await update_data(users, message.author )
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

with open('users.json', 'w') as f:
        json.dump(users, f)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1

async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp

async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await client.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))

client.run(TOKEN)
