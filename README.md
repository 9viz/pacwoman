# pacwoman

![logo](https://github.com/Th3-Hum4n/pacwoman/blob/master/pacwoman-logo.png)

A search and download-only AUR helper with an aim to write scripts around it easier. It uses python 3 and uses one external package for configuration making it portable.

# Dependencies

* python3
* pyyaml

To install `pyyaml`, run `pip3 install pyyaml --user` in your terminal.

# Usage

pacwoman doesn't have any setup file and won't have one either. It is designed to be like that.

To launch it, run `python3 /path/to/pacwoman.py`. To make it easier to launch the script, make an alias to call the above command in your shellrc.

pacwoman has a config file which you can edit to suit your needs. The default config is located at `res/config.yaml`. To use a custom config, DO NOT edit `res/config.yaml` rather copy it and specify the path of the custom config to pacwoman by running `pacwoman -c /path/to/config/file`

# The Why

The reason why this program only downloads the PKGBUILD and does nothing else is because many Arch Users blindly use AUR helpers like yay and install AUR packages without reading the PKGBUILD. New arch users don't realize that AUR packages can contain **malware**, once if found, there are deleted. The way we can find if a package is malicious or not is by reading the PKGBUILD.

The main reason why I adopted this "download-only" model is because I liked to run makepkg myself and I wanted the end user, including me, to read the PKGBUILD more often. I admit that when I used arch for the first time, I didn't read the PKGBUILDs. I started to read them once I found out that AUR packages are not checked, i.e., devs don't check if they have malware.


I want this project to stay simple and hackable, and follow the suckless philoshopy of keeping the source code less than 2000 lines. The latter is for me to write efficient code, and is an interesting challenge.
Moreover, I see pacwoman as a tool to script around rather a full blown AUR
helper which does everything by itself. A couple of shitty helper scripts are in
`autils` and I use them when I use Arch Linux. They are pretty okay.

# (Non-)Features

* Be a wrapper around pacman, like yay.
* Resolve AUR dependencies.

# Contributors

* The logo was made by [0xfi](https://github.com/0xfi)
* Major refactoring of code was done by [Sweets](https://github.com/Sweets)
* Error insults from sudo file headers and by [Diamond](https://github.com/diamondburned)
