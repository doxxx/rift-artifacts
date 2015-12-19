import sys
import re
from time import perf_counter

from lxml import etree


def normalize_whitespace(s):
    return re.sub(r"\s\s+", " ", s.strip())


class TagStackBuilder(object):
    def __init__(self):
        self.tagStack = []

    # noinspection PyUnusedLocal
    def start(self, tag, attrib):
        self.tagStack.append(tag)

    def end(self, tag):
        popped = self.tagStack.pop()
        assert popped == tag

    def close(self):
        pass


class ItemMapper(TagStackBuilder):
    def __init__(self):
        super().__init__()
        self.items = {}
        self.itemKey = None

    def data(self, data):
        tag = self.tagStack[-1]
        if tag == "ItemKey":
            self.itemKey = data
        elif tag == "AddonType":
            self.items[self.itemKey] = data

    def comment(self, text):
        pass

    def close(self):
        super().close()
        return self.items


class ArtifactCollectionMapper(TagStackBuilder):
    def __init__(self):
        super().__init__()
        self.collectionName = ""
        self.itemKeys = []
        self.collections = []

    def data(self, data):
        tags = self.tagStack[-3:]
        if tags == ["ArtifactCollection", "Name", "English"]:
            #print("collection name segment: ", repr(data))
            self.collectionName += data
        elif tags == ["Items", "Item", "ItemKey"]:
            #print("itemkey: ", repr(data))
            self.itemKeys.append(data)

    def end(self, tag):
        if tag == "ArtifactCollection":
            self.collections.append({ "name": normalize_whitespace(self.collectionName), "items": self.itemKeys })
            self.collectionName = ""
            self.itemKeys = []
        super().end(tag)

    def comment(self, text):
        pass

    def close(self):
        super().close()
        return self.collections


def load_collections(filename):
    print("Loading Artifact Collections...", end="", flush=True)
    start = perf_counter()
    parser = etree.XMLParser(target=ArtifactCollectionMapper())
    result = etree.parse(filename, parser)
    elapsed = perf_counter() - start
    print(" done ({0:.1f}s)".format(elapsed), flush=True)
    return result


def load_items(filename):
    print("Loading Items...", end="", flush=True)
    start = perf_counter()
    parser = etree.XMLParser(target=ItemMapper())
    result = etree.parse(filename, parser)
    elapsed = perf_counter() - start
    print(" done ({0:.1f}s)".format(elapsed), flush=True)
    return result


def map_collection_item_keys(collection, items):
    return {
        "name": collection["name"],
        "items": list(map(lambda key: items.get(key, ""), collection["items"]))
    }


def map_all_collection_item_keys(collections, items):
    print("Mapping ItemKeys to AddonTypes...", end="", flush=True)
    start = perf_counter()
    collections = list(map(lambda c: map_collection_item_keys(c, items), collections))
    elapsed = perf_counter() - start
    print(" done ({0:.1f}s)".format(elapsed), flush=True)
    return collections


def output_lua(filename, collections):
    print("Writing ArtifactCollections LUA...", end="", flush=True)
    start = perf_counter()
    f = open(filename, "wt", encoding="UTF8")
    f.write("INDY_ArtifactCollections = {\n")
    collections.sort(key=lambda c: c["name"])
    for collection in collections:
        f.write('  ["')
        f.write(collection["name"])
        f.write('"] = { ')
        items = collection["items"]
        items.sort()
        for item in items:
            f.write('["' + item + '"] = true, ')
        f.write('},\n')
    f.write('}\n')
    f.close()
    elapsed = perf_counter() - start
    print(" done ({0:.1f}s)".format(elapsed), flush=True)


def main(args):
    items = load_items(args[0])
    collections = load_collections(args[1])
    collections = map_all_collection_item_keys(collections, items)
    output_lua(args[2], collections)


if __name__ == '__main__':
    main(sys.argv[1:])
