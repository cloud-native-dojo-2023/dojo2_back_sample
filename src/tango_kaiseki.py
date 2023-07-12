import MeCab
import re
def split_noun(text):

    mecabTagger = MeCab.Tagger()

    noun_count = {}

    node = mecabTagger.parseToNode(text)
    while node:
        word = node.surface
        hinshi = node.feature.split(",")[0]
        if word in noun_count.keys() and hinshi == "名詞":
            noun_freq = noun_count[word]
            noun_count[word] = noun_freq + 1
        elif hinshi =="名詞":
            noun_count[word] = 1
        else:
            pass
        node = node.next

    return sorted(noun_count.items(), key=lambda x:x[1], reverse=True)

def mrp_analisys(text):
    mecabTagger = MeCab.Tagger()

    noun_count = {}

    node = mecabTagger.parseToNode(text)

    while node:
        word = node.surface
        hinshi = node.feature.split(",")[0]
        if word =='':
            pass
        elif word in noun_count.keys():
            noun_freq = noun_count[word]
            noun_count[word] = noun_freq + 1
        else:
            noun_count[word] = 1
        node = node.next

    # return sorted(noun_count.items(), key=lambda x:x[1], reverse=True)
    return noun_count.items()

def cleanning(jp_string):
    cleaned = re.sub('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％ 　]', '', jp_string)
    cleaned = re.sub('(\r?\n)|(\r\n?)','', cleaned)
    return cleaned