Nissu = [4,1,3,1,3,4,2,4,3]
kougeihinsu = 9
Akibi = [1,1,1]
buinsu = 3
for koigeihin in range(0,kougeihinsu):
    tantou = 1
    for buin in range(1, buinsu):
        if Akibi[buin] < Akibi[tantou - 1]:
            tantou = buin + 1
    print(f'工芸品{koigeihin + 1}→部員{tantou}:{Akibi[tantou - 1]}日目〜{Akibi[tantou - 1] + Nissu[koigeihin] - 1}日目')
    Akibi[tantou - 1] = Akibi[tantou - 1] + Nissu[koigeihin]
