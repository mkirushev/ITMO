from enum import Enum

class TokenType(Enum):
    STRING = "string"
    NUMBER = "number"
    LF = "line feed"
    SPACE = "space"
    ASSIGN = "assign"
    BOOL = "boolean"
    DASH = "dash"
    OSB = "opening square bracket"
    CSB = "closing square bracket"
    OCB = "opening curly bracket"
    CCB = "closing curly bracket"
    COMMA = "comma"
    HASH = "hash"
    NULL = "null"
    IDENTIFIER = "identifier"


class Token:
    def __init__(self, type: TokenType):
        self.__type = type

    def __str__(self):
        return f"[{self.__type}]"

    def get_type(self) -> TokenType:
        return self.__type


class ValueToken(Token):
    def __init__(self, value: str, type: TokenType):
        super().__init__(type)
        self.__value = value

    def __str__(self):
        return f"[{self.get_type()}]: {self.__value}"

    def get_value(self) -> str:
        return self.__value


class StringToken(ValueToken):
    def __init__(self, value: str):
        super().__init__(value, TokenType.STRING)


class NumberToken(ValueToken):
    def __init__(self, value: str):
        super().__init__(value, TokenType.NUMBER)


class LFToken(Token):
    def __init__(self):
        super().__init__(TokenType.LF)


class SpaceToken(Token):
    def __init__(self):
        super().__init__(TokenType.SPACE)


class AsignToken(Token):
    def __init__(self):
        super().__init__(TokenType.ASSIGN)


class BoolToken(ValueToken):
    def __init__(self, value: str):
        super().__init__(value, TokenType.BOOL)


class DashToken(Token):
    def __init__(self):
        super().__init__(TokenType.DASH)


class OSBToken(Token):
    def __init__(self):
        super().__init__(TokenType.OSB)


class CSBToken(Token):
    def __init__(self):
        super().__init__(TokenType.CSB)


class OCBToken(Token):
    def __init__(self):
        super().__init__(TokenType.OCB)


class CCBToken(Token):
    def __init__(self):
        super().__init__(TokenType.CCB)


class CommaToken(Token):
    def __init__(self):
        super().__init__(TokenType.COMMA)


class HashToken(Token):
    def __init__(self):
        super().__init__(TokenType.HASH)


class NullToken(Token):
    def __init__(self):
        super().__init__(TokenType.NULL)


class IdentifierToken(ValueToken):
    def __init__(self, value: str):
        super().__init__(value, TokenType.IDENTIFIER)
