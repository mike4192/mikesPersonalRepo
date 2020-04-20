

# Installation Steps, Software Installed, and Configurations Applied
The list below may reference a section with more information about that bullet
* [Desktop Ubuntu Install Notes](#desktop-ubuntu-install-notes)
* [Laptop Ubuntu Install Notes](#laptop-ubuntu-install-notes)
* [Monitor Scaling Notes](#monitor-scaling-notes)
* [Grub Scaling](#grub-scaling-so-font-is-bigger-on-high-DPI-screen)
* [Mouse Sensitivity](#mouse-sensitivity-notes)
* Software Installed:
    * git
    * git-cola
    * anaconda
    * [VSCode](#vscode)
    * tldr: Summarizes man info with practical example usage
    * fzf: Command line fuzzy finder
    * broot: Visualization of directory structure
    * [tmux](#tmux)



## Desktop Ubuntu Install Notes
* When installing from a USB stick, need to boot USB device that has Ubuntu installation as a UEFI device
* Choose to install bootloader on existing EFI partition which holds windows bootloakder

## Laptop Ubuntu Install Notes
* Can only install if SecureBoot is disabled, and hard drive mode is AHCI instead of RAID
* Switching from RAID to AHCI may break existing OS installation, do research on internet first


## Monitor Scaling Notes
* Ubutnu 18.04 doesn't support fractional scaling for high DPI screen, and 200% is too large
* For a high resolution screen, can get a better scaling by running the following commands. Replace ```DP-0``` with own monitor. Can find monitor info by ```xrandr --current```
    ```bash
    xrandr --output DP-0 --scale 1.25x1.25
    gsettings set org.gnome.desktop.interface scaling-factor 2
    gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "{'Gdk/WindowScalingFactor': <2>}"
    ```
* Before the setting commands work, need to first export the following. Can do so automatically on startup by adding the following to ~/bash.rc

    ```bash
    export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/
    ```    

* Automate this scalin process on startup by creating a bash script with the above commands and adding it as a startup application. Make sure to make it executable by changing permission: ```sudo chmod +x scalingConfig.sh```
* Bash scripts must have #!/bin/bash at their start    

### Grub Scaling so font is bigger on high DPI screen
* Get to grub menu on boot, press esc, type ```videoinfo```
* Note down a smaller supported resolution, and exit. Boot into linux
* Modify grub config
    ```sudo gedit /etc/default/grub```
* Add the following, make sure no spaces
    ```
    GRUB_GFXMODE="1600x1200"
    GRUB_GFXPAYLOAD_LINUX="keep"
    ```
* Run ```sudo update-grub```

## Mouse Sensitivity Notes
* First, see list of devices via ```xinput list```, output will look like:
    ```terminal
    ⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
    ⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
    ⎜   ↳ Logitech M720 Triathlon                 	id=9	[slave  pointer  (2)]
    ⎜   ↳ Logitech K850                           	id=10	[slave  pointer  (2)]
    ⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Power Button                            	id=6	[slave  keyboard (3)]
    ↳ Power Button                            	id=7	[slave  keyboard (3)]
    ↳ Sleep Button                            	id=8	[slave  keyboard (3)]
    ↳ UVC Camera (046d:0821)                  	id=11	[slave  keyboard (3)]
    ↳ Logitech M720 Triathlon                 	id=12	[slave  keyboard (3)]
    ↳ Logitech K850                           	id=13	[slave  keyboard (3)]
    ```
* Then, query properties for mouse via ```xinput list-props "pointer:Logitech M720 Triathlon"```
    ```terminal
    Device 'Logitech M720 Triathlon':
	Device Enabled (154):	1
	Coordinate Transformation Matrix (156):	1.100000, 0.000000, 0.000000, 0.000000, 1.100000, 0.000000, 0.000000, 0.000000, 1.000000
	libinput Natural Scrolling Enabled (288):	0
	libinput Natural Scrolling Enabled Default (289):	0
	libinput Scroll Methods Available (290):	0, 0, 1
	libinput Scroll Method Enabled (291):	0, 0, 0
	libinput Scroll Method Enabled Default (292):	0, 0, 0
	libinput Button Scrolling Button (293):	2
	libinput Button Scrolling Button Default (294):	2
	libinput Middle Emulation Enabled (295):	0
	libinput Middle Emulation Enabled Default (296):	0
	libinput Accel Speed (297):	1.000000
	libinput Accel Speed Default (298):	0.000000
	libinput Accel Profiles Available (299):	1, 1
	libinput Accel Profile Enabled (300):	1, 0
	libinput Accel Profile Enabled Default (301):	1, 0
	libinput Left Handed Enabled (302):	0
	libinput Left Handed Enabled Default (303):	0
	libinput Send Events Modes Available (273):	1, 0
	libinput Send Events Mode Enabled (274):	0, 0
	libinput Send Events Mode Enabled Default (275):	0, 0
	Device Node (276):	"/dev/input/event3"
	Device Product ID (277):	1133, 16478
	libinput Drag Lock Buttons (304):	<no items>
	libinput Horizontal Scroll Enabled (305):	1
    ```
* Pertinent parameters to set are libinput Accel Speed (min max value of [-1 to 1], and Coordinate Transformation Matrix, which is like a sensitivity scaling). Example setting:
    ```terminal
    xinput --set-prop "pointer:Logitech M720 Triathlon" 156 1.1, 0, 0, 0, 1.1, 0, 0, 0, 1

    ```
* Settings are not saved after reboot. Set at startup by creating a bash file with the desired command, setting it as executable, and adding it as a startup script. The file would contain for example:
    ```bash
    #!/bin/sh
    xinput --set-prop "pointer:Logitech M720 Triathlon" 156 1.1, 0, 0, 0, 1.1, 0, 0, 0, 1
    ```
    Set as executable via ```sudo chmod +x```

## tmux
Remapped default key mappings to more convenient settings:
  * `Ctrl-b` to `Ctrl-a`
  * Pane splits from `"`, `%` to `|`, `-`
  * Pane traversal to `Alt+arrow_key`

Set the following configuration settings in `~/.tmux.conf`: 
```
# remap prefix from 'C-b' to 'C-a'
unbind C-b
set-option -g prefix C-a
bind-key C-a send-prefix

# split panes using | and -
bind | split-window -h
bind - split-window -v
unbind '"'
unbind %

# switch panes using Alt-arrow without prefix
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D

# Allow ctrl+arrow for word jumping,
# for example
set-window-option -g xterm-keys on

# Get prompt color in tmux
set -g default-terminal "screen-256color"
```
## VSCode
* Installed Markdown Preview Enhanced
* Installed ROS tools
* Installed Cmake language support
* Installed python, c++, python linter support
* Added custom key binding to allow switching from code to terminal via Ctrl+ ` :
    *Press Cmd+Shift+Pm ad Open Keyboard shortcuts JSON file, add following:
    ```
    // Toggle between terminal and editor focus
    { "key": "ctrl+`", "command": "workbench.action.terminal.focus"},
    { "key": "ctrl+`", "command": "workbench.action.focusActiveEditorGroup", "when": "terminalFocus"}
    ```
* In settings.json file, added ignores for pycache files and folders, and disabled parameter hints for python
    ```
    "editor.hover.enabled": true,
    "editor.parameterHints.enabled": false,
    "files.exclude": {
        "**/.git": true,
        "**/*.pyc": {"when": "$(basename).py"}, 
        "**/__pycache__": true
    ```

## Bash Aliases
```
alias gs="git status" # Git status shortcut
alias ll="ls -lah" # shortcut to show all files, with human readable sizes
alias mv="mv -i" # Move interactive to avoid accidental overwrite
alias cl="clear" # Shortcut for clear
```