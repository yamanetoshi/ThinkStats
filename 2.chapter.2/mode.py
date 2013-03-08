import Pmf

def Mode(hist):
    list = []
    for key, val in sorted(hist.Items(), key=lambda x:x[1], reverse=True):
        if list == []:
            list.append(key)
            v = val
        else:
            if v == val:
                list.append(key)
    return list
