import disnake
from disnake.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()  # Комманда help
    async def help(self, interaction, category="list"):

        category = category.lower()

        if category == "list":

            embed = disnake.Embed(
                title='/help категория "лист":',
                description=f"list - показывает список всех категорий.\n\nall - Показывает комманды для участников сервера\n\nmoderation - Показывает комманды для модерации\n\nadmin - Показывает комманды для администрации",
                color=0xffffff
            )

        elif category == "all":

            embed = disnake.Embed(
                title="Список всех комманд участников:",
                description=f"/help - Отображает список всех комманд в выбранной категории\n\n/avatar - Показывает аватар (ваш или упомянутого участника сервера)",
                color=0x04ff00
            )

        elif category == "moderation":

            embed = disnake.Embed(
                title="Список команд модерации:",
                description=f"/mute - Отправляет участника в мут\n\n/kick - Выгоняет участника с этого сервера\n\n/ban - Банит участника на сервере",
                color=0x233afd
            )

        elif category == 'admin':

            embed = disnake.Embed(
                title="Список команд администратора:",
                description="/clear - Очищает указанное количество сообщений на сервере",
                color=0xff5252
            )

        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
