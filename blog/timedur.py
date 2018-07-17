def duration(finish_time , beginnig_time):
    diff = finish_time[1: finish_time.index(',')] - beginnig_time
    duration = diff.total_seconds()
    h = duration // (60 * 60)
    m = (duration % (60 * 60)) / 60
    s = (duration % (3600))
    return h, m, s