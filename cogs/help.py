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
                title='/help category list:',
                description=f"list - Shows a list of all categories.\n\nall - Shows commands for all users\n\nmoderation - Shows commands for moderation\n\nadmin - Shows administration commands",
                color=0xffffff
            )

        elif category == "all":

            embed = disnake.Embed(
                title="All User commands list:",
                description=f"/help - Displays a list of all commands in the selected category\n\n/avatar - Shows an avatar (yours or the mentioned user)",
                color=0x04ff00
            )

        elif category == "moderation":

            embed = disnake.Embed(
                title="Moderation commands list:",
                description=f"/mute - Sends a member to timeout\n\n/kick - Kicks a member from this server\n\n/ban - Bans a member from the server (permanently or temporarily)",
                color=0x233afd
            )

        elif category == 'admin':

            embed = disnake.Embed(
                title="Admin commands list:",
                description="/clear - Clears the specified number of messages on the server",
                color=0xff5252
            )

        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
