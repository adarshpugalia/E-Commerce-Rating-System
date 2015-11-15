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
review = "What can I say about this place. The staff of the restaurant is nice and the eggplant is not bad. Apart from that, very uninspired food, lack of atmosphere and too expensive. I am a staunch vegetarian and was sorely dissapointed with the veggie options on the menu. Will be the last time I visit, I recommend others to avoid."
result = nlp.parse(review)
print result

# count = 0
# temp_result = result['sentences']
# parse_length = len(temp_result)
# for i in xrange(parse_length):
#     sentence = temp_result[i]['text']
#     sentence = str(sentence)
#     searchObj = re.search(r'color', sentence, re.M|re.I)
#     if searchObj:
#         count += 1
#
# if count > 0:
#     print review
