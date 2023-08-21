from disnake.ext import commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()  # Тестовая комманда ping
    async def clear(self, interaction):

        await interaction.response.send_message("Pong!")


def setup(bot):
    bot.add_cog(Clear(bot))
