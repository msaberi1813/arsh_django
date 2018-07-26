def duration2(ss , ff):
    arr1 = ss.split(':')
    print(arr1[0])
    arr2 = ff.split(':')
    one = float(arr1[0])*3600+float(arr1[1])*60+float(arr1[2])
    two = float(arr2[0])*3600+float(arr2[1])*60+float(arr2[2])
    diff = two - one
    diff_h =round( diff // 3600 ,0)
    diff_m = round((diff % 3600)//60,0)
    diff_s = round((diff % 3600)%60,0)
    diff_h=int(diff_h)
    diff_m=int(diff_m)
    diff_s=int(diff_s)
    s=""
    if diff_h!= 0:
        s+=str(diff_h) +"ساعت"
    if diff_m!=0:
        if diff_h!= 0:
            s += " و "
        s+= str(diff_m) +"دقیقه"

    if diff_s!=0:
        if s!="":
            s += " و "
        s+=str(diff_s) +"ثانیه"
    return s