import Pmf

def ProbCommon(f, t, p):
    ret = 0
    for k, v in p.GetDict().iteritems():
        if (f <= k) and (k <= t):
           ret += v

    return ret

def ProbEarly(p):
    return ProbCommon(0, 37, p)

def ProbOnTime(p):
    return ProbCommon(38, 40, p)

def ProbLate(p):
    return ProbCommon(41, 99, p)
