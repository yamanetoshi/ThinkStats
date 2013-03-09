# -*- coding: utf-8 -*-

import survey
import thinkstats
import math
import Pmf
import myplot

table = survey.Pregnancies()
table.ReadRecords()

first_p = []
other_p = []

for i in table.records:
    if i.outcome == 1:
        if i.birthord == 1:
            first_p.append(i.prglength)
        else:
            other_p.append(i.prglength)

first_hist = Pmf.MakeHistFromList(first_p, name=u"第一子")
other_hist = Pmf.MakeHistFromList(other_p, name=u"第二子以降")

myplot.Hists([first_hist, other_hist])
myplot.Show()
