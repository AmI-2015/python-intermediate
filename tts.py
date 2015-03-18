'''
Created on Mar 13, 2014

@author: Dario Bonino <dario.bonino@polito.it>

Copyright (c) 2014 Dario Bonino
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
'''
#!/usr/bin/python

import os

def say(text, language='en'):
    # prepare the command to fetch the mp3 file generated by gogle tts
    wget_line = 'wget -q -U Mozilla -O test.mp3 "http://translate.google.com/translate_tts?ie=UTF-8&tl=' + language + '&q=' + text + '"'

    # fetch the mp3
    os.system(wget_line)

    # play it (system dependent)
    os.system("mplayer -quiet -nolirc -msglevel all=-1 test.mp3")


def main():
    # the string to render as speech, initially empty
    string = ""
    while (string != "exit"):
        # get the next input
        string = raw_input("Insert text here:\n>")
        
        # if the given string is "exit" interrupt the loop and say goodbye
        if(string == "exit"):
            tts_text = "Goodbye!"
        else:
            # replace not allowed characters
            # TODO this shall be better accomplished filtering out all chars not allowed in a url-encoded parameter
            tts_text = string.replace(" ", "+")

        say(tts_text)
        
if __name__ == "__main__":
    # call the main function
    main()    
