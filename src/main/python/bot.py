import os
from dotenv import load_dotenv
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

def main():
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        print(str(message.author) + " said '" + str(message.content) + "'")

    client.run(TOKEN)

if __name__ == "__main__":
    main()