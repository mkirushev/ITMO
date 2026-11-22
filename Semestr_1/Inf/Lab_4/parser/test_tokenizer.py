import pytest

from tokenizer import tokenize


TRIVIA = {"SPACE", "LF", "TABS", "EOF", "COMMENT", "HASH"}


def token_key(token):
    if hasattr(token, "get_value"):
        return token.get_type().name, token.get_value()
    return token.get_type().name, None


def raw(text):
    tokens = list(tokenize(text))
    while tokens and tokens[-1].get_type().name == "EOF":
        tokens.pop()
    return tokens


def significant(text):
    return [token_key(token) for token in raw(text)
            if token.get_type().name not in TRIVIA]


def whole(text):
    return [token_key(token) for token in raw(text)]


def I(value):
    return ("IDENTIFIER", value)


def S(value):
    return ("STRING", value)


def N(value):
    return ("NUMBER", value)


def B(value):
    return ("BOOL", value)


def TABS(level):
    return ("TABS", level)


def COMMENT(text):
    return ("COMMENT", text)


NULL = ("NULL", None)
ASSIGN = ("ASSIGN", None)
DASH = ("DASH", None)
SPACE = ("SPACE", None)
LF = ("LF", None)
COMMA = ("COMMA", None)
OSB = ("OSB", None)
CSB = ("CSB", None)
OCB = ("OCB", None)
CCB = ("CCB", None)


@pytest.mark.parametrize("literal", [
    "0", "1", "7", "42", "+7", "-7", "-0", "+0",
    "1234567890", "-1234567890", "9223372036854775808",
])
def test_integer_numbers(literal):
    assert significant(f"key: {literal}\n") == [I("key"), ASSIGN, N(literal)]


@pytest.mark.parametrize("literal", [
    "0.0", "1.0", "0.5", ".5", "+.5", "-.5",
    "1.", "-1.", "+1.", "1.2", "-1.2", "+1.2",
    "3.14159", "-3.14159", "0.001", "-0.001",
])
def test_fractional_numbers(literal):
    assert significant(f"key: {literal}\n") == [I("key"), ASSIGN, N(literal)]


@pytest.mark.parametrize("literal", [
    "1e3", "1E3", "1e+3", "1e-3", "1E+3", "1E-3",
    "-1e3", "+1e3", "-1e-3", "+1e+3",
    "1.5e10", "1.5e+10", "1.5E-10", "-1.5e-10",
    ".5e2", "-.5e2", "1.e3", "-1.e-3", "0e0", "-0E-0",
    "1e0", "123e-045", "+0.0e+0",
])
def test_exponent_numbers(literal):
    assert significant(f"key: {literal}\n") == [I("key"), ASSIGN, N(literal)]


@pytest.mark.parametrize("literal", [
    "1.2.3", "1e", "1e+", "1e-", "1E+", "e3", "E3",
    "1e3.5", "--1", "+-1", "-+1", "++1", "1..2", "..5",
    ".", "-.", "+.", "1e--2", "1e+-2", "1.2e3e4", "1.e", "1.2e+",
])
def test_malformed_numbers_are_not_number_tokens(literal):
    try:
        tokens = significant(f"key: {literal}\n")
    except Exception:
        return
    assert (NUMBER := ("NUMBER", literal)) not in tokens


@pytest.mark.parametrize("literal,expected", [
    ("true", B("true")),
    ("false", B("false")),
    ("True", B("True")),
    ("False", B("False")),
    ("TRUE", B("TRUE")),
    ("FALSE", B("FALSE")),
    ("null", NULL),
    ("Null", NULL),
    ("NULL", NULL),
    ("~", NULL),
])
def test_boolean_and_null_forms(literal, expected):
    assert significant(f"key: {literal}\n") == [I("key"), ASSIGN, expected]


@pytest.mark.parametrize("literal,expected", [
    ("trueish", I("trueish")),
    ("false_value", I("false_value")),
    ("nullable", I("nullable")),
    ("nothing", I("nothing")),
    ("yes", I("yes")),
    ("off", I("off")),
])
def test_keywords_are_not_prefixes(literal, expected):
    assert significant(f"key: {literal}\n") == [I("key"), ASSIGN, expected]


@pytest.mark.parametrize("yaml_text,expected_value", [
    ('key: "str"\n', "str"),
    ("key: 'str'\n", "str"),
    ('key: ""\n', ""),
    ("key: ''\n", ""),
    ('key: " "\n', " "),
    ('key: "  "\n', "  "),
    ('key: "a b c"\n', "a b c"),
    ('key: "  padded  "\n', "  padded  "),
    ('key: "a:b"\n', "a:b"),
    ('key: "x#y"\n', "x#y"),
    ('key: "-x"\n', "-x"),
    ('key: "[not a list]"\n', "[not a list]"),
    ('key: "{not a map}"\n', "{not a map}"),
    ('key: "it\'s"\n', "it's"),
    ("key: 'it''s'\n", "it's"),
    ('key: \'say "hi"\'\n', 'say "hi"'),
    ('key: "a\\"b"\n', 'a"b'),
    ('key: "a\\\\b"\n', "a\\b"),
    ('key: "a\\nb"\n', "a\nb"),
    ('key: "a\\tb"\n', "a\tb"),
    ('key: "a\\u0041b"\n', "aAb"),
    ('key: "line1\nline2"\n', "line1\nline2"),
])
def test_string_values(yaml_text, expected_value):
    assert significant(yaml_text) == [I("key"), ASSIGN, S(expected_value)]


@pytest.mark.parametrize("yaml_text", [
    '"key": 1\n',
    "'key': 1\n",
])
def test_quoted_keys(yaml_text):
    assert significant(yaml_text) == [S("key"), ASSIGN, N("1")]


@pytest.mark.parametrize("yaml_text,expected", [
    ("key: abc\n", I("abc")),
    ("key: my-key\n", I("my-key")),
    ("key: _private\n", I("_private")),
    ("key: name_2\n", I("name_2")),
    ("key: abc def\n", S("abc def")),
    ("key: abc  def\n", S("abc  def")),
    ("key: 2024-01-01\n", S("2024-01-01")),
    ("key: http://example.com/a#frag\n", S("http://example.com/a#frag")),
    ("key: value#not-comment\n", S("value#not-comment")),
    ("key: a@b\n", S("a@b")),
])
def test_plain_scalars(yaml_text, expected):
    assert significant(yaml_text) == [I("key"), ASSIGN, expected]


@pytest.mark.parametrize("yaml_text,expected", [
    ("key: -5\n", [I("key"), ASSIGN, N("-5")]),
    ("key: +5\n", [I("key"), ASSIGN, N("+5")]),
    ("key: -.5\n", [I("key"), ASSIGN, N("-.5")]),
    ("key: - 5\n", [I("key"), ASSIGN, DASH, N("5")]),
    ("key: - item\n", [I("key"), ASSIGN, DASH, I("item")]),
    ("- item\n", [DASH, I("item")]),
    ("-item\n", [I("-item")]),
    ("my-key: 1\n", [I("my-key"), ASSIGN, N("1")]),
])
def test_dash_disambiguation(yaml_text, expected):
    assert significant(yaml_text) == expected


@pytest.mark.parametrize("yaml_text,expected", [
    ("[]\n", [OSB, CSB]),
    ("[1, 2]\n", [OSB, N("1"), COMMA, N("2"), CSB]),
    ("[a, [b, c]]\n", [OSB, I("a"), COMMA, OSB, I("b"), COMMA, I("c"), CSB, CSB]),
    ('["a,b", 2]\n', [OSB, S("a,b"), COMMA, N("2"), CSB]),
    ("{}\n", [OCB, CCB]),
    ("{a: 1}\n", [OCB, I("a"), ASSIGN, N("1"), CCB]),
    ("{a: 1, b: [2, 3]}\n", [
        OCB, I("a"), ASSIGN, N("1"), COMMA,
        I("b"), ASSIGN, OSB, N("2"), COMMA, N("3"), CSB, CCB,
    ]),
])
def test_flow_collections(yaml_text, expected):
    assert significant(yaml_text) == expected


@pytest.mark.parametrize("yaml_text,expected", [
    ("# comment\n", []),
    ("key: value # comment\n", [I("key"), ASSIGN, I("value")]),
    ('key: "x#y"\n', [I("key"), ASSIGN, S("x#y")]),
    ('key: "# not a comment"\n', [I("key"), ASSIGN, S("# not a comment")]),
    ("key: http://example.com#frag\n", [I("key"), ASSIGN, S("http://example.com#frag")]),
    ("key: value#not-comment\n", [I("key"), ASSIGN, S("value#not-comment")]),
    ("# a: b\nkey: 1\n", [I("key"), ASSIGN, N("1")]),
    ("# - x\nkey: 1\n", [I("key"), ASSIGN, N("1")]),
])
def test_comments_are_not_values(yaml_text, expected):
    assert significant(yaml_text) == expected


def test_comment_token_keeps_text():
    comments = [value for name, value in whole("key: value # comment\n")
                if name == "COMMENT"]
    assert comments
    assert "comment" in comments[0]


@pytest.mark.parametrize("yaml_text,expected", [
    ("a: 1\n", [I("a"), ASSIGN, SPACE, N("1"), LF]),
    ("a: 1", [I("a"), ASSIGN, SPACE, N("1")]),
    ("a: 1\r\n", [I("a"), ASSIGN, SPACE, N("1"), LF]),
    ("a: 1\n\n", [I("a"), ASSIGN, SPACE, N("1"), LF, LF]),
    ("\n", [LF]),
    ("", []),
    ("a : 1\n", [SPACE, I("a"), ASSIGN, SPACE, N("1"), LF]),
    ("a:  a\n", [I("a"), ASSIGN, SPACE, SPACE, I("a"), LF]),
    ("a:\n  b: 1\n", [
        I("a"), ASSIGN, LF, TABS(1), I("b"), ASSIGN, SPACE, N("1"), LF,
    ]),
    ("a:\n    b: 1\n", [
        I("a"), ASSIGN, LF, TABS(2), I("b"), ASSIGN, SPACE, N("1"), LF,
    ]),
    ("a:\n\tb: 1\n", [
        I("a"), ASSIGN, LF, TABS(1), I("b"), ASSIGN, SPACE, N("1"), LF,
    ]),
    ("- a\n- b\n", [DASH, SPACE, I("a"), LF, DASH, SPACE, I("b"), LF]),
])
def test_whitespace_and_line_structure(yaml_text, expected):
    assert whole(yaml_text) == expected


def test_readme_sample():
    yaml_text = 'field1: "str"\nobj1:\n  field2: 10\n  field3: true\n'
    assert whole(yaml_text) == [
        I("field1"), ASSIGN, SPACE, S("str"), LF,
        I("obj1"), ASSIGN, LF,
        TABS(1), I("field2"), ASSIGN, SPACE, N("10"), LF,
        TABS(1), I("field3"), ASSIGN, SPACE, B("true"), LF,
    ]


@pytest.mark.parametrize("yaml_text,expected", [
    ('a: ""\nb: 1\n', [I("a"), ASSIGN, S(""), I("b"), ASSIGN, N("1")]),
    ("a: ''\nb: 1\n", [I("a"), ASSIGN, S(""), I("b"), ASSIGN, N("1")]),
    ('a: "x"\nb: "y"\n', [I("a"), ASSIGN, S("x"), I("b"), ASSIGN, S("y")]),
    ('a: "x#y"\nb: 2\n', [I("a"), ASSIGN, S("x#y"), I("b"), ASSIGN, N("2")]),
    ('a: "-5"\nb: 2\n', [I("a"), ASSIGN, S("-5"), I("b"), ASSIGN, N("2")]),
    ('a: "line1\nline2"\nb: 2\n', [
        I("a"), ASSIGN, S("line1\nline2"), I("b"), ASSIGN, N("2"),
    ]),
    ('a: "x" # c\nb: 2\n', [
        I("a"), ASSIGN, S("x"), I("b"), ASSIGN, N("2"),
    ]),
    ("a: 1 # c\nb: 2\n", [I("a"), ASSIGN, N("1"), I("b"), ASSIGN, N("2")]),
    ("# only comment\na: 1\nb: 2\n", [
        I("a"), ASSIGN, N("1"), I("b"), ASSIGN, N("2"),
    ]),
])
def test_state_does_not_leak_between_lines(yaml_text, expected):
    assert significant(yaml_text) == expected


@pytest.mark.parametrize("yaml_text,fragment", [
    ('key: "unterminated\n', "quote"),
    ("key: 'unterminated\n", "quote"),
    ('key: "bad \\q"\n', "escape"),
    ("key: 1.23.24\n", "number"),
    ("key: 1e\n", "number"),
])
def test_lexical_errors(yaml_text, fragment):
    try:
        keys = whole(yaml_text)
    except Exception as exc:
        message = str(exc).lower()
        assert fragment in message or "lex" in message
        return
    assert any(name == "ERROR" and fragment in str(value).lower()
               for name, value in keys)


@pytest.mark.parametrize("yaml_text", [
    ": v\n", "a::b\n", "a: \n", ":\n",
])
def test_no_empty_value_tokens(yaml_text):
    assert all(value != "" for _, value in significant(yaml_text))


@pytest.mark.parametrize("yaml_text", [
    "a: 1b\n", "a: trueish\n", "a: nullify\n", "a: -5x\n",
])
def test_no_token_swallows_its_neighbour(yaml_text):
    values = [value for name, value in significant(yaml_text)]
    assert all(value not in {"1", "true", "null", "-5"} for value in values[2:])


# def test_tokens_have_source_positions():
#     tokens = raw("a: 1\nb: 2\n")
#     assert tokens
#     for token in tokens:
#         assert isinstance(token.line, int)
#         assert isinstance(token.column, int)
#     assert (tokens[0].line, tokens[0].column) == (1, 1)
#     second_number = next(token for token in tokens if token_key(token) == N("2"))
#     assert (second_number.line, second_number.column) == (2, 4)
