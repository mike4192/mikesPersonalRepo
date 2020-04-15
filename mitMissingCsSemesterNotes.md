# General Linux Notes from MIT's The Missing Semester of your CS Education

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

## SSH Alias and Auto Password
You can create an alias and automatic login via an identity key for a host you frequently connect to. For example instead of always typing 

`ssh ubuntu@ubuntuRosPi.local`

and entering a password, you can instead just login via some alias name

`ssh upi`


First modify the file `~/.ssh/config`, add information such as the following:
```
Host your_alias_name
    User username
    Hostname remote.sshserver.com
    IdentityFile ~/.ssh/authorised_keys2
```
Where 'your_alias_name' is a short name for the connection, something like 'pi' for example. The identity file will be covered below.

Generate a rsa private and public key for the client machine (the computer used to connect to the remote). The public key will then be copied to the remote. On the client, generate a ssh key:

`ssh-keygen -t rsa`

Press enter twice to save to the default location and with no passphrase. Consider creating a new rsa key instead of reusing one. Copy the `id_rsa.pub` file to the remote, e.g. via scp. This command will still prompt for the remote's password:

`scp ~/.ssh/id_rsa.pub ubuntu@ubuntuRosPi.local:~/.ssh/authorized_keys`

Now you should be able to ssh to a remote by the shortcut name, and without having to input a password.

## Command Line Environment
* 

## tmux Usage
tmux is a terminal multiplexer. Some important keys. Note, for the shortcuts below, the syntax `C-b n` means hold Ctrl and the key b together, then let go and type the following key, n in this case.
* **`tmux`:** Start a new session
* **`tmux new -s NAME`:** Strt a tmux session with a name
* **`tmux ls`:** List existing tmux sessions
* **`tmux attach -t 0`:** Attach to existing tmux session with id 0
* **C-b ":** Create new pane splitting down
* **C-b %:** Create new pane splitting right
* **C-b [arrow_key]:** Move between panes
* **C-b d:** Detach from pane (but it still exists)
* **C-b c:** Create new tmux window
* **C-b p:** Switch to previous window
* **C-b n:** Switch to next window
* **C-d:** Exit and kill window
* **C-b z:** Make current pane fullscreen, command again to revert back
* **C-b C-[arrow_key]:** Resize a pane. This means press ctrl+b, let go, then press ctrl + an arrow key
* **C-b [:** Enter scrolling mode, go up and down with arrow keys or PgUp and PgDown, `q` to exit


## Debugging and Logging
* Most system and program logs placed under `/var/log/` 

