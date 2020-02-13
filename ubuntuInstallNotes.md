### Ubuntu Install Notes
* When installing from a USB stick, need to boot USB device that has Ubuntu installation as a UEFI device
* Choose to install bootloader on existing EFI partition which holds windows bootloakder


### List of software installed
* git
* git-cola
* anaconda
* vscode
    * Markdown Preview Enhanced Plugin





### Monitor Scaling Notes
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