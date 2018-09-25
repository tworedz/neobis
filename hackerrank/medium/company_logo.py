from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
[print(i[0],i[1]) for i in OrderedCounter(sorted(input())).most_common(3)]
