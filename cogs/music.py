import disnake
from disnake.ext import commands


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='not_works', description='not_works')
    @commands.has_permissions(administrator=True)
    async def music(self, interaction):

        embed = disnake.Embed(
            title=f'not_works',
            description=f'not_works',
            color=0xffffff
        )

        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(Music(bot))