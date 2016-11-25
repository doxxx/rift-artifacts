# rift-artifacts

Produces a Lua table of artifact collection names and the item IDs for the artifacts in each collection.

It uses the Rift Discovery data dumps from [here](http://webcdn.triongames.com/addons/assets/) (beware, URL _must_ end in `/` otherwise the links on the page are incorrect). 
If that location is no longer valid, check [ZorbaTHut's addon information thread](http://forums.riftgame.com/technical-discussions/addon-api-development/333518-official-addon-information-station.html#post3964688).

# Pre-requisites

This project uses Python 3.4 (or newer) and describes its dependencies in a pip `requirements.txt` file. You can install all the packages required by running:

    pip install -r requirements.txt

If you are using Windows, you can download the lxml extension (e.g. `lxml‑3.6.4‑cp35‑cp35m‑win_amd64.whl` for CPython 3.5 64-bit) from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) and manually install using:

    pip install C:\path\to\downloaded\package.whl

If you would rather have pip compile the package, you will need to ensure that you have the correct version of Visual Studio installed (the Express edition will suffice), and run the first `pip install` command inside a "Visual Studio Command Prompt". Please see the [lxml installation instructions](http://lxml.de/installation.html) for further information.

Another alternative for Windows 10 is to use the _Windows Subsystem for Linux_. Once installed, in a Bash window you can use `sudo apt install python3 python3-lxml` to install Python and the lxml library, and then run Python as described below.

## Usage

First, extract the `ArtifactCollections.xml` and `Items.xml` files from the `Rift_Discoveries_<date>.zip` file.

Then run:

```
python main.py Items.xml ArtifactCollections.xml ArtifactCollections.lua
```

The output will be written to `ArtifactCollections.lua`.
