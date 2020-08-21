from classes import *

#Things:
wallet = Thing('Wallet', "Keep the cash! You can't find an ID.")
tournament_flyer= Thing('Tournament Flyer', 'Looks like the recently deceased William won the Othello AI tournament.')
botella_verde = Thing('a green water bottle',
               'This looks a lot like Danny\'s botella verde.')
Gregs_markers = Thing("Greg\'s markers",
                      "You can tell that these markers have been thrown at hundreds of students")
Meteor = Thing('Meteor', 'A meteor that arrived from outer space. Maybe a physics teacher would be interested in it.')
vintage_camera = Thing('Vintage Camera', 'Wow! Cool vintage camera. Maybe a photography teacher would like this.')
encrypted_password = Thing('An encrypted password', 'Try to find someone good at math who could decode it.')
bloody_knife = Thing('A Bloody Knife', 'Wow, the blood on this knife looks a lot like William\'s.')
bloody_gloves = Thing('Bloody Gloves', 'Some bloody gloves. Whoever committed this murder had small hands.')
parisa_thermos = Thing('Parisa\'s Thermos', 'This Thermos belongs to Parisa. Give it to her when you get the chance.')
rowing_boat = Thing('Rowing Boat Toy', 'A vintage rowing boat toy. If you know anyone who likes to row (someone energetic), they may be interested.')
williams_note = Thing('William\'s Note', 'I think whoever is plotting my murder is hiding out in the master bedroom. I hope I get to them before they get to me.')
parisa_confession = Thing('Parisa\'s murder Confession', 'I had to stop William before his AI got out of hand. After the Othello tournament, I saw that his AI would soon destroy the world. I only did what I had to in order to save mankind.')
powerful_AI = Thing('USB drive','This USB drive contains William\'s AI. It has the power to destroy the world. Keep it safe or destroy it, your choice.')


# Keys:
captain_key = Key('Captain\'s quarters key', 'A key that obviously unlocks the Captain\'s quarters', 'The Captain\'s Quarters')
decrypted_password = Key('Safe Password', 'A password to a safe.', 'The Safe in the Captain\'s Quarters')
master_bedroom_key = Key('Master Bedroom Key', 'A key to the master befroom.','The Master Bedroom')


#Characters
noDesireForExchange = [Thing('',''),Thing('','')]
matthew_casey = Character('Matthew Casey', 'Man, I love meteors.',[Meteor, captain_key])
kelli_yon = Character('Kelli Yon', 'Photography is so cool! I love capturing special moments.', [vintage_camera,captain_key])
richard_lautze = Character('Richard Lautze', 'My ability to decrypt messages is BYI. I just love decryption!',[encrypted_password,decrypted_password])
danny = Character('Danny Cardozlad', 'I\'m in a bad mood because someone stole my botella verde (green water bottle). I miss it so much.',[botella_verde,master_bedroom_key])
riley = Character('Riley','God, I love rowing and being energetic! I just wish I could row out all my energy, but that\'s not possible because I hav god-like infinite energy.',[rowing_boat, botella_verde])
parisa = Character('Parisa', 'Alright you\'ve caught me. But I did it for you.',[parisa_thermos, powerful_AI])
ben = Character('Ben Slater', 'Come to YMG and write a poem with me.',noDesireForExchange)
charlotte = Character('Charlotte', 'In all my years at Urban, I\'ve never had a student murdered before', noDesireForExchange)
dan = Character('Dan Miller', 'What a way to start my time at Urban. This is all so exciting.',noDesireForExchange)
kaern = Character('Kaern', 'How does that make you feel?',noDesireForExchange)
esteban = Character('Esteban', 'There may be a murdered student, but I still expect my class to show up on time with their homework completed.', noDesireForExchange)
captain = Character('Captain','I can\'t get my safe open. The password on that piece of paper is encrypted.', noDesireForExchange)
yachty = Character('Lil Yachty','I\'m lil yachty on a yacht. Go stream my new album.',noDesireForExchange)


# Places:
main_cabin = Place('Main Cabin', 'Welcome to the main Cabin. If you look carefully, you can still see the bloody spot in the carpet where William was murdered.',[dan,kaern,danny],[bloody_knife,bloody_gloves,tournament_flyer])
engine_room = Place('Engine Room', 'There are quite a few engines in here. Everything seems to be going well.',[esteban],[vintage_camera])
sky_deck = Place('Sky Deck','Wow what a view. You can see at least 4 stars from here.',[ben],[Meteor])
captain_quarters = Place('The Captain\'s Quarters','The captain is steering and welcomes you with a warm smile.',[captain],[encrypted_password])
safe = Place('The Safe in the Captain\'s Quarters', 'This safe has quite a few secrets.',[],[williams_note,rowing_boat,parisa_thermos])
master_bedroom = Place('The Master Bedroom', 'This is the murderer\'s lair. Go to the police to turn in the murderer.',[parisa],[parisa_confession])
police = Place('The Police', '',[],[])
main_hallway = Place('Main Hallway','The main hallway of the yacht.',[],[tournament_flyer])
teachers_lounge = Place('The Teacher\'s Lounge','All the teachers are just hanging out and chatting even though a student was just murdered.',[richard_lautze, kelli_yon,charlotte, yachty],[Gregs_markers,wallet,tournament_flyer])
classroom = Place('A Classroom on a Yacht','Of course the teachers got a yacht with a classroom. Riley and Matthew are doing math on a chalk board.',[riley,matthew_casey],[tournament_flyer])

#exits
main_cabin.add_exits([main_hallway,engine_room])
engine_room.add_exits([main_cabin])
sky_deck.add_exits([captain_quarters,main_hallway])
captain_quarters.add_exits([sky_deck,safe])
safe.add_exits([captain_quarters])
master_bedroom.add_exits([main_hallway, police])
police.add_exits([master_bedroom])
main_hallway.add_exits([main_cabin,sky_deck,master_bedroom,teachers_lounge,classroom])
teachers_lounge.add_exits([main_hallway])
classroom.add_exits([main_hallway])

#locked buildings
safe.locked = True
captain_quarters.locked = True
master_bedroom.locked = True

# Player:
me = Player('Private Investigator',main_cabin)



