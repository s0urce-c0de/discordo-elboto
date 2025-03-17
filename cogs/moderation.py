import discord
from discord.ext import commands

class Moderation(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot: commands.Bot = bot	
  
  def cog_check(self, ctx: commands.Context):
    print(ctx.args, ctx.kwargs)
    return True

  @commands.command(aliases=["setnick"])
  #@commands.check_any(commands.has_permissions(manage_nicknames=True), commands.check(lambda ctx:[print(ctx.kwargs),True][1]))
  async def nick(self, ctx: commands.Context, member: discord.Member, nick: str):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention}', silent=True)

async def setup(bot: commands.Bot):
  await bot.add_cog(Moderation(bot))
