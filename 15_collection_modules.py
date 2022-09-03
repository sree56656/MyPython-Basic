from collections import Counter
from collections import defaultdict
from collections import namedtuple

c = Counter('adscdfsadf')
print(Counter(c))
print(c.most_common())

sentence = "how do you do"
print(Counter(sentence.split()))
