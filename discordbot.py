import discord
import MMmodel as mm

true_ = './True.csv'
fake_ = './Fake.csv'

X,Y = mm.preprocessing(fake_, true_)
model, tok = mm.modeling(X, Y)

client = discord.Client()

@client.event  
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('/TrueNews'):
        try:
            val = message.content[10:]
            result = mm.input_(model, val, tok)
            await message.channel.send(f"The given article headline or an article is {round(100*result,2)}% chances TRUE!")
        except:
            await message.channel.send("Please write your article headline or title with /TrueNews <Article>")

    print(f'{client.user} has connected to Discord!')

client.run("ODIwNTE2MTQ4NDYxODMwMjE2.YE2TNg.JRWLyMBgsILcpHOe0ZA5xvROS3Q")