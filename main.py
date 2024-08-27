import random
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

slad_weglowy = {}

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def mem(ctx):
    '''Wysyłą losowy mem'''
    images = os.listdir('images')
    image = random.choice(images)
    with open(f'images/{image}', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

@bot.command()
async def hello(ctx):
    '''Wita się'''
    await ctx.send(f'Cześć, jestem bot{bot.user}! Jeśli potrzebujesz pomocy wpisz $help :)')

@bot.command()
async def bye(ctx):
    '''Pa,pa'''
    await ctx.send(f"\\U0001f642")

rady = ['Oszczędzaj wodę poprzez naprawę przecieków i używanie pryszniców z niskim zużyciem wody.',
'Recyklinguj wszystkie możliwe materiały, takie jak papier, szkło i plastik.',
'Korzystaj z reusable worków zakupowych zamiast jednorazowych plastikowych.',
'Unikaj plastikowych słomek i używaj słomek ze stali nierdzewnej lub szkła.',
'Wybieraj produkty organiczne i lokalne, aby zmniejszyć emisję gazów cieplarnianych z transportu.',
'Korzystaj z publicznego transportu, roweru lub chodzenia pieszo, zamiast korzystać z samochodu.',
'Ogranicz zużycie energii poprzez wyłączanie świateł i urządzeń elektrycznych, gdy nie są potrzebne.',
'Sadź więcej roślin, aby zwiększyć ilość tlenu w powietrzu i zatrzymać erozję gleby.',
'Unikaj jedzenia mięsa w co najmniej jeden dzień w tygodniu, aby zmniejszyć emisję gazów cieplarnianych.',
'Upowszechniaj świadomość ekologiczną poprzez edukację innych i zachęcanie do podejmowania proekologicznych działań.',
'Naprawiaj i ponownie wykorzystuj przedmioty, zanim zdecydujesz się na zakup nowych.',
'Ogranicz zużycie jednorazowych plastikowych butelek, wybierając butelki wielokrotnego użytku.',
'Wybieraj produkty o minimalnym opakowaniu, aby zmniejszyć ilość odpadów.',
'Używaj energooszczędnych urządzeń, aby zmniejszyć zużycie energii elektrycznej.',
'Zbieraj i segreguj odpady organiczne do kompostowania.',
'Wspieraj lokalne inicjatywy ekologiczne i organizacje pozarządowe.',
'Utrzymuj opony pojazdów odpowiednio napompowane, aby zmniejszyć zużycie paliwa.',
'Unikaj używania chemikaliów i pestycydów w ogrodach, aby chronić środowisko naturalne.',
'Popieraj zakładanie parków miejskich i terenów zielonych w swojej okolicy.',
'Bądź eko-świadomy przy zakupie elektroniki, wybierając produkty o niższym zużyciu energii i dłuższym czasie użytkowania.']

@bot.command()
async def ecorada(ctx):
    '''Daje losową rade ecologiczną'''
    await ctx.send(random.choice(rady))
    
@bot.command()
async def ecomem(ctx):
    '''Wysyła mem o ecologi'''
    ecoimages = os.listdir('ecoimages')
    ecoimage = random.choice(ecoimages)
    with open(f'ecoimages/{ecoimage}', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

ecolink = ['https://pl.wikipedia.org/wiki/Globalne_ocieplenie',
           'https://pl.wikipedia.org/wiki/Efekt_cieplarniany',
           'https://pl.wikipedia.org/wiki/Ekologia',
           'https://pl.wikipedia.org/wiki/Ekologia_kulturowa',
           'https://pl.wikipedia.org/wiki/Kolektor_słoneczny',
           'https://pl.wikipedia.org/wiki/Samochód_elektryczny',
           'https://pl.wikipedia.org/wiki/Ekologia_informacji']

@bot.command()
async def ecolink(ctx):
    '''Wyśiwetla losowy link do ecopedi'''
    await ctx.send(random.choice(ecolink))

@bot.command()
async def oblicz(ctx, km: float, loty: int, posilki_miesne: int):
    """
    Oblicza roczny ślad węglowy na podstawie km, loty i posiłki mięsne.
    """
    # Przykładowe współczynniki emisji CO2
    emisja_samochod = 0.12  # kg CO2/km
    emisja_lot = 500        # kg CO2/lot
    emisja_posilek_miesny = 3 # kg CO2/posiłek mięsny

    # Obliczenie śladu węglowego
    calkowita_emisja = (km * emisja_samochod) + (loty * emisja_lot) + (posilki_miesne * emisja_posilek_miesny * 52)

    # Zapisanie wyniku do słownika
    user_id = ctx.author.id
    slad_weglowy[user_id] = calkowita_emisja

    # Wysłanie wyniku do użytkownika
    await ctx.send(f'Twój roczny ślad węglowy to około {calkowita_emisja:.2f} kg CO2.')

@bot.command()
async def moj_slad(ctx):
    """Wyświetla aktualnie przechowywany ślad węglowy użytkownika."""
    user_id = ctx.author.id
    if user_id in slad_weglowy:
        await ctx.send(f'Twój roczny ślad węglowy to {slad_weglowy[user_id]:.2f} kg CO2.')
    else:
        await ctx.send('Nie masz jeszcze obliczonego śladu węglowego. Użyj $oblicz, aby go obliczyć.')

bot.run("MTE5OTQwMDAzMjU1NDcxNzI0NA.Gdg-cH.sEx5AYgqlfWnBcb9vgkynjTlSz-kDOVILx4Xno")