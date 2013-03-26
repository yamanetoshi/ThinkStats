import random
import myplot
import Cdf
import Pmf

def main():
    rands = [random.random() for i in range(1000)]
    pmf = Pmf.MakePmfFromList(rands, 'speeds')
    myplot.Pmf(pmf)
#    cdf = Cdf.MakeCdfFromList(rands, 'rands')
#    myplot.Cdf(cdf)
    myplot.Show(title='PMF of running speed',
               xlabel='random.random()',
               ylabel='probability')


if __name__ == '__main__':
    main()
