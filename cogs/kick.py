import disnake.member
import disnake.embeds
from disnake.ext import commands


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()  # Комманда kick
    @commands.has_permissions(kick_members=True, administrator=True)
    async def kick(self, interaction, member: disnake.Member, *, reason):

        embed = disnake.Embed(
            title=f"Member ****<@{member.id}>**** was kicked from the server",
            description=f"Moderator: ****<@{interaction.author.id}>****\n\nReason: ****{reason}****",
            color=0xfa0000
        )

        await interaction.response.send_message(embed=embed)
        await member.kick(reason=reason)


def setup(bot):
    bot.add_cog(Kick(bot))
