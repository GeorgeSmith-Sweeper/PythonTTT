from ui import CommandLinePrompt, GameModeOptions 

class GameModePrompt:
    def ask_user_for_mode():
        mode_selected = CommandLinePrompt.get_input(GameModeOptions.show_options())
        return mode_selected 

class ModeValidation:
    def __init__(self, mode):
        self.mode = mode
        
    def validate(self):
        if self.mode == '1' or self.mode == '2' or self.mode == '3':
            GameConfig.mode = self.mode
        else:
           raise ValueError


def prompt_till_valid():
    try:    
        mode = ModeValidation(GameModePrompt.ask_user_for_mode())
        mode.validate()
    except ValueError:
        prompt_till_valid()
            

class GameConfig:
    mode = None
    
'''
    Ui = CommandLine()
    Config = GameConfig(Ui)
    Game = Game(Config)
'''

if __name__ == "__main__":
    prompt_till_valid()
