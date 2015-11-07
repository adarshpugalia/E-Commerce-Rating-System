import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
import re

class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 8080)))

    def parse(self, text):
        return json.loads(self.server.parse(text))

nlp = StanfordNLP()
review = "The case pictured is a soft violet color, but the case cover I received was a dark purple. While I'm sure the quality of the product is fine, the color is very different."
result = nlp.parse(review)

count = 0
temp_result = result['sentences']
parse_length = len(temp_result)
for i in xrange(parse_length):
    sentence = temp_result[i]['text']
    sentence = str(sentence)
    searchObj = re.search(r'color', sentence, re.M|re.I)
    if searchObj:
        count += 1

if count > 0:
    print review
