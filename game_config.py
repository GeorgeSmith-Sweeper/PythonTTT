from ui import CommandLinePrompt, GAME_MODE_STRING, LANGUAGE_MODE_STRING, PLAYER1_SYMBOL_STRING 

SET_UP = {
    'question': {
        'Language': LANGUAGE_MODE_STRING,
        'Game_Mode': GAME_MODE_STRING,
        'Player1_Symbol': PLAYER1_SYMBOL_STRING
        },
    'valid_choices': { 
        'Language': ['1', '2'],
        'Game_Mode': ['1', '2', '3'],
        'Player1_Symbol': ['X', 'O'],
        }
    }

config = {"Language": None}

class SetUpPrompts():

    def ask_user_questions(self, question, valid_choices):
        mode_selected = CommandLinePrompt.get_input(question)
        if self.validate_choice(mode_selected, valid_choices):
            return mode_selected
        else:
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
