#Improved Redge after more experience
import functionheaders as fs
from functionheaders import * 

token = 'MTAxMjc3MjM2Mzc3NzA5MzcxMg.G3Y6pR.Zfxjr91X4kAz7spTheY6nxLNYd4TKrGHQWeahA'
#https://discord.com/api/oauth2/authorize?client_id=921811125799125023&permissions=527744384064&scope=bot 


intents = discord.Intents.all()
intents.members = True #New intents for discord bots. Can use this many times
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def Start(ctx):
    i = 0
    SRObjects = []
    f = open("sr.txt")
    for i in f.readline():
        SRObjects.append({f.readline(),"FirstIteration","FirstIteration"})
    #populate array with sr's
    for i in range(1,1000):
        for iter in SRObjects:
            result = fs.Reddit_parse(iter)
            if (result != -1):
                embed=discord.Embed(title=iter.title,description=iter.SR)
                embed.add_field(name="Link",value={iter.link})
                await ctx.channel.send(embed=embed)
                sleep(10)
            else:
                sleep(15)
#will define commands here, but functions in other. 

bot.run(token)

