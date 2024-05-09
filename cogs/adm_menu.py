import disnake
from disnake.ext import commands


class AnnouncementsSelect(disnake.ui.select):
    def __init__(self):
        options = [
            disnake.SelectOption(label='Отправить новость', value='news', description='Описание'),
            disnake.SelectOption(label='Отправить анонс', value='announcement'),
            disnake.SelectOption(label='Отправить обновление', value='update')
        ]
        super().__init__(
            placeholder='Список', options=options, min_values=0, max_values=1)

    async def callback(self, interaction: disnake.MessageInteraction):
        if not interaction.values:
            await interaction.response.defer()
        else:
            await interaction.response.send_message(
                f'Что вы желаете прислать?'
            )


class Announcements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistence_views_added = False

    @commands.command()
    async def announcement(self, ctx):
        view = disnake.ui.View()
        view.add_item(AnnouncementsSelect())
        await ctx.send('Тест1', view=view)

    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistence_views_added:
            return

        view = disnake.ui.View(timeout=None)
        view.add_item(AnnouncementsSelect())
        self.bot.add_view(view)


def setup(bot):
    bot.add_cog(Announcements(bot))
