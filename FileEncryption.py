infile = open('info_security.txt', 'r')

infile_data = infile.read()

word_total = infile_data.strip()

outfile = open('encrypted.txt', 'w')

encryption_list = {'A':'34', 'a': '!', 
'B': '@', 'b':'#', 
'C':'$', 'c':'%', 
'D':'^', 'd':'&', 
'E':'&', 'e':'*', 
'F':'(', 'f':')', 
'G':'-', 'g':'=', 
'H':'+', 'h':'~', 
'I':'`', 'i':'<', 
'J':'>', 'j':',', 
'K':'.', 'k':'?', 
'L':'/', 'l':'45', 
'M':'1', 'm':'2', 
'N':'3', 'n':'4', 
'O':'5', 'o':'6', 
'P':'7', 'p':'8', 
'Q':'9', 'q':'10', 
'R':'11', 'r':'12', 
'S':'13', 's':'14', 
'T':'15', 't':'16', 
'U':'17', 'u':'18', 
'V':'19', 'v':'20', 
'W':'21', 'w':'22', 
'X':'23', 'x':'24', 
'Y':'25', 'y':'26', 
'Z':'27', 'z':'28'}

message = ""

for letter in word_total:

    if letter in encryption_list:
        message = message + encryption_list[letter]
    else:
        message = message + letter

outfile.write(str(message))