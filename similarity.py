from recommendations import *
from math import *

# 欧几里得距离评价
def sim_distance(prefs, person1, person2):
    share = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            share[item] = 1
    if len(share) == 0:
        return 0
    result = sum(pow(prefs[person1][item]-prefs[person2][item],2) for item in share)
    result = 1/(1+sqrt(result))

    return result

# 皮尔逊相关度评价
def sim_pearson(prefs, person1, person2):
    share = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            share[item] = 1
    if len(share) == 0:
        return 0 
    sum1 = sum(prefs[person1][item] for item in share)
    sum2 = sum(prefs[person2][item] for item in share)
    sum1_Sq = sum(pow(prefs[person1][item], 2) for item in share)
    sum2_Sq = sum(pow(prefs[person2][item], 2) for item in share)
    sum_multi = sum(prefs[person1][item]*prefs[person2][item] for item in share)

    num = sum_multi - (sum1*sum2/len(share))
    den = sqrt((sum1_Sq-pow(sum1,2)/len(share))*(sum2_Sq-pow(sum2,2)/len(share)))
    result = num/den
    
    return result


print(sim_distance(critics,'Lisa Rose','Gene Seymour'))
print(sim_pearson(critics,'Lisa Rose','Gene Seymour'))