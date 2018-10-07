for i in range(1,10):
    print(' '*7*(i-1),end='')
    for  j  in range (i,10):
        print("{}x{}={:2} ".format(i, j, i*j),end='')
    print()
