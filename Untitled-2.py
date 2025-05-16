import time
alphabet = ["A", 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']
letters = "AAAAAAAAAAAAAAAAAAAAAAAAAA"
runs = 0
going = True
rounds = 0
times_looped = 0
print(letters[1])
print(alphabet[0])
while rounds != 26:
    times_looped = times_looped + 1
    time.sleep(0)
    print(runs)
    print(letters, times_looped)
    if runs == 26:
        runs = 0
        rounds = rounds + 1
    if rounds >= 26:
        break
    letters = letters.replace(letters[rounds], alphabet[runs], 1)
    runs = runs + 1
letters = "AAAAAAAAAAAAAAAAAAAAAAAAAA"
while rounds <= 26:
    runs = 0
    number = 0
    while number < 26:
        letters = letters.replace(letters[number], alphabet[runs], 1)
        print(letters)
        runs = runs + 1
        if runs == 26:
            letters = "AAAAAAAAAAAAAAAAAAAAAAAAAA"
            runs = 0
            number = number + 1
            rounds = rounds + 1

                
print('hi')
                