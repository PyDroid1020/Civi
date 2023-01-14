# Civi
## Simple library to create level system to your discord bot 


# Here's example how to use the library

```py
from Ci.civ import Civi
import nextcord
from nextcord.ext import commands

Intents = nextcord.Intents.default()
Intents.message_content = True
Intents.guild_messages = True
Intents.guilds = True
client = commands.Bot(command_prefix="-" , intents=Intents)

@client.event
async def on_ready():
    print(client.user.name + " is ready !")

@client.event
async def on_message(message:nextcord.Message):
    Civi.update_level_data(message)


@client.slash_command(name="info")
async def user_info(interaction):
    guild = interaction.guild
    user = interaction.user
    xp = Civi.get_user_xp(guild.id , user.id)
    rank = Civi.get_user_rank(guild.id , user.id)
    level = Civi.get_user_level(guild.id , user.id)
    Embed = nextcord.Embed()
    Embed.description = f"Xp:{xp}\nRank:{rank}\nLevel:{level}"
    await interaction.send(embed=Embed)


client.run("YOUR TOKEN")
```

# Level options
```py
Civi.setup() # Use it in client on_ready event

Civi.update_level_data(message) # Use it in on_message event.

Civi.get_user_xp(guild_id , member_id) # Return user xp

Civi.get_user_level(guild_id , member_id) # Return user level

Civi.get_user_rank(guild_id , member_id) # Return user rank

Civi.set_user_xp(guild_id , member_id , xp) # Set user xp

Civi.add_user_xp(guild_id , member_id , xp) # Add more xp to user 

Civi.decrease_user_xp(guild_id , member_id , xp) # Decrease xp from user
```

# Settins Options
```py
Civi.settings.guild.reset_guild_data(guild_id) # Delete all guild data

Civi.settings.repair() # Fix Civi
```

# Install Civi
```
You can't now but you can download "civ" file in Ci/ folder and import it
```
