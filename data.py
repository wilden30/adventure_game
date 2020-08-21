from classes import *



# Things:
wallet = Thing('Wallet',
               "Looks like Scott's wallet. We should return it to him.")
sushi = Thing('Sushi',
               'Sushi! Yummy! Bring it to a math teacher!')
coffee = Thing('Coffee',
               'The caffienated nectar of the gods.')
estebans_cart = Thing("Esteban's Cart",
                      "Esteban's cart. What is in it, Dinosaur? Giraffe? Who knows.")
cookie = Thing('Cookie', 'A huge cookie')
donut = Thing('Donut', 'A huge donut')
cupcake = Thing('Cupcake', 'A huge cupcake')
computer = Thing('Computer', 'A computer that Parisa would like')
goodGrade = Thing('Good Grade', 'Parisa gave you this for a computer.')

# Keys:
try:
    skeleton_key = Key('Skeleton Key', 'A key that unlocks many doors', 'all')
except NameError as e:
    skeleton_key = Thing('Not a Skeleton Key', 'You must first implement the Key class')

cp_key = Key('CP Key', 'This key unlocks Coffee to the People', 'CP')

# Characters:
noDesireForExchange = [Thing('',''),Thing('','')]

scott = Character('Scott',
                 "I can't believe I lost my wallet again! "
                 "I wish someone could find it for me.",noDesireForExchange)
parisa = Character('Parisa', 'ACHOO!',[computer, cp_key])
kaern = Character('Kaern',
                   'How does that make you feel?',noDesireForExchange)
riley = Character('Riley',
                    'No one brought food to the meeting!'
                    'Maybe the Haight Street Market (HSM) is open; we can get food there.',noDesireForExchange)
donald = Character('Donald',
                    "I actually don't have a bad hairline.",noDesireForExchange)
rebecca = Character('Rebecca',
                  'Hey! Want to play ultimate frisbee?',noDesireForExchange)
student = Character('Student',
                    "I once went into Garden Room and got kicked out! ",noDesireForExchange)
scared_student = Character('Terrified Student',
                           "I don't even go to the bathroom on the first floor anymore!",noDesireForExchange)


# Places:

front_desk = Place('Front Desk',"The Front Desk - I don't know why you say goodbye I say hello.",
                    [parisa], [computer])
cp = Place('CP', 'Coffee to the People - right on!',
            [], [wallet, coffee])
nse = Place('NSE', 'the North Street Extension - The new new new building', [], [cupcake])
infinity = Place('Infinity', 'Hotel Infinity - You can check out but you can never leave.', [riley], [])
hsm = Place('HSM', 'Haight Street Market - Part of the slow food movement.',
            [], [sushi])
gym = Place('Gym', 'the Gym - The stage is for seniors!',
                  [kaern], [])
bound_together = Place('Bound Together', 'Bound Together - The Anarchist Collective',
                   [scott], [cp_key])
old_library = Place('Old Library', 'The Old Library. This was once a library.',
            [], [])
haight = Place('Haight', 'Haight Street',
                 [donald], [cookie])
admissions = Place('Admissions', 'Admissions. We call them visitors not shadows.',
                [], [])
garden_room = Place("Garden Room", "the Garden Room. You only get to take classes here room if you take Spanish.",
                 [student], [estebans_cart])
charlottes_office = Place("Charlotte's Office", "in Charlotte's Office. WHat now?",
                      [scared_student], [])
bunny_meadow = Place('Bunny Meadow', 'Bunny Meadow on a beautiful day',
                       [rebecca], [])



# Exits:
front_desk.add_exits([hsm, admissions, garden_room, bunny_meadow])
hsm.add_exits([front_desk])
admissions.add_exits([front_desk, gym])
charlottes_office.add_exits([bound_together, garden_room])
garden_room.add_exits([front_desk, nse, admissions, charlottes_office])
bunny_meadow.add_exits([front_desk, cp, gym, infinity])
gym.add_exits([bunny_meadow, admissions])
nse.add_exits([cp, infinity, haight, garden_room])
haight.add_exits([nse, bound_together])
cp.add_exits([nse, bunny_meadow])
infinity.add_exits([old_library, nse, bunny_meadow])
old_library.add_exits([infinity])
bound_together.add_exits([haight])

# Locked Buildings
cp.locked = True

# Player:
# The Player should start at front_desk.
me = Player('Gandalf',front_desk)

