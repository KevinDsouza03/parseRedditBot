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
    for i in f:
        SRObjects.append({"SR" : i.strip(),"title" : "FirstIteration", "link" : "FirstIteration"})
    #populate array with sr's
    for i in range(1,1000):
        sleep(5)
        for iter in SRObjects:
            result = fs.Reddit_parse(iter)
            if (result != -1):
                embed=discord.Embed(title=iter["title"],description=iter["title"])
                embed.add_field(name="Link",value={iter["link"]})
                await ctx.channel.send(embed=embed)
                sleep(10)
            else:
                print("Sleeping")
                pass

#will define commands here, but functions in other. 

bot.run(token)

