from discord.ext import commands
import aiohttp
import discord

client = commands.Bot(command_prefix='.')

class NSFW(commands.Cog):   
    
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession(loop=self.client.loop)

    @commands.command(name='anal', description="Neko anal")
    @commands.is_nsfw()
    async def anal(self, ctx):
        
        async with self.session.get("https://nekos.life/api/v2/img/anal") as resp:
            nekos = await resp.json()

        
        embed = discord.Embed(title = f'Anal', colour=discord.Colour.purple())
        embed.set_image(url=nekos['url'])
        await ctx.send(embed=embed)

    @commands.command(name='boobs', description="Neko boobs")
    @commands.is_nsfw()
    async def boobs(self, ctx):
        
        async with self.session.get("https://nekos.life/api/v2/img/lewd") as resp:
            nekos = await resp.json()

        embed = discord.Embed(title = f'Boobs', colour=discord.Colour.purple())
        embed.set_image(url=nekos['url'])
        await ctx.send(embed=embed)

    @commands.command(name='hentaigif', description="Hentai gif")
    @commands.is_nsfw()
    async def gif(self, ctx):
        
        async with self.session.get("https://nekos.life/api/v2/img/classic") as resp:
            nekos = await resp.json()

        embed = discord.Embed(title = f'Hentaigif', colour=discord.Colour.purple())
        embed.set_image(url=nekos['url'])
        await ctx.send(embed=embed)

    @commands.command(name='hentai', description="Hentai")
    @commands.is_nsfw()
    async def hentai(self, ctx):
        
        async with self.session.get("https://nekos.life/api/v2/img/hentai") as resp:
            nekos = await resp.json()

        embed = discord.Embed(title = f'Hentai', colour=discord.Colour.purple())
        embed.set_image(url=nekos['url'])
        await ctx.send(embed=embed)

    @commands.command(name='lewd', description="Lewd nekos")
    @commands.is_nsfw()
    async def lewd(self, ctx):
        
        async with self.session.get("https://nekos.life/api/v2/img/lewd") as resp:
            nekos = await resp.json()

        embed = discord.Embed(title = f'Lewd', colour=discord.Colour.purple())
        embed.set_image(url=nekos['url'])
        await ctx.send(embed=embed)

    @commands.command(name='pussy', description="Neko pussy")
    @commands.is_nsfw()
    async def pussy(self, ctx):
        
        async with self.session.get("https://nekos.life/api/v2/img/pussy") as resp:
            nekos = await resp.json()

        embed = discord.Embed(title = f'Pussy', colour=discord.Colour.purple())
        embed.set_image(url=nekos['url'])
        await ctx.send(embed=embed)

    @commands.command(name='trap', description="Neko trap")
    @commands.is_nsfw()
    async def trap(self, ctx):
        
        async with self.session.get("https://nekos.life/api/v2/img/trap") as resp:
            nekos = await resp.json()

        embed = discord.Embed(title = f'Trap', colour=discord.Colour.purple())
        embed.set_image(url=nekos['url'])
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(NSFW(client))