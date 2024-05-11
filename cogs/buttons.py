import disnake
from disnake.ext import commands


class ButtonView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="🎮", style=disnake.ButtonStyle.grey, custom_id="button1")
    async def button1(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        # Получаем роль по ее ID (необходимо указать конкретный ID вместо ...).
        role = interaction.guild.get_role(1142455444619673680)

        if role in interaction.author.roles:
            await interaction.author.remove_roles(role)
        else:
            await interaction.author.add_roles(role)

        await interaction.response.defer()


class ButtonsRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False

    @commands.command()
    async def buttons(self, ctx):
        view = ButtonView()

        # Получаем роль по ее ID (необходимо указать конкретный ID вместо ...).
        role = ctx.guild.get_role(1234197077303492628)

        embed = disnake.Embed(color=0x2F3136)
        embed.set_author(name="Мероприятия:")
        embed.description = f"{role.mention}\n\nНа сервере ежедневно проходят различные мероприятия. " \
                            "Для того чтобы быть в курсе предстоящих событий, нажми на кнопку ниже. " \
                            "Повторное нажатие убирает роль."
        embed.set_image(url="https://i.imgur.com/QzB7q9J.png")
        await ctx.send(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_ready(self):
        if self.persistent_views_added:
            return

        # Message ID сообщения, где будет кнопка, добавляется после отправки команды.
        self.bot.add_view(ButtonView(), message_id=1238207443733970999)


def setup(bot):
    bot.add_cog(ButtonsRole(bot))
