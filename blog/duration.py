def duration2(ss , ff):
    arr1 = ss.split(':')
    print(arr1[2])
    arr2 = ff.split(':')
    for i in range(len(arr1)):
        arr1[i] = str(arr1[i])
    for i in range(len(arr2)):
        arr1[i] = str(arr1[i])
    one = int(arr1[0])*3600+int(arr1[1])*60+int(arr1[2])
    if len(arr2) == 3:
        two = int(arr2[0])*3600+int(arr2[1])*60+int(arr2[2])
    else:
        two = int(arr2[0]) * 3600 + int(arr2[1]) * 60
    diff = two - one
    diff_h =( diff // 3600 )
    diff_m = ((diff % 3600)//60)
    diff_s = ((diff % 3600)%60)
    s=""
    if diff_h!= 0:
        s+=str(diff_h) +"ساعت"
    if diff_m!=0:
        if diff_h!= 0:
            s += " و "
        s+= str(diff_m) +"دقیقه"
    if len(arr2) == 3:
        if diff_s!=0:
            if s!="":
                s += " و "
            s+=str(diff_s) +"ثانیه"
    if diff_s<=0 and diff_m<=0 and diff_h<=0:
        s+=" 0 دقیقه"
    return s
