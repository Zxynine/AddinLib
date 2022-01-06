




valueToKeyMap:'dict[int,KeyCode]' = {}
nameToKeyMap:'dict[str,KeyCode]' = {}
def GetKeyCode(key:str):
	repr = None # Either ord OR the dict access will throw an error
	if len(key) == 1: repr = valueToKeyMap.get(ord(key))
	return repr or nameToKeyMap.get(key.lower(), key)

def GetSequenceRepr(keySeq:str):
	keys = keySeq.split('+')
	vk = GetKeyCode(keys[-1])
	# Make each word capital and replace the end key with the representation
	keys = list(map(str.capitalize,keys[:-1]))+[vk.repr,]
	return '+'.join(keys), vk.repr





class KeyCode:
	def __init__(self, name:str, value:int, representation:str, hex:hex):
		self.id = value
		self.name = name
		self.hex = hex
		self.repr = representation
		nameToKeyMap[name.lower()] = self #Lower ensures consistency, just be sure that when you search, you also use lower
		valueToKeyMap[value] = self

class KeyModifier:
	def __init__(self, name:str, value:int, representation:str, hex:hex):
		self.id = value
		self.name = name
		self.hex = hex
		self.repr = representation
		nameToKeyMap[name.lower()] = self #Lower ensures consistency, just be sure that when you search, you also use lower
		valueToKeyMap[value] = self




class AllKeyCodes:
	EscapeKeyCode =            KeyCode("Escape",            16777216,          'Esc',           0x01000000)
	TabKeyCode =               KeyCode("Tab",               16777217,          'Tab',           0x01000001)
	BacktabKeyCode =           KeyCode("Backtab",           16777218,          'BkTab',         0x01000002)
	BackspaceKeyCode =         KeyCode("Backspace",         16777219,          'Bksp',          0x01000003)
	ReturnKeyCode =            KeyCode("Return",            16777220,          'Return',        0x01000004)
	EnterKeyCode =             KeyCode("Enter",             16777221,          'Enter',         0x01000005)
	InsertKeyCode =            KeyCode("Insert",            16777222,          'Ins',           0x01000006)
	DeleteKeyCode =            KeyCode("Delete",            16777223,          'Del',           0x01000007)
	PauseKeyCode =             KeyCode("Pause",             16777224,          'Pause',         0x01000008)
	PrintKeyCode =             KeyCode("Print",             16777225,          'Print',         0x01000009)
	SysReqKeyCode =            KeyCode("Sys Req",           16777226,          'SysReq',        0x0100000a)
	ClearKeyCode =             KeyCode("Clear",             16777227,          'Clear',         0x0100000b)
	HomeKeyCode =              KeyCode("Home",              16777232,          'Home',          0x01000010)
	EndKeyCode =               KeyCode("End",               16777233,          'End',           0x01000011)
	LeftKeyCode =              KeyCode("Left",              16777234,          'Left',          0x01000012)
	UpKeyCode =                KeyCode("Up",                16777235,          'Up',            0x01000013)
	RightKeyCode =             KeyCode("Right",             16777236,          'Right',         0x01000014)
	DownKeyCode =              KeyCode("Down",              16777237,          'Down',          0x01000015)
	PageUpKeyCode =            KeyCode("PageUp",            16777238,          'PgDn',          0x01000016)
	PageDownKeyCode =          KeyCode("PageDown",          16777239,          'PgUp',          0x01000017)
	ShiftKeyCode =             KeyCode("Shift",             16777248,          'Shift',         0x01000020)
	ControlKeyCode =           KeyCode("Control",           16777249,          'Ctrl',          0x01000021)
	MetaKeyCode =              KeyCode("Meta",              16777250,          'Meta',          0x01000022)
	AltKeyCode =               KeyCode("Alt",               16777251,          'Alt',           0x01000023)
	CapsLockKeyCode =          KeyCode("CapsLock",          16777252,          'CapsLk',        0x01000024)
	NumLockKeyCode =           KeyCode("NumLock",           16777253,          'NumLk',         0x01000025)
	ScrollLockKeyCode =        KeyCode("ScrollLock",        16777254,          'ScrLk',         0x01000026)
	F1KeyCode =                KeyCode("F1",                16777264,          "F1",            0x01000030)
	F2KeyCode =                KeyCode("F2",                16777265,          "F2",            0x01000031)
	F3KeyCode =                KeyCode("F3",                16777266,          "F3",            0x01000032)
	F4KeyCode =                KeyCode("F4",                16777267,          "F4",            0x01000033)
	F5KeyCode =                KeyCode("F5",                16777268,          "F5",            0x01000034)
	F6KeyCode =                KeyCode("F6",                16777269,          "F6",            0x01000035)
	F7KeyCode =                KeyCode("F7",                16777270,          "F7",            0x01000036)
	F8KeyCode =                KeyCode("F8",                16777271,          "F8",            0x01000037)
	F9KeyCode =                KeyCode("F9",                16777272,          "F9",            0x01000038)
	F10KeyCode =               KeyCode("F10",               16777273,          "F10",           0x01000039)
	F11KeyCode =               KeyCode("F11",               16777274,          "F11",           0x0100003a)
	F12KeyCode =               KeyCode("F12",               16777275,          "F12",           0x0100003b)
	F13KeyCode =               KeyCode("F13",               16777276,          "F13",           0x0100003c)
	F14KeyCode =               KeyCode("F14",               16777277,          "F14",           0x0100003d)
	F15KeyCode =               KeyCode("F15",               16777278,          "F15",           0x0100003e)
	F16KeyCode =               KeyCode("F16",               16777279,          "F16",           0x0100003f)
	F17KeyCode =               KeyCode("F17",               16777280,          "F17",           0x01000040)
	F18KeyCode =               KeyCode("F18",               16777281,          "F18",           0x01000041)
	F19KeyCode =               KeyCode("F19",               16777282,          "F19",           0x01000042)
	F20KeyCode =               KeyCode("F20",               16777283,          "F20",           0x01000043)
	F21KeyCode =               KeyCode("F21",               16777284,          "F21",           0x01000044)
	F22KeyCode =               KeyCode("F22",               16777285,          "F22",           0x01000045)
	F23KeyCode =               KeyCode("F23",               16777286,          "F23",           0x01000046)
	F24KeyCode =               KeyCode("F24",               16777287,          "F24",           0x01000047)
	F25KeyCode =               KeyCode("F25",               16777288,          "F25",           0x01000048)
	F26KeyCode =               KeyCode("F26",               16777289,          "F26",           0x01000049)
	F27KeyCode =               KeyCode("F27",               16777290,          "F27",           0x0100004a)
	F28KeyCode =               KeyCode("F28",               16777291,          "F28",           0x0100004b)
	F29KeyCode =               KeyCode("F29",               16777292,          "F29",           0x0100004c)
	F30KeyCode =               KeyCode("F30",               16777293,          "F30",           0x0100004d)
	F31KeyCode =               KeyCode("F31",               16777294,          "F31",           0x0100004e)
	F32KeyCode =               KeyCode("F32",               16777295,          "F32",           0x0100004f)
	F33KeyCode =               KeyCode("F33",               16777296,          "F33",           0x01000050)
	F34KeyCode =               KeyCode("F34",               16777297,          "F34",           0x01000051)
	F35KeyCode =               KeyCode("F35",               16777298,          "F35",           0x01000052)
	Super_LKeyCode =           KeyCode("Super_L",           16777299,          'LSuper',        0x01000053)
	Super_RKeyCode =           KeyCode("Super_R",           16777300,          'RSuper',        0x01000054)
	MenuKeyCode =              KeyCode("Menu",              16777301,          'Menu',          0x01000055)
	Hyper_LKeyCode =           KeyCode("Hyper_L",           16777302,          'LHyper',        0x01000056)
	Hyper_RKeyCode =           KeyCode("Hyper_R",           16777303,          'RHyper',        0x01000057)
	HelpKeyCode =              KeyCode("Help",              16777304,          'Help',          0x01000058)
	Direction_LKeyCode =       KeyCode("Direction_L",       16777305,          'None',          0x01000059)
	Direction_RKeyCode =       KeyCode("Direction_R",       16777312,          'None',          0x01000060)
	SpaceKeyCode =             KeyCode("Space",             32,                'Space',         0x00000020)
	ExclamKeyCode =            KeyCode("Exclam",            33,                '!',             0x00000021)
	QuoteDblKeyCode =          KeyCode("QuoteDbl",          34,                '"',             0x00000022)
	NumberSignKeyCode =        KeyCode("Number Sign",       35,                '#',             0x00000023)
	DollarKeyCode =            KeyCode("Dollar",            36,                '$',             0x00000024)
	PercentKeyCode =           KeyCode("Percent",           37,                '%',             0x00000025)
	AmpersandKeyCode =         KeyCode("Ampersand",         38,                '&',             0x00000026)
	ApostropheKeyCode =        KeyCode("Apostrophe",        39,                "'",             0x00000027)
	ParenLeftKeyCode =         KeyCode("ParenLeft",         40,                '(',             0x00000028)
	ParenRightKeyCode =        KeyCode("ParenRight",        41,                ')',             0x00000029)
	AsteriskKeyCode =          KeyCode("Asterisk",          42,                '*',             0x0000002a)
	PlusKeyCode =              KeyCode("Plus",              43,                '+',             0x0000002b)
	CommaKeyCode =             KeyCode("Comma",             44,                ',',             0x0000002c)
	MinusKeyCode =             KeyCode("Minus",             45,                '-',             0x0000002d)
	PeriodKeyCode =            KeyCode("Period",            46,                '.',             0x0000002e)
	SlashKeyCode =             KeyCode("Slash",             47,                '/',             0x0000002f)
	NoKeyKeyCode =             KeyCode("NoKey",             0,                 'None',          0x00000000)
	LeftButtonKeyCode =        KeyCode("LeftButton",        1,                 'LMB',           0x00000001)
	RightButtonKeyCode =       KeyCode("RightButton",       2,                 'RMB',           0x00000002)
	MiddleButtonKeyCode =      KeyCode("MiddleButton",      4,                 'MMB',           0x00000004)
	D0KeyCode =                KeyCode("0",                 48,                "0",             0x00000030)
	D1KeyCode =                KeyCode("1",                 49,                "1",             0x00000031)
	D2KeyCode =                KeyCode("2",                 50,                "2",             0x00000032)
	D3KeyCode =                KeyCode("3",                 51,                "3",             0x00000033)
	D4KeyCode =                KeyCode("4",                 52,                "4",             0x00000034)
	D5KeyCode =                KeyCode("5",                 53,                "5",             0x00000035)
	D6KeyCode =                KeyCode("6",                 54,                "6",             0x00000036)
	D7KeyCode =                KeyCode("7",                 55,                "7",             0x00000037)
	D8KeyCode =                KeyCode("8",                 56,                "8",             0x00000038)
	D9KeyCode =                KeyCode("9",                 57,                "9",             0x00000039)
	ColonKeyCode =             KeyCode("Colon",             58,                ':',             0x0000003a)
	SemicolonKeyCode =         KeyCode("Semicolon",         59,                ';',             0x0000003b)
	LessKeyCode =              KeyCode("Less",              60,                '<',             0x0000003c)
	EqualKeyCode =             KeyCode("Equal",             61,                '=',             0x0000003d)
	GreaterKeyCode =           KeyCode("Greater",           62,                '>',             0x0000003e)
	QuestionKeyCode =          KeyCode("Question",          63,                '?',             0x0000003f)
	AtKeyCode =                KeyCode("At",                64,                '@',             0x00000040)
	AKeyCode =                 KeyCode("A",                 65,                "A",             0x00000041)
	BKeyCode =                 KeyCode("B",                 66,                "B",             0x00000042)
	CKeyCode =                 KeyCode("C",                 67,                "C",             0x00000043)
	DKeyCode =                 KeyCode("D",                 68,                "D",             0x00000044)
	EKeyCode =                 KeyCode("E",                 69,                "E",             0x00000045)
	FKeyCode =                 KeyCode("F",                 70,                "F",             0x00000046)
	GKeyCode =                 KeyCode("G",                 71,                "G",             0x00000047)
	HKeyCode =                 KeyCode("H",                 72,                "H",             0x00000048)
	IKeyCode =                 KeyCode("I",                 73,                "I",             0x00000049)
	JKeyCode =                 KeyCode("J",                 74,                "J",             0x0000004a)
	KKeyCode =                 KeyCode("K",                 75,                "K",             0x0000004b)
	LKeyCode =                 KeyCode("L",                 76,                "L",             0x0000004c)
	MKeyCode =                 KeyCode("M",                 77,                "M",             0x0000004d)
	NKeyCode =                 KeyCode("N",                 78,                "N",             0x0000004e)
	OKeyCode =                 KeyCode("O",                 79,                "O",             0x0000004f)
	PKeyCode =                 KeyCode("P",                 80,                "P",             0x00000050)
	QKeyCode =                 KeyCode("Q",                 81,                "Q",             0x00000051)
	RKeyCode =                 KeyCode("R",                 82,                "R",             0x00000052)
	SKeyCode =                 KeyCode("S",                 83,                "S",             0x00000053)
	TKeyCode =                 KeyCode("T",                 84,                "T",             0x00000054)
	UKeyCode =                 KeyCode("U",                 85,                "U",             0x00000055)
	VKeyCode =                 KeyCode("V",                 86,                "V",             0x00000056)
	WKeyCode =                 KeyCode("W",                 87,                "W",             0x00000057)
	XKeyCode =                 KeyCode("X",                 88,                "X",             0x00000058)
	YKeyCode =                 KeyCode("Y",                 89,                "Y",             0x00000059)
	ZKeyCode =                 KeyCode("Z",                 90,                "Z",             0x0000005a)
	BracketLeftKeyCode =       KeyCode("BracketLeft",       91,                '[',             0x0000005b)
	BackslashKeyCode =         KeyCode("Backslash",         92,                '\\',            0x0000005c)
	BracketRightKeyCode =      KeyCode("BracketRight",      93,                ']',             0x0000005d)
	AsciiCircumKeyCode =       KeyCode("AsciiCircum",       94,                '^',             0x0000005e)
	UnderscoreKeyCode =        KeyCode("Underscore",        95,                '_',             0x0000005f)
	QuoteLeftKeyCode =         KeyCode("QuoteLeft",         96,                '`',             0x00000060) #The Grave
	BraceLeftKeyCode =         KeyCode("BraceLeft",         123,               '{',             0x0000007b)
	BarKeyCode =               KeyCode("Bar",               124,               '|',             0x0000007c)
	BraceRightKeyCode =        KeyCode("BraceRight",        125,               '}',             0x0000007d)
	AsciiTildeKeyCode =        KeyCode("AsciiTilde",        126,               '~',             0x0000007e)


class KeyboardModifiers:
	NoKeyboardModifier =       KeyModifier("None",          0,                 'None',          0x00000000)
	CtrlKeyboardModifier =     KeyModifier("Control",       67108864,          'Ctrl',          0x04000000)
	AltKeyboardModifier =      KeyModifier("Alt",           134217728,         'Alt',           0x08000000)
	MetaKeyboardModifier =     KeyModifier("Meta",          268435456,         'Meta',          0x10000000)
	ShiftKeyboardModifier =    KeyModifier("Shift",         33554432,          'Shift',         0x40000000)



# print(valueToKeyMap)

# KeyCodes = {
#   	{"EscapeKeyCode",                  "Escape",                 16777216,              'Esc',           0x01000000},
#   	{"TabKeyCode",                     "Tab",                    16777217,              'Tab',           0x01000001},
#   	{"BacktabKeyCode",                 "Backtab",                16777218,              'BkTab',         0x01000002},
#   	{"BackspaceKeyCode",               "Backspace",              16777219,              'Bksp',          0x01000003},
#   	{"ReturnKeyCode",                  "Return",                 16777220,              'Return',        0x01000004},
#   	{"EnterKeyCode",                   "Enter",                  16777221,              'Enter',         0x01000005},
#   	{"InsertKeyCode",                  "Insert",                 16777222,              'Ins',           0x01000006},
#   	{"DeleteKeyCode",                  "Delete",                 16777223,              'Del',           0x01000007},
#   	{"PauseKeyCode",                   "Pause",                  16777224,              'Pause',         0x01000008},
#   	{"PrintKeyCode",                   "Print",                  16777225,              'Print',         0x01000009},
#   	{"SysReqKeyCode",                  "SysReq",                 16777226,              'SysReq',        0x0100000a},
#   	{"ClearKeyCode",                   "Clear",                  16777227,              'Clear',         0x0100000b},
#   	{"HomeKeyCode",                    "Home",                   16777232,              'Home',          0x01000010},
#   	{"EndKeyCode",                     "End",                    16777233,              'End',           0x01000011},
#   	{"LeftKeyCode",                    "Left",                   16777234,              'Left',          0x01000012},
#   	{"UpKeyCode",                      "Up",                     16777235,              'Up',            0x01000013},
#   	{"RightKeyCode",                   "Right",                  16777236,              'Right',         0x01000014},
#   	{"DownKeyCode",                    "Down",                   16777237,              'Down',          0x01000015},
#   	{"PageUpKeyCode",                  "PageUp",                 16777238,              'PgDn',          0x01000016},
#   	{"PageDownKeyCode",                "PageDown",               16777239,              'PgUp',          0x01000017},
#   	{"ShiftKeyCode",                   "Shift",                  16777248,              'Shift',         0x01000020},
#   	{"ControlKeyCode",                 "Control",                16777249,              'Ctrl',          0x01000021},
#   	{"MetaKeyCode",                    "Meta",                   16777250,              'Meta',          0x01000022},
#   	{"AltKeyCode",                     "Alt",                    16777251,              'Alt',           0x01000023},
#   	{"CapsLockKeyCode",                "CapsLock",               16777252,              'CapsLk',        0x01000024},
#   	{"NumLockKeyCode",                 "NumLock",                16777253,              'NumLk',         0x01000025},
#   	{"ScrollLockKeyCode",              "ScrollLock",             16777254,              'ScrLk',         0x01000026},
#   	{"F1KeyCode",                      "F1",                     16777264,              "F1",            0x01000030},
#   	{"F2KeyCode",                      "F2",                     16777265,              "F2",            0x01000031},
#   	{"F3KeyCode",                      "F3",                     16777266,              "F3",            0x01000032},
#   	{"F4KeyCode",                      "F4",                     16777267,              "F4",            0x01000033},
#   	{"F5KeyCode",                      "F5",                     16777268,              "F5",            0x01000034},
#   	{"F6KeyCode",                      "F6",                     16777269,              "F6",            0x01000035},
#   	{"F7KeyCode",                      "F7",                     16777270,              "F7",            0x01000036},
#   	{"F8KeyCode",                      "F8",                     16777271,              "F8",            0x01000037},
#   	{"F9KeyCode",                      "F9",                     16777272,              "F9",            0x01000038},
#   	{"F10KeyCode",                     "F10",                    16777273,              "F10",           0x01000039},
#   	{"F11KeyCode",                     "F11",                    16777274,              "F11",           0x0100003a},
#   	{"F12KeyCode",                     "F12",                    16777275,              "F12",           0x0100003b},
#   	{"F13KeyCode",                     "F13",                    16777276,              "F13",           0x0100003c},
#   	{"F14KeyCode",                     "F14",                    16777277,              "F14",           0x0100003d},
#   	{"F15KeyCode",                     "F15",                    16777278,              "F15",           0x0100003e},
#   	{"F16KeyCode",                     "F16",                    16777279,              "F16",           0x0100003f},
#   	{"F17KeyCode",                     "F17",                    16777280,              "F17",           0x01000040},
#   	{"F18KeyCode",                     "F18",                    16777281,              "F18",           0x01000041},
#   	{"F19KeyCode",                     "F19",                    16777282,              "F19",           0x01000042},
#   	{"F20KeyCode",                     "F20",                    16777283,              "F20",           0x01000043},
#   	{"F21KeyCode",                     "F21",                    16777284,              "F21",           0x01000044},
#   	{"F22KeyCode",                     "F22",                    16777285,              "F22",           0x01000045},
#   	{"F23KeyCode",                     "F23",                    16777286,              "F23",           0x01000046},
#   	{"F24KeyCode",                     "F24",                    16777287,              "F24",           0x01000047},
#   	{"F25KeyCode",                     "F25",                    16777288,              "F25",           0x01000048},
#   	{"F26KeyCode",                     "F26",                    16777289,              "F26",           0x01000049},
#   	{"F27KeyCode",                     "F27",                    16777290,              "F27",           0x0100004a},
#   	{"F28KeyCode",                     "F28",                    16777291,              "F28",           0x0100004b},
#   	{"F29KeyCode",                     "F29",                    16777292,              "F29",           0x0100004c},
#   	{"F30KeyCode",                     "F30",                    16777293,              "F30",           0x0100004d},
#   	{"F31KeyCode",                     "F31",                    16777294,              "F31",           0x0100004e},
#   	{"F32KeyCode",                     "F32",                    16777295,              "F32",           0x0100004f},
#   	{"F33KeyCode",                     "F33",                    16777296,              "F33",           0x01000050},
#   	{"F34KeyCode",                     "F34",                    16777297,              "F34",           0x01000051},
#   	{"F35KeyCode",                     "F35",                    16777298,              "F35",           0x01000052},
#   	{"Super_LKeyCode",                 "Super_L",                16777299,              'LSuper',        0x01000053},
#   	{"Super_RKeyCode",                 "Super_R",                16777300,              'RSuper',        0x01000054},
#   	{"MenuKeyCode",                    "Menu",                   16777301,              'Menu',          0x01000055},
#   	{"Hyper_LKeyCode",                 "Hyper_L",                16777302,              'LHyper',        0x01000056},
#   	{"Hyper_RKeyCode",                 "Hyper_R",                16777303,              'RHyper',        0x01000057},
#   	{"HelpKeyCode",                    "Help",                   16777304,              'Help',          0x01000058},
#   	{"Direction_LKeyCode",             "Direction_L",            16777305,              'None',          0x01000059},
#   	{"Direction_RKeyCode",             "Direction_R",            16777312,              'None',          0x01000060},
#   	{"SpaceKeyCode",                   "Space",                  32,                    'Space',         0x20      },
#   	{"ExclamKeyCode",                  "Exclam",                 33,                    '!',             0x21      },
#   	{"QuoteDblKeyCode",                "QuoteDbl",               34,                    '"',             0x22      },
#   	{"NumberSignKeyCode",              "NumberSign",             35,                    ' ',             0x23      },
#   	{"DollarKeyCode",                  "Dollar",                 36,                    '$',             0x24      },
#   	{"PercentKeyCode",                 "Percent",                37,                    '%',             0x25      },
#   	{"AmpersandKeyCode",               "Ampersand",              38,                    '&',             0x26      },
#   	{"ApostropheKeyCode",              "Apostrophe",             39,                    "'",             0x27      },
#   	{"ParenLeftKeyCode",               "ParenLeft",              40,                    '(',             0x28      },
#   	{"ParenRightKeyCode",              "ParenRight",             41,                    ')',             0x29      },
#   	{"AsteriskKeyCode",                "Asterisk",               42,                    '*',             0x2a      },
#   	{"PlusKeyCode",                    "Plus",                   43,                    '+',             0x2b      },
#   	{"CommaKeyCode",                   "Comma",                  44,                    ',',             0x2c      },
#   	{"MinusKeyCode",                   "Minus",                  45,                    '-',             0x2d      },
#   	{"PeriodKeyCode",                  "Period",                 46,                    '.',             0x2e      },
#   	{"SlashKeyCode",                   "Slash",                  47,                    '/',             0x2f      },
#   	{"NoKeyKeyCode",                   "NoKey",                  0,                     'None',          0x00      },
# 	    {"LeftButtonKeyCode",              "LeftButton",             1,                     'LMB',           0x00000001},
#       {"RightButtonKeyCode",             "RightButton",            2,                     'RMB',           0x00000002},
# 	    {"MiddleButtonKeyCode",            "MiddleButton",           4,                     'MMB',           0x00000004},
#   	{"D0KeyCode",                      "0",                      48,                    "0",             0x30      },
#   	{"D1KeyCode",                      "1",                      49,                    "1",             0x31      },
#   	{"D2KeyCode",                      "2",                      50,                    "2",             0x32      },
#   	{"D3KeyCode",                      "3",                      51,                    "3",             0x33      },
#   	{"D4KeyCode",                      "4",                      52,                    "4",             0x34      },
#   	{"D5KeyCode",                      "5",                      53,                    "5",             0x35      },
#   	{"D6KeyCode",                      "6",                      54,                    "6",             0x36      },
#   	{"D7KeyCode",                      "7",                      55,                    "7",             0x37      },
#   	{"D8KeyCode",                      "8",                      56,                    "8",             0x38      },
#   	{"D9KeyCode",                      "9",                      57,                    "9",             0x39      },
#   	{"ColonKeyCode",                   "Colon",                  58,                    ':',             0x3a      },
#   	{"SemicolonKeyCode",               "Semicolon",              59,                    ';',             0x3b      },
#   	{"LessKeyCode",                    "Less",                   60,                    '<',             0x3c      },
#   	{"EqualKeyCode",                   "Equal",                  61,                    '=',             0x3d      },
#   	{"GreaterKeyCode",                 "Greater",                62,                    '>',             0x3e      },
#   	{"QuestionKeyCode",                "Question",               63,                    '?',             0x3f      },
#   	{"AtKeyCode",                      "At",                     64,                    '@',             0x40      },
#   	{"AKeyCode",                       "A",                      65,                    "A",             0x41      },
#   	{"BKeyCode",                       "B",                      66,                    "B",             0x42      },
#   	{"CKeyCode",                       "C",                      67,                    "C",             0x43      },
#   	{"DKeyCode",                       "D",                      68,                    "D",             0x44      },
#   	{"EKeyCode",                       "E",                      69,                    "E",             0x45      },
#   	{"FKeyCode",                       "F",                      70,                    "F",             0x46      },
#   	{"GKeyCode",                       "G",                      71,                    "G",             0x47      },
#   	{"HKeyCode",                       "H",                      72,                    "H",             0x48      },
#   	{"IKeyCode",                       "I",                      73,                    "I",             0x49      },
#   	{"JKeyCode",                       "J",                      74,                    "J",             0x4a      },
#   	{"KKeyCode",                       "K",                      75,                    "K",             0x4b      },
#   	{"LKeyCode",                       "L",                      76,                    "L",             0x4c      },
#   	{"MKeyCode",                       "M",                      77,                    "M",             0x4d      },
#   	{"NKeyCode",                       "N",                      78,                    "N",             0x4e      },
#   	{"OKeyCode",                       "O",                      79,                    "O",             0x4f      },
#   	{"PKeyCode",                       "P",                      80,                    "P",             0x50      },
#   	{"QKeyCode",                       "Q",                      81,                    "Q",             0x51      },
#   	{"RKeyCode",                       "R",                      82,                    "R",             0x52      },
#   	{"SKeyCode",                       "S",                      83,                    "S",             0x53      },
#   	{"TKeyCode",                       "T",                      84,                    "T",             0x54      },
#   	{"UKeyCode",                       "U",                      85,                    "U",             0x55      },
#   	{"VKeyCode",                       "V",                      86,                    "V",             0x56      },
#   	{"WKeyCode",                       "W",                      87,                    "W",             0x57      },
#   	{"XKeyCode",                       "X",                      88,                    "X",             0x58      },
#   	{"YKeyCode",                       "Y",                      89,                    "Y",             0x59      },
#   	{"ZKeyCode",                       "Z",                      90,                    "Z",             0x5a      },
#   	{"BracketLeftKeyCode",             "BracketLeft",            91,                    '[',             0x5b      },
#   	{"BackslashKeyCode",               "Backslash",              92,                    '\\',            0x5c      },
#   	{"BracketRightKeyCode",            "BracketRight",           93,                    ']',             0x5d      },
#   	{"AsciiCircumKeyCode",             "AsciiCircum",            94,                    '^',             0x5e      },
#   	{"UnderscoreKeyCode",              "Underscore",             95,                    '_',             0x5f      },
#   	{"QuoteLeftKeyCode",               "QuoteLeft",              96,                    '`',             0x60      },
#   	{"BraceLeftKeyCode",               "BraceLeft",              123,                   '{',             0x7b      },
#   	{"BarKeyCode",                     "Bar",                    124,                   '|',             0x7c      },
#   	{"BraceRightKeyCode",              "BraceRight",             125,                   '}',             0x7d      },
#   	{"AsciiTildeKeyCode",              "AsciiTilde",             126,                   '~',             0x7e      }
# }

# KeyboardModifiers={	
#   	{"NoKeyboardModifier",             "None",                   0,                     0x00000000},
#   	{"CtrlKeyboardModifier",           "Control",                67108864,              0x04000000},
#   	{"AltKeyboardModifier",            "Alt",                    134217728,             0x08000000},
#   	{"MetaKeyboardModifier",           "Meta",                   268435456,             0x10000000},
#   	{"ShiftKeyboardModifier",          "Shift",                  33554432,              0x40000000}
# }


# Note: On Mac OS X, the ControlModifier value corresponds to the Command keys on the Macintosh keyboard, 
# and the MetaModifier value corresponds to the Control keys. The KeypadModifier value will also be set when an arrow 
# key is pressed as the arrow keys are considered part of the keypad.

# Note: On Windows Keyboards, MetaModifier and Key_Meta are mapped to the Windows key.

