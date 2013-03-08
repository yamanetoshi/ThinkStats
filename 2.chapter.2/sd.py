# -*- coding: utf-8 -*-

import survey
import thinkstats
import math

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

print u' 第一子の妊娠期間の標準偏差：', math.sqrt(thinkstats.Var(first_p))
print u' 第二子以降の妊娠期間の標準偏差：', math.sqrt(thinkstats.Var(other_p))

