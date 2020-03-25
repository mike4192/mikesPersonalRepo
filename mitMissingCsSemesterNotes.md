# Notes on MIT's The Missing Semester of your CS Education Notes

## The Shell
* ```$PATH``` is a list of directory paths the system will search through to find a command (such as ```echo``` or ```date```)
* ```which``` will show location and binary of the selected command, for example:
    * ```which echo``` will output ```/usr/bin/echo/```
* On linux, all paths start with forward slash
* ```mv``` takes two arguments: first is path or file to move, and second is path or file to be moved and/or renamed to
* ```cp``` takes two arguments: first is file to copy, and second is location and name of copied file
* ```rm``` is remove command. By default does not delete directory recursively, must be passed with ```rm -r``` to delete a directory with files or subdirectories
* ```man``` shows manual for a command, q to quit
* Angle brackets (```<``` and ```>```) allowing rewiring input and output streams. Left angle bracket means rewire input to program to come from a file or command, and right angle bracket rewires output of a program to go somewhere. Default output with no brackets is the terminal
* Double angle bracket, ```>>``` does append to other text
* ```tail``` prints end of text, can pass a argument such as ```tail -n1``` to only get last line of some text, like from ``` ls -l```
* ```sudo``` do as super user, run as root, only applies to first program/command
* ```sudo su``` will run shell as root (change from $ to # will indicate running as root)
