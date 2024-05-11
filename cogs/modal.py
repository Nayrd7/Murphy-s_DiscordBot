import disnake
from disnake.ext import commands
 
 
class RecruitementModal(disnake.ui.Modal):
    def __init__(self, arg):
        self.arg = arg  # arg - это аргумент, который передается в конструкторе класса RecruitementSelect

        components = [
            disnake.ui.TextInput(label="Ваше имя", placeholder="Введите ваше имя", custom_id="name"),
            disnake.ui.TextInput(label="Ваш возраст", placeholder="Введите ваш возраст", custom_id="age")
        ]
        if self.arg == "moderator":
            title = "Набор на должность модератора"
        else:
            title = "Набор на должность ведущего"
        super().__init__(title=title, components=components, custom_id="recruitementModal")
 
    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        name = interaction.text_values["name"]
        age = interaction.text_values["age"]
        embed = disnake.Embed(color=0x2F3136, title="Заявка отправлена!")
        embed.description = f"{interaction.author.mention}, Благодарим вас за **заявку**! " \
                            f"Если вы нам **подходите**, администрация **свяжется** с вами в ближайшее время."
        embed.set_thumbnail(url=interaction.author.display_avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        channel = interaction.guild.get_channel(1238204591607119962)  # Вставить ID канала куда будут отправляться заявки
        await channel.send(f"Заявка на должность {self.arg} от {name} {interaction.author.mention} ({age} лет)")
 
 
class RecruitementSelect(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Модератор", value="moderator", description="Модератор сервера"),
            disnake.SelectOption(label="Ведущий", value="eventsmod", description="Ведущий мероприятий"),
        ]
        super().__init__(
            placeholder="Выбери желаемую роль", options=options, min_values=0, max_values=1, custom_id="recruitement"
        )
 
    async def callback(self, interaction: disnake.MessageInteraction):
        if not interaction.values:
            await interaction.response.defer()
        else:
            await interaction.response.send_modal(RecruitementModal(interaction.values[0]))
 
 
class Recruitement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistents_views_added = False
 
    @commands.command()
    async def recruit(self, ctx):
        view = disnake.ui.View()
        view.add_item(RecruitementSelect())
        # Тут можно добавть эмбед с описанием ролей
        await ctx.send('Выбери желаемую роль', view=view)
 
    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return
 
        view = disnake.ui.View(timeout=None)
        view.add_item(RecruitementSelect())
        self.bot.add_view(view, message_id=1238204822449164318)  # Вставить ID сообщения, которое отправится после использования с команда !recruit
 
 
def setup(bot):
    bot.add_cog(Recruitement(bot))