from output.keycodes import KeyCodes

# To fix = [ and ] are dots
# @ is a ligature
# Backtick is backslash
# Backslash is

KEY_MAP = {
    "CTRL": [{"Modifiers": ["MOD_LEFT_CONTROL"], "Keys": []}],
    "CONTROL": [{"Modifiers": ["MOD_LEFT_CONTROL"], "Keys": []}],
    "LEFT_CTRL": [{"Modifiers": ["MOD_LEFT_CONTROL"], "Keys": []}],
    "RIGHT_CTRL": [{"Modifiers": ["MOD_RIGHT_CONTROL"], "Keys": []}],
    "ALT": [{"Modifiers": ["MOD_LEFT_ALT"], "Keys": []}],
    "LEFT_ALT": [{"Modifiers": ["MOD_LEFT_ALT"], "Keys": []}],
    "RIGHT_ALT": [{"Modifiers": ["MOD_RIGHT_ALT"], "Keys": []}],
    "SHIFT": [{"Modifiers": ["MOD_LEFT_SHIFT"], "Keys": []}],
    "LEFT_SHIFT": [{"Modifiers": ["MOD_LEFT_SHIFT"], "Keys": []}],
    "RIGHT_SHIFT": [{"Modifiers": ["MOD_RIGHT_SHIFT"], "Keys": []}],
    "GUI": [{"Modifiers": ["MOD_LEFT_GUI"], "Keys": []}],
    "WIN": [{"Modifiers": ["MOD_LEFT_GUI"], "Keys": []}],
    "LEFT_GUI": [{"Modifiers": ["MOD_LEFT_GUI"], "Keys": []}],
    "RIGHT_GUI": [{"Modifiers": ["MOD_RIGHT_GUI"], "Keys": []}],

    "ESC": [{"Modifiers": [], "Keys": ["KEY_ESC"]}],
    "ESCAPE": [{"Modifiers": [], "Keys": ["KEY_ESC"]}],

    "F1": [{"Modifiers": [], "Keys": ["KEY_F1"]}],
    "F2": [{"Modifiers": [], "Keys": ["KEY_F2"]}],
    "F3": [{"Modifiers": [], "Keys": ["KEY_F3"]}],
    "F4": [{"Modifiers": [], "Keys": ["KEY_F4"]}],
    "F5": [{"Modifiers": [], "Keys": ["KEY_F5"]}],
    "F6": [{"Modifiers": [], "Keys": ["KEY_F6"]}],
    "F7": [{"Modifiers": [], "Keys": ["KEY_F7"]}],
    "F8": [{"Modifiers": [], "Keys": ["KEY_F8"]}],
    "F9": [{"Modifiers": [], "Keys": ["KEY_F9"]}],
    "F10": [{"Modifiers": [], "Keys": ["KEY_F10"]}],
    "F11": [{"Modifiers": [], "Keys": ["KEY_F11"]}],
    "F12": [{"Modifiers": [], "Keys": ["KEY_F12"]}],

    "SYSRQ": [{"Modifiers": [], "Keys": ["KEY_SYSRQ"]}],
    "PRINT": [{"Modifiers": [], "Keys": ["KEY_SYSRQ"]}],
    "PRINTSCR": [{"Modifiers": [], "Keys": ["KEY_SYSRQ"]}],
    "SCROLLLOCK": [{"Modifiers": [], "Keys": ["KEY_SCROLLLOCK"]}],
    "SCROLL": [{"Modifiers": [], "Keys": ["KEY_SCROLLLOCK"]}],
    "PAUSE": [{"Modifiers": [], "Keys": ["KEY_PAUSE"]}],
    "BREAK": [{"Modifiers": [], "Keys": ["KEY_PAUSE"]}],
    "BRK": [{"Modifiers": [], "Keys": ["KEY_PAUSE"]}],


    "`": [{"Modifiers": [], "Keys": ["KEY_102ND"]}],
    "1": [{"Modifiers": [],	"Keys": ["KEY_1"]}],
    "2": [{"Modifiers": [],	"Keys": ["KEY_2"]}],
    "3": [{"Modifiers": [],	"Keys": ["KEY_3"]}],
    "4": [{"Modifiers": [],	"Keys": ["KEY_4"]}],
    "5": [{"Modifiers": [],	"Keys": ["KEY_5"]}],
    "6": [{"Modifiers": [],	"Keys": ["KEY_6"]}],
    "7": [{"Modifiers": [],	"Keys": ["KEY_7"]}],
    "8": [{"Modifiers": [],	"Keys": ["KEY_8"]}],
    "9": [{"Modifiers": [],	"Keys": ["KEY_9"]}],
    "0": [{"Modifiers": [],	"Keys": ["KEY_0"]}],
    "-": [{"Modifiers": [],	"Keys": ["KEY_MINUS"]}],
    "=": [{"Modifiers": [], "Keys": ["KEY_EQUAL"]}],

    "¬": [{"Modifiers": ["MOD_LEFT_SHIFT"], "Keys": ["KEY_GRAVE"]}],
    "!": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_1"]}],
    "\"": [{"Modifiers": ["MOD_LEFT_SHIFT"], "Keys": ["KEY_2"]}],
    "£": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_3"]}],
    "$": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_4"]}],
    "%": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_5"]}],
    "^": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_6"]}],
    "&": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_7"]}],
    "*": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_8"]}],
    "(": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_9"]}],
    ")": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_0"]}],
    "_": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_MINUS"]}],
    "+": [{"Modifiers": ["MOD_LEFT_SHIFT"], "Keys": ["KEY_EQUAL"]}],

    "|": [{"Modifiers": ["MOD_LEFT_SHIFT"], "Keys": ["KEY_GRAVE"]}],
    "¹": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_1"]}],
    "²": [{"Modifiers": ["MOD_RIGHT_ALT"], "Keys": ["KEY_2"]}],
    "³": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_3"]}],
    "€": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_4"]}],
    "½": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_5"]}],
    "¾": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_6"]}],
    "{": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_LEFTBRACE"]}],
    "[": [{"Modifiers": [],	"Keys": ["KEY_LEFTBRACE"]}],
    "]": [{"Modifiers": [],	"Keys": ["KEY_RIGHTBRACE"]}],
    "}": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_RIGHTBRACE"]}],
    "\\": [{"Modifiers": [],	"Keys": ["KEY_GRAVE"]}],
    "¸": [{"Modifiers": ["MOD_RIGHT_ALT"], "Keys": ["KEY_EQUAL"]}, {"Modifiers": [], "Keys": ["KEY_SPACE"]}],
    "BACKSPACE": [{"Modifiers": [], "Keys": ["KEY_BACKSPACE"]}],


    "TABULATOR": [{"Modifiers": [], "Keys": ["KEY_TAB"]}],
    "TAB": [{"Modifiers": [], "Keys": ["KEY_TAB"]}],
    "\t": [{"Modifiers": [], "Keys": ["KEY_TAB"]}],
    "q": [{"Modifiers": [],	"Keys": ["KEY_Q"]}],
    "w": [{"Modifiers": [],	"Keys": ["KEY_W"]}],
    "e": [{"Modifiers": [],	"Keys": ["KEY_E"]}],
    "r": [{"Modifiers": [],	"Keys": ["KEY_R"]}],
    "t": [{"Modifiers": [],	"Keys": ["KEY_T"]}],
    "y": [{"Modifiers": [],	"Keys": ["KEY_Y"]}],
    "u": [{"Modifiers": [],	"Keys": ["KEY_U"]}],
    "i": [{"Modifiers": [],	"Keys": ["KEY_I"]}],
    "o": [{"Modifiers": [],	"Keys": ["KEY_O"]}],
    "p": [{"Modifiers": [],	"Keys": ["KEY_P"]}],

    "Q": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_Q"]}],
    "W": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_W"]}],
    "E": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_E"]}],
    "R": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_R"]}],
    "T": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_T"]}],
    "Y": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_Y"]}],
    "U": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_U"]}],
    "I": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_I"]}],
    "O": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_O"]}],
    "P": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_P"]}],

    "@": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_APOSTROPHE"]}],
    "¶": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_R"]}],
    "ŧ": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_T"]}],
    "←": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_Y"]}],
    "↓": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_U"]}],
    "→": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_I"]}],
    "ø": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_O"]}],
    "þ": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_P"]}],

    "ENTER": [{"Modifiers": [], "Keys": ["KEY_ENTER"]}],
    "RETURN": [{"Modifiers": [], "Keys": ["KEY_ENTER"]}],
    "\n": [{"Modifiers": [], "Keys": ["KEY_ENTER"]}],


    "CAPSLOCK": [{"Modifiers": [], "Keys": ["KEY_CAPSLOCK"]}],
    "CAPS": [{"Modifiers": [], "Keys": ["KEY_CAPSLOCK"]}],
    "a": [{"Modifiers": [],	"Keys": ["KEY_A"]}],
    "s": [{"Modifiers": [],	"Keys": ["KEY_S"]}],
    "d": [{"Modifiers": [],	"Keys": ["KEY_D"]}],
    "f": [{"Modifiers": [],	"Keys": ["KEY_F"]}],
    "g": [{"Modifiers": [],	"Keys": ["KEY_G"]}],
    "h": [{"Modifiers": [],	"Keys": ["KEY_H"]}],
    "j": [{"Modifiers": [],	"Keys": ["KEY_J"]}],
    "k": [{"Modifiers": [],	"Keys": ["KEY_K"]}],
    "l": [{"Modifiers": [],	"Keys": ["KEY_L"]}],
    ";": [{"Modifiers": [],	"Keys": ["KEY_SEMICOLON"]}],
    "'": [{"Modifiers": [],	"Keys": ["KEY_APOSTROPHE"]}],
    "#": [{"Modifiers": [],	"Keys": ["KEY_BACKSLASH"]}],

    "A": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_A"]}],
    "S": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_S"]}],
    "D": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_D"]}],
    "F": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_F"]}],
    "G": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_G"]}],
    "H": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_H"]}],
    "J": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_J"]}],
    "K": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_K"]}],
    "L": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_L"]}],
    ":": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_SEMICOLON"]}],
    "~": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_BACKSLASH"]}],

    "æ": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_A"]}],
    "ß": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_S"]}],
    "ð": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_D"]}],
    "đ": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_F"]}],
    "ŋ": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_G"]}],
    "ħ": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_H"]}],

    "ĸ": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_K"]}],
    "ł": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_L"]}],

    "z": [{"Modifiers": [],	"Keys": ["KEY_Z"]}],
    "x": [{"Modifiers": [],	"Keys": ["KEY_X"]}],
    "c": [{"Modifiers": [],	"Keys": ["KEY_C"]}],
    "v": [{"Modifiers": [],	"Keys": ["KEY_V"]}],
    "b": [{"Modifiers": [],	"Keys": ["KEY_B"]}],
    "n": [{"Modifiers": [],	"Keys": ["KEY_N"]}],
    "m": [{"Modifiers": [],	"Keys": ["KEY_M"]}],
    ",": [{"Modifiers": [],	"Keys": ["KEY_COMMA"]}],
    ".": [{"Modifiers": [],	"Keys": ["KEY_DOT"]}],
    "/": [{"Modifiers": [],	"Keys": ["KEY_SLASH"]}],


    "Z": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_Z"]}],
    "X": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_X"]}],
    "C": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_C"]}],
    "V": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_V"]}],
    "B": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_B"]}],
    "N": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_N"]}],
    "M": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_M"]}],
    "<": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_COMMA"]}],
    ">": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_DOT"]}],
    "?": [{"Modifiers": ["MOD_LEFT_SHIFT"],	"Keys": ["KEY_SLASH"]}],

    "«": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_Z"]}],
    "»": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_X"]}],
    "¢": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_C"]}],
    "“": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_V"]}],
    "”": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_B"]}],
    "µ": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_M"]}],

    "·": [{"Modifiers": ["MOD_RIGHT_ALT"],	"Keys": ["KEY_DOT"]}],



    " ": [{"Modifiers": [], "Keys": ["KEY_SPACE"]}],
    "SPACE": [{"Modifiers": [], "Keys": ["KEY_SPACE"]}],
    "SPACEBAR": [{"Modifiers": [], "Keys": ["KEY_SPACE"]}],

    "INSERT": [{"Modifiers": [], "Keys": ["KEY_INSERT"]}],
    "INS": [{"Modifiers": [], "Keys": ["KEY_INSERT"]}],
    "HOME": [{"Modifiers": [], "Keys": ["KEY_HOME"]}],
    "POS1": [{"Modifiers": [], "Keys": ["KEY_HOME"]}],
    "PAGEUP": [{"Modifiers": [], "Keys": ["KEY_PAGEUP"]}],
    "DELETE": [{"Modifiers": [], "Keys": ["KEY_DELETE"]}],
    "DEL": [{"Modifiers": [], "Keys": ["KEY_DELETE"]}],
    "END": [{"Modifiers": [], "Keys": ["KEY_END"]}],
    "PAGEDOWN": [{"Modifiers": [], "Keys": ["KEY_PAGEDOWN"]}],
    "RIGHT": [{"Modifiers": [], "Keys": ["KEY_RIGHT"]}],

    "LEFT": [{"Modifiers": [], "Keys": ["KEY_LEFT"]}],
    "DOWN": [{"Modifiers": [], "Keys": ["KEY_DOWN"]}],
    "UP": [{"Modifiers": [], "Keys": ["KEY_UP"]}],
    "RIGHT_ARROW": [{"Modifiers": [], "Keys": ["KEY_RIGHT"]}],
    "LEFT_ARROW": [{"Modifiers": [], "Keys": ["KEY_LEFT"]}],
    "DOWN_ARROW": [{"Modifiers": [], "Keys": ["KEY_DOWN"]}],
    "UP_ARROW": [{"Modifiers": [], "Keys": ["KEY_UP"]}],


    "COMPOSE": [{"Modifiers": [], "Keys": ["KEY_COMPOSE"]}],

    "NUMLOCK": [{"Modifiers": [], "Keys": ["KEY_NUMLOCK"]}],
    "NUM": [{"Modifiers": [], "Keys": ["KEY_NUMLOCK"]}],


    "F13": [{"Modifiers": [], "Keys": ["KEY_F13"]}],
    "F14": [{"Modifiers": [], "Keys": ["KEY_F14"]}],
    "F15": [{"Modifiers": [], "Keys": ["KEY_F15"]}],
    "F16": [{"Modifiers": [], "Keys": ["KEY_F16"]}],
    "F17": [{"Modifiers": [], "Keys": ["KEY_F17"]}],
    "F18": [{"Modifiers": [], "Keys": ["KEY_F18"]}],
    "F19": [{"Modifiers": [], "Keys": ["KEY_F19"]}],
    "F20": [{"Modifiers": [], "Keys": ["KEY_F20"]}],
    "F21": [{"Modifiers": [], "Keys": ["KEY_F21"]}],
    "F22": [{"Modifiers": [], "Keys": ["KEY_F22"]}],
    "F23": [{"Modifiers": [], "Keys": ["KEY_F23"]}],
    "F24": [{"Modifiers": [], "Keys": ["KEY_F24"]}]
}

class GBKeyboard(object):
    def __init__(self):
        self.codes = KeyCodes()

    def encode(self, text):
        output = []
        for digit in text:
            if digit in KEY_MAP:
                for item in KEY_MAP[digit]:
                    mod_byte = 0
                    key_bytes = ""
                    for mod in item['Modifiers']:
                        mod_byte = mod_byte | self.codes[mod]
                    for key in item['Keys']:
                        key_bytes = key_bytes + chr(self.codes[key])

                    encoded = chr(mod_byte) + chr(0) + key_bytes + (chr(0) * (6 - len(key_bytes)))
                    output.append(encoded)

        return output
