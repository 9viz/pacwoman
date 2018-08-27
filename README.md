**pacwoman**

A simple AUR helper which only downloads the packages and does nothing other than. It's written in python 3.6 and is very much work in progress.
NOTE: It does not download dependencies automatically. That is something the user have to do.

**Usage**

In your terminal, type ```python /path/to/pacwoman.py```
And enter the package name you want to download when prompted.

To launch it easier, add an alias to your shell.
Example:
Add the following to your .bashrc file located in your home directory.
```alias pacwoman="python /path/to/pacwoman.py"```


To use a custom configuration, run `pacwoman -c /full/path/to/config.yaml`. NOTE: The path should be the full path. Ex: If my configuration is present in `$HOME/etc/pacwoman.conf`, I have to run `pacwoman -c /home/the_human/etc/pacwoman.conf`

The default configuration is located at `res/config.yaml`. You may edit that to make a custom config

**The Why**

The reason why this program only downloads the PKGBUILD and does nothing else is because many Arch Users blindly use AUR helpers like yay and install AUR packages without reading the PKGBUILD. New arch users don't realize that AUR packages can contain **malware**, once if found, there are deleted. The way we can find if a package is malicious or not is by reading the PKGBUILD.

The main reason why I adopted this "download-only" model is because I liked to run makepkg myself and I wanted the end user, including me, to read the PKGBUILD more often. I admit that when I used arch for the first time, I didn't read the PKGBUILDs. I started to read them once I found out that AUR packages are not checked, i.e., devs don't check if they have malware.

**Goals for the Future**

-Add some sort of tab-completion support.

**What this project won't do**

-Be a wrapper around pacman, like yay.

-Resolve AUR dependencies

I want this project to stay simple and hackable, and follow the suckless philoshopy of keeping the source code less than 2000 lines. The latter is for me to write efficient code, and is an interesting challenge.


I think this project reached all the realistic goals I wanted to have. So the development on this project, from this point, will be really slow.

DISCLAIMER: This is my first large python project which depends on a lot of sub modules. So bad code ahead. Pointing out bad code and saying how to improve it really appreciated.
