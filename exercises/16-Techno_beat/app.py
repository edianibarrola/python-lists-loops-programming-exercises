def lyrics_generator(numlist):
    song_lyrics = " "
    three_in_a_row = 0
    for num in numlist:
        if num == 0:
            song_lyrics +=  "Boom "
        if num == 1:
            song_lyrics += "Drop the base "
            three_in_a_row += 1
        if three_in_a_row == 3:
            song_lyrics += "!!!Break the base!!!"
            three_in_a_row = 0

    return song_lyrics

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))