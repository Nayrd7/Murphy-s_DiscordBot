import datetime

import disnake.embeds
from disnake.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(ban_members=True, administrator=True)
    async def ban(self, interaction, user: disnake.User, time: str, reason: str):

        time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        cool_time = disnake.utils.format_dt(time, style="R")

        bot_reason = f'Moderator: {interaction.author.name}. Reason: {reason}.'

        embed = disnake.Embed(
            title=f'Moderator used command "/ban"',
            description=f"Member <@{user.id}> was baned from this server.\n\nModerator: <@{interaction.author.id}>.\n\nReason: ****{reason}****.\n\nTime left: {cool_time}.",
            color=0xfa0000
        )

        await interaction.response.send_message(embed=embed)
        await user.ban(reason=bot_reason)


def setup(bot):
    bot.add_cog(Ban(bot))
