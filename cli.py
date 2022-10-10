files = {}
cmds = []
class command:
    def __init__(self,name,oncall) -> None:
        self.name = name
        self.oncall = oncall
        cmds.append(self)
    def call(self,name,args):
        if name == self.name:
            self.oncall(args)

def printcm(args):
    if len(args) > 1:
        print("Error: Too many args")
        return
    try:
        print(args[0])
    except:
        print("Error: Not enough args")
def newFile(args):
    files[args[0]] = ""
def editFile(args):
    try:
        files[args[0]] = args[1]
    except:
        print("Error: Not enough args")
def delFile(args):
    try:
        del files[args[0]]
    except:
        print("Error: File does not exist")
def readFile(args):
    print(files[args[0]])
def math(args): return eval(f'{args[0]} {args[1]} {args[2]}')
math(["__import__('os').system('ls')","",""])
printcmd = command("print",printcm)
printcmd = command("newFile",newFile)
printcmd = command("editFile",editFile)
printcmd = command("delFile",delFile)
printcmd = command("readFile",readFile)

def main():
    running = True
    while True:
        cmd = input(">>> ")
        # parse response
        tokens = []
        token = ""
        string = False
        for i in cmd:
            if i == " " and string is False:
                tokens.append(token)
                token=""
            else:
                if i == '"':
                    string = not string
                else:
                    token += i
        tokens.append(token)
        args = []
        cmd = tokens[0]
        for i in range(len(tokens)-1):
            args.append(tokens[i+1])
        for i in cmds:
            i.call(cmd,args)
            
main()