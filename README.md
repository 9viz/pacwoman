**pacwoman**

A simple AUR helper which only downloads the packages and does nothing other than. It's written in python 3.6 and is very much work in progress.
Note: It does not download dependencies automatically. That is something the user have to do.

**Usage**

In your terminal, type ```python /path/to/pacwoman.py```
And enter the package name you want to download when prompted.

To launch it easier, add an alias to your shell.
Example:
Add the following to your .bashrc file located in your home directory.
```alias pacwoman="python /path/to/pacwoman.py"```

**The Why**

The reason why this program only downloads the PKGBUILD and does nothing else is because many Arch Users blindly use AUR helpers like yay and install AUR packages without reading the PKGBUILD. New arch users don't realize that AUR packages can contain **malware**, once if found, there are deleted. The way we can find if a package is malicious or not is by reading the PKGBUILD.

The main reason why I adopted this "download-only" model is because I liked to run makepkg myself and I wanted the end user, including me, to read the PKGBUILD more often. I admit that when I used arch for the first time, I didn't read the PKGBUILDs. I started to read them once I found out that AUR packages are not checked, i.e., devs don't check if they have malware.

**Goals for the Future**

-Add some sort of tab-completion support.
-List the details of the packages.

**What this project won't do**

-Be a wrapper around pacman, like yay.
-Resolve AUR dependencies

I want this project to stay simple and hackable, and follow the suckless philoshopy of keeping the source code less than 2000 lines. The latter is for me to write efficient code, and is an interesting challenge.

DISCLAIMER: This is my first large python project which depends on a lot of sub modules. So bad code ahead. Pointing out bad code and saying how to improve it really appreciated.
