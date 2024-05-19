import discord
from discord.ext import commands

class Guide(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("guide.py is ready")

    @commands.command()
    async def guide(self, ctx):
        embed_msg = discord.Embed(title="Guide to ApocalypseGambl", description="If you are stuck or don't know what to do, refer to this guide.", color=discord.Color.green())
        embed_msg.set_author(name=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar)
        embed_msg.add_field(name="How to get BOTTLE CAPS!!!", value="1. Beg to get caps using the **?beg** command.\n2. Gamble your earnings with the listed commands in the **Gambling** category. Refer to **?cmds**.\n3. BE NUMBER ONE.", inline=True)
        embed_msg.add_field(name="To start your epic journey, use the ?start command", value="You will have 8 bottle caps to start with.", inline=False)
        embed_msg.set_footer(text="use ?cmds for a list of the bot commands btw. GREEN CAPS ARE WORTH 4 BLUE CAPS!!!")

        await ctx.reply(embed = embed_msg)

async def setup(client):
    await client.add_cog(Guide(client))