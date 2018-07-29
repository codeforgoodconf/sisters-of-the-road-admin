#Mac: Homebrew Package Manager, Pyenv, Python, and Node Setup

There is a package manager for Mac called [homebrew](https://brew.sh). This app makes installing applications relatively painless. This is good to use to install some basic requirements. If you're not using a Mac, you don't want to do this.

##Install Homebrew

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

This will explain what it is doing at each step.

##Install Necessary Libraries

In order to build and run this project, you'll have to have python and node.js. A great way to get a desired version of python for a given project is to use the app [pyenv](https://github.com/pyenv/pyenv). 

```bash
brew install pyenv
```

You will also need to add the following to your `~/.bash_profile` (or `~/.bashrc` on linux): 

```bash
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
```

Now close and reopen your terminal _or_ do this:

```bash
source ~/.bash_profile 
```

##Install Python
It's a good idea to install python2 and python3 into your system since various programs use one version or the other during the install process. The following will set your global `python` to be the latest python 2 and `python3` to be the latest python 3.

Get a list of python versions available:

```bash
pyenv install --list
```

Find the latest python 2 version and the latest python 3 version (note this is a long list, scroll up until you see numbers like `2.7.15`. **Don't** use anything like `stackless-2.7.14` or `pypy-5.7.1`.) As of this writing, the latest python 2 is `2.7.15` and the latest python 3 is `3.7.0` so today we would do this:

```bash
pyenv install 2.7.15
pyenv install 3.7.0
```

Then set these as the global versions:

```bash
pyenv global 2.7.15 3.7.0
```

Now you should see something like this:

```
$ pyenv versions
  system
* 2.7.15 (set by /Users/yourname/.pyenv/version)
* 3.7.0 (set by /Users/yourname/.pyenv/version)
```

And this

```
$ python -V
Python 2.7.15
$ python3 -V
Python 3.7.0
```

##Install Node.js

```bash
brew install node
```
