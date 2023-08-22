from disnake.ext import commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()  # Тестовая комманда ping
    async def clear(self, interaction, amount: int):

        await interaction.channel.purge(limit=amount + 1)
        await interaction.response.send_message(f"Administrator: <@{interaction.author.id}> - cleared {amount} messages.")


def setup(bot):
    bot.add_cog(Clear(bot))
