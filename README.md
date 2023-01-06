# Civi
## Simple library to create level system to your discord bot 


# Here's example how to use the library

```py
from Ci.civ import Civi
import nextcord as discord
from nextcord.ext import commands

intex = discord.Intents.default()
intex.message_content = True
intex.guild_messages = True
intex.guilds = True
client = commands.Bot(command_prefix="-" , intents=intex)

@client.event
async def on_ready():
    print(client.user.name + " is ready !")

@client.event
async def on_message(message:discord.Message):
    Civi.update_level_data(message.guild.id , message.author.id)


@client.slash_command(name="info")
async def level(interaction ):
    guild = interaction.guild
    user = interaction.user
    xp = Civi.get_user_xp(guild.id , user.id)
    rank = Civi.get_user_rank(guild.id , user.id)
    level = Civi.get_user_level(guild.id , user.id)
    Embed = discord.Embed()
    Embed.description = f"Xp:{xp}\nRank:{rank}\nLevel:{level}"
    await interaction.send(embed=Embed)


client.run("YOUR TOKEN")
```
