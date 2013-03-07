# -*- coding: utf-8 -*-

import survey

table = survey.Pregnancies()
table.ReadRecords()

outcome = 0
for i in table.records:
    if i.outcome == 1:
        outcome += i.outcome

print u' 生児出生数：', outcome
