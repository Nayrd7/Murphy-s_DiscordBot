import disnake.member
import disnake.embeds
from disnake.ext import commands


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()  # Комманда kick
    @commands.has_permissions(kick_members=True, administrator=True)
    async def kick(self, interaction, member: disnake.Member, *, reason):

        bot_reason = f'Модератор: {interaction.author.name}. Причина: {reason}.'

        embed = disnake.Embed(
            title=f'Модератор использовал комманду "/kick"',
            description=f"Участник ****<@{member.id}>**** был кикнут с сервера.\n\nМодератор: ****<@{interaction.author.id}>****.\n\nПричина: ****{reason}****.",
            color=0xfa0000
        )

        await interaction.response.send_message(embed=embed)
        await member.kick(reason=bot_reason)


def setup(bot):
    bot.add_cog(Kick(bot))
