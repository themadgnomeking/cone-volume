#CHALLENGE
# We have five favoriate songs named A, B, C, D, and E. 
# We've created a playlist of these songs and are using an app to manage the playlist.
# The songs start in the order A, B, C, D, E. The app has four buttons:
#   * Button 1: Moves the song of the playlist to the end of the playlist
#     For example, if the playlist is currently A, B, C, D, E, then it changes to B, C, D, E, A
#   * Button 2: Moves the last song of the playlist to the beginning of the playlist.
#     For example, if the playlist is currently A, B, C, D, E, then it changes to E, A, B, C, D
#   * Button 3: Swaps the first two songs of the playlist. 
#     For example, if the playlist is currently A, B, C, D, E, then it changes to B, A, C, D, E
#   * Button 4: Plays the playlist!

#INPUT
# The input consists of pairs of lines, where the first line of a pair gives the number of buttons (1, 2, 3, or 4),
# and the second gives the number of times the user presses this button (between 1 and 10).
# This is, the first line is the number of a button, the second line is the number of times it is pressed,
# the thiird line is the number of a button, the fourth line is the number of times it is pressed.
# The input ends with these two lines:
#---------------------------
#4
#1
#---------------------------
#indicating that the user pressed button 4 once.

#OUTPUT
# Output the order of the songs in the playlist after all the buttons are pressed.
# The output must be on one line, with a space separating each pair of songs.

song_list = 'ABCDE'

button_selection = '11114'

while len(button_selection) > 0:
    if button_selection[0] == '1':
        song_list = song_list[1] + song_list[2] + song_list[3] + song_list[4] + song_list[0]
        #button_selection = button_selection[1:]
        
    if button_selection[0] == '1':
        song_list = song_list[4] + song_list[0] + song_list[1] + song_list[2] + song_list[3]
        #button_selection = button_selection[1:]
    if button_selection[0] == '1':
        song_list = song_list[1] + song_list[0] + song_list[2] + song_list[3] + song_list[4]
        #button_selection = button_selection[1:]
    if button_selection[0] == '4':
        #button_selection = ''
        print(song_list)
    button_selection = button_selection[1:]