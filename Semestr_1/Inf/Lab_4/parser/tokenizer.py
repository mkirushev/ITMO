from tokens import *

def tokenize(text: str) -> list[Token]:
    # Здесь логика разбиения на токены
    return [
        StringToken("Hello, World", None),
        LFToken(None),
        NumberToken("67", None)
    ]

def printTokens(tokens: list[Token]):
    for token in tokens:
        print(token)


printTokens(tokenize(""))
