'''
Created on 18/03/2015

@author: Dario Bonino <dario.bonino@gmail.com>

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
from subprocess import Popen, PIPE
from mutagen import mp3
import time

def play(filename):
    
    #build the player
    player = Popen("mplayer -slave -quiet -nolirc -msglevel all=-1 -idle", stdin=PIPE, stdout=PIPE, shell=True)
    
    #load the mp3 file
    metadata = mp3.MP3(filename)
    
    # show audio data
    try:
        if(metadata.has_key('TIT2')):
            print "Title: %s"%metadata['TIT2'].text[0]
        if(metadata.has_key('TALB')):
            print "Album: %s"%metadata['TALB'].text[0]
        if(metadata.has_key('TCON')):
            print "Genre: %s"%metadata['TCON'].text[0]
        if(metadata.has_key('TPE2')):
            print "Artist: %s"%metadata['TPE2'].text[0]
    except:
        pass
    
    #play
    player.stdin.write("loadfile \"%s\"\n"%filename)

    #play for 10s
    time.sleep(10)
    
    #stop
    player.stdin.write("quit\n");

if __name__ == '__main__':
    play(r'blues.mp3') #r stands for raw string
    