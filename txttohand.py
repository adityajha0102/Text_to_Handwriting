from PIL import Image
from fpdf import FPDF

img = Image.open(r"C:\Users\Sanjay\Desktop\Projects\txttohandwritting-master\file\\bg.png")
sizeOfSheet = img.width
gap, _ = 0, 0 #changing
allowedchar = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM()[]+%&*{}"<>,|.=-?;1234567890'


def Write(char):
    if char == '\n':
        pass
    else:
        global gap, _
        char.lower()
        cases = Image.open(r"C:\Users\Sanjay\Desktop\Projects\txttohandwritting-master\file\\%s.png" % char)
        img.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases


def Letters(word):
    global gap, _
    if gap > sizeOfSheet - 55 * (len(word)):  #changing initially 95
        gap = 0
        _ += 130

    for letter in word:
        if letter == '\n':
            _ += 40

        if letter in allowedchar:
            if letter.isupper():
                letter = letter.lower()
                letter = letter + 'upper'
            elif letter.islower():
                pass
            elif letter == '.':
                letter = "fullstop"
            elif letter == ',':
                letter = "comma"
            elif letter == '-':
                letter = "hiphen"
            elif letter == ':':
                letter = "colon"
            elif letter == '!':
                letter = "exclamation"
            elif letter == '?':
                letter = "question"
            elif letter == ";":
                letter = "semicolon"
            elif letter == '(':
                letter = "bracketopen"
            elif letter == ')':
                letter = "bracketclose"
            elif letter == '[':
                letter = "squarebracketopen"
            elif letter == ']':
                letter = "squarebracketclose"
            elif letter == '+':
                letter = "plus"
            elif letter == '%':
                letter = "modulus"
            elif letter == '&':
                letter = "ampercent"
            elif letter == '*':
                letter = "into"
            elif letter == '{':
                letter = "curlybracketopen"
            elif letter == '}':
                letter = "curlybracketclose"
            elif letter == '"':
                letter = "doublequotes"
            elif letter == '<':
                letter = "lessthan"
            elif letter == '>':
                letter = "greaterthan"
            elif letter == '=':
                letter = "equalto"
            elif letter == '|':
                letter = "or"

            Write(letter)


def Word(Input):
    wordlist = Input.split(' ')
    for i in wordlist:
        Letters(i)
        Write('space')


if __name__ == '__main__':

    try:
        with open(r"C:\Users\Sanjay\Desktop\Projects\txttohandwritting-master\file\\black.txt", 'r') as file:
            data = file.read()#.replace('\n', '')
            l = len(data)
            nn = len(data) // 1100
            print(nn)
            print(l)
            chunks, chunk_size = len(data), len(data) // nn +1
            p = [data[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

            for i in range(0, len(p)):
                Word(p[i])
                Write('\n')
                img.save(r"C:\Users\Sanjay\Desktop\Projects\txttohandwritting-master\Output_file\\%doutt.png" % i)
                img1 = Image.open(r"C:\Users\Sanjay\Desktop\Projects\txttohandwritting-master\file\\bg.png")
                img = img1
                gap, _ = 0, 0
    except ValueError as E:
        print("{}\nTry again", format(E))
    imageList = []
    for i in range(0, len(p)):
        imageList.append(r"C:\Users\Sanjay\Desktop\Projects\txttohandwritting-master\Output_file\\%doutt.png" % i)

    cover = Image.open(imageList[0])
    width, height = cover.size
    pdf = FPDF(unit="pt", format=[width, height])
    for i in range(0, len(imageList)):
        pdf.add_page()
        pdf.image(imageList[i], 0, 0)
    pdf.output(r"C:\Users\Sanjay\Desktop\Projects\txttohandwritting-master\Output_file\\neww_2.pdf", "F")
