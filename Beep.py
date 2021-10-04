import winsound
import random
freq = []
for i in range(5000,5400):
    freq.append(i)
#freq = [500,600,700,400,100,2040,2340,244,38,235,523,433,346,463,363,46,45,53]
#random.shuffle(freq)
dur = 100
for i in freq:
    freq
    winsound.Beep(i, dur)

