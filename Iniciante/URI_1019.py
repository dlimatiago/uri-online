N = int(input())
hours = N // 3600
lefth =  N / 3600 - hours
minutes = lefth * 60
seconds = N % 60
print('{}:{}:{}'.format(hours, int(minutes), int(seconds)))
