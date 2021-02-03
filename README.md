# Holy Spirit Bot

### Description
➙ This bot was designed for the InterVarsity Christian Fellowship's Newark chapter Discord server. It was inspired from a previous project I had worked on for a software engineering course I took at NJIT (hence the reason it doesn't use `@bot.command` decorators, this bot will definitely be overhauled at some point).  
➙ See: [chat-app](https://github.com/senorando/chat_app)  
➙ App: [def-not-discord](def-not-discord.herokuapp.com)
### Invite to your Server!
➙ [Invite Link](https://discord.com/api/oauth2/authorize?client_id=802002127434153986&permissions=0&scope=bot)
### How to Use
1. Clone this repo using `git clone https://github.com/senorando/holy-spirit-bot/`  
2. Create a file named `keys.env`  
3. Create a an account with RapidAPI and get your API Key  
4. Login to [Discord Developers](https://discord.com/developers) and create an application. Be sure to enable all intents and grab your bot token!  
5. Invite your bot to your server by navigating to the OAuth2 menu, selecting `bot` in the huge box, and navigating to the link underneath  
6. Format your `keys.env` file as follows:  
`BOT_TOKEN='paste_token_here'`  
`RAPID_API_KEY='paste_key_here'`  
**Keep your keys/tokens a secret, don't share them with anyone!**
7. Ensure `discord.py` is installed by running  
`pip install discord.py`  
**or**  
`pip3 install discord.py`
8. In the terminal type in `python3 bot/main.py` and once the terminal spits our `I am online` you're good to go!
### Technologies/Framework
➙ Python 3.8.1  
➙ discord.py  
➙ [Heroku](https://heroku.com)
### Main Features
➙ On a new member join, the bot will censor the new member's name by giving them a default name!  
➙ DMs a new member a pre made embedded message upon joining!  
### Commands:  
*All commands that produce an output will send it in their corresponding channel in an embedded format*  
*Once a command is sent, the bot will automatically delete the command message from the channel*  
1. `$bible <book> <chapter> <verse>`  
➙ **Description:** Returns the desired Bible verse. *Only supports BBE translation at the moment, more version options to come soon!*  
2. `$joke`  
➙ **Description:** Returns a random joke using a joke API from RapidAPI  
3. `$yoda <enter a phrase>`  
➙ **Description:** Uses Funtranslations Yoda API to translate an incoming phrase into yoda speak.  
4. `$help <command>[optional]`  
➙ **Description:** Displays all commands and a brief description of them. Takes in a command as an optional parameter to give a more specific description for it.  
5. `$about`  
➙ **Description:** Gives a brief description of the bot. Might get removed for lack of use.  
6. `.embed <title> <"a message surrounded by quotes"> <a color in hexadecimal>`  
➙ **Description:** Returns an embedded message with the author of the command appearing as the author of the embed. Currently supports only a single string for the title, will add support for longer strings in the near future.  
7. `.$welcome`  
`.$nickname`  
`.$roles`  
`.$discord`  
`.$thanks`  
➙ **Description:** Returns the specified embedded message that's been pre made for our specific Discord server. You may modify the embeds in `bot/embeds.py` or you may remove the commands from `bot/main.py`
### Help
➙ Should any further help be necessary, DM me on Discord @senorando#0799
### Changelog
**V1**  
**2/1/2021**  
➙ First official version of the bot. 
