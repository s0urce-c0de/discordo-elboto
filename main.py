import discord, os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
  await bot.load_extension("cogs.moderation")
  print(f'Logged in as {bot.user} (ID: {bot.user.id})')
  print('------')

#@bot.command(aliases=["setnick"])
#async def nick(ctx: commands.Context, member: discord.Member, nick: str):
#  await member.edit(nick=nick)
#  await ctx.send(f'Nickname was changed for {member.mention}', silent=True)

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
