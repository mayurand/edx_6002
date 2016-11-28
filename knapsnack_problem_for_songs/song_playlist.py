def song_sort(songs, max_size, playlist):
    try:
        if songs[0][2] > max_size:
            return None
        else:
            playlist.append(songs[0][0])
            max_size = max_size - songs[0][2]
            songs.pop(0)
            song_sort(songs, max_size, playlist)
    except:
        return None   

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    playlist = []
    if songs[0][2] > max_size:
        return []
    else:
        playlist.append(songs[0][0])
        max_size = max_size - songs[0][2]
        songs.pop(0)
             
    # Sort the songs based on their length
    songs = sorted(songs, key=lambda student: student[2])
        
    # Call the song_sort function which recursively calls itself
    song_sort(songs, max_size, playlist)
    return playlist        
    #return song_sort(songs, max_size, playlist)
    #print(playlist)


songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 20

  
print(song_playlist(songs, max_size))            
