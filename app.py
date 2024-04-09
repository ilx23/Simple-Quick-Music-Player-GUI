# Import necessary libraries
from tkinter import *
from tkinter import messagebox
import pygame
import os


# Function to play the selected music
def play_music():
    """
    Play the selected music.

    This function updates the current music label with the name of the selected music file,
    loads the selected music file for playback using Pygame mixer, and starts playing the loaded music file.

    Raises:
        NameError: If there are no music files available.

    Returns:
        None
    """
    global current_music
    try:
        # Update the current music label and load the selected music file for playback
        current_music_label.config(text=music_files[current_music_index])
        current_music = music_files[current_music_index]
        pygame.mixer.music.load(current_music)
        pygame.mixer.music.play()
    except (NameError, TypeError):
        # Display an error message if there are no music files available
        messagebox.showerror("Error", "No music file to play")


# Function to stop music playback
def stop_music():
    """
    Stop the music playback.

    This function stops the currently playing music.

    Returns:
        None
    """
    pygame.mixer.music.stop()


# Function to play the next music track
def next_music():
    """
    Play the next music track in the playlist.

    This function moves to the next music track in the playlist and plays it.

    Raises:
        NameError: If there are no music files available.

    Returns:
        None
    """
    global current_music_index
    try:
        # Move to the next music track in the playlist
        if current_music_index >= len(music_files) - 1:
            current_music_index = 0
        else:
            current_music_index += 1
        play_music()
    except (NameError, TypeError):
        # Display an error message if there are no music files available
        messagebox.showerror("Error", "No music file to play")


# Function to play the previous music track
def previous_music():
    """
    Play the previous music track in the playlist.

    This function moves to the previous music track in the playlist and plays it.

    Raises:
        NameError: If there are no music files available.

    Returns:
        None
    """
    global current_music_index
    try:
        # Move to the previous music track in the playlist
        if current_music_index == 0:
            current_music_index = len(music_files) - 1
        else:
            current_music_index -= 1
        play_music()
    except (NameError, TypeError):
        # Display an error message if there are no music files available
        messagebox.showerror("Error", "No music file to play")


# Initialize the Tkinter application
app = Tk()
app.geometry('300x100')
app.title('Music Player')

# Initialize Pygame mixer for music playback
pygame.mixer.init()

# Get the list of music files in the current directory
music_files = [file for file in os.listdir() if file.endswith(".mp3")]

# Set the current music index and label if music files are found
current_music_index = 0 if music_files else None
current_music = music_files[current_music_index] if music_files else None

# Create and pack GUI elements for music player controls
current_music_label = Label(app, text=current_music if current_music else "No music files found")
current_music_label.pack()
play_button = Button(app, text='Play', command=play_music)
play_button.pack(side='left', padx=10)
stop_button = Button(app, text='Stop', command=stop_music)
stop_button.pack(side="left", padx=10)
next_button = Button(app, text='Next', command=next_music)
next_button.pack(side="left", padx=10)
previous_button = Button(app, text='Previous', command=previous_music)
previous_button.pack(side="left", padx=10)

# Start the Tkinter event loop
app.mainloop()
