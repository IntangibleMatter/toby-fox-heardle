#!/usr/bin/env python3

import re

base_link = "https://soundcloud.com/tobyfox-music/{}"

data_formatted = """	{{
		url: "{link}",
		answer: "{title}",
	}},"""

# replace with the string names of each track
tracks = [
    "Flashback(Excerpt)",
    "Feature Presentation",
    "And Now For Today’s Sponsors…!",
    "MIKE, the BOARD, please!",
    "Sandy Board",
    "Adventure Board",
    "Query?",
    "Quiz!",
    "Dig! Dig! To The Center of the Earth!",
    "Pushing Buddies",
    "Ruder Buster",
    "Physical Challenge",
    "Board Clear!",
    "Welcome to the Green Room",
    "Vapor Buster",
    "Paradise, Paradise",
    "Raft Ride",
    "SOUTH OF THE BORDER!!",
    "Sound Check",
    "Raise Up Your Bat",
    "KING OF ROLYPOLY",
    "Glowing Snow",
    "Big City Board",
    "Doom Board",
    "Metaphysical Challenge",
    "TV WORLD",
    "It’s TV Time!",
    "Hall of Fame",
    "Breath",
    "Black Knife",
    "Crickets",
    "Old wooden rafters",
    "Hymn",
    "Another day in hometown",
    "Friends",
    "Castle Funk",
    "Knock You Down!! (Rhythm Ver.)",
    "Gingerbread House",
    "The distance between two",
    "C",
    "ATRIUM",
    "Dark Sanctuary",
    "From Now On(Battle 2)",
    "Gyaa Ha ha!",
    "Fireplace",
    "A DARK ZONE",
    "Mysterious Ringing",
    "Ever Higher",
    "Wise words",
    "Piano that may not be played that well",
    "12am",
    "The Second Sanctuary",
    "Ripple",
    "13am",
    "The Third Sanctuary",
    "Dark Place",
    "Heavy Footsteps",
    "Crumbling Tower",
    "SPAWN",
    "GUARDIAN",
    "Need a hand!?",
    "The place where it rained",
    "The Ol’ Jitterbug",
    "Neverending Night",
    "The LEGEND...?",
    "With Hope Crossed On Our Hearts",
]

for track in tracks:
    tformatted = track.lower()
    tformatted = re.sub(r"(?=\W)[^ ]", "", tformatted)
    tformatted = tformatted.strip()
    tformatted = tformatted.replace(" ", "-", 4)
    if tformatted.count(" ") > 0:
        tformatted = tformatted[:tformatted.find(" ")]

    # print(data_formatted.format(
    #    link=base_link.format(tformatted), title=f"{track} - Deltarune"))
    print(f"\"{track} - Deltarune\",")
