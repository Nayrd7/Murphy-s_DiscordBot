import datetime

import disnake
from disnake.ext import commands


class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(mute_members=True, administrator=True)
    async def mute(self, interaction, member: disnake.Member, time: str, reason: str):
        time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        cool_time = disnake.utils.format_dt(time, style="R")
        embed = disnake.Embed(
            title=f'Administrator used command "/mute"',
            description=f"Member <@{member.id}> was timed out.\n\nModerator: <@{interaction.author.id}>.\n\nReason: ****{reason}****.\n\nTime left: {cool_time}.",
            color=0xfa0000
        )

        await member.timeout(reason=reason, until=time)
        await interaction.response.send_message(embed=embed)

    @commands.slash_command()
    @commands.has_permissions(mute_members=True, administrator=True)
    async def unmute(self, interaction, member: disnake.Member):

        embed = disnake.Embed(
            title=f'Administrator used command "/unmute"',
            description=f"Member <@{member.id}> was untimed out\n\nModerator: <@{interaction.author.id}>",
            color=0xfa0000
        )

        await member.timeout(reason=None, until=None)
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Mute(bot))
