import disnake
from disnake.ext import commands


class Announcements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def ann(self, interaction, title, description, color_hex):

        color_hex = int(color_hex, 16)

        embed = disnake.Embed(
            title=f'{title}',
            description=f'{description}',
            color=color_hex
        )

        await interaction.channel.purge(limit=1)
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(Announcements(bot))
