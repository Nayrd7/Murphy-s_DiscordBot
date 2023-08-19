import disnake.embeds
from disnake.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()  # Комманда help
    async def help(self, interaction):

        embed = disnake.Embed(
            title="Commands list:",
            description=f"/help - Displays a list of Murphy's Bot commands\n/kick - Excludes the user from the given server\n/ban - ",
            color=0xffffff
        )

        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
