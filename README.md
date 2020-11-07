# MultiDDLC
An instancer for DDLC, for those who enjoy the game with mods.

* Be sure to have version `python3` or later.
* Put a copy of DDLC in the same directory as `MultiDDLC.py` named `DDLC_Linux-core.zip`
(The DDLC.exe should be directly in the zip, no sub-folders)

# For linux, use wine.
`sudo dpkg --add-architecture i386`

`wget -nc https://dl.winehq.org/wine-builds/winehq.key`
`sudo apt-key add winehq.key`

Ubuntu 20.10 	`sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ groovy main' `

Ubuntu 20.04
Linux Mint 20.x `sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main'`

Ubuntu 18.04
Linux Mint 19.x `sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main' `

`sudo apt update`

`sudo apt install --install-recommends winehq-stable`
