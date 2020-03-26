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
* If assigning a variable (e.g.: ```foo=bar```), must be no spaces between equal sign on both sides as spaces usually indicate arguments
* ```||``` and ```&&```: ```||``` can seperate two commands. If the first one returns false, the second one is executed, if the first one returns true, the second is **not** executed. For ```&&```, if the first fails, the second wont be executed. If the first succeeds, the second will be executed if it also succeeds
* Commands can be concatenated with `;`
* Can list out only files of a specific name or file extension with *, for example: ```ls *.sh``` will show only files ending in .sh in current dir
* To get output of program as string, prepend with \$ and put in parentheses. For example: ```$(date)```.  Utilize this in some script such as:
    ```bash
    echo "Today's date is $(date)" ```
* Dollar sign and other commands:
    * **`$0`**: Name of file
    * **`$1`**, `$3`: Argument input to file
    * **`$_`**: Argument to previous command
    * **`$?`**: Return code of previous command. 0 is good, 1 is failed (think C style program main return)
    * **`$@`**: All arguments into file
    * **`$$`**: Process ID number for current script
    * **`!!`**: Entire last command including arguments
* Curly braces, `{}` can be used to autoatically expand a command to multiple things. For example:
    ```bash
    convert image.{png,jpg}
    # Will convert to
    convert image.png image.jpg
    ```
* Can use `shellcheck` tool for debugging shell script files
* **`find`**
    * **`find . -name src -type d`**: Looks in current directory recurseively for a directory named src
    * **`find . -name "*.tmp" -exec rm {} \\;`**: finds files with .tmp extension and deletes them
* Find text inside files in some directory, for example, search for any files in directory recursively that have foobar
    ```bash
    grep -R foobar .
    ```



## Useful Tools
* **`tldr`**: practical example summary of programs/commands