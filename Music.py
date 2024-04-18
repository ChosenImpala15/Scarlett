import os
from dotenv import load_dotenv, find_dotenv
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth

def authorization():
	#load env variables
	load_dotenv(find_dotenv())

	# Set your credentials
	client_id = os.environ.get("SPOTIFY_API_ID")
	client_secret = os.environ.get("SPOTIFY_API_SECRET")
	redirect_uri = 'http://localhost:4000/'

	# Set the scope for the Spotify API
	scope = 'user-read-currently-playing user-library-modify playlist-modify-public playlist-modify-private user-modify-playback-state user-read-playback-state'

	# Authorization flow
	return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, cache_path='cache.txt'))

def playback_state():
	stateDict = {}
	try:
		sp = authorization()
		
		playbackState = sp.current_playback()
		
		stateDict["shuffle"] = playbackState["shuffle_state"]
		stateDict["repeat"] = playbackState["repeat_state"]
		
		return(stateDict)
		
	except:
		pass

def pause_track(firstArg = None):
	firstArg
	print("Pausing...")
	try:
		sp = authorization()
		
		sp.pause_playback()
		return("Paused playback.")
	except:
		pass
      
def play_track(firstArg = None):
	firstArg
	print("Resuming...")
	try:
		sp = authorization()

		sp.start_playback()
		return("Resumed playback.")
	except:
		pass

def next_track(firstArg = None):
	firstArg
	print("Skipping...")
	try:
		sp = authorization()

		sp.next_track()
		#add time delay so it gets the song it switched to not the one playing before
		time.sleep(1)
		return("Skipped to next song. " + current_track_after_skip())
	except:
		pass

def previous_track(firstArg = None):
	firstArg
	print("Going back...")
	try:
		sp = authorization()

		sp.previous_track()
		#add time delay so it gets the song it switched to not the one playing before
		time.sleep(1)
		return("Skipped to previous song. " + current_track_after_skip())
	except:
		pass

def restart_track(firstArg = None):
	firstArg
	print("Restarting...")
	try:
		sp = authorization()

		sp.seek_track(0)
		return("Song has been restarted.")
	except:
		pass

def current_track(firstArg = None):
	firstArg
	print("Retrieving current song...")
	try:
		sp = authorization()
		
		playingJson = sp.current_user_playing_track()
		if (playingJson["is_playing"]==True):
			artist= str(playingJson["item"]["artists"][0]["name"])
			song = str("The current song is "+playingJson["item"]["name"]+ " by ")
			songInfo=(song+artist)
			return(songInfo)
		else:
			return("Nothing is playing")
	except:
		pass

def current_track_after_skip(firstArg = None):
	firstArg
	try:
		sp = authorization()
		
		playingJson = sp.current_user_playing_track()
		if (playingJson["is_playing"]==True):
			artist= str(playingJson["item"]["artists"][0]["name"])
			song = str("The current song is "+playingJson["item"]["name"]+ " by ")
			songInfo=(song+artist)
			return(songInfo)
		else:
			return("Nothing is playing")
	except:
		pass

def like_track(firstArg = None):
	firstArg
	idList = []
	print("Liking...")
	try:
		sp = authorization()
		
		playingJson = sp.current_user_playing_track()
		if (playingJson["is_playing"]==True):
			id = playingJson["item"]["id"]
			idList.append(id)
			sp.current_user_saved_tracks_add(idList)

			return("Song added to your library")
		else:
			return("Nothing is playing")
	except:
		pass

def dislike_track(firstArg = None):
	firstArg
	idList = []
	print("Disliking...")
	try:
		sp = authorization()
		
		playingJson = sp.current_user_playing_track()
		if (playingJson["is_playing"]==True):
			id = playingJson["item"]["id"]
			idList.append(id)
			sp.current_user_saved_tracks_delete(idList)

			return("Song removed from your library")
		else:
			return("Nothing is playing")
	except:
		pass

def search_track(firstArg):
	search = firstArg
	print("Searching for track...")
	
	sp = authorization()
		
	searchJson = sp.search(q=search, type="track", limit=1)
	if (searchJson["tracks"]["total"]>=1):
		uri = searchJson["tracks"]["items"][0]["uri"]
		name = searchJson["tracks"]["items"][0]["name"]
		artist = searchJson["tracks"]["items"][0]["artists"][0]["name"]
		sp.add_to_queue(uri=uri)
		sp.next_track()

		return(f'"{name}" by {artist} is now playing')
	else:
		return("Not found")

def search_playlist(firstArg):
	search = firstArg
	print("Searching for playlist...")
	
	sp = authorization()
		
	searchJson = sp.search(q=search, type="playlist", limit=1)
	if (searchJson["playlists"]["total"]>=1):
		uri = searchJson["playlists"]["items"][0]["uri"]
		name = searchJson["playlists"]["items"][0]["name"]
		start_music()
		sp.start_playback(context_uri=uri)
		sp.shuffle(state=True)
		sp.repeat(state="context")
		#add time delay so it gets the song it switched to not the one playing before
		time.sleep(3)
		return(f'Playing the playlist "{name}". {current_track_after_skip()}')
	else:
		return("Not found")
	
def toggle_shuffle(firstArg = None):
	print("Toggling shuffle...")
	firstArg
	currentState = playback_state()
	try:
		sp = authorization()
		
		if (currentState["shuffle"]==True):
			sp.shuffle(state=False)

			return("Shuffle has been turned off.")
		else:
			sp.shuffle(state=True)

			return("Shuffle has been turned on.")
	except:
		pass

def toggle_repeat(firstArg = None):
	print("Toggling repeat...")
	firstArg
	currentState = playback_state()
	try:
		sp = authorization()
		
		if (currentState["repeat"]=="context"):
			sp.repeat(state="track")

			return("Repeating current song...")
		else:
			sp.repeat(state="context")

			return("Repeating current playlist...")
	except:
		pass

def set_track_volume(firstArg):
	volume = firstArg
	print("Setting volume...")
	try:
		sp = authorization()
		
		sp.volume(volume_percent=volume)
		return(f'Volume set to {volume}')
	except:
		pass

def start_music(firstArg = None):
	
	if(firstArg == None):
		device = "pc"
	else:
		device = firstArg
	print("Starting music...")
	try:
		
		sp = authorization()
			
		devices = sp.devices()

		for i in range(len(devices["devices"])):
			if device in (devices["devices"][i]['type']).lower() or device in (devices["devices"][i]['name']).lower():
				id = devices["devices"][i]["id"]
				sp.transfer_playback(id, force_play=True)
				return(f'Music has been started on {device}')

		return("No device matching")
	except:
		return("Transfer Failed")


if __name__ == '__main__':
	print(search_playlist("disney"))