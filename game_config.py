from ui import CommandLinePrompt, GAME_MODE_STRING, LANGUAGE_MODE_STRING 

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
        config_options = ['Language', 'Game_Mode']
        for option in config_options:
            config[option] = self.ask_user_questions(set_up['question'][option], set_up['valid_choices'][option])

if __name__ == "__main__":
    setup = SetUpPrompts()
    setup.run_set_up(SET_UP)
'''    
if __name__ == "__main__":
    setup = SetUpPrompts()
    language = setup.ask_user_questions(LanguageModeOptions)
'''     
'''
class GameModePrompt:
    def ask_user_questions():
        mode_selected = CommandLinePrompt.get_input(GameModeOptions.show_options())
        return mode_selected 

class LanguageModePrompt():
    def ask_user_questions():
        mode_selected = CommandLinePrompt.get_input(LanguageModeOptions.show_options())
        return mode_selected 

class GameModeValidation:
    def __init__(self, mode):
        self.mode = mode
        
    def validate(self):
        if self.mode == '1' or self.mode == '2' or self.mode == '3':
            GameConfig.mode = self.mode
        else:
           return False 
    
class LanguageModeValidation:
    def __init__(self, language):
        self.language = language
        
    def validate(self):
        if self.language == '1' or self.language == '2': 
            GameConfig.language = self.language
        else:
           return False 

class PromptLoop(GameModeOptions, LanguageModeOptions):
    def __init__(self):
        self.GameModeOptions = GameModeOptions 
        self.LanguageModeOptions = LanguageModeOptions 
        self.all_options = [self.mode_options, self.language_options]

def prompt_till_valid(prompts):
        while len(prompts.all_options) > 0:
            mode = GameModeValidation(GameModePrompt.ask_user_questions())
            while mode.validate() == False: 
                mode = GameModeValidation(GameModePrompt.ask_user_questions())
            prompts.all_options.pop() 

class GameConfig:
    mode = None
    language = None

if __name__ == "__main__":
    config = PromptLoop(GameModeOptions, LanguageModeOptions)
    prompt_till_valid(config)
'''
