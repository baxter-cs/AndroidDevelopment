#!python2

print "Python Morse encoder/decoder (BETA)"

#DICTIONARIES
eng_to_morse_dict = {
'A':'.-',     'B':'-...',   'C':'-.-.', 
'D':'-..',    'E':'.',      'F':'..-.',
'G':'--.',    'H':'....',   'I':'..',
'J':'.---',   'K':'-.-',    'L':'.-..',
'M':'--',     'N':'-.',     'O':'---',
'P':'.--.',   'Q':'--.-',   'R':'.-.',
'S':'...',    'T':'-',      'U':'..-',
'V':'...-',   'W':'.--',    'X':'-..-',
'Y':'-.--',   'Z':'--..',

'0':'-----',  '1':'.----',  '2':'..---',
'3':'...--',  '4':'....-',  '5':'.....',
'6':'-....',  '7':'--...',  '8':'---..',
'9':'----.',

'.':'.-.-.-'
}

morse_to_eng_dict = {
'.-':'A', '-...':'B', '-.-.':'C',
'-..':'D', '.':'E', '..-.':'F',
'--.':'G', '....':'H', '..':'I',
'.---':'J','-.-':'K','.-..':'L',
'--':'M','-.':'N','---':'O',
'.--.':'P','--.-':'Q','.-.':'R',
'...':'S','-':'T','..-':'U',
'...-':'V','.--':'W','-..-':'X',
'-.--':'Y','--..':'Z',

#TO-DO: FILL THIS IN
#'':'','':'','':'',
#'':'','':'','':'',
#'':'','':'','':'',
#'':''

#PUNCTUATION
'.-.-.-':'.', '--..--':',', '..--..':'?',
'.----.':"'", '-.-.--':'!',

#PROSIGN
'-.-.-':'STARTING SIGNAL',
'.-...':'WAIT',
'...-.':'UNDERSTOOD',
'........':'ERROR'
}

#INPUT ENGLISH
def eng_to_morse():
    msg = raw_input('English: ')
    for char in msg:
        if char != " ":
            print eng_to_morse_dict[char.upper()],
        else:
            print "/"
            
#INPUT MORSE
def morse_to_eng():
    print "FORMAT: '.- .- /.- /'"
    msg = raw_input('Morse: ')
    # msg = ".- .- /.- .- /"
    letterbuffer = []
    wordbuffer = []
    sentencebuffer = []
    for char in msg:
        if char == "/":
            wordbuffer = "".join(wordbuffer)
            sentencebuffer.append(wordbuffer)
            sentencebuffer.append(" ")
            wordbuffer = []
        elif char == " ":
            letterbuffer = "".join(letterbuffer)
            letterbuffer = morse_to_eng_dict[letterbuffer]
            wordbuffer.append(letterbuffer)
            letterbuffer = []
        elif char == "." or char == "-":
            letterbuffer.append(char)
    print "".join(sentencebuffer)

#USER
def prompt_user():
    print "Translate Morse to English (1)"
    print "Translate English to Morse (2)"
    choice = raw_input("Choose: ")
    if choice == "1":
        morse_to_eng()
    elif choice == "2":
        eng_to_morse()
    else:
        print "Please enter a valid number"
        prompt_user()
        
prompt_user()
    