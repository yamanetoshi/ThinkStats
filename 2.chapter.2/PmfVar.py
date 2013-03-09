import Pmf

def PmfVar(pmf):
    ret = 0
    mu = pmf.Mean()
    for k, v in pmf.GetDict().iteritems():
        ret += ((k - mu) ** 2) * v

    return ret
