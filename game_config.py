from ui import CommandLinePrompt, GameModeOptions, LanguageModeOptions 

# Only difference are the options objects
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
           raise ValueError
    
class LanguageModeValidation:
    def __init__(self, language):
        self.language = language
        
    def validate(self):
        if self.language == '1' or self.language == '2': 
            GameConfig.language = self.language
        else:
           raise ValueError


def prompt_till_valid():
    try:    
        mode = GameModeValidation(GameModePrompt.ask_user_questions())
        mode.validate()
    except ValueError:
        prompt_till_valid()
            
class GameConfig:
    mode = None
    language = None

if __name__ == "__main__":
    prompt_till_valid()
