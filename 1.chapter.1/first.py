# -*- coding: utf-8 -*-

import survey

table = survey.Pregnancies()
table.ReadRecords()

# print u' 妊娠レコードの総数 : ' , len(table.records)

count = 0

first_count = 0
first_prglength = 0
other_count = 0
other_prglength = 0

for i in table.records:
    if i.outcome == 1:
        count += 1
        if i.birthord == 1:
            first_count += 1
            first_prglength += i.prglength * 7 * 24
        else:
            other_count += 1
            other_prglength += i.prglength * 7 * 24

print u' 生児出生数 : ', count
print u' 第一子妊娠期間の平均：', first_prglength/first_count
print u' 第二子以降妊娠期間の平均：', other_prglength/other_count
