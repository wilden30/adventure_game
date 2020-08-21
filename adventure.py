from data2 import *

try:
    import readline
except ImportError:
    pass

###########
# Parsing #
###########

def adv_parse(line):
    tokens = line.split()
    if not tokens:
        raise SyntaxError('No command given')
    command = tokens.pop(0)
    if command in ('talk', 'go'):
        if not tokens or tokens[0] != 'to':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS[command]))
        return (command + '_to', ' '.join(tokens[1:]))
    elif command == 'check':
        if not tokens or tokens[0] != 'backpack':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS['check backpack']))
        return ('check_backpack', '')
    elif command =='give':
        if not tokens or 'to' not in tokens:
            raise SyntaxError('Unrecognizable command.')
        return (command, ' '.join(tokens).split(' to '))
    elif command == 'unlock':
        return ('unlock', ' '.join(tokens))
    else:
        return (command, ' '.join(tokens))

##############
# Evaluation #
##############

def adv_eval(exp):
    operator, operand = exp[0], exp[1]
    if operator not in COMMAND_NUM_ARGS:
        help()
        raise SyntaxError('Invalid command: {}'.format(operator))
    elif operator in SPECIAL_FORMS:
        function = SPECIAL_FORMS[operator]
    else:
        function = getattr(me, operator)

    if COMMAND_NUM_ARGS[operator] == 0:
        function()
    elif COMMAND_NUM_ARGS[operator] == 1:
        function(operand)
    else:
        function(operand[0],operand[1])

def help():
    print('There are {} possible commands:'.format(len(COMMAND_FORMATS)))
    for usage in COMMAND_FORMATS.values():
        print('   ', usage)

def check_win_state(player):
    """Checks if the player is in a winning state.""" 
    #when location is police
    if player.place == police:
        return True
    else:
        return False

    '''
    if player.place != old_library:
        return False

    print()
    player_backpack = player.check_backpack()
    if 'Wallet' in player_backpack and 'Sushi' in player_backpack:
        return True
    else:
        print()
        print("Looks like you're missing some items. Can't go to the project party yet!")
        return False
    '''

########
# REPL #
########

def read_eval_print_loop():
    print(WELCOME_MESSAGE)
    if not isinstance(me, Player):
        print('Oh no! You need to create a player at the bottom of data.py to start the game.')
        return

    help()
    while True:
        if check_win_state(me):
            print(WIN_MESSAGE)
            return
        print()
        try:
            line = input('adventure> ')
            exp = adv_parse(line)
            adv_eval(exp)
        except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
            print('\nGood game. Bye!')
            return
        # If the player input was badly formed or if something doesn't exist
        except SyntaxError as e:
            print('ERROR:', e)

#################
# Configuration #
#################

COMMAND_FORMATS = {
    'look': 'look',
    'go': 'go to [place]',
    'take': 'take [thing]',
    'talk': 'talk to [character]',
    'check backpack': 'check backpack',
    'help': 'help',
    'unlock': 'unlock [place]',
    'give':'give [thing] to [character]'
}

COMMAND_NUM_ARGS = {
    'look': 0,
    'go_to': 1,
    'take': 1,
    'talk_to': 1,
    'check_backpack': 0,
    'help': 0,
    'unlock': 1,
    'give': 2
}

SPECIAL_FORMS = {
    'help': help,
}

#find clues, and go to the cops once you find the murderer's identity. you are a private investigator hired by urban.
WELCOME_MESSAGE = """
Welcome to the Private Investigation game!

It's a bright sunny day, and you are on the Urban Yacht.
The student William Denton was murdered on this boat yesterday, and Urban has hired you to figure out what happened.
Investigate the clues, and once you figure out the murderer's identity, turn him/her/them in to the cops.

"""

WIN_MESSAGE = """
You succesfully ascertained the identity of the murderer and turned her into the police. 

Urban thanks you for your work and pays you with a $20 gift card to HSM.

Congratulations! You won the Urban murder mystery game!
"""


if __name__ == '__main__':
    read_eval_print_loop()

