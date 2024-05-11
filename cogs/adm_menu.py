import disnake
from disnake.ext import commands


class AmdmenuModal(disnake.ui.Modal):
    def __init__(self, arg):
        self.arg = arg  # arg - это аргумент, который передается в конструкторе класса RecruitementSelect

        title = 'Отправить пост:'

        components = [
            disnake.ui.TextInput(label="Название поста", placeholder="Введите название поста", custom_id="title"),
            disnake.ui.TextInput(label="Контент", placeholder="Введите текст...", custom_id="content"),
            disnake.ui.TextInput(label="ID канала для отправки", placeholder="Вставьте ID канала, в который хотите отправить пост", custom_id="channel_id")
        ]
        super().__init__(title=title, components=components, custom_id="recruitementModal")
 
    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        title = interaction.text_values["title"]
        content = interaction.text_values["content"]
        channel_id = interaction.text_values["channel_id"]

        embed = disnake.Embed(color=0x2F3136, title=f"{title}")
        embed.description = f"{content}"
        embed.set_thumbnail(url=interaction.author.display_avatar.url)

        channel = interaction.guild.get_channel(channel_id)  # Вставить ID канала куда будут отправляться заявки
        await channel.send(embed=embed)


class ButtonView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Отправить новый пост", style=disnake.ButtonStyle.grey, custom_id="")
    async def admmenu(self, button: disnake.ui.Button, interaction: disnake.Interaction):

        await interaction.response.defer()


class AmdmenuButton(commands.Cog):
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
        # Нужно будет скопировать ID сообщения и вставить вместо "...", после выполнения данных действий
        # необходимо перезапустить бота.
        self.bot.add_view(ButtonView(), message_id=1238207443733970999)


def setup(bot):
    bot.add_cog(AmdmenuButton(bot))
