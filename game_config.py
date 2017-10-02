from ui import CommandLinePrompt, GAME_MODE_STRING, LANGUAGE_MODE_STRING, PLAYER1_SYMBOL_STRING, PLAYER2_SYMBOL_STRING, Ui
SET_UP = {
    'question': {
        'Language': LANGUAGE_MODE_STRING,
        'Game_Mode': GAME_MODE_STRING,
        },
    'valid_choices': { 
        'Language': ['1', '2'],
        'Game_Mode': ['1', '2', '3'],
        }
    }

SYMBOL_SET_UP = {
    'Player1': PLAYER1_SYMBOL_STRING,
    'Player2': PLAYER2_SYMBOL_STRING, 
    }

config = {
   'Language': None,
   'Game_Mode': None,
   'Player1': None,
   'Player2': None,
    }

class SymbolPrompts():
    def ask_user_questions(self, question):
        symbol_selected = CommandLinePrompt.get_input(question)
        if self.validate_user_symbol(symbol_selected) and self.is_symbol_unique(symbol_selected):
            return symbol_selected
        else:
            self.ask_user_questions(question)

    def validate_user_symbol(self, symbol):
        if len(symbol) is not 1 or symbol == ' ':
            Ui.msg('You must select a symbol. (one character, no spaces)')
            return False
        return symbol
    
    def is_symbol_unique(self, symbol):
        if config['Player1'] is not symbol:
            return True

    def gather_symbols(self, setup):
        for player in setup:
            config[player] = self.ask_user_questions(setup[player])
        
class SetUpPrompts():
    def ask_user_questions(self, question, valid_choices):
        mode_selected = CommandLinePrompt.get_input(question)
        if self.validate_choice(mode_selected, valid_choices):
            return mode_selected
        else:
            Ui.msg('That is not a valid choice. Try Again')
            self.ask_user_questions(question, valid_choices)

    def validate_choice(self, choice, valid_choices):
        if choice in valid_choices:
            return choice

    def run_set_up(self, set_up):
        config_options = []
        for key in set_up['question']:
            config_options.append(key)
        
        for option in config_options:
            config[option] = self.ask_user_questions(set_up['question'][option], set_up['valid_choices'][option])

if __name__ == "__main__":
    setup = SetUpPrompts()
    setup.run_set_up(SET_UP)
    symbol_setup = SymbolPrompts()
    symbol_setup.gather_symbols(SYMBOL_SET_UP)
