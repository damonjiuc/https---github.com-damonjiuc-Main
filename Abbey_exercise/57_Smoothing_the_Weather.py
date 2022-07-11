n = 168
mas = ('30.0 27.8 40.0 48.3 48.4 49.4 38.7 44.2 46.9 34.3 53.7 35.4 30.0 17.4 21.7 15.9 9.8 3.3 10.0 -4.3 17.4 22.2 22.0 24.9 29.1 35.2 41.7 44.1 47.3 57.3 49.0 49.4 46.4 38.5 43.2 35.2 31.3 24.9 19.8 27.2 1.4 4.4 10.6 8.3 26.0 4.9 17.5 24.8 35.4 35.2 40.0 48.7 45.3 45.2 50.0 49.2 42.6 40.2 40.0 34.6 43.7 22.6 20.0 13.5 12.7 -2.2 11.8 18.1 12.9 27.5 7.1 24.1 28.7 22.3 36.9 43.8 49.2 38.4 50.1 48.4 47.7 51.0 42.4 46.5 34.9 23.4 15.3 15.8 24.7 9.0 10.0 0.8 14.8 10.0 18.5 22.0 37.4 35.7 41.5 48.1 59.0 57.3 48.1 49.3 46.7 43.1 47.7 38.0 38.3 38.5 19.5 17.3 1.7 8.4 2.0 3.6 4.1 15.9 20.0 34.4 30.0 34.6 45.6 52.4 52.5 62.6 50.2 49.4 47.3 44.1 39.1 22.7 29.6 13.9 11.1 6.3 23.3 -1.8 10.0 12.9 12.7 15.0 21.0 24.4 29.9 21.5 40.0 44.4 56.9 49.1 51.0 48.4 47.3 42.5 43.4 47.2 15.4 22.0 20.5 6.6 19.0 9.0 10.0 7.9 12.7 18.2 20.0 25.4')
splited = mas.split(' ')
floated= []
for i in range(n):
    floated.append(float(splited[i]))
smoothed = []
smoothed.append(floated[0])
for i in range(n - 2):
    current = (floated[i] + floated[i + 1] + floated[i + 2]) / 3
    if current % 1 == 0:
        smoothed.append(int(current))
    else:
        smoothed.append(current)
smoothed.append(floated[n - 1])
for i in range(len(smoothed)):
    print(smoothed[i], end=' ')