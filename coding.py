import discord
from discord.ext import commands

import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Halo,saya adalah robot pecinta lingkungan♻️❤️')

@bot.command()
async def fakta(ctx):
    kumpulan_fakta =["⚠️Jumlah Sampah Tinggi: Indonesia menghasilkan sekitar 64 juta ton sampah per tahun, dengan sebagian besar berakhir di TPA atau mencemari lingkungan karena daur ulang masih rendah (sekitar 13-15%).",
                    "🍟Penyumbang Terbesar: Sampah makanan menjadi penyumbang terbesar, diikuti sampah plastik yang menempatkan Indonesia di peringkat atas negara penghasil sampah plastik.",
                    "🧷Plastik: Ancaman Abadi: Sampah plastik membutuhkan 100 hingga 500 tahun untuk terurai, mencemari lautan dan mengancam kehidupan laut, bahkan manusia menelan 5 gram plastik setiap minggu",
                    "☣️Dampak Pencemaran: Sampah melepaskan zat kimia berbahaya ke tanah dan air, sedangkan pembakaran sampah melepaskan dioksin dan materi berbahaya lainnya ke udara.",
                    "♻️Dampak Iklim: Dekomposisi sampah organik di TPA menghasilkan gas metana, gas rumah kaca kuat yang mempercepat pemanasan global."
                    ]
    fakta_random = random.choice(kumpulan_fakta)
    await ctx.send(fakta_random)

bot.run("TOKEN HERE")