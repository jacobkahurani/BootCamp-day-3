def find_max_min(li):
    most = li[0]
    least = li[0]
    for i in range(0,len(li)):
        if(li[i] > most):
            most = li[i]
    for i in range(0,len[li]):
        if(li[i] < least):
            least = li[i]
    if most == least:
        return [len(li)]
    else:
        return [least,most]
        