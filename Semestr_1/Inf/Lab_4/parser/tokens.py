from enum import Enum

class TokenType(Enum):
    STRING = "string"
    NUMBER = "number"
    LF = "line feed"
    # и так далее для всех возможных токенов


class Token:
    def __init__(self, type: TokenType, pos: Position):
        self.__type = type
        self.__pos = pos

    def __str__(self):
        return f"[{self.__type}]"

    def get_type(self) -> TokenType:
        return self.__type

    def get_position(self) -> Position:
        return self.__pos


class ValueToken(Token):
    def __init__(self, value: str, type: TokenType, pos: Position):
        super().__init__(type, pos)
        self.__value = value

    def __str__(self):
        return f"[{self.get_type()}]: {self.__value}"

    def get_value(self) -> str:
        return self.__value


class StringToken(ValueToken):
    def __init__(self, value: str, pos: Position):
        super().__init__(value, TokenType.STRING, pos)


class NumberToken(ValueToken):
    def __init__(self, value: str, pos: Position):
        super().__init__(value, TokenType.NUMBER, pos)


class LFToken(Token):
    def __init__(self, pos: Position):
        super().__init__(TokenType.LF, pos)

# Здесь продолжать делать классы для разных типов токеновfrom enum import Enum

class TokenType(Enum):
    STRING = "string"
    NUMBER = "number"
    LF = "line feed"


class Token:
    def __init__(self, type: TokenType, pos: Position):
        self.__type = type
        self.__pos = pos

    def __str__(self):
        return f"[{self.__type}]"

    def get_type(self) -> TokenType:
        return self.__type

    def get_position(self) -> Position:
        return self.__pos


class ValueToken(Token):
    def __init__(self, value: str, type: TokenType, pos: Position):
        super().__init__(type, pos)
        self.__value = value

    def __str__(self):
        return f"[{self.get_type()}]: {self.__value}"

    def get_value(self) -> str:
        return self.__value


class StringToken(ValueToken):
    def __init__(self, value: str, pos: Position):
        super().__init__(value, TokenType.STRING, pos)


class NumberToken(ValueToken):
    def __init__(self, value: str, pos: Position):
        super().__init__(value, TokenType.NUMBER, pos)


class LFToken(Token):
    def __init__(self, pos: Position):
        super().__init__(TokenType.LF, pos)
