from discord.ext import commands
class RemoveAllChatMessages(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx):
        await ctx.channel.purge(limit=100)
class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")


def setup(client):
    client.add_cog(Ping(client))
    client.add_cog(RemoveAllChatMessages(client))
