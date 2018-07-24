def duration2(ss , ff):
    arr1 = ss.split(':')
    print(arr1[0])
    arr2 = ff.split(':')
    one = int(arr1[0])*60+int(arr1[1])
    two = int(arr2[0])*60+int(arr2[1])
    diff = two - one
    diff_h = diff // 60
    diff_m = diff % 60

    return str(str(diff_h) +"ساعت"+" و " +str(diff_m) +"دقیقه")