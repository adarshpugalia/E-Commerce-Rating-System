import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
from nltk.tree import Tree

class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("0.0.0.0", 3456)))

    def parse(self, text):
        return json.loads(self.server.parse(text))


if __name__ == "__main__":
    nlp = StanfordNLP()
    result = nlp.parse("I bought this for my husband who plays the piano.  He is having a wonderful time playing these old hymns.  The music  is at times hard to read because we think the book was published for singing from more than playing from.  Great purchase though!")
    pprint(result)
