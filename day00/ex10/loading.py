import time

def ft_progress(lst):
    start_time = time.time()
    for i, element in enumerate(lst, 1):

        elaps_time = time.time() - start_time
        eta = elaps_time * 100 / (i/len(lst))
        percentage = i/len(lst) * 100
        equals = int((percentage / 5)) * "=" + ">"
        print(f'ETA: {eta:.2f}s [ {percentage:.2f}%] [{equals:<20}] {i}/{len(lst)} '
              f'| elapsed time {elaps_time:.2f}s\n...', end='')
        print("\033[2K\033[A\033[2K\033[3D", end = '')
        yield i


listy = range(3332)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.0001)
print()
print(ret)