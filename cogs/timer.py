import datetime

import disnake
from disnake.ext import commands


class Timer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def timer(self, interaction, time, title):

        time = datetime.datetime.now() + datetime.timedelta(days=int(time))
        cool_time = disnake.utils.format_dt(time, style="R")

        embed = disnake.Embed(
            title=f"{title}",
            description=f"{cool_time}",
            color=0xff0000
        )

        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(Timer(bot))
