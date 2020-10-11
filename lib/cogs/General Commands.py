import cogs
import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

class General_Commands(commands.Cog):   
    
        def __init__(self, client):
                self.client = client
                
        @commands.command(name='about', description="About the bot")
        async def about(self, ctx):
                try:
                         
                        embed = discord.Embed(
                                title = f'IVRY info',
                                colour = 0x9B59B6
                        )
                        embed.set_thumbnail(url=ctx.bot.user.avatar_url)

                        embed.add_field(name='Created by', value=f'I1470s#0396', inline=False)

                        embed.add_field(name='Status', value=f'Online 🟢', inline=False)

                        embed.add_field(name='Website', value=f'[Click Me](https://ivry.tk)', inline=False)

                        embed.add_field(name='Discord Server', value=f'[Click Me](https://discord.gg/ppn2U99)', inline=False)

                        embed.add_field(name='Known issues', value=f'.mute and member welcomes dont work on other servers this will work in (V.1.1)', inline=False)

                        embed.set_footer(
                        text=f"Version (V.1.0.7)")

                        await ctx.send(embed=embed)
                except Exception as e:
                        await ctx.send(f'{e}')

        @commands.command(name='credits', description="Bot credits")
        async def credits(self, ctx):
                try:
                         
                        embed = discord.Embed(
                                title = f'IVRY Credits',
                                colour = 0x9B59B6
                        )
                        embed.add_field(name=':keyboard: Developers', value=f'[i1470s#0396](https://ivry.tk)')
                        embed.add_field(name=':open_hands: Contributors:', value=f'[asianmin#2060](https://www.youtube.com/channel/UCWe_MB0vTXLjoXpp7D86ybA)')
                        embed.add_field(name=':books: Libraries', value=f'[Discord.py](https://github.com/Rapptz/discord.py)\n[Youtube_dl](https://github.com/ytdl-org/youtube-dl/)')
                        embed.add_field(name=':tools: Miscellaneous', value=f'[MIT(License)](https://opensource.guide/legal/)', inline=False)

                        await ctx.send(embed=embed)
                except Exception as e:
                        await ctx.send(f'{e}')

        @commands.command(name='donate', description="Donate to the bot")
        async def donate(self, ctx):
                try:
                         
                        embed = discord.Embed(
                                title = f'IVRY Donations',
                                colour = 0x9B59B6
                        )
                        embed.add_field(name=f'Donations keep us alive!:', value=f'[Click Me](https://discord.gg)')


                        await ctx.send(embed=embed)
                except Exception as e:
                        await ctx.send(f'{e}')

        @commands.command(name="userinfo", description="User info search")
        async def userinfo(self, ctx, member: discord.Member = None):
                if not member:  
                        member = ctx.message.author  
                embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                                        title=f"User Info - {member}")
                embed.set_thumbnail(url=member.avatar_url)

                embed.add_field(name="ID", value=member.id, inline=False)
                embed.add_field(name="Display Name", value=member.display_name, inline=False)

                embed.add_field(name="Created Account On", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

                await ctx.send(embed=embed)

        @commands.command(name='serverinfo', description="Info about the server")
        async def serverinfo(self, ctx):
                try:
                        count = 0

                        members = await ctx.guild.fetch_members().flatten()

                        for people in members:
                                if people.bot:
                                        count = count + 1
                        else:
                                pass

                        embed = discord.Embed(
                                title = f'{ctx.guild.name} info',
                                colour = 0x9B59B6
                        )
                        embed.set_thumbnail(url=ctx.guild.icon_url)

                        embed.add_field(name='Owner name', value=f'<@{ctx.guild.owner_id}>')
                        embed.add_field(name='Server ID', value=ctx.guild.id)

                        embed.add_field(name='Server region', value=ctx.guild.region)
                        embed.add_field(name='Members', value=ctx.guild.member_count)
                        embed.add_field(name='bots', value=count)

                        embed.add_field(name='Text Channels', value=len(ctx.guild.text_channels))
                        embed.add_field(name='Voice Channels', value=len(ctx.guild.voice_channels))

                        embed.add_field(name='Created On', value=ctx.guild.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))

                        await ctx.send(embed=embed)
                except Exception as e:
                        await ctx.send(f'{e}')

        @commands.command(name='hi', description="Hello :)")
        async def hi(self, ctx):
                await ctx.send(f'Hello :)')

        @commands.command(name='fucku', description="Try it :p")
        async def fucku(self, ctx):
                await ctx.send(f'No Fuck You')
                
                return

def setup(client):
    client.add_cog(General_Commands(client))