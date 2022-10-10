import sys


def readLines(txt):
    lines = []
    text = ""
    for i in txt:
        if i == "\n":
            lines.append(text)
            text = ""
        else:
            text += i
    lines.append(text)
    return lines

def read(line):
    txt = ""
    string = False
    tokens = []
    for i in line:
        if i == " " and not string and txt != "" and not "\t" in txt:
            tokens.append(txt)
            txt = ""
        else:
            if i == '"':
                string = not string
            txt += i
    tokens.append(txt)
    return tokens

class interpreter:
    def __init__(self) -> None:
        self.customcmds = {}
        pass
    def createCustom(self,func,name):
        self.customcmds[name] = func
    def run(self,code,otf={}):
        chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        numbs = "1234567890"
        vars = {}
        lineN = 0
        openBrackets = 0
        funcs = {}
        def convertVars(tokens,vars):
            for i in tokens:
                if i in vars:
                    tokens[i] = vars[i]
        def _parseString(txt):
            qAm = 0
            ret = ""
            for i in txt:
                if i == '"':
                    qAm += 1
                else:
                    ret += i
                if qAm == 2:
                    break
            return ret
        def _print(item):
            if item in vars:
                print(vars[item])
            elif item[0] == '"':
                print(_parseString(item))
        def _createVar(name,value):
            if name in vars:
                print("ERROR: variable already exists")
                return
            if value in vars:
                vars[name] = vars[value]
            elif value[0] == '"':
                vars[name] = _parseString(value)
            elif value.isnumeric():
                vars[name] = int(value)
            else:
                print("ERROR: unknown identifier: " + value)
        def _editVar(name,asignment,value):
            if asignment == "=":
                if value in vars:
                    vars[name] = vars[value]
                elif value[0] == '"':
                    vars[name] = value
                if value.isnumeric():
                    vars[name] = int(value)
                else:
                    print("ERROR: unknown identifier: " + value)
            elif asignment == "+=":
                if vars[name][0] == '"' and value[0] == '"':
                    vars[name] = '"' + _parseString(vars[name]) + _parseString(value) + '"'
                if value in vars:
                    vars[name] += vars[value]
                elif value.isnumeric():
                    vars[name] += int(value)
                else:
                    print("ERROR: unknown identifier: " + value)
            elif asignment == "-=":
                if value[0] == '"' or vars[name] == '"':
                    print("ERROR: cannot use string in math")
                if value in vars:
                    vars[name] -= vars[value]
                elif value.isnumeric():
                    vars[name] -= int(value)
                else:
                    print("ERROR: unknown identifier: " + value)
            elif asignment == "*=":
                if value[0] == '"' or vars[name] == '"':
                    print("ERROR: cannot use string in math")
                if value in vars:
                    vars[name] *= vars[value]
                elif value.isnumeric():
                    vars[name] *= int(value)
                else:
                    print("ERROR: unknown identifier: " + value)
            elif asignment == "/=":
                if value[0] == '"' or vars[name] == '"':
                    print("ERROR: cannot use string in math")
                if value in vars:
                    vars[name] /= vars[value]
                elif value.isnumeric():
                    vars[name] /= int(value)
                else:
                    print("ERROR: unknown identifier: " + value)
            elif asignment == "^=":
                if value[0] == '"' or vars[name] == '"':
                    print("ERROR: cannot use string in math")
                if value in vars:
                    vars[name] = pow(vars[name],vars[value])
                elif value.isnumeric():
                    vars[name] = pow(vars[name],int(value))
                else:
                    print("ERROR: unknown identifier: " + value)
        lines = readLines(code)
        while lineN < len(lines):
            line = lines[lineN]
            tokens = read(line)
            if openBrackets < 1:
                if tokens[0] == "print":
                    _print(tokens[1])
                elif tokens[0] == "var":
                    _createVar(tokens[1],tokens[3])
                elif tokens[0] in vars:
                    _editVar(tokens[0],tokens[1],tokens[2])
                elif tokens[0] == "jump":
                    lineN = int(tokens[1])-2
                elif tokens[0] in self.customcmds:
                    i = 1
                    cmds = []
                    for a in range(len(tokens)-1):
                        cmds.append(tokens[i])
                    self.customcmds[tokens[0]](cmds)
                elif tokens[0] == "if":
                    convertVars(tokens,vars)
                    if tokens[2] == "==":
                        if tokens[1] == tokens[3]:
                            openBrackets -= 1
                    elif tokens[2] == ">":
                        if tokens[1] > tokens[3]:
                            openBrackets -= 1
                    elif tokens[2] == "<":
                        if tokens[1] < tokens[3]:
                            openBrackets -= 1
                    elif tokens[2] == ">=":
                        if tokens[1] >= tokens[3]:
                            openBrackets -= 1
                    elif tokens[2] == "<=":
                        if tokens[1] <= tokens[3]:
                            openBrackets -= 1
                elif tokens[0] == "#" or tokens[0] == "{" or tokens[0] == "}" or tokens[0] == " " or tokens[0] == "\t" or tokens[0] == "":
                    pass
                elif tokens[0] == "def":
                    flines = []
                    ofb = 0
                    for i in range(len(lines)):
                        if i >= lineN:
                            tks = read(lines[i])
                            if "{" in tks:
                                ofb += 1
                            if "}" in tks:
                                ofb -= 1
                            if ofb < 1:
                                break
                            if i > lineN:
                                flines.append(lines[i])
                    funcs[tokens[1]] = flines
                elif tokens[0] in funcs:
                    preln = lineN
                    ctxt = ""
                    for i in funcs[tokens[0]]:
                        for a in i:
                            ctxt += a
                        ctxt += "\n"
                    ctxt.strip("\n")
                    self.run(ctxt,funcs)
                    lineN = preln
                elif tokens[0] in otf:
                    preln = lineN
                    ctxt = ""
                    for i in otf[tokens[0]]:
                        for a in i:
                            ctxt += a
                        ctxt += "\n"
                    ctxt.strip("\n")
                    self.run(ctxt,funcs)
                    lineN = preln
                else:
                    print(f"ERROR: unknown command: {tokens[0]} {lineN}")
            lineN += 1
            if "{" in tokens:
                openBrackets += 1
            if "}" in tokens:
                openBrackets -= 1
        

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    content = f.read()
    f.close()
    interpret = interpreter()
    def hellow(cmds):
        print("hi")
    interpret.createCustom(hellow,"hello")
    interpret.run(content)
