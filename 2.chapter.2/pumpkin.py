import math
import thinkstats

def Pumpkin(t):
    mu = thinkstats.Mean(t)
    var = thinkstats.Var(t, mu)
    sd = math.sqrt(var)

    return mu, var, sd
