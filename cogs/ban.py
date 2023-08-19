import disnake.embeds
from disnake.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()  # Комманда ban
    @commands.has_permissions(ban_members=True, administrator=True)
    async def ban(self, interaction, member: disnake.Member, *, reason):

        embed = disnake.Embed(
            title=f"Member ****{member.name}**** was banned from the server",
            description=f"Moderator: ****{interaction.author.name}****\n\nReason: ****{reason}****",
            color=0xfa0000
        )

        await interaction.response.send_message(embed=embed)
        await member.kick(reason=reason)


def setup(bot):
    bot.add_cog(Ban(bot))
