# A "simple" adventure game.

class Player(object):
    def __init__(self, name, place):
        """Create a player object."""
        self.name = name
        self.place = place
        self.backpack = []

    def look(self):
        self.place.look()

    def go_to(self, location):
        """Go to a location, i.e., change player's place if it's among the exits of player's current place.
        """
        if location in list(self.place.exits):
            if self.place.exits[location].locked:
                print(str(location) + ' is locked, use a key to unlock it.')
            else:
                self.place = self.place.exits[location] #no idea if I'm doing this right?
                print('You are at ' + str(self.place.name))
        else:
            print('Can\'t go to ' + str(location) + ' from ' + str(self.place.name))


        #"*** YOUR CODE HERE - You only need to add an else statement followed by a print ***"

    def talk_to(self, person):
        print(str(self.place.characters[person].name)+ ' says ' +str(self.place.characters[person].message))
       
        #"*** YOUR CODE HERE ***"

    def take(self, thing):
        if self.place.take(thing):
            print('player takes '+ str(thing))
            self.backpack.append(self.place.things[thing])
            self.place.things.pop(thing)

        else:
            print(str(thing) +'is not here')

        """Take a thing if thing is at player's current place
        """

     
        #"*** YOUR CODE HERE ***"

    def check_backpack(self):
        namelist = []
        for item in self.backpack:
            print(str(item.name) + ' '+ str(item.description))
            namelist.append(item.name)
        return namelist
        """Print each item with its description and return a list of item names.
        """
        

    def unlock(self, place):
        """If player has a key, unlock a locked neighboring place.
        """
        for item in self.backpack:
            if isinstance(item, Key):
                if place in list(self.place.exits):
                    item.use(self.place.exits[place])
        if self.place.exits[place].locked:
            print('can\'t unlock ' + str(self.place.name))
        
        #"*** YOUR CODE HERE ***"

    def give(self, objectToGive, personToGiveTo):
        if objectToGive in [item.name for item in self.backpack] and personToGiveTo in list(self.place.characters):
            self.place.characters[personToGiveTo].giveObject(self, self.backpack[[item.name for item in self.backpack].index(objectToGive)])
        else:
            print('Either ' + str(personToGiveTo) + ' isn\'t here or you can\'t give '+ str(objectToGive) + ' to ' +str(personToGiveTo))

   

class Character(object):
    def __init__(self, name, message, objectExchange):
        self.name = name
        self.message = message
        self.desiredObject = objectExchange[0]
        self.objectToGive = objectExchange[1]

    def talk(self):
        return self.message

    def giveObject(self, player, thing):
        if thing.name == self.desiredObject.name:
            player.backpack.append(self.objectToGive)
            player.backpack.remove(thing)
            print(str(self.name) +' says thank you so much for ' + str(thing.name) +'! Here is ' + str(self.objectToGive.name))
            self.objectToGive = Thing('','')
        else:
            print('I don\'t want that!')



class Thing(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, place):
        print("You can't use a {0} here".format(self.name))

class Key(Thing):
    def __init__(self, name, description, placeItUnlocks):
        Thing.__init__(self, name, description)
        self.placeItUnlocks = placeItUnlocks

    def use(self, place):
        if self.placeItUnlocks == 'all' or self.placeItUnlocks == place.name:
            place.locked = False
            print(str(place.name) + ' is unlocked!')
        else:
            print(str(self.name) + ' can\'t unlock ' + str(place.name))

class Treasure(Thing):
    def __init__(self, name, description, value, weight):
        Thing.__init__(self, name, description)
        self.value = value
        self.weight = weight

class Place(object):
    def __init__(self, name, description, characters, things):
        self.name = name
        self.description = description
        self.characters = {character.name: character for character in characters}
        self.things = {thing.name: thing for thing in things}
        self.locked = False
        self.exits = {} # {'name': (exit, 'description')}

    def look(self):
        print('You are currently at ' + str(self.name) + '. You take a look around and see:\n') #may not need all the \n
        print('Characters:\n')
        if len(list(self.characters)) != 0:
            for character in list(self.characters):
                print('     '+str(character)+'\n')
        else:
            print('no one\n')
        print('Things:\n')
        if len(list(self.things)) != 0:
            for thing in list(self.things):
                print('     '+str(thing)+'\n')
        else:
            print('nothing in particular\n')
        print('You can exit to:\n')
        if len(list(self.exits)) != 0:
            for exit in list(self.exits):
                print('     '+str(exit)+'\n')
        else:
            print('There are no exits\n')

            #"*** YOUR CODE HERE ***"


    def take(self, thing):
        if thing in list(self.things):
            
            return True
        else:
            return False
         #"*** YOUR CODE HERE ***"
  
    def check_exits(self):
        print(1)
     #"*** YOUR CODE HERE ***"
 
    def add_exits(self, places):
        for place in places:
            self.exits[place.name] = place
        #"*** YOUR CODE HERE ***"
