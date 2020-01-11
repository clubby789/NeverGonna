"""
we're no strangers to bar:foo -> new variable 'foo' of type bar
gotta make foo 2 -> foo = 2
your heart's been aching but you're too shy to say 'INPUT' -> returns user input
inside we both know foo == "bar" then -> if foo == "bar":
i just wanna tell you "foo" -> print("foo")
i just wanna tell you foo -> print(foo)
never gonna let you down -> else
never gonna give you up -> endif/endloop
we've know foo for 10 -> for foo in range(10)
a full commitment's what I'm thinking of foo -> while foo
"""

TYPES = ["str","int"]
ERRORS = {
    "BadType":"Type is not defined",
    "OpenQuote": "Mismatched Quotations",
    "UnVar": "Undefined Variable"
}
TOKENS = {
    "i just wanna tell you " : "ijwty ",
    "we're no strangers to " : "wnst ",
    "gotta make " : "gm "
}
class ngVar:
    def __init__(self, type, name):
        self.name = name
        self.type = type
        if self.type == "str":
            self.contents = ""
        if self.type == "int":
            self.contents = 0
    def __str__(self):
        return str(self.contents)

class ngInterpreter:
    def __init__(self, liveMode=True):
        self.objects = {}
        self.liveMode = liveMode

    def exception(self, error):
        longError = ERRORS[error]
        print("[X] ERROR: {} - {}".format(error, longError))
        if not self.liveMode:
            exit()

    def print(self, operands, strings):
        operands = operands.split(" ")
        outstr = ''
        for symbol in operands:
            if symbol[:3] == "STR":
                outstr += strings[int(symbol[3:])] + " "
            elif self.checkVariableExists(symbol):
                outstr += self.objects[symbol].contents + " "
            else:
                self.exception("UnVar")
        print(outstr )


    def checkVariableExists(self, variable):
        try:
            self.objects[variable]
            return True
        except KeyError:
            return False

    def declareVariable(self, type, name):
        if type not in TYPES:
            self.exception("BadType")
            return -1
        variable = ngVar(type,name)
        self.objects[name] = variable
    
    def assignVariable(self, variable, contents, strings):
        if not self.checkVariableExists(variable):
            self.exception("UnVar")
            return -1
        for symbol in contents.split(" "):
            if symbol[:3] == "STR":
                # print("Replacing {} with {}".format(symbol, strings[int(symbol[3:])]))
                contents = contents.replace(symbol, strings[int(symbol[3:])])
            elif self.checkVariableExists(symbol):
                contents = contents.replace(symbol, self.objects[symbol].contents)
                # print("REPLACING " + symbol + " with " + self.objects[symbol].contents )
        self.objects[variable].contents = contents

    def doReplacements(self, line):
        for command,token in TOKENS.items():
            line = line.replace(command, token)
        return line

    def findStrings(self, line):
        strings = []
        pos = 0
        while pos < len(line):
            if line[pos] == '"':
                startPos = pos+1
                endPos = line.find('"', startPos+1)
                if endPos == -1:
                    self.exception("OpenQuote")
                    return -1
                string = line[startPos:endPos]
                strings.append(string)
                pos = endPos
            pos += 1
        return strings

    def parseCommand(self, command, operands, strings):
        if command == "wnst":
            type,name = operands.split(":")
            self.declareVariable(type, name)
        if command == "gm":
            variable,contents = operands.split(":")
            self.assignVariable(variable, contents, strings)
        if command == "ijwty":
            self.print(operands, strings)

    def parseLine(self, line):
        line = self.doReplacements(line)
        strings = self.findStrings(line)
        count = 0
        for string in strings:
            line=line.replace('"'+string+'"', "STR"+str(count), 1)
            count += 1
        if strings == -1:
            return -1
        # Replace variables

        split = line.find(" ")
        if split == -1:
            command = line
            operands = None
        else:
            command, operands = line[:split], line[split+1:]
        self.parseCommand(command, operands, strings)
        return line
        
        

interpreter = ngInterpreter()
while True:
    line = input("NG> ")
    result = interpreter.parseLine(line)
    #for k,v in interpreter.objects.items():
        #print("{} - {}".format(k,v))