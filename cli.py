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
    if len(args) > 1:
        print("Error: Too many args")
        return
    f = open(args[0],"w")
    f.close()
def editFile(args):
    if len(args) > 2:
        print("Error: Too many args")
        return
    f = open(args[0],"w")
    f.write(args[1])
    f.close()
def readFile(args):
    f = open(args[0])
    print(f.read())
    f.close()
printcmd = command("print",printcm)
printcmd = command("newFile",newFile)
printcmd = command("editFile",editFile)
printcmd = command("readFile",readFile)

def main():
    running = True
    while running:
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
        if cmd == "quit()":
            running = False
        for i in range(len(tokens)-1):
            args.append(tokens[i+1])
        for i in cmds:
            i.call(cmd,args)
            
if __name__ == "__main__":
    main()