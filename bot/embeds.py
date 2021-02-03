import discord
'''
    discord.Embed Parameters ALL PARAMETERS ARE OPTIONAL
        title = string              The title of the embed
        url = url                   The url to link the title
        description = string        The body of the embed
        color = 0x000000            Hexadecimal color code
        image = url                 The url of an image to display at the bottom
        
'''
THUMBNAIL = {
    'DM': 'https://img.icons8.com/dusk/2x/confetti.png',
    'WELCOME': 'https://images-ext-1.discordapp.net/external/L1ha170QumlvFo7KCNiaC-DU8RRJ9A0GhrfbsqJHJK4/https/media.discordapp.net/attachments/757695156957872149/804554651143897143/IV_Logo.png',
    'NICKNAME': 'https://images-ext-1.discordapp.net/external/OT4X1bzI8Zcsbzg8OjiUYpL7N7kzbfQkQRWOfuvUAOE/https/img.icons8.com/dusk/2x/employee-card.png',
    'DISCORD': 'https://images-ext-1.discordapp.net/external/vrirdmSgcCSfPfuB0zyfSM8MxuD72FhrS_GNu0owPig/https/images-ext-1.discordapp.net/external/aN0rLP_s5UfLRRdKX3Lhp848RvZ_pMtU9G2876ma204/https/img.icons8.com/fluent/2x/discord-logo.png',
    'ROLES': 'https://images-ext-1.discordapp.net/external/fTrRalnTwlCJpsbDu_0Ns8Iz0pkEFEX4IyM4qM9gfN0/https/images-ext-1.discordapp.net/external/d3Ji0WaGhi6n7AUlKqeSL0-UiUKo9QKSAYC5knw5lZw/https/images-ext-2.discordapp.net/external/Zf9Lti5gDeNab0xXDteyw2WzqRvhht_Fqm__Ow0M9bg/https/images-ext-2.discordapp.net/external/t-RNfdquJyMqS1BeY9vYKEknYHFco7WCeo6grSp5ADk/https/img.icons8.com/dusk/2x/students.png',
    'THANKS': 'https://images-ext-1.discordapp.net/external/FPUdKP2oWk8OdQuEkub0COJK5EkSlb_0E1i3aae6bDE/https/images-ext-1.discordapp.net/external/-32_vOfQMKaWfe_iynWybiH4CKGDQ9wYEftHFi-UlAo/https/media.discordapp.net/attachments/757695156957872149/805230289739448351/bread_and_wine.png',}

DM = discord.Embed(
    title = 'Thanks for joining the InterVarsity Newark Discord! 🙌',
    description = ('Hi there, my name is **Holy Spirit Bot**!' +
        '\n\nIf this is your first time on Discord, I\'d like to personally welcome you to our community.' +
        '\n\nHere at InterVarsity we believe that everyone is loved by God and we wish to spread His love to every student we meet on our Newark campus' +
        '\n\n**Server Rules**' +
        '\n**1.** We\'re all here to spread God\'s love so please avoid silly theological debates 😕' +
        '\n**2.** This server is here to serve you! Spread Jesus, have fun, and share testimonies! 🔥' +
        '\n**3.** Most importantly keep it clean and respectful. ❤' +
        '\n**4.** If you haven\'t noticed already, I\'ve changed your nickname within the server so please change it to your actual name!🤭' +
        '\n\n➙ Once you\'ve agreed to the rules in our [welcome channel](https://discord.gg/mxvTcgwf2n), head over to our [roles channel](https://discord.gg/KKZzjq2D8u) and select your school!' +
        '\n➙ After that, share with us your favorite Bible verse by going into the [general channel](https://discord.gg/XQrHFugAGE) and typing the following:' +
        '\n➙ `$bible book chapter verse` ***note:*** *substitute the values of \'book,\' \'chapter,\' and \'verse\'*'),
    color = 0x00f1ff)
DM.set_thumbnail(url = THUMBNAIL['DM'])

WELCOME = discord.Embed(
    title = 'Welcome to the InterVarsity Christian Fellowship Newark Discord Server!',
    description = '**Rules**'+
                '\n**1.** We are here to support each other and build unity in Christ, so let’s try to refrain from silly theological debates. 🥴'+
                '\n**2.** Spread Jesus, have fun, and share testimonies! This chat is here to serve you, encourage you, and ultimately draw you closer to Jesus! ✝ So share as much as you want!'+
                '\n**3.** Keep it clean, respectful, and with the love of Christ! ❤🔥',
    color = 0x00ffff,)
WELCOME.set_thumbnail(url = THUMBNAIL['WELCOME'])

NICKNAME = discord.Embed(
    title =  'Please Change Your Nickname!',
    description = 'Being as we want to keep things clean in this server we would like it if everyone would change their name upon joining 🙏'+
                '\n\nFrom the right side of your screen, simply right click on yourself and click `Change Nickname`'+
                '\n\nPlease change it to your first and last name so we may be able to identify who you are'+
                '\n\nYour name change will only be visible in this server so don\'t worry about revealing your name if you\'re in other Discord servers!',
    color = 0xff9a00,)
NICKNAME.set_thumbnail(url = THUMBNAIL['NICKNAME'])
NICKNAME.set_footer(text = 'Thank you! 😇')

ROLES = discord.Embed(
    title = 'Tell Us Which School You Go To!',
    description = 'Visit the [roles channel](https://discord.gg/KKZzjq2D8u) to show us what school you go to and receive a cool color when you chat! God bless you!',
    color = 0xff9a00,)
ROLES.set_thumbnail(url = THUMBNAIL['ROLES'])

DISCORD = discord.Embed(
    title = 'Discord Link',
    url = 'https://discord.gg/mxvTcgwf2n',
    description = 'Come one, come all! Help us give others the opportunity to know Jesus :)',
    color = 0xff9a00,)
DISCORD.set_thumbnail(url = THUMBNAIL['DISCORD'])

THANKS = discord.Embed(
    title = 'Join us in fellowship!',
    description = 'To access the rest of the server and join us in fellowship, click on the bread and wine below! Enjoy your time and God bless you!',
    color = 0x00ffff,)
THANKS.set_thumbnail(url = THUMBNAIL['THANKS'])