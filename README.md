#Python Intermediate
-----

Exercises proposed in the Python Candies lesson about intermediate-level Python development and quick interaction prototyping.

The descriptions of each exercise are reported below: 

###Exercise 3 - Text To Speech

Write a program to make the computer «speak» text strings given by users on the console. The program must ask for new words until the word «exit» is entered, in such a case it should greet the user by saying «Goodbye».

*Suggestion:*

* check how the Google’s [tts service](http://translate.google.com/translate_tts?tl=en&q=hello) works

###Exercise 1 - System metrics

Write a program to provide a set of system metrics :

* the current load average,
* the operating system version, name, architecture,
* the total and the free memory
* Add some information on CPU and disk usage

Monitor the CPU percentage value and trigger a vocal warning if the CPU goes over a given threshold, e.g., 10%.

*Suggestion:*

* The ```psutil``` module offers system-independent access to the O.S. performance metrics


###Exercise 2 - Music crawler

Write a program that, given a starting folder, crawls all the folder sub-directories to find music files.

* Root folders are provided at the program prompt, on the command line
* Typing the word «exit» stops the program execution 

*Suggestion:*

* The os module allows to access operating system facilities (e.g., bash commands)
* Consider .mp3 and .flac files only


###Exercise 4 - Mp3 Player

Write a program for playing a given mp3 audio file.

*Suggestion:*

* Exploit the mplayer software as in the Text To Speech exercise


###Exercise 5 - Vocal mail fetch

Write a program that:

* Monitors your inbox folder for unseen messages
* Provides a vocal summary of newly received messages including the message count, and for each message the sender(s) and the title

*Suggestion:*

* Assume that the mail server is accessible through IMAP
* The Python modules that enable mailbox access and mail reading are: imaplib and email
