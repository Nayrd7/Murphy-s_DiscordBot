import datetime

import disnake
from disnake.ext import commands


class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def mute(self, interaction, member: disnake.Member, time: str, reason: str):
        time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        await member.timeout(reason=reason, until=time)
        await interaction.response.send_message(f"Timed out {member.mention} for {time} for {reason}", ephemeral=True)


def setup(bot):
    bot.add_cog(Mute(bot))
