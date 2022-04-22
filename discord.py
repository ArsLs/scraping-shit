import discord
import time


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))



def client_init():
    token = ''
    with open('token.txt') as f:
        token = f.readline()
    # time.sleep(0.1)

    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.__contains__('$hello'):
            await message.channel.send('Hello!')

    client.run(token)



