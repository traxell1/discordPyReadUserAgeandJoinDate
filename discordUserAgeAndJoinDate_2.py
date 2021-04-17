
import discord
intents = discord.Intents.default()
intents.members = True

discord_token = 'application/bot token'  # please change this to the appropriate bot token.

client = discord.Client(bot=True, reconnect=True, intents=intents)




@client.event
async def on_ready():
    serverID = 123456789  # please change this to the appropriate server ID.

    guild = client.get_guild(serverID)

    for member in guild.members:
        if "2021-04-" in str(member.created_at):  # filters out accounts that were created in april 2021. Year-Month-
            print("member {}. Created at {}. Joined on {}".format(member, member.created_at, member.joined_at))

client.run(discord_token)
