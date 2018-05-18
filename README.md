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

**Todo**

Since this program is very much work in progress, there are a lot features which are yet to be done.
- Download all the packages when evoked with "-Syu"
- Make a config file where user can enable colored output and possibly alter the syntax.
- Make the output pretty and more readable.
- Make an installer so that user won't need to create an alias.

DISCLAIMER: This is my first large python project which depends on a lot of sub modules. So bad code ahead. Pointing out bad code and saying how to improve it really appreciated.
