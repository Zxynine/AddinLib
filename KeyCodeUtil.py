


from adsk.core import KeyCodes


valueToKeyMap:'dict[int,KeyCode]' = {}
nameToKeyMap:'dict[str,KeyCode]' = {}

class KeyCode:
	def __init__(self, name:str, value:int, hex:hex):
		self.id = value
		self.name = name
		self.hex = hex
		nameToKeyMap[name.lower()] = self
		valueToKeyMap[value] = self

class AllKeyCodes:
	EscapeKeyCode =                  KeyCode("Escape",                 16777216,              0x01000000)
	TabKeyCode =                     KeyCode("Tab",                    16777217,              0x01000001)
	BacktabKeyCode =                 KeyCode("Backtab",                16777218,              0x01000002)
	BackspaceKeyCode =               KeyCode("Backspace",              16777219,              0x01000003)
	ReturnKeyCode =                  KeyCode("Return",                 16777220,              0x01000004)
	EnterKeyCode =                   KeyCode("Enter",                  16777221,              0x01000005)
	InsertKeyCode =                  KeyCode("Insert",                 16777222,              0x01000006)
	DeleteKeyCode =                  KeyCode("Delete",                 16777223,              0x01000007)
	PauseKeyCode =                   KeyCode("Pause",                  16777224,              0x01000008)
	PrintKeyCode =                   KeyCode("Print",                  16777225,              0x01000009)
	SysReqKeyCode =                  KeyCode("SysReq",                 16777226,              0x0100000a)
	ClearKeyCode =                   KeyCode("Clear",                  16777227,              0x0100000b)
	HomeKeyCode =                    KeyCode("Home",                   16777232,              0x01000010)
	EndKeyCode =                     KeyCode("End",                    16777233,              0x01000011)
	LeftKeyCode =                    KeyCode("Left",                   16777234,              0x01000012)
	UpKeyCode =                      KeyCode("Up",                     16777235,              0x01000013)
	RightKeyCode =                   KeyCode("Right",                  16777236,              0x01000014)
	DownKeyCode =                    KeyCode("Down",                   16777237,              0x01000015)
	PageUpKeyCode =                  KeyCode("PageUp",                 16777238,              0x01000016)
	PageDownKeyCode =                KeyCode("PageDown",               16777239,              0x01000017)
	ShiftKeyCode =                   KeyCode("Shift",                  16777248,              0x01000020)
	ControlKeyCode =                 KeyCode("Control",                16777249,              0x01000021)
	MetaKeyCode =                    KeyCode("Meta",                   16777250,              0x01000022)
	AltKeyCode =                     KeyCode("Alt",                    16777251,              0x01000023)
	CapsLockKeyCode =                KeyCode("CapsLock",               16777252,              0x01000024)
	NumLockKeyCode =                 KeyCode("NumLock",                16777253,              0x01000025)
	ScrollLockKeyCode =              KeyCode("ScrollLock",             16777254,              0x01000026)
	F1KeyCode =                      KeyCode("F1",                     16777264,              0x01000030)
	F2KeyCode =                      KeyCode("F2",                     16777265,              0x01000031)
	F3KeyCode =                      KeyCode("F3",                     16777266,              0x01000032)
	F4KeyCode =                      KeyCode("F4",                     16777267,              0x01000033)
	F5KeyCode =                      KeyCode("F5",                     16777268,              0x01000034)
	F6KeyCode =                      KeyCode("F6",                     16777269,              0x01000035)
	F7KeyCode =                      KeyCode("F7",                     16777270,              0x01000036)
	F8KeyCode =                      KeyCode("F8",                     16777271,              0x01000037)
	F9KeyCode =                      KeyCode("F9",                     16777272,              0x01000038)
	F10KeyCode =                     KeyCode("F10",                    16777273,              0x01000039)
	F11KeyCode =                     KeyCode("F11",                    16777274,              0x0100003a)
	F12KeyCode =                     KeyCode("F12",                    16777275,              0x0100003b)
	F13KeyCode =                     KeyCode("F13",                    16777276,              0x0100003c)
	F14KeyCode =                     KeyCode("F14",                    16777277,              0x0100003d)
	F15KeyCode =                     KeyCode("F15",                    16777278,              0x0100003e)
	F16KeyCode =                     KeyCode("F16",                    16777279,              0x0100003f)
	F17KeyCode =                     KeyCode("F17",                    16777280,              0x01000040)
	F18KeyCode =                     KeyCode("F18",                    16777281,              0x01000041)
	F19KeyCode =                     KeyCode("F19",                    16777282,              0x01000042)
	F20KeyCode =                     KeyCode("F20",                    16777283,              0x01000043)
	F21KeyCode =                     KeyCode("F21",                    16777284,              0x01000044)
	F22KeyCode =                     KeyCode("F22",                    16777285,              0x01000045)
	F23KeyCode =                     KeyCode("F23",                    16777286,              0x01000046)
	F24KeyCode =                     KeyCode("F24",                    16777287,              0x01000047)
	F25KeyCode =                     KeyCode("F25",                    16777288,              0x01000048)
	F26KeyCode =                     KeyCode("F26",                    16777289,              0x01000049)
	F27KeyCode =                     KeyCode("F27",                    16777290,              0x0100004a)
	F28KeyCode =                     KeyCode("F28",                    16777291,              0x0100004b)
	F29KeyCode =                     KeyCode("F29",                    16777292,              0x0100004c)
	F30KeyCode =                     KeyCode("F30",                    16777293,              0x0100004d)
	F31KeyCode =                     KeyCode("F31",                    16777294,              0x0100004e)
	F32KeyCode =                     KeyCode("F32",                    16777295,              0x0100004f)
	F33KeyCode =                     KeyCode("F33",                    16777296,              0x01000050)
	F34KeyCode =                     KeyCode("F34",                    16777297,              0x01000051)
	F35KeyCode =                     KeyCode("F35",                    16777298,              0x01000052)
	Super_LKeyCode =                 KeyCode("Super_L",                16777299,              0x01000053)
	Super_RKeyCode =                 KeyCode("Super_R",                16777300,              0x01000054)
	MenuKeyCode =                    KeyCode("Menu",                   16777301,              0x01000055)
	Hyper_LKeyCode =                 KeyCode("Hyper_L",                16777302,              0x01000056)
	Hyper_RKeyCode =                 KeyCode("Hyper_R",                16777303,              0x01000057)
	HelpKeyCode =                    KeyCode("Help",                   16777304,              0x01000058)
	Direction_LKeyCode =             KeyCode("Direction_L",            16777305,              0x01000059)
	Direction_RKeyCode =             KeyCode("Direction_R",            16777312,              0x01000060)
	SpaceKeyCode =                   KeyCode("Space",                  32,                    0x20      )
	ExclamKeyCode =                  KeyCode("Exclam",                 33,                    0x21      )
	QuoteDblKeyCode =                KeyCode("QuoteDbl",               34,                    0x22      )
	NumberSignKeyCode =              KeyCode("NumberSign",             35,                    0x23      )
	DollarKeyCode =                  KeyCode("Dollar",                 36,                    0x24      )
	PercentKeyCode =                 KeyCode("Percent",                37,                    0x25      )
	AmpersandKeyCode =               KeyCode("Ampersand",              38,                    0x26      )
	ApostropheKeyCode =              KeyCode("Apostrophe",             39,                    0x27      )
	ParenLeftKeyCode =               KeyCode("ParenLeft",              40,                    0x28      )
	ParenRightKeyCode =              KeyCode("ParenRight",             41,                    0x29      )
	AsteriskKeyCode =                KeyCode("Asterisk",               42,                    0x2a      )
	PlusKeyCode =                    KeyCode("Plus",                   43,                    0x2b      )
	CommaKeyCode =                   KeyCode("Comma",                  44,                    0x2c      )
	MinusKeyCode =                   KeyCode("Minus",                  45,                    0x2d      )
	PeriodKeyCode =                  KeyCode("Period",                 46,                    0x2e      )
	SlashKeyCode =                   KeyCode("Slash",                  47,                    0x2f      )
	NoKeyKeyCode =                   KeyCode("NoKey",                  0,                     0x00      )
	LeftButtonKeyCode =              KeyCode("LeftButton",             1,                     0x01      )
	RightButtonKeyCode =             KeyCode("RightButton",            2,                     0x02      )
	MiddleButtonKeyCode =            KeyCode("MiddleButton",           4,                     0x04      )
	D0KeyCode =                      KeyCode("0",                      48,                    0x30      )
	D1KeyCode =                      KeyCode("1",                      49,                    0x31      )
	D2KeyCode =                      KeyCode("2",                      50,                    0x32      )
	D3KeyCode =                      KeyCode("3",                      51,                    0x33      )
	D4KeyCode =                      KeyCode("4",                      52,                    0x34      )
	D5KeyCode =                      KeyCode("5",                      53,                    0x35      )
	D6KeyCode =                      KeyCode("6",                      54,                    0x36      )
	D7KeyCode =                      KeyCode("7",                      55,                    0x37      )
	D8KeyCode =                      KeyCode("8",                      56,                    0x38      )
	D9KeyCode =                      KeyCode("9",                      57,                    0x39      )
	ColonKeyCode =                   KeyCode("Colon",                  58,                    0x3a      )
	SemicolonKeyCode =               KeyCode("Semicolon",              59,                    0x3b      )
	LessKeyCode =                    KeyCode("Less",                   60,                    0x3c      )
	EqualKeyCode =                   KeyCode("Equal",                  61,                    0x3d      )
	GreaterKeyCode =                 KeyCode("Greater",                62,                    0x3e      )
	QuestionKeyCode =                KeyCode("Question",               63,                    0x3f      )
	AtKeyCode =                      KeyCode("At",                     64,                    0x40      )
	AKeyCode =                       KeyCode("A",                      65,                    0x41      )
	BKeyCode =                       KeyCode("B",                      66,                    0x42      )
	CKeyCode =                       KeyCode("C",                      67,                    0x43      )
	DKeyCode =                       KeyCode("D",                      68,                    0x44      )
	EKeyCode =                       KeyCode("E",                      69,                    0x45      )
	FKeyCode =                       KeyCode("F",                      70,                    0x46      )
	GKeyCode =                       KeyCode("G",                      71,                    0x47      )
	HKeyCode =                       KeyCode("H",                      72,                    0x48      )
	IKeyCode =                       KeyCode("I",                      73,                    0x49      )
	JKeyCode =                       KeyCode("J",                      74,                    0x4a      )
	KKeyCode =                       KeyCode("K",                      75,                    0x4b      )
	LKeyCode =                       KeyCode("L",                      76,                    0x4c      )
	MKeyCode =                       KeyCode("M",                      77,                    0x4d      )
	NKeyCode =                       KeyCode("N",                      78,                    0x4e      )
	OKeyCode =                       KeyCode("O",                      79,                    0x4f      )
	PKeyCode =                       KeyCode("P",                      80,                    0x50      )
	QKeyCode =                       KeyCode("Q",                      81,                    0x51      )
	RKeyCode =                       KeyCode("R",                      82,                    0x52      )
	SKeyCode =                       KeyCode("S",                      83,                    0x53      )
	TKeyCode =                       KeyCode("T",                      84,                    0x54      )
	UKeyCode =                       KeyCode("U",                      85,                    0x55      )
	VKeyCode =                       KeyCode("V",                      86,                    0x56      )
	WKeyCode =                       KeyCode("W",                      87,                    0x57      )
	XKeyCode =                       KeyCode("X",                      88,                    0x58      )
	YKeyCode =                       KeyCode("Y",                      89,                    0x59      )
	ZKeyCode =                       KeyCode("Z",                      90,                    0x5a      )
	BracketLeftKeyCode =             KeyCode("BracketLeft",            91,                    0x5b      )
	BackslashKeyCode =               KeyCode("Backslash",              92,                    0x5c      )
	BracketRightKeyCode =            KeyCode("BracketRight",           93,                    0x5d      )
	AsciiCircumKeyCode =             KeyCode("AsciiCircum",            94,                    0x5e      )
	UnderscoreKeyCode =              KeyCode("Underscore",             95,                    0x5f      )
	QuoteLeftKeyCode =               KeyCode("QuoteLeft",              96,                    0x60      )
	BraceLeftKeyCode =               KeyCode("BraceLeft",              123,                   0x7b      )
	BarKeyCode =                     KeyCode("Bar",                    124,                   0x7c      )
	BraceRightKeyCode =              KeyCode("BraceRight",             125,                   0x7d      )
	AsciiTildeKeyCode =              KeyCode("AsciiTilde",             126,                   0x7e      )


alternateMappings = {
	'!':AllKeyCodes.ExclamKeyCode,
	' ':AllKeyCodes.SpaceKeyCode,
	'/':AllKeyCodes.SlashKeyCode,
	'\\':AllKeyCodes.BackslashKeyCode,
	',':AllKeyCodes.CommaKeyCode,
	'[':AllKeyCodes.BracketLeftKeyCode,
	']':AllKeyCodes.BracketRightKeyCode,
	'{':AllKeyCodes.BraceLeftKeyCode,
	'}':AllKeyCodes.BraceRightKeyCode
}



class KeyboardModifiers:
	NoKeyboardModifier =             KeyCode("None",                   0,                     0x00000000)
	CtrlKeyboardModifier =           KeyCode("Control",                67108864,              0x04000000)
	AltKeyboardModifier =            KeyCode("Alt",                    134217728,             0x08000000)
	MetaKeyboardModifier =           KeyCode("Meta",                   268435456,             0x10000000)
	ShiftKeyboardModifier =          KeyCode("Shift",                  33554432,              0x40000000)

# Note: On Mac OS X, the ControlModifier value corresponds to the Command keys on the Macintosh keyboard, 
# and the MetaModifier value corresponds to the Control keys. The KeypadModifier value will also be set when an arrow 
# key is pressed as the arrow keys are considered part of the keypad.

# Note: On Windows Keyboards, MetaModifier and Key_Meta are mapped to the Windows key.

