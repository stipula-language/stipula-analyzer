# Generated from Stipula.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,294,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,1,0,3,0,49,8,0,1,0,3,0,52,8,0,1,0,1,0,
        4,0,56,8,0,11,0,12,0,57,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,67,8,1,10,
        1,12,1,70,9,1,1,2,1,2,1,2,1,2,5,2,76,8,2,10,2,12,2,79,9,2,1,3,1,
        3,1,3,3,3,84,8,3,1,4,1,4,1,4,1,4,1,4,5,4,91,8,4,10,4,12,4,94,9,4,
        1,4,1,4,1,4,1,4,1,4,5,4,101,8,4,10,4,12,4,104,9,4,1,4,1,4,1,4,4,
        4,109,8,4,11,4,12,4,110,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,121,
        8,5,10,5,12,5,124,9,5,1,5,1,5,1,5,1,5,5,5,130,8,5,10,5,12,5,133,
        9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,144,8,6,10,6,12,6,147,
        9,6,3,6,149,8,6,1,6,1,6,1,6,1,6,1,6,5,6,156,8,6,10,6,12,6,159,9,
        6,3,6,161,8,6,1,6,1,6,1,6,1,6,1,6,3,6,168,8,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,7,5,7,178,8,7,10,7,12,7,181,9,7,1,7,5,7,184,8,7,10,7,
        12,7,187,9,7,1,8,1,8,1,8,3,8,192,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,3,9,207,8,9,1,10,1,10,1,10,1,10,3,10,213,
        8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        5,12,227,8,12,10,12,12,12,230,9,12,1,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,3,13,240,8,13,1,13,1,13,3,13,244,8,13,1,14,1,14,1,14,3,
        14,249,8,14,1,15,1,15,1,15,3,15,254,8,15,1,16,3,16,257,8,16,1,16,
        1,16,1,17,1,17,1,17,3,17,264,8,17,1,18,1,18,1,18,3,18,269,8,18,1,
        19,1,19,1,19,3,19,274,8,19,1,20,3,20,277,8,20,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,292,8,21,1,21,
        0,0,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,0,6,3,0,35,35,38,39,41,42,2,0,38,38,43,43,1,0,22,23,1,0,24,29,
        1,0,30,31,1,0,32,33,311,0,44,1,0,0,0,2,62,1,0,0,0,4,71,1,0,0,0,6,
        80,1,0,0,0,8,85,1,0,0,0,10,117,1,0,0,0,12,134,1,0,0,0,14,179,1,0,
        0,0,16,191,1,0,0,0,18,193,1,0,0,0,20,208,1,0,0,0,22,216,1,0,0,0,
        24,220,1,0,0,0,26,243,1,0,0,0,28,245,1,0,0,0,30,250,1,0,0,0,32,256,
        1,0,0,0,34,260,1,0,0,0,36,265,1,0,0,0,38,270,1,0,0,0,40,276,1,0,
        0,0,42,291,1,0,0,0,44,45,5,1,0,0,45,46,5,43,0,0,46,48,5,2,0,0,47,
        49,3,2,1,0,48,47,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,52,3,4,2,
        0,51,50,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,55,3,8,4,0,54,56,
        3,12,6,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,
        58,59,1,0,0,0,59,60,5,3,0,0,60,61,5,0,0,1,61,1,1,0,0,0,62,63,5,4,
        0,0,63,68,5,43,0,0,64,65,5,5,0,0,65,67,5,43,0,0,66,64,1,0,0,0,67,
        70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,3,1,0,0,0,70,68,1,0,0,
        0,71,72,5,6,0,0,72,77,3,6,3,0,73,74,5,5,0,0,74,76,3,6,3,0,75,73,
        1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,5,1,0,0,0,79,
        77,1,0,0,0,80,83,5,43,0,0,81,82,5,7,0,0,82,84,7,0,0,0,83,81,1,0,
        0,0,83,84,1,0,0,0,84,7,1,0,0,0,85,86,5,8,0,0,86,87,5,9,0,0,87,92,
        5,43,0,0,88,89,5,5,0,0,89,91,5,43,0,0,90,88,1,0,0,0,91,94,1,0,0,
        0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,96,
        5,10,0,0,96,97,5,9,0,0,97,102,5,43,0,0,98,99,5,5,0,0,99,101,5,43,
        0,0,100,98,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,
        0,103,105,1,0,0,0,104,102,1,0,0,0,105,106,5,10,0,0,106,108,5,2,0,
        0,107,109,3,10,5,0,108,107,1,0,0,0,109,110,1,0,0,0,110,108,1,0,0,
        0,110,111,1,0,0,0,111,112,1,0,0,0,112,113,5,3,0,0,113,114,5,11,0,
        0,114,115,5,12,0,0,115,116,5,43,0,0,116,9,1,0,0,0,117,122,5,43,0,
        0,118,119,5,5,0,0,119,121,5,43,0,0,120,118,1,0,0,0,121,124,1,0,0,
        0,122,120,1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,122,1,0,0,
        0,125,126,5,13,0,0,126,131,5,43,0,0,127,128,5,5,0,0,128,130,5,43,
        0,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,
        0,0,132,11,1,0,0,0,133,131,1,0,0,0,134,135,5,12,0,0,135,136,5,43,
        0,0,136,137,5,43,0,0,137,138,5,13,0,0,138,139,5,43,0,0,139,148,5,
        9,0,0,140,145,5,43,0,0,141,142,5,5,0,0,142,144,5,43,0,0,143,141,
        1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,149,
        1,0,0,0,147,145,1,0,0,0,148,140,1,0,0,0,148,149,1,0,0,0,149,150,
        1,0,0,0,150,151,5,10,0,0,151,160,5,14,0,0,152,157,5,43,0,0,153,154,
        5,5,0,0,154,156,5,43,0,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,
        1,0,0,0,157,158,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,160,152,
        1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,167,5,15,0,0,163,164,
        5,9,0,0,164,165,3,30,15,0,165,166,5,10,0,0,166,168,1,0,0,0,167,163,
        1,0,0,0,167,168,1,0,0,0,168,169,1,0,0,0,169,170,5,2,0,0,170,171,
        3,14,7,0,171,172,5,3,0,0,172,173,5,11,0,0,173,174,5,12,0,0,174,175,
        5,43,0,0,175,13,1,0,0,0,176,178,3,16,8,0,177,176,1,0,0,0,178,181,
        1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,185,1,0,0,0,181,179,
        1,0,0,0,182,184,3,24,12,0,183,182,1,0,0,0,184,187,1,0,0,0,185,183,
        1,0,0,0,185,186,1,0,0,0,186,15,1,0,0,0,187,185,1,0,0,0,188,192,3,
        18,9,0,189,192,3,20,10,0,190,192,3,22,11,0,191,188,1,0,0,0,191,189,
        1,0,0,0,191,190,1,0,0,0,192,17,1,0,0,0,193,194,5,16,0,0,194,195,
        5,9,0,0,195,196,3,30,15,0,196,197,5,10,0,0,197,198,5,2,0,0,198,199,
        3,14,7,0,199,200,5,3,0,0,200,206,5,17,0,0,201,202,5,2,0,0,202,203,
        3,14,7,0,203,204,5,3,0,0,204,207,1,0,0,0,205,207,3,18,9,0,206,201,
        1,0,0,0,206,205,1,0,0,0,207,19,1,0,0,0,208,209,3,30,15,0,209,212,
        5,18,0,0,210,211,5,43,0,0,211,213,5,5,0,0,212,210,1,0,0,0,212,213,
        1,0,0,0,213,214,1,0,0,0,214,215,5,43,0,0,215,21,1,0,0,0,216,217,
        3,30,15,0,217,218,5,19,0,0,218,219,5,43,0,0,219,23,1,0,0,0,220,221,
        3,26,13,0,221,222,5,20,0,0,222,223,5,12,0,0,223,224,5,43,0,0,224,
        228,5,2,0,0,225,227,3,16,8,0,226,225,1,0,0,0,227,230,1,0,0,0,228,
        226,1,0,0,0,228,229,1,0,0,0,229,231,1,0,0,0,230,228,1,0,0,0,231,
        232,5,3,0,0,232,233,5,11,0,0,233,234,5,12,0,0,234,235,5,43,0,0,235,
        25,1,0,0,0,236,239,5,34,0,0,237,238,5,30,0,0,238,240,3,28,14,0,239,
        237,1,0,0,0,239,240,1,0,0,0,240,244,1,0,0,0,241,244,5,41,0,0,242,
        244,5,43,0,0,243,236,1,0,0,0,243,241,1,0,0,0,243,242,1,0,0,0,244,
        27,1,0,0,0,245,248,7,1,0,0,246,247,5,30,0,0,247,249,3,28,14,0,248,
        246,1,0,0,0,248,249,1,0,0,0,249,29,1,0,0,0,250,253,3,32,16,0,251,
        252,7,2,0,0,252,254,3,30,15,0,253,251,1,0,0,0,253,254,1,0,0,0,254,
        31,1,0,0,0,255,257,5,21,0,0,256,255,1,0,0,0,256,257,1,0,0,0,257,
        258,1,0,0,0,258,259,3,34,17,0,259,33,1,0,0,0,260,263,3,36,18,0,261,
        262,7,3,0,0,262,264,3,34,17,0,263,261,1,0,0,0,263,264,1,0,0,0,264,
        35,1,0,0,0,265,268,3,38,19,0,266,267,7,4,0,0,267,269,3,36,18,0,268,
        266,1,0,0,0,268,269,1,0,0,0,269,37,1,0,0,0,270,273,3,40,20,0,271,
        272,7,5,0,0,272,274,3,38,19,0,273,271,1,0,0,0,273,274,1,0,0,0,274,
        39,1,0,0,0,275,277,5,31,0,0,276,275,1,0,0,0,276,277,1,0,0,0,277,
        278,1,0,0,0,278,279,3,42,21,0,279,41,1,0,0,0,280,292,5,34,0,0,281,
        292,5,35,0,0,282,292,5,38,0,0,283,292,5,39,0,0,284,292,5,41,0,0,
        285,292,5,42,0,0,286,292,5,43,0,0,287,288,5,9,0,0,288,289,3,30,15,
        0,289,290,5,10,0,0,290,292,1,0,0,0,291,280,1,0,0,0,291,281,1,0,0,
        0,291,282,1,0,0,0,291,283,1,0,0,0,291,284,1,0,0,0,291,285,1,0,0,
        0,291,286,1,0,0,0,291,287,1,0,0,0,292,43,1,0,0,0,32,48,51,57,68,
        77,83,92,102,110,122,131,145,148,157,160,167,179,185,191,206,212,
        228,239,243,248,253,256,263,268,273,276,291
    ]

class StipulaParser ( Parser ):

    grammarFileName = "Stipula.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'stipula'", "'{'", "'}'", "'assets'", 
                     "','", "'fields'", "'='", "'agreement'", "'('", "')'", 
                     "'=>'", "'@'", "':'", "'['", "']'", "'if'", "'else'", 
                     "'-o'", "'->'", "'>>'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", "'-'", 
                     "'*'", "'/'", "'now'", "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NOT", "AND", "OR", "EQ", "NEQ", "LE", 
                      "GE", "LEQ", "GEQ", "PLUS", "MINUS", "TIMES", "DIVISION", 
                      "NOW", "BOOL", "TRUE", "FALSE", "TIMEDELTA", "NUMBER", 
                      "INTEGER", "DATESTRING", "STRING", "ID", "WS", "LINECOMMENT", 
                      "BLOCKCOMMENT" ]

    RULE_stipula = 0
    RULE_assetsDecl = 1
    RULE_fieldsDecl = 2
    RULE_fieldInit = 3
    RULE_agreement = 4
    RULE_agree = 5
    RULE_functionDecl = 6
    RULE_functionBody = 7
    RULE_statement = 8
    RULE_ifThenElse = 9
    RULE_assetOperation = 10
    RULE_fieldOperation = 11
    RULE_eventDecl = 12
    RULE_timeExpression = 13
    RULE_timeExpression1 = 14
    RULE_expression = 15
    RULE_expression1 = 16
    RULE_expression2 = 17
    RULE_expression3 = 18
    RULE_expression4 = 19
    RULE_expression5 = 20
    RULE_expression6 = 21

    ruleNames =  [ "stipula", "assetsDecl", "fieldsDecl", "fieldInit", "agreement", 
                   "agree", "functionDecl", "functionBody", "statement", 
                   "ifThenElse", "assetOperation", "fieldOperation", "eventDecl", 
                   "timeExpression", "timeExpression1", "expression", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    NOT=21
    AND=22
    OR=23
    EQ=24
    NEQ=25
    LE=26
    GE=27
    LEQ=28
    GEQ=29
    PLUS=30
    MINUS=31
    TIMES=32
    DIVISION=33
    NOW=34
    BOOL=35
    TRUE=36
    FALSE=37
    TIMEDELTA=38
    NUMBER=39
    INTEGER=40
    DATESTRING=41
    STRING=42
    ID=43
    WS=44
    LINECOMMENT=45
    BLOCKCOMMENT=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StipulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.contractId = None # Token

        def agreement(self):
            return self.getTypedRuleContext(StipulaParser.AgreementContext,0)


        def EOF(self):
            return self.getToken(StipulaParser.EOF, 0)

        def ID(self):
            return self.getToken(StipulaParser.ID, 0)

        def assetsDecl(self):
            return self.getTypedRuleContext(StipulaParser.AssetsDeclContext,0)


        def fieldsDecl(self):
            return self.getTypedRuleContext(StipulaParser.FieldsDeclContext,0)


        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StipulaParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(StipulaParser.FunctionDeclContext,i)


        def getRuleIndex(self):
            return StipulaParser.RULE_stipula

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStipula" ):
                return visitor.visitStipula(self)
            else:
                return visitor.visitChildren(self)




    def stipula(self):

        localctx = StipulaParser.StipulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stipula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(StipulaParser.T__0)
            self.state = 45
            localctx.contractId = self.match(StipulaParser.ID)
            self.state = 46
            self.match(StipulaParser.T__1)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 47
                self.assetsDecl()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 50
                self.fieldsDecl()


            self.state = 53
            self.agreement()
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.functionDecl()
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12):
                    break

            self.state = 59
            self.match(StipulaParser.T__2)
            self.state = 60
            self.match(StipulaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssetsDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self.assetId = list() # of Tokens

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(StipulaParser.ID)
            else:
                return self.getToken(StipulaParser.ID, i)

        def getRuleIndex(self):
            return StipulaParser.RULE_assetsDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssetsDecl" ):
                return visitor.visitAssetsDecl(self)
            else:
                return visitor.visitChildren(self)




    def assetsDecl(self):

        localctx = StipulaParser.AssetsDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assetsDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(StipulaParser.T__3)
            self.state = 63
            localctx._ID = self.match(StipulaParser.ID)
            localctx.assetId.append(localctx._ID)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 64
                self.match(StipulaParser.T__4)
                self.state = 65
                localctx._ID = self.match(StipulaParser.ID)
                localctx.assetId.append(localctx._ID)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldsDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StipulaParser.FieldInitContext)
            else:
                return self.getTypedRuleContext(StipulaParser.FieldInitContext,i)


        def getRuleIndex(self):
            return StipulaParser.RULE_fieldsDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldsDecl" ):
                return visitor.visitFieldsDecl(self)
            else:
                return visitor.visitChildren(self)




    def fieldsDecl(self):

        localctx = StipulaParser.FieldsDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fieldsDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(StipulaParser.T__5)
            self.state = 72
            self.fieldInit()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 73
                self.match(StipulaParser.T__4)
                self.state = 74
                self.fieldInit()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fieldId = None # Token
            self.value = None # Token

        def ID(self):
            return self.getToken(StipulaParser.ID, 0)

        def BOOL(self):
            return self.getToken(StipulaParser.BOOL, 0)

        def TIMEDELTA(self):
            return self.getToken(StipulaParser.TIMEDELTA, 0)

        def NUMBER(self):
            return self.getToken(StipulaParser.NUMBER, 0)

        def DATESTRING(self):
            return self.getToken(StipulaParser.DATESTRING, 0)

        def STRING(self):
            return self.getToken(StipulaParser.STRING, 0)

        def getRuleIndex(self):
            return StipulaParser.RULE_fieldInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldInit" ):
                return visitor.visitFieldInit(self)
            else:
                return visitor.visitChildren(self)




    def fieldInit(self):

        localctx = StipulaParser.FieldInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fieldInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            localctx.fieldId = self.match(StipulaParser.ID)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 81
                self.match(StipulaParser.T__6)
                self.state = 82
                localctx.value = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7456063225856) != 0)):
                    localctx.value = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgreementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self.partyId = list() # of Tokens
            self.fieldId = list() # of Tokens
            self.stateId = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(StipulaParser.ID)
            else:
                return self.getToken(StipulaParser.ID, i)

        def agree(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StipulaParser.AgreeContext)
            else:
                return self.getTypedRuleContext(StipulaParser.AgreeContext,i)


        def getRuleIndex(self):
            return StipulaParser.RULE_agreement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgreement" ):
                return visitor.visitAgreement(self)
            else:
                return visitor.visitChildren(self)




    def agreement(self):

        localctx = StipulaParser.AgreementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_agreement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(StipulaParser.T__7)
            self.state = 86
            self.match(StipulaParser.T__8)
            self.state = 87
            localctx._ID = self.match(StipulaParser.ID)
            localctx.partyId.append(localctx._ID)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 88
                self.match(StipulaParser.T__4)
                self.state = 89
                localctx._ID = self.match(StipulaParser.ID)
                localctx.partyId.append(localctx._ID)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(StipulaParser.T__9)
            self.state = 96
            self.match(StipulaParser.T__8)
            self.state = 97
            localctx._ID = self.match(StipulaParser.ID)
            localctx.fieldId.append(localctx._ID)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 98
                self.match(StipulaParser.T__4)
                self.state = 99
                localctx._ID = self.match(StipulaParser.ID)
                localctx.fieldId.append(localctx._ID)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self.match(StipulaParser.T__9)
            self.state = 106
            self.match(StipulaParser.T__1)
            self.state = 108 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 107
                self.agree()
                self.state = 110 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==43):
                    break

            self.state = 112
            self.match(StipulaParser.T__2)
            self.state = 113
            self.match(StipulaParser.T__10)
            self.state = 114
            self.match(StipulaParser.T__11)
            self.state = 115
            localctx.stateId = self.match(StipulaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgreeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self.partyId = list() # of Tokens
            self.fieldId = list() # of Tokens

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(StipulaParser.ID)
            else:
                return self.getToken(StipulaParser.ID, i)

        def getRuleIndex(self):
            return StipulaParser.RULE_agree

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgree" ):
                return visitor.visitAgree(self)
            else:
                return visitor.visitChildren(self)




    def agree(self):

        localctx = StipulaParser.AgreeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_agree)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            localctx._ID = self.match(StipulaParser.ID)
            localctx.partyId.append(localctx._ID)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 118
                self.match(StipulaParser.T__4)
                self.state = 119
                localctx._ID = self.match(StipulaParser.ID)
                localctx.partyId.append(localctx._ID)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(StipulaParser.T__12)
            self.state = 126
            localctx._ID = self.match(StipulaParser.ID)
            localctx.fieldId.append(localctx._ID)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 127
                self.match(StipulaParser.T__4)
                self.state = 128
                localctx._ID = self.match(StipulaParser.ID)
                localctx.fieldId.append(localctx._ID)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.startStateId = None # Token
            self.partyId = None # Token
            self.functionId = None # Token
            self._ID = None # Token
            self.fieldId = list() # of Tokens
            self.assetId = list() # of Tokens
            self.precondition = None # ExpressionContext
            self.endStateId = None # Token

        def functionBody(self):
            return self.getTypedRuleContext(StipulaParser.FunctionBodyContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(StipulaParser.ID)
            else:
                return self.getToken(StipulaParser.ID, i)

        def expression(self):
            return self.getTypedRuleContext(StipulaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return StipulaParser.RULE_functionDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = StipulaParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(StipulaParser.T__11)
            self.state = 135
            localctx.startStateId = self.match(StipulaParser.ID)
            self.state = 136
            localctx.partyId = self.match(StipulaParser.ID)
            self.state = 137
            self.match(StipulaParser.T__12)
            self.state = 138
            localctx.functionId = self.match(StipulaParser.ID)
            self.state = 139
            self.match(StipulaParser.T__8)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 140
                localctx._ID = self.match(StipulaParser.ID)
                localctx.fieldId.append(localctx._ID)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 141
                    self.match(StipulaParser.T__4)
                    self.state = 142
                    localctx._ID = self.match(StipulaParser.ID)
                    localctx.fieldId.append(localctx._ID)
                    self.state = 147
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 150
            self.match(StipulaParser.T__9)
            self.state = 151
            self.match(StipulaParser.T__13)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 152
                localctx._ID = self.match(StipulaParser.ID)
                localctx.assetId.append(localctx._ID)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 153
                    self.match(StipulaParser.T__4)
                    self.state = 154
                    localctx._ID = self.match(StipulaParser.ID)
                    localctx.assetId.append(localctx._ID)
                    self.state = 159
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 162
            self.match(StipulaParser.T__14)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 163
                self.match(StipulaParser.T__8)
                self.state = 164
                localctx.precondition = self.expression()
                self.state = 165
                self.match(StipulaParser.T__9)


            self.state = 169
            self.match(StipulaParser.T__1)
            self.state = 170
            self.functionBody()
            self.state = 171
            self.match(StipulaParser.T__2)
            self.state = 172
            self.match(StipulaParser.T__10)
            self.state = 173
            self.match(StipulaParser.T__11)
            self.state = 174
            localctx.endStateId = self.match(StipulaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StipulaParser.StatementContext)
            else:
                return self.getTypedRuleContext(StipulaParser.StatementContext,i)


        def eventDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StipulaParser.EventDeclContext)
            else:
                return self.getTypedRuleContext(StipulaParser.EventDeclContext,i)


        def getRuleIndex(self):
            return StipulaParser.RULE_functionBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionBody" ):
                return visitor.visitFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def functionBody(self):

        localctx = StipulaParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 176
                    self.statement() 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 11012296146944) != 0):
                self.state = 182
                self.eventDecl()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifThenElse(self):
            return self.getTypedRuleContext(StipulaParser.IfThenElseContext,0)


        def assetOperation(self):
            return self.getTypedRuleContext(StipulaParser.AssetOperationContext,0)


        def fieldOperation(self):
            return self.getTypedRuleContext(StipulaParser.FieldOperationContext,0)


        def getRuleIndex(self):
            return StipulaParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = StipulaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.ifThenElse()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.assetOperation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.fieldOperation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfThenElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # ExpressionContext
            self.ifBody = None # FunctionBodyContext
            self.elseBody = None # FunctionBodyContext

        def expression(self):
            return self.getTypedRuleContext(StipulaParser.ExpressionContext,0)


        def functionBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StipulaParser.FunctionBodyContext)
            else:
                return self.getTypedRuleContext(StipulaParser.FunctionBodyContext,i)


        def ifThenElse(self):
            return self.getTypedRuleContext(StipulaParser.IfThenElseContext,0)


        def getRuleIndex(self):
            return StipulaParser.RULE_ifThenElse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfThenElse" ):
                return visitor.visitIfThenElse(self)
            else:
                return visitor.visitChildren(self)




    def ifThenElse(self):

        localctx = StipulaParser.IfThenElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifThenElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(StipulaParser.T__15)
            self.state = 194
            self.match(StipulaParser.T__8)
            self.state = 195
            localctx.condition = self.expression()
            self.state = 196
            self.match(StipulaParser.T__9)
            self.state = 197
            self.match(StipulaParser.T__1)
            self.state = 198
            localctx.ifBody = self.functionBody()
            self.state = 199
            self.match(StipulaParser.T__2)
            self.state = 200
            self.match(StipulaParser.T__16)
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 201
                self.match(StipulaParser.T__1)
                self.state = 202
                localctx.elseBody = self.functionBody()
                self.state = 203
                self.match(StipulaParser.T__2)
                pass
            elif token in [16]:
                self.state = 205
                self.ifThenElse()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssetOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExpressionContext
            self.right = None # Token
            self.destination = None # Token

        def expression(self):
            return self.getTypedRuleContext(StipulaParser.ExpressionContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(StipulaParser.ID)
            else:
                return self.getToken(StipulaParser.ID, i)

        def getRuleIndex(self):
            return StipulaParser.RULE_assetOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssetOperation" ):
                return visitor.visitAssetOperation(self)
            else:
                return visitor.visitChildren(self)




    def assetOperation(self):

        localctx = StipulaParser.AssetOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assetOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            localctx.left = self.expression()
            self.state = 209
            self.match(StipulaParser.T__17)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 210
                localctx.right = self.match(StipulaParser.ID)
                self.state = 211
                self.match(StipulaParser.T__4)


            self.state = 214
            localctx.destination = self.match(StipulaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExpressionContext
            self.right = None # Token

        def expression(self):
            return self.getTypedRuleContext(StipulaParser.ExpressionContext,0)


        def ID(self):
            return self.getToken(StipulaParser.ID, 0)

        def getRuleIndex(self):
            return StipulaParser.RULE_fieldOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldOperation" ):
                return visitor.visitFieldOperation(self)
            else:
                return visitor.visitChildren(self)




    def fieldOperation(self):

        localctx = StipulaParser.FieldOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fieldOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            localctx.left = self.expression()
            self.state = 217
            self.match(StipulaParser.T__18)
            self.state = 218
            localctx.right = self.match(StipulaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.trigger = None # TimeExpressionContext
            self.startStateId = None # Token
            self.endStateId = None # Token

        def timeExpression(self):
            return self.getTypedRuleContext(StipulaParser.TimeExpressionContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(StipulaParser.ID)
            else:
                return self.getToken(StipulaParser.ID, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StipulaParser.StatementContext)
            else:
                return self.getTypedRuleContext(StipulaParser.StatementContext,i)


        def getRuleIndex(self):
            return StipulaParser.RULE_eventDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventDecl" ):
                return visitor.visitEventDecl(self)
            else:
                return visitor.visitChildren(self)




    def eventDecl(self):

        localctx = StipulaParser.EventDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_eventDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            localctx.trigger = self.timeExpression()
            self.state = 221
            self.match(StipulaParser.T__19)
            self.state = 222
            self.match(StipulaParser.T__11)
            self.state = 223
            localctx.startStateId = self.match(StipulaParser.ID)
            self.state = 224
            self.match(StipulaParser.T__1)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16271485764096) != 0):
                self.state = 225
                self.statement()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 231
            self.match(StipulaParser.T__2)
            self.state = 232
            self.match(StipulaParser.T__10)
            self.state = 233
            self.match(StipulaParser.T__11)
            self.state = 234
            localctx.endStateId = self.match(StipulaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.right = None # TimeExpression1Context

        def NOW(self):
            return self.getToken(StipulaParser.NOW, 0)

        def PLUS(self):
            return self.getToken(StipulaParser.PLUS, 0)

        def timeExpression1(self):
            return self.getTypedRuleContext(StipulaParser.TimeExpression1Context,0)


        def DATESTRING(self):
            return self.getToken(StipulaParser.DATESTRING, 0)

        def ID(self):
            return self.getToken(StipulaParser.ID, 0)

        def getRuleIndex(self):
            return StipulaParser.RULE_timeExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimeExpression" ):
                return visitor.visitTimeExpression(self)
            else:
                return visitor.visitChildren(self)




    def timeExpression(self):

        localctx = StipulaParser.TimeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_timeExpression)
        self._la = 0 # Token type
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(StipulaParser.NOW)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 237
                    self.match(StipulaParser.PLUS)
                    self.state = 238
                    localctx.right = self.timeExpression1()


                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(StipulaParser.DATESTRING)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.match(StipulaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeExpression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Token
            self.right = None # TimeExpression1Context

        def TIMEDELTA(self):
            return self.getToken(StipulaParser.TIMEDELTA, 0)

        def ID(self):
            return self.getToken(StipulaParser.ID, 0)

        def PLUS(self):
            return self.getToken(StipulaParser.PLUS, 0)

        def timeExpression1(self):
            return self.getTypedRuleContext(StipulaParser.TimeExpression1Context,0)


        def getRuleIndex(self):
            return StipulaParser.RULE_timeExpression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimeExpression1" ):
                return visitor.visitTimeExpression1(self)
            else:
                return visitor.visitChildren(self)




    def timeExpression1(self):

        localctx = StipulaParser.TimeExpression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_timeExpression1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            localctx.left = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==38 or _la==43):
                localctx.left = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 246
                self.match(StipulaParser.PLUS)
                self.state = 247
                localctx.right = self.timeExpression1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expression1Context
            self.operator = None # Token
            self.right = None # ExpressionContext

        def expression1(self):
            return self.getTypedRuleContext(StipulaParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(StipulaParser.ExpressionContext,0)


        def AND(self):
            return self.getToken(StipulaParser.AND, 0)

        def OR(self):
            return self.getToken(StipulaParser.OR, 0)

        def getRuleIndex(self):
            return StipulaParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = StipulaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            localctx.left = self.expression1()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22 or _la==23:
                self.state = 251
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 252
                localctx.right = self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(StipulaParser.Expression2Context,0)


        def NOT(self):
            return self.getToken(StipulaParser.NOT, 0)

        def getRuleIndex(self):
            return StipulaParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = StipulaParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 255
                self.match(StipulaParser.NOT)


            self.state = 258
            self.expression2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expression3Context
            self.operator = None # Token
            self.right = None # Expression2Context

        def expression3(self):
            return self.getTypedRuleContext(StipulaParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(StipulaParser.Expression2Context,0)


        def EQ(self):
            return self.getToken(StipulaParser.EQ, 0)

        def NEQ(self):
            return self.getToken(StipulaParser.NEQ, 0)

        def GE(self):
            return self.getToken(StipulaParser.GE, 0)

        def LE(self):
            return self.getToken(StipulaParser.LE, 0)

        def GEQ(self):
            return self.getToken(StipulaParser.GEQ, 0)

        def LEQ(self):
            return self.getToken(StipulaParser.LEQ, 0)

        def getRuleIndex(self):
            return StipulaParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)




    def expression2(self):

        localctx = StipulaParser.Expression2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            localctx.left = self.expression3()
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0):
                self.state = 261
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 262
                localctx.right = self.expression2()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expression4Context
            self.operator = None # Token
            self.right = None # Expression3Context

        def expression4(self):
            return self.getTypedRuleContext(StipulaParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(StipulaParser.Expression3Context,0)


        def PLUS(self):
            return self.getToken(StipulaParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(StipulaParser.MINUS, 0)

        def getRuleIndex(self):
            return StipulaParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)




    def expression3(self):

        localctx = StipulaParser.Expression3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            localctx.left = self.expression4()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30 or _la==31:
                self.state = 266
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 267
                localctx.right = self.expression3()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expression5Context
            self.operator = None # Token
            self.right = None # Expression4Context

        def expression5(self):
            return self.getTypedRuleContext(StipulaParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(StipulaParser.Expression4Context,0)


        def TIMES(self):
            return self.getToken(StipulaParser.TIMES, 0)

        def DIVISION(self):
            return self.getToken(StipulaParser.DIVISION, 0)

        def getRuleIndex(self):
            return StipulaParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)




    def expression4(self):

        localctx = StipulaParser.Expression4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            localctx.left = self.expression5()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32 or _la==33:
                self.state = 271
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 272
                localctx.right = self.expression4()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(StipulaParser.Expression6Context,0)


        def MINUS(self):
            return self.getToken(StipulaParser.MINUS, 0)

        def getRuleIndex(self):
            return StipulaParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = StipulaParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 275
                self.match(StipulaParser.MINUS)


            self.state = 278
            self.expression6()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOW(self):
            return self.getToken(StipulaParser.NOW, 0)

        def BOOL(self):
            return self.getToken(StipulaParser.BOOL, 0)

        def TIMEDELTA(self):
            return self.getToken(StipulaParser.TIMEDELTA, 0)

        def NUMBER(self):
            return self.getToken(StipulaParser.NUMBER, 0)

        def DATESTRING(self):
            return self.getToken(StipulaParser.DATESTRING, 0)

        def STRING(self):
            return self.getToken(StipulaParser.STRING, 0)

        def ID(self):
            return self.getToken(StipulaParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(StipulaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return StipulaParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = StipulaParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression6)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(StipulaParser.NOW)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(StipulaParser.BOOL)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.match(StipulaParser.TIMEDELTA)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 283
                self.match(StipulaParser.NUMBER)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 5)
                self.state = 284
                self.match(StipulaParser.DATESTRING)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 6)
                self.state = 285
                self.match(StipulaParser.STRING)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 7)
                self.state = 286
                self.match(StipulaParser.ID)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 8)
                self.state = 287
                self.match(StipulaParser.T__8)
                self.state = 288
                self.expression()
                self.state = 289
                self.match(StipulaParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





