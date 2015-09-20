# rift-artifacts

Produces a Lua table of artifact collection names and the item IDs for the artifacts in each collection.

It uses the Rift Discovery data dumps from [here](http://webcdn.triongames.com/addons/assets/). 
If that location is no longer valid, check [ZorbaTHut's addon information thread](http://forums.riftgame.com/technical-discussions/addon-api-development/333518-official-addon-information-station.html#post3964688).

# Pre-requisites

This project uses Python 3.4 and describes its dependencies in a pip `requirements.txt` file. You can install all the packages required by running:

    pip install -r requirements.txt

If you are using Windows, you will need to ensure that you have Visual Studio 2010 installed (the [Express edition](http://go.microsoft.com/?linkid=9709949) will suffice), and run the `pip` command inside a "Visual Studio Command Prompt". Please see the [lxml installation instructions](http://lxml.de/installation.html) for further information.

## Usage

First, extract the `ArtifactCollections.xml` and `Items.xml` files from the `Rift_Discoveries_<date>.zip` file.

Then run:

```
python main.py Items.xml ArtifactCollections.xml ArtifactCollections.lua
```

The output will be written to `ArtifactCollections.lua`.
