def rotate_left(d, arr):
    ad = d % len(arr) #num of actual rotation
    aright = arr[:ad]
    aleft = arr[ad:]
    na = aleft + aright
    return na

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    d = 4
    print(rotate_left(d, arr))