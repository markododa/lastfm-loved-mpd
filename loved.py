#!/usr/bin/python
# coding: utf-8
import sys
from mylast import *
import subprocess
limit=1
def get_loved_tracks(limit=limit):
    return lastfm_network.get_user(lastfm_username).get_loved_tracks(limit)

def count_loved_tracks():
    return len(get_loved_tracks())

def print_loved_tracks():
    tracks = ''
    for i, track in enumerate(get_loved_tracks()):
        tracks += (str(track.track.get_artist())+" - "+str(track.track.get_title()))+'\n'
    return tracks[0:len(tracks)-2]

def generate_playlist(limit=limit):
    for i, track in enumerate(get_loved_tracks(limit)):
        tracks = subprocess.check_output(['echo', 'mpc', 'search', 'any', str(track.track.get_artist()), 'title', str(track.track.get_title())]).splitlines()
        print(tracks)
        if len(tracks) == 0:
            print(str(track.track.get_artist())+' '+str(track.track.get_title())+' not found', file=sys.stderr)
        elif len(tracks) >= 1:
            print('/data/Music/Maki/'+str(tracks[0].decode('UTF-8')))


generate_playlist()
