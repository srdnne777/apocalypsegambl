import discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("commands.py is ready")

    @commands.command()
    async def cmds(self, ctx):
        embed_msg = discord.Embed(title="List of commands", description="Provided are a list of commands within their specific categories.", color=discord.Color.green())
        embed_msg.set_author(name=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar)
        embed_msg.add_field(name="Help commands:", value="?guide\n?cmds", inline=False)
        embed_msg.add_field(name="Start your journey:", value="?start", inline=False)
        embed_msg.add_field(name="Gain money:", value="?beg", inline=False)
        embed_msg.add_field(name="Money management:", value="?balance\n?convert [green/blue] [amount] (type selected will be caps type to convert to)", inline=False)
        embed_msg.add_field(name="Gambling:", value="?coinflip [green/blue] [amount] [heads/tails]\n?dice [amount] [number (1-6)]", inline=False)
        embed_msg.set_footer(text="you can set [amount] fields to all, max or maximum.")

        await ctx.reply(embed = embed_msg)

async def setup(client):
    await client.add_cog(Commands(client))