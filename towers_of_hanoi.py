def towers(disks, src, tmp, dst):
    if disks == 1:
        print("move disk from {} to {}".format(src, dst))
    else:
        towers(disks-1, src, dst, tmp)
        print("move disk from {} to {}".format(src, dst))
        towers(disks-1, tmp, src, dst)


towers(64, '1', '2', '3')