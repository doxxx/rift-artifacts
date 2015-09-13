# rift-artifacts

A Python 3 script which produces a Lua table of artifact collection names and the item IDs for the artifacts in each collection.

It uses the Rift Discovery data dumps from [here](http://webcdn.triongames.com/addons/assets/). 
If that location is no longer valid, check [ZorbaTHut's addon information thread](http://forums.riftgame.com/technical-discussions/addon-api-development/333518-official-addon-information-station.html#post3964688).

## How to use

First, extract the `ArtifactCollections.xml` and `Items.xml` files from the `Rift_Discoveries_<date>.zip` file.

Then run:

```
python main.py Items.xml ArtifactCollections.xml ArtifactCollections.lua
```

The output will be written to `ArtifactCollections.lua`.
