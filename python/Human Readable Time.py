def make_readable(sec):
    H = sec / 3600
    M = sec /60 % 60
    S = sec % 60
    HH = str("%02d" % (H))
    MM = str("%02d" % (M))
    SS = str("%02d" % (S))
    return HH + ":" + MM + ":" + SS
