import random
import sys

namePrefixes = [
    "Gloom",
	"Gray",
	"Dire",
	"Black",
	"Shadow",
	"Haze",
	"Wind",
	"Storm",
	"Warp",
	"Night",
	"Moon",
	"Star",
	"Pit",
	"Fire",
	"Cold",
	"Seethe",
	"Sharp",
	"Ash",
	"Blade",
	"Steel",
	"Stone",
	"Rust",
	"Mold",
	"Blight",
	"Plague",
	"Rot",
	"Ooze",
	"Puke",
	"Snot",
	"Bile",
	"Blood",
	"Pulse",
	"Gut",
	"Gore",
	"Flesh",
	"Bone",
	"Spine",
	"Mind",
	"Spirit",
	"Soul",
	"Wrath",
	"Grief",
	"Foul",
	"Vile",
	"Sin",
	"Chaos",
	"Dread",
	"Doom",
	"Bane",
	"Death",
	"Viper",
	"Dragon",
	"Devil"
]

nameSuffixes = [
    "Touch",
	"Spell",
	"Feast",
	"Wound",
	"Grin",
	"Maim",
	"Hack",
	"Bite",
	"Rend",
	"Burn",
	"Rip",
	"Kill",
	"Call",
	"Vex",
	"Jade",
	"Web",
	"Shield",
	"Killer",
	"Razor",
	"Drinker",
	"Shifter",
	"Crawler",
	"Dancer",
	"Bender",
	"Weaver",
	"Eater",
	"Widow",
	"Maggot",
	"Spawn",
	"Wight",
	"Grumble",
	"Growler",
	"Snarl",
	"Wolf",
	"Crow",
	"Hawk",
	"Cloud",
	"Bang",
	"Head",
	"Skull",
	"Brow",
	"Eye",
	"Maw",
	"Tongue",
	"Fang",
	"Horn",
	"Thorn",
	"Claw",
	"Fist",
	"Heart",
	"Shank",
	"Skin",
	"Wing",
	"Pox",
	"Fester",
	"Blister",
	"Pus",
	"Slime",
	"Drool",
	"Froth",
	"Sludge",
	"Venom",
	"Poison",
	"Break",
	"Shard",
	"Flame",
	"Maul",
	"Thirst",
	"Lust"
]

nameAppelations = [
    "the Hammer",
	"the Axe",
	"the Sharp",
	"the Jagged",
	"the Flayer",
	"the Slasher",
	"the Impaler",
	"the Hunter",
	"the Slayer",
	"the Mauler",
	"the Destroyer",
	"the Quick",
	"the Witch",
	"the Mad",
	"the Wraith",
	"the Shade",
	"the Dead",
	"the Unholy",
	"the Howler",
	"the Grim",
	"the Dark",
	"the Tainted",
	"the Unclean",
	"the Hungry",
	"the Cold"
]

def getUniqueMonsterNames(numberOfUniqueMonsterNames):
    uniqueMonsterNames = []
    for i in range(0, numberOfUniqueMonsterNames):
        shouldNameHaveAppelation = bool(random.randint(0,1))

        uniqueMonsterNamePrefix     = random.choice(namePrefixes)
        uniqueMonsterNameSuffix     = random.choice(nameSuffixes)
        uniqueMonsterNameAppelation = random.choice(nameAppelations)

        uniqueMonsterName = ""
        if shouldNameHaveAppelation:
            uniqueMonsterName = uniqueMonsterNamePrefix + " " + uniqueMonsterNameSuffix + " " + uniqueMonsterNameAppelation
        else:
            uniqueMonsterName = uniqueMonsterNamePrefix + " " + uniqueMonsterNameSuffix

        uniqueMonsterNames.append(uniqueMonsterName)

    return uniqueMonsterNames



print("Welcome to the Diablo 2 Unique Monster Name Generator!")

if len(sys.argv) > 1 and sys.argv[1].isdigit():
    numberOfMonsterNames = int(sys.argv[1])
else:
    numberOfMonsterNamesAsString = input("How many unique monster names would you like? ")
    
    while (not numberOfMonsterNamesAsString.isdigit()):
        numberOfMonsterNamesAsString = input("Sorry, that's not a valid number. How many unique monster names would you like? ")

    numberOfMonsterNames = int(numberOfMonsterNamesAsString)

monsterNames = getUniqueMonsterNames(numberOfMonsterNames)

if numberOfMonsterNames == 1:
    print("Your unique creepy crawler's name is:")
else:
    print("Your unique creepy crawlers' names are:")

for name in monsterNames:
    print(name)
