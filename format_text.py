#!/usr/bin/env python3

import re

base_link = "https://soundcloud.com/tobyfox-music/{}"

data_formatted = """	{{
		url: "{link}",
		answer: "{title}",
	}},"""

# replace with the string names of each track
tracks = [
    "Faint Glow",
    "Girl Next Door",
    "My Castle Town",
    "Ohhhhohohoho!",
    "Queen",
    "A CYBER'S WORLD?",
    "A Simple Diversion",
    "Almost To The Guys!",
    "Cool Beat",
    "When I Get Mad I Dance Like This",
    "Cyber Battle (Solo) (with Lena Raine)",
    "When I Get Happy I Dance Like This",
    "Sound Studio",
    "Berdly",
    "Smart Race",
    "Faint Courage (Game Over)",
    "WELCOME TO THE CITY",
    "Mini Studio",
    "Holiday Studio",
    "Cool Mixtape",
    "HEY EVERY !",
    "Spamton",
    "NOW'S YOUR CHANCE TO BE A",
    "Elegant Entrance",
    "Bluebird of Misfortune",
    "Pandora Palace",
    "KEYGEN",
    "Acid Tunnel of Love",
    "It's Pronounced \\\"Rules\\\"",
    "Lost Girl",
    "Ferris Wheel",
    "Attack of the Killer Queen (with Lena Raine and Marcy Nabors)",
    "Giga Size",
    "Powers Combined",
    "Knock You Down !!",
    "The Dark Truth",
    "Digital Roots",
    "Deal Gone Wrong",
    "BIG SHOT",
    "A Real Boy!",
    "Dialtone",
    "Chill Jailbreak Alarm To Study And Relax To",
    "Until Next Time",
    "Berdly (Rejected Concept)",

]

for track in tracks:
    tformatted = track.lower()
    tformatted = re.sub(r"(?=\W)[^ ]", "", tformatted)
    tformatted = tformatted.strip()
    tformatted = tformatted.replace(" ", "-", 4)
    if tformatted.count(" ") > 0:
        tformatted = tformatted[:tformatted.find(" ")]

    print(data_formatted.format(
        link=base_link.format(tformatted), title=f"{track} - Deltarune"))
