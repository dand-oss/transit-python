from constants import *
from class_hash import ClassDict
from transit_types import Keyword, Symbol
import uuid
class NoneHandler(object):
    @staticmethod
    def tag(_):
        return '_'
    @staticmethod
    def rep(_):
        return None
    @staticmethod
    def string_rep(n):
        return None

class IntHandler(object):
    @staticmethod
    def tag(i):
        return 'i'
    @staticmethod
    def rep(i):
        return i
    @staticmethod
    def string_rep(i):
        return str(i)

class FloatHandler(object):
    @staticmethod
    def tag(_):
        return "f"
    @staticmethod
    def rep(f):
        return str(f)
    @staticmethod
    def string_rep(f):
        return FloatHandler.rep(f)

class StringHandler(object):
    @staticmethod
    def tag(s):
        return 's'
    @staticmethod
    def rep(s):
        return s
    @staticmethod
    def string_rep(s):
        return s

class BooleanHandler(object):
    @staticmethod
    def tag(_):
        return '?'
    @staticmethod
    def rep(b):
        return b
    @staticmethod
    def string_rep(b):
        return b and 't' or 'f'

class ArrayHandler(object):
    @staticmethod
    def tag(a):
        return 'array'
    @staticmethod
    def rep(a):
        return a
    @staticmethod
    def string_rep(a):
        return None

class MapHandler(object):
    @staticmethod
    def tag(m):
        return 'map'
    @staticmethod
    def rep(m):
        return m
    @staticmethod
    def string_rep(m):
        return None

class KeywordHandler(object):
    @staticmethod
    def tag(k):
        return ':'
    @staticmethod
    def rep(k):
        return str(k)
    @staticmethod
    def string_rep(k):
        return str(k)

class SymbolHandler(object):
    @staticmethod
    def tag(s):
        return '$'
    @staticmethod
    def rep(s):
        return str(s)
    @staticmethod
    def string_rep(s):
        return str(s)

class UuidHandler(object):
    mask = pow(2, 64) - 1
    @staticmethod
    def tag(_):
        return "u"
    @staticmethod
    def rep(u):
        i = u.int
        return (i >> 64, i & UuidHandler.mask)
    @staticmethod
    def string_rep(u):
        return str(u)

class Handler(ClassDict):
    def __init__(self):
        super(Handler, self).__init__()
        self[type(None)] = NoneHandler
        self[bool] = BooleanHandler
        self[str] = StringHandler
        self[list] = ArrayHandler
        self[tuple] = ArrayHandler
        self[dict] = MapHandler
        self[int] = IntHandler
        self[float] = FloatHandler
        self[long] = IntHandler
        self[Keyword] = KeywordHandler
        self[Symbol] = SymbolHandler
        self[uuid.UUID] = UuidHandler