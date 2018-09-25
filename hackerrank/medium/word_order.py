from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
cnt = OrderedCounter(input() for _ in range(int(input())))

print(len(cnt))
print(*cnt.values(), sep=' ')
