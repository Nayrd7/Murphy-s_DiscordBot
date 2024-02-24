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

        embed_member = disnake.Embed(
            title=f'Уведомление о бане',
            description=f'Вы были забанены на сервере ****{interaction.guild.name}****.\nПо причине: ****{reason}****\nМодератор: ****{interaction.author.name}****.'
        )

        await interaction.response.send_message(embed=embed)
        await user.send(embed=embed_member)
        await user.ban(reason=bot_reason)


def setup(bot):
    bot.add_cog(Ban(bot))
