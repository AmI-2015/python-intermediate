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
import os

#the main
def main():
    # the root_folder variable,initially empty
    root_folder = ""
    
    #loop until exit is typed
    while (root_folder != "exit"):
        
        # get the next input
        root_folder = raw_input("Insert the root folder:\n>")
        
        # if the given string is "exit" interrupt the loop and say goodbye
        if(root_folder == "exit"):
            print ("Goodbye!")
        else:
            #scan the folder for music files
            directory_scan(root_folder)
    
def directory_scan(root_folder):
    #file counter
    i = 1
    
    #walk down the folder, following symlinks
    for directory in os.walk(root_folder, followlinks=True):
        
        #iterate over files in the current directory            
        for filename in directory[2]:
            
            # check the file extension
            if filename.endswith('.mp3') or filename.endswith('.flac'):
                #print the filename
                print("%d %s"%(i,filename));
                i+=1
                
if __name__ == '__main__':
    main()