import Pmf

def PmfRemainingLifetime(y, pmf):
    newDic = {}
    for k, v in pmf.GetDict().iteritems():
        if y < k:
            newDic[k - y] = v

    return Pmf.MakePmfFromDict(newDic)


