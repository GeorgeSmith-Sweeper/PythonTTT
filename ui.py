class Ui:
    def msg(message):
        print(message)

class CommandLinePrompt:
    def get_input(choice):
        return input(choice)

class GameModeOptions:
    def show_options():
        OPTIONS_STRING = ('\n'
                          'Please select from the following game modes'
                          '\n'
                          '1) Human Vs Human'
                          '\n'
                          '2) Human Vs Computer'
                          '\n'
                          '3) Computer Vs Computer'
                          '\n'
                          )
        return OPTIONS_STRING 

class LanguageModeOptions:
    def show_options():
        OPTIONS_STRING = ('\n'
                          'Would you like play in English or French?'
                          '\n'
                          '1) English'
                          '\n'
                          '2) French'
                          '\n'
                          )
        return OPTIONS_STRING 


GAME_MODE_STRING = ('\n'
                    'Please select from the following game modes'
                    '\n'
                    '1) Human Vs Human'
                    '\n'
                    '2) Human Vs Computer'
                    '\n'
                    '3) Computer Vs Computer'
                    '\n'
                    )

LANGUAGE_MODE_STRING = ('\n'
                        'Would you like play in English or French?'
                        '\n'
                        '1) English'
                        '\n'
                        '2) French'
                        '\n'
                        )
