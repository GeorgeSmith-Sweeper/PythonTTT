class Ui:
    def msg(message):
        print(message)

class CommandLinePrompt:
    def get_input(choice):
        return input(choice)

class GameModeOptions:
    def show_options():
        options_string = ('\n'
                          'Please select from the following game modes'
                          '\n'
                          '1) Human Vs Human'
                          '\n'
                          '2) Human Vs Computer'
                          '\n'
                          '3) Computer Vs Computer'
                          '\n'
                          )
        return options_string 

class LanguageModeOptions:
    def show_options():
        options_string = ('\n'
                          'Would you like play in English or French?'
                          '\n'
                          '1) English'
                          '\n'
                          '2) French'
                          '\n'
                          )
        return options_string 
