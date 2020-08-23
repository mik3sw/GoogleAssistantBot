from configparser import ConfigParser
import config
# General functions and utilities

#Build a button menu (inline and keyboard)
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

#Read message text from 'strings.ini'
def txtReader(setting):
    s = ConfigParser();
    s.read('strings.ini')
    return s.get(setting, config.language)