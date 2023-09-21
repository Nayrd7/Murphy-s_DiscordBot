import datetime

import disnake.embeds
from disnake.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(ban_members=True, administrator=True)
    async def ban(self, interaction, user: disnake.User, reason: str):

        bot_reason = f'Модератор: {interaction.author.name}. Причина бана: {reason}.'

        embed = disnake.Embed(
            title=f'Модератор использовал комманду: "/ban"',
            description=f"Участник <@{user.id}> Был забанен на сервере.\n\nМодератор: <@{interaction.author.id}>.\n\nПричина: ****{reason}****.",
            color=0xfa0000
        )

        await interaction.response.send_message(embed=embed)
        await user.ban(reason=bot_reason)


def setup(bot):
    bot.add_cog(Ban(bot))
