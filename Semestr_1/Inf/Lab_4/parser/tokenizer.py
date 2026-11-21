from tokens import *

def is_num(txt: str) -> bool:
    for s in txt:
        if not s.isdecimal():
            return False
    return True


def is_identifier(txt: str) -> bool:
    for s in txt:
        if (not s.isalpha()) and (not s.isdecimal()) and (not s in '_-'):
            return False
    return True 

def get_tokentype(txt: str) -> Token:
    if txt == "\n":
        return LFToken()
    elif txt == " ":
        return SpaceToken()
    elif txt == ":":
        return AsignToken()
    elif txt == "false":
        return BoolToken("false")
    elif txt == "true":
        return BoolToken("true")
    elif txt == "-":
        return DashToken()
    elif txt == "[":
        return OCBToken()
    elif txt == "]":
        return CCBToken()
    elif txt == "{":
        return OSBToken()
    elif txt == "}":
        return CSBToken()
    elif txt == ",":
        return CommaToken()
    elif txt == "#":
        return HashToken()
    elif txt == "null":
        return NullToken()
    elif is_num(txt):
        return NumberToken(txt)
    elif is_identifier(txt):
        return IdentifierToken(txt)
    else:
        return StringToken(txt)

def tokenize(text: str) -> list[Token]:
    tokens = []
    now = ""
    check = False
    for s in text:
        if s == ":":
            tokens.append(get_tokentype(now))
            tokens.append(get_tokentype(s))
            now = ""
        elif s == " " and not check:
            tokens.append(get_tokentype(s))
        elif s == "\n":
            if now == "":
                tokens.append(get_tokentype(s))
                continue
            if check:
                tokens.append(StringToken(now[:-1]))
            else:
                tokens.append(get_tokentype(now))
            tokens.append(get_tokentype(s))
            now = ""
            check = False
        elif (s == "\"" or s == "\'") and len(now) > 0:
            now += s
        elif s == "\"" or s == "\'":
            check = True
            continue
        elif s == "#":
            tokens.append(get_tokentype(s))
        elif s == "-":
            tokens.append(get_tokentype(s))
        else:
            now += s
    return tokens

def printTokens(tokens: list[Token]):
    for token in tokens:
        print(token)


printTokens(tokenize())