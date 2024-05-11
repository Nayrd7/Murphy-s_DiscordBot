import disnake
from disnake.ext import commands


class AdmmenuModal(disnake.ui.Modal):
    def __init__(self):

        components = [
            disnake.ui.TextInput(
                label='Введите ID канала',
                placeholder='ID канала',
                custom_id='id_channel',
            ),
            disnake.ui.TextInput(
                label='Введите название поста',
                placeholder='Название поста',
                custom_id='title',
            ),
            disnake.ui.TextInput(
                label='Введите содержимое поста',
                placeholder='Содержимое поста',
                custom_id='content',
            ),
            disnake.ui.TextInput(
                label='Введите цвет поста',
                placeholder='HEX формат:',
                custom_id='hex_color',
            )
        ]

        super().__init__(title='Отправка поста в канал', components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        id_channel = interaction.text_values["id_channel"]
        title = interaction.text_values["title"]
        content = interaction.text_values["content"]
        hex_color = interaction.text_values["hex_color"]

        embed = disnake.Embed(title=title, description=content, colour=int(hex_color, 16))

        channel = interaction.guild.get_channel(int(id_channel))

        await channel.send('@everyone', embed=embed)
        await interaction.response.send_message('Сообщение было отправлено', ephemeral=True)


class AdmmenuModalSend(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def admmenu(self, interaction: disnake.AppCmdInter):

        modal = AdmmenuModal()
        await interaction.response.send_modal(modal)


def setup(bot):
    bot.add_cog(AdmmenuModalSend(bot))
