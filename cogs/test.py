import disnake
from disnake.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='тест', description='Публикация вашего сообщения в новостной канал.')
    @commands.has_permissions(administrator=True)
    async def test(self, interaction, title=commands.Param(name='заголовок', description='Заголовок публикации'), description=commands.Param(name='сообщение', description='Текст публицкации'), color_hex=commands.Param(name='цвет', description='Цвет сообщения в HEX')):

        color_hex = int(color_hex, 16)

        embed = disnake.Embed(
            title=f'{title}',
            description=f'{description}',
            color=color_hex
        )

        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(Test(bot))