from recommendations import *
from math import *
from similarity import *

# 用户偏好相似度匹配
def topMatches(prefs, person, n, sim):
    scores = []
    for other in prefs:
        if other!=person:
            scores.append((sim(prefs, person, other),other))
    scores.sort()
    scores.reverse()
    return scores[0:n]

print(topMatches(critics, 'Toby', 3, sim_pearson))


