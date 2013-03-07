# -*- coding: utf-8 -*-

import survey

table = survey.Pregnancies()
table.ReadRecords()

first = 0
other = 0

for i in table.records:
    if i.birthord == 1:
        first += 1
    elif i.birthord <= 10:
        other += 1

print u' 第一子：', first
print u' 第二子以降：', other
