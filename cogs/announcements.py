import disnake
from disnake.ext import commands


class Announcements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ann(self, ctx, title, description, color_hex):

        color_hex = int(color_hex, 16)

        embed = disnake.Embed(
            title=f'{title}',
            description=f'{description}',
            color=color_hex
        )

        await ctx.channel.purge(limit=1)
        await ctx.send('> @everyone', embed=embed)


def setup(bot):
    bot.add_cog(Announcements(bot))
