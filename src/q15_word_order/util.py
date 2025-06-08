from collections import OrderedDict

def word_order_counter(words):
    word_count = OrderedDict()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return len(word_count), list(word_count.values())
