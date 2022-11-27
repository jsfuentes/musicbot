import discord
from discord.ext import commands

from musicbot.settings import env

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description="DEEZ NUTS",
    intents=intents
)

@bot.event
async def on_ready():
    print("IM READY")

async def start_discord_bot():
    async with bot:
        await bot.add_cog(Music(bot))
        await bot.start(env('DISCORD_TOKEN'))