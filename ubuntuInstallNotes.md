### Ubuntu Install Notes
* When installing from a USB stick, need to boot USB device that has Ubuntu installation as a UEFI device
* Choose to install bootloader on existing EFI partition which holds windows bootloakder

### Install notes for XPS-13 laptop
* Can only install if SecureBoot is disabled, and hard drive mode is AHCI instead of RAID
* Switching from RAID to AHCI may break existing OS installation, do research on internet first

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