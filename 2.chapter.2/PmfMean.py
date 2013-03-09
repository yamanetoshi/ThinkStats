import Pmf

def PmfMean(pmf):
    ret = 0
    for k, v in pmf.GetDict().iteritems():
        ret += k * v

    return ret
