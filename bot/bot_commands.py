import json, requests, random, os
from os.path import join, dirname
from dotenv import load_dotenv


class spiritBot:
    dotenv_path = join(dirname(__file__), 'keys.env')
    load_dotenv(dotenv_path)
    RAPID_API_KEY = os.environ['RAPID_API_KEY']
    
    def yoda(self, input):
        strIn = ""
        for word in input:
            strIn += (" " + word)
        headers = {"Content-Type": "application/json"}
        api_url = "https://api.funtranslations.com/translate/yoda.json?text={}".format(strIn)
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return {
                "contents": {
                    "translated": 'Sorry we\'ve run out of API calls for funtranslations. Please try again in an hour :('}}
    
    def joke(self):
        url = "https://rapidapi.p.rapidapi.com/v1/joke"

        headers = {
            'x-rapidapi-host': "joke3.p.rapidapi.com",
            'x-rapidapi-key': "{}".format(self.RAPID_API_KEY)
        }

        response = requests.request("GET", url, headers=headers)
        json_body = response.json()
        joke =  json.dumps(json_body["content"]).replace("\"","").replace("\\", "")
        
        return joke

    def bible(self, params):
        url = "https://ajith-holy-bible.p.rapidapi.com/GetVerseOfaChapter"
        
        if len(params) == 3:
            if(params[1].isdigit() and params[2].isdigit()):
                querystring = {
                    "Verse": params[2],
                    "Book": params[0],
                    "chapter": params[1]
                }
            else:
                embedded_res = {
                    'title': 'Invalid verse :(',
                    'text': 'Sorry this Bible verse doesn\'t exist. Check for typos or if it\'s an error in the bot, please let the programmer know.',
                    'COM': 'bible',
                    'foot': ''
                }
                return embedded_res
            
        elif len(params) == 4:
            book = (params[0] + ' ' + params[1])
            querystring = {
                "Verse": params[3],
                "Book": book,
                "chapter": params[2]
            }
        headers = {
            'x-rapidapi-host': "ajith-holy-bible.p.rapidapi.com",
            'x-rapidapi-key': "{}".format(self.RAPID_API_KEY)
        }
        
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        book = json.dumps(response['Book'])
        if len(params) == 3:
            b = (book[1].upper() + book[2:].lower())
        elif len(params) == 4:
            b = (book[1:3] + book[3].upper() + book[4:].lower())
        cv = (json.dumps(response['Chapter']) + ":" + json.dumps(response['Verse']))
        text = json.dumps(response['Output']).replace("\"", "")
        bcv = (b + ' ' + cv).replace("\"", "")
        if text == 'Wrong slection!!! Please try again.':
            return {
            'title': 'Invalid verse :(',
            'text': 'Sorry this Bible verse doesn\'t exist. Check for typos or if you believe it\'s an error in the bot, please let the programmer know.',
            'COM': 'bible',
            'foot': '',}
        else:
            foot = 'BBE'        

        embedded_res = {
            'title': bcv,
            'text': "❝" + text + "❞",
            'COM': 'bible',
            'foot': foot
        }
        return embedded_res
    
    def bible_new(self, params):

        return params

    def command(self, input):
        RES = {
            'title': '',
            'text': '',
            'COM' : '',
        }
        INVALID_COMMAND = "Command not recognized. Type `!!help` to see the commands"
        ABOUT = 'Welcome to the InterVarsity Christian Fellowship Newark Discord server! My name is *Holy Spirit Bot* and I\'m here to help spread the love of God!'
        HELP = ("All commands start with `!!` and are followed by the command and any parameters: " +
        "\n**1.** `!!about`" + 
        "\n➙ **Description:** Tells you about *Holy Spirit Bot*!" +
        "\n**2.** `!!help`" + 
        "\n➙ **Description:** Displays all *Holy Spirit Bot* commands!" +
        "\n**3.**  `!!joke`" + 
        "\n➙ **Description:** Generates a random joke!" +
        "\n**4.**  `!!yoda <phrase>`" +
        "\n➙ **Description:** Converts your inputted phrase into yoda language!" + 
        "\n**5.**  `!!bible <book> <chapter> <verse>`" +
        "\n➙ **Description:** Gets the Bible verse of your choosing! As of right now the version is BBE, but more versions are on the way!" +
        "\n➙ **Ex:** `!!bible John 3 16`" +
        "\n➙ **Ex:** `!!bible 1 Timothy 3 4`"
        )
        YODA_FAIL = "Please enter a word or phrase to translate. (Ex: `!!yoda The quick brown fox jumped over the lazy dog`)"
        
        BIBLE_TOO_MANY = "You\'ve entered too many parameters! The command\'s parameters are as follows: \n\n`!!bible book chapter verse` \nEx: `!!bible Luke 1 1`"
        BIBLE_TOO_FEW = "You\'ve entered too few parameters! The command\'s parameters are as follows: \n\n`!!bible book chapter verse` \nEx: `!!bible Luke 1 1`"
        
        CMD_PAR = input.split()
        print("\nCMD_PAR: ", CMD_PAR)
        if CMD_PAR[0] == "!!":
            COMMAND = CMD_PAR[1].lower()
            print(COMMAND)
            if len(CMD_PAR) > 2:
                PARAMS = CMD_PAR[2:]
            else:
                PARAMS = ""
        else:
            COMMAND = CMD_PAR[0][2:].lower()
            print("COMMAND: " + COMMAND)
            if len(CMD_PAR) > 1:
                PARAMS = CMD_PAR[1:]
            else:
                PARAMS = ""
        
        RES['COM'] = COMMAND

        if COMMAND == "about":
            RES['title'] = 'About'
            if len(PARAMS) > 0:
                RES['text'] = "The command `about` doesn\'t need any parameters"
                return RES
            RES['text'] = ABOUT
            return RES
        elif COMMAND == "help":
            RES['title'] = 'Help'
            if len(PARAMS) > 1:
                RES['text'] = "The `help` command can take one parameter, a command, or it can take no parameters"
                return RES
            elif len(PARAMS) == 1:
                if PARAMS[0].lower() == 'about':
                    RES['text'] = "`!!about`: Tells you about *Holy Spirit Bot*!"
                    return RES
                elif PARAMS[0].lower() == 'joke':
                    RES['text'] = "`!!joke`: Returns a random joke."
                    return RES
                elif PARAMS[0].lower() == 'help':
                    RES['text'] = "`!!help <command>`: You're using it right now!"
                    return RES
                elif PARAMS[0].lower() == 'yoda':
                    RES['text'] = "`!!yoda <message>`: Translates your inputted message into yoda language!"
                    return RES
                elif PARAMS[0].lower() == 'bible':
                    RES['text'] = "`!!bible <book> <chapter> <verse>`: Displays the Bible verse inputted. :)"
                    return RES
                RES['text'] = "The command you need help for doesn\'t exist! Talk to the creator of this bot if you'd like to see new features added!"
                return RES
            RES['text'] = HELP
            return RES
        elif COMMAND == "joke":
            RES['title'] = 'Random joke!'
            if len(PARAMS) > 0:
                RES['text'] = "The `joke` command doesn't take any parameters. Try again with `!!joke`"
                return RES
            RES['text'] = self.joke()
            return RES
        elif COMMAND == "bible":
            RES['title'] = 'Incorrect number of parameters for `!!bible` :('
            if len(PARAMS) > 4:
                RES['text'] = BIBLE_TOO_MANY
                return RES
            elif len(PARAMS) < 3:
                RES['text'] = BIBLE_TOO_FEW
                return RES
            return self.bible(PARAMS)
        elif COMMAND == "yoda":
            RES['title'] = 'Yoda!'
            if len(PARAMS) == 0:
                RES['text'] = YODA_FAIL
                return RES
            else:
                RES['text'] = self.yoda(PARAMS)["contents"]["translated"]
                return RES
        else:
            RES['title'] = 'Invalid command :('
            RES['text'] = INVALID_COMMAND
            return RES
