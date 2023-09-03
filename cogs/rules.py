import disnake
from disnake.ext import commands


class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rules(self, ctx):

        embed = disnake.Embed(
            title="Server Rules:",
            description=f"# Conflicts:\n# 1. Insults/Humiliation/Threats towards the participants\n## mute 4 hours\n# 2. Inadequate/Toxic behavior\n## mute 1 day\n# 3. Breeding/Support for conflict situations\n## mute 7 days\n# 4. Provocation of participants to commit violations\n## ban\n# 5. Draining of members personal data\n## ban\n# 6. Excessive use of obscene language (more than 5 words per 5 messages)\n## mute 1 hour\n# 7. Insulting the relatives of the members\n## mute 7 days\n# 8. Discussion and publication of political and military topics, as well as provocative statements of their views on these topics, etc.\n## ban\n# 9. Outright harassment, slander, breeding false rumors about the participants of the server\n## ban\n# 10. Discord on the topic of race, nationality, etc.\n## mute 30 days\n# 11. Abuse of the rights of special roles, if any\n## removing the role\n# 12. Insulting the creator of the server / moderator (Exception: The Creator, the Moderator considered your message as a joke)\n## ban\n# 12. Noises/extraneous sounds interfering with participants in voice chat\n## mute before correction\n# 13. Using sound. devices without the approval of voice channel participants\n## mute 4 hours\n# Chat and communication:\n# 14. Using channels for other purposes\n## mute 1 hour\n# 15. Spam\n## mute 4 hours\n# 16. Flood \n## mute 3 hours\n# 17. Caps\n## mute 3 hours\n# 18. Publication and demonstration of any kind of NSFW content\n## ban\n# 19. Publication and demonstration of any kind of NSFL content\n## ban\n# 20. Nazism, fascism, etc.\n## ban\n# 21. Advertising\n## ban\n# 22. Publication of malicious materials\n## ban\n# 23. Publishing videos and links containing screamers\n## mute 30 days\n# 24. Publication/demonstration of extremist content on the server# ban\n# 25. Multiple mentions of server participants\n## mute 1 day",
            color=0xff0000
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Rules(bot))
