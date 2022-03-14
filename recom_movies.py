from recommendations import *
from math import *
from similarity import *

# 影片推荐
def getRecommendations(prefs, person, sim):
    totals = {}
    simSum = {}
    scores = []
    for other in prefs:
        if other == person: continue
        similarity = sim(prefs, person, other)
        if similarity <= 0: continue
        for item in prefs[other]:
            if item not in prefs[person]:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * similarity
                simSum.setdefault(item, 0)
                simSum[item] += similarity
    for item in totals:
        scores.append((totals[item] / simSum[item],item))
    scores.sort()
    scores.reverse()

    return scores

print(getRecommendations(critics, 'Toby', sim_pearson))

