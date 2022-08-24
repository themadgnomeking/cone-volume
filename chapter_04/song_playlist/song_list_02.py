#solution as per the book
songs = 'ABCDE'

button = 0

while button != 4:
    button = int(input("what's the button input 1, 2, 3, or 4?"))
    presses = int(input("This is how many presses you have: "))
    for i in range(presses):
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button ==  3:
            songs = songs[1] + songs[0] + songs[2:]
output = ''

for song in songs:
    output = output + song + ' '

print(output[:1])