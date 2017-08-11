import os
import tweepy
import time
from subprocess import Popen,PIPE,STDOUT
import pytumblr
from keys import *
from random import choice
from mastodon import Mastodon
from time import sleep

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_token_key, twitter_token_secret)
api = tweepy.API(auth)
tumblr_client = pytumblr.TumblrRestClient(tumblr_consumer_key, tumblr_consumer_secret, tumblr_token_key, tumblr_token_secret)
mastodon_client = Mastodon(api_base_url='https://botsin.space',client_id=mastodon_client_id,client_secret=mastodon_client_secret,access_token=mastodon_access_token)

# define your directory path
basedir = "/home/vgan/spacesh1ps/"

# only make the animated gifs at midnight and noon
hour_now = time.strftime("%H") 
if hour_now == "00":
	spaceship_image = basedir + "renders/animated/animation.gif"
        animated = True
else:
	spaceship_image = basedir + "renders/spacesh1p.png"
        animated = False

def makeImage():
        spacesh1pscmd = [ basedir + "blender", "-b", "-P", basedir + "spaceship_generator.py" ]
        animationcmd = [ "/usr/bin/convert", "-delay","0", "-loop", "0", basedir + "renders/animated/*.png", spaceship_image ]
        p1 = Popen(spacesh1pscmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        output = p1.stdout.read()
        print(output)
        if animated == True:
        	p2 = Popen(animationcmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        	output = p2.stdout.read()
        print(output)

def sendToInterwebs(spaceship_image,spaceship_imageobj,spaceship_name):
        try:
	       	tumblr_client.create_photo('space-sh1ps', state="published", tags=["Procedurally Genenerated","Image Bot","Spaceship"], caption=str(spaceship_name), data=str(spaceship_image))
		sleep(3)
                
        except:
                print("tumbling failed :(")
        try:
        	toot_text = spaceship_name
        	media_dict = mastodon.media_post(spaceship_image)
        	mastodon_client.status_post(toot_text, media_ids=[media_dict], sensitive=False)
        except:
                print("tooting failed :|")

        try:
	        tweet_text = spaceship_name
	        tweet = api.update_with_media(spaceship_image,status=" " + tweet_text , file=spaceship_imageobj)
	        sleep(3)
        except:
                print("tweeting failed :/")


def cleanup():
	try:
		dirPath = basedir + "renders/animated"
		fileList = os.listdir(dirPath)
		for fileName in fileList:
 			os.remove(dirPath+"/"+fileName)
		os.remove(spaceship_image)
	except:
        	print("Cleanup failed")

def GenerateSpaceShipName():
	prefixes =  ["The SS","The SSE","The","The LWSS","The HWSS","The CS","The USS","The BS","The FTLS","The HMS","The BC","The SC","The STS","","","","",""]
	prefix = choice(prefixes)

	animals = [ "Badger","Dragon","Wolf","Beluga","Whale","Coyote","Crocodile", "Phoenix","Eagle","Falcon","Centipede","Gremlin","Griffin","Harpy","Hawk","Jellyfish","Lion","Lucky","Peacock","Pegasus","Pelican","Piranha","Rhino","Serpent","Spider","Termite","Raven","Pelican","Condor","Albatross","Tortoise", "Unicorn","Vulture","Viper","Vampire","Wolf","Wolverine","Woodpecker" ]
	animal = choice(animals)

 	name1_list = [ animal,animal,animal,animal,animal,animal,animal,"Cryptic","Cursed","Baby","Daddy","Girl","Momma","Dark","Grieving","Karmic","Charming","Falling","Frontier","Final","Forlorn","Decrepit","Barbaric","Delicate","Sentimental","Benevolent", "Altruistic","Twisted","Humble", "Bashful", "Depressed","Diabolical","Arrogant","Ferocious","Tiny","Dying","Ancient","Imaginary","Mechanical","Pregnant","Robotic","Rusty","Curious","Wish Upon a", "Ace of","Big","Little","Divine","Eternal","Royal","Star","Fire","Galactic","Hell","Ice","Immortal","Imperial","Majestic","Malevolent","New","Pandora\'s","Perilous","Rebellious","Relentless","Unrelenting","Reliant","Remorseless","Rising","Shooting","Silent","Steel","Stellar","Storm","Thunder","Unstoppable","Untouchable","Vigilant","Wild","","","","","" ]
	name1 = choice(name1_list)

	name2_list = [ "",animal,animal,animal,animal,animal,animal,animal,animal,animal,animal,animal,animal,animal,animal,"Achilles","Actium","Adder","Adventurer","Agememnon","Albatross","Alexander","Alexandria","Alice","Alto","Amanda","Amazon","Ambition","Analyzer","Anarchy","Anastasia","Andromeda","Angel","Angelica","Anna","Annihilator","Antagonist","Antioch","Apocalypse","Apollo","Aquila","Aquitaine","Arcadia","Arcadian","Archmage","Arden","Ares","Argo","Argonaut","Aries","Arizona","Ark","Armada","Armageddon","Arrow","Artemis","Arthas","Ashaton","Assassin","Athens","Atlas","Aurora","Avadora","Avalanche","Avalon","Avenger","Avius","Babylon","Baldrin","Bandit","Barbara","Basilisk","Bastion","Battalion","Battlestar","Bayonet","Behemoth","Beholder","Berserk","Baby","Daddy","Girl","Momma","Bishop","Cloud","Sparrow","Viper","Blade","Blossom","Bob","Bravery","Britain","Brotherhood","Buccaneer","Burn","Burninator","Buzzard","Caelestis","Cain","Calamity","Calypso","Carbonaria","Carnage","Carthage","Cataclysm","Cataphract","Celina","Centurion","Challenger","Chimera","Chronos","Churchill","Civilization","Clap","Claymore","Colossus","Comet","Commissioner","Condor","Confidence","Conqueror","Conquistador","Conscience","Constantine","Constellation","Cordoba","Corsair","Cossack","Courage","Covenant","Crack","Crash","Cromwell","Crusher","Cyclone","Cyclops","Cyclopse","Cydonia","Dagger","Dakota","Damascus","Dart","Dauntless","Death","Defiance","Defiant","Deimos","Deinonychus","Deonida","Desire","Despot","Destiny","Destroyer","Destructor","Detection","Detector","Determination","Devastator","Development","Diplomat","Discovery","Dispatcher","Star","Tooth","Dreadnought","Dream","Duke","Elba","Elena","Elizabeth","Elysium","Emissary","Empress","Endeavor","Enterprise","Escorial","Euphoria","Europa","Evolution","Exarch","Excalibur","Excursionist","Executioner","Executor","Experience","Exploration","Explorer","Exterminator","Facade","Fade","Fafnir", "Fate","Flavia","Fortitude","Fortune","Francesca","Freedom","Frenzy","Frontier","Fudgy","Core","Galatea","Gallimimus","Gauntlet","Geisha","Genesis","Ghunne","Gibraltar","Gladiator","Gladius","Globetrotter","Glorious","Goliath","Guard","Guardian","Halo","Hammer","Hannibal","Harbinger","Harlegand","Harlequin","Harmony","Helios","Herald","Hercules","Herminia","Hope","Horizon","Hunter","Huntress","Hurricane","Icarus","Lance","Independence","Inferno","Infineon","Infinitum","Infinity","Ingenuity","Innuendo","Inquisitor","Insurgent","Intelligence","Interceptor","Intervention","Intrepid","Intruder","Invader","Invictus","Invincible","Irmanda","Isabella","Janissary","Javelin","Judgment","Juggernaut","Karma","Karnack","Katherina","Kennedy","Khan","Kingfisher","Kipper","Knossos","Kraken","Kryptoria","Kyozist","Lancaster","Lavanda","Legacy","Leo","Leviathan","Liberator","Liberty","Lifebringer","Lightning","Loki","Lucidity","Luisa","Lullaby","Lupus","Mace","Voyage","Malta","Manchester","Manhattan","Manticore","Marauder","Marchana","Marduk","Maria","Matador","Memory","Memphis","Mercenary","Merkava","Messenger","Meteor","Millenium","Midway","Minotuar","Montgomery","Muriela","Myrmidon","Navigator","Nebuchadnezzar","Nemesis","Neptune","Nero","Neurotoxin","Neutron","Nexus","Niagara","Night","Nightfall","Nightingale","Nihilus","Nineveh","Ninja","Nirvana","Nomad","Normandy","Nostradamus","Nuria","Oberon","Oblivion","Observer","Ohio","Olavia","Omen","Opal","Oregon","Orion","Paladin","Panama","Pandora","Paradise","Paramount","Pathfinder","Patience","Patriot","Pennsylvania","Phalanx","Philadelphia","Phobetor","Phobos","Pilgrim","Pinnacle","Pioneer","Plaiedes","Polaris","Pontiac","Poseidon","Praetor","Prennia","Priestess","Prometheus","Promise","Prophet","Providence","Proximo","Pursuer","Pursuit","Pyrrhus","Rafaela","Rampart","Ramses","Rascal","Ravager","Ravana","Raven","Raving","Reaver","Remus","Renault","Repulse","Resolution","Retribution","Revenant","Revolution","Rhapsody","Rhodes","Ripper","Rising","Romulus","Roosevelt","Royal","Saber","Sagittarius","Samurai","Sandra","Sara","Saragossa","Saratoga","Scavenger","Scimitar","Scorpio","Scythe","Seleucia","Seraphim","Serenity","Rising","Shade","Shear Razor","Shirley","Siberia","Watcher","Siren","Slayer","Sonne","Sparta","Spartacus","Spectator","Spectrum","Stalker","Stalwart","Finder","Fury","Opal","Talon","Fall","Gazer","Hammer","Hunter","Aurora","Flare","Storm","Spike","Strike","Striker","Sunder","Suzanna","Syracuse","Templar","Tenacity","Tennessee","Teresa","Terigon","Thanatos","Alliance","Colossus","Commissioner","Diplomat","Executioner","Exterminator","Gladiator","Guardian","Head","Harbinger","Inquisitor","Javelin","Leviathan","Liberator","Messenger","Paladin","Promise","Prophet","Siren","Spectator","Titan","Traveler","Trident","Vagabond","Warrior","Watcher","Thebes","Thor","Thylacine","Titan","Titania","Tomahawk","Torment","Totale","Tourist","Trafalgar","Trailblazer","Tranquility","Traveler","Trenxal","Trident","Trinity","Triumph","Troy","Twilight","Typhoon","Tyrant","Ulysses","Unity","Ural","Utopia","Vagabond","Valhala","Valhalla","Valiant","Valkyrie","Valor","Vanguard","Vanquisher","Vengeance","Venom","Vera","Verdant","Verminus","Vespira","Victoria","Victory","Vindicator","Virginia","Vision","Visitor","Voyager","Wind","Warlock","Warrior","Washington","Watcher","Wellington","Wisdom","Star","Wyvern","Xerxes","Yucatan","Zenith","Zephyr","Zeus","Zion"]
	name2 = choice(name2_list) # keep it from using same first + last
	while name1 == name2:
        	name1 = choice(name1_list)
		name2 = choice(name2_list)
	spaceship_name = (prefix + " " + name1 + " " + name2)
	return spaceship_name

def doTheDamnThing():
	makeImage()
	sleep(5)
	if os.path.isfile(spaceship_image):
		size = os.path.getsize(spaceship_image)
		while size > 3000000:
			print("size is " + str(size)) 
        		print("too big, cleanup and try again..")
			cleanup()
			makeImage()
		spaceship_name = GenerateSpaceShipName()     
		spaceship_imageobj = open(spaceship_image)
		sleep(3)
		sendToInterwebs(spaceship_image,spaceship_imageobj,spaceship_name)
		cleanup()
	else:
		print("no image file. wtf?")

doTheDamnThing()
