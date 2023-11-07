import disnake
from disnake.ext import commands


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='приглашение', description='Оффициальная вечная ссылка приглашение на сервер дискорд Nayrd.')
    @commands.has_permissions()
    async def invite(self, interaction):

        embed = disnake.Embed(
            title=f'Ссылка приглашения на сервер:',
            description=f'https://discord.gg/A4jTGxJEYY',
            color=0xffffff
        )

        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(Invite(bot))