# Generated from miniparser.g4 by ANTLR 4.13.1
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
        4,1,63,299,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        5,0,68,8,0,10,0,12,0,71,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,87,8,1,1,2,1,2,5,2,91,8,2,10,2,12,2,94,9,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,105,8,4,10,4,12,4,108,
        9,4,1,5,1,5,1,5,3,5,113,8,5,1,6,1,6,3,6,117,8,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,132,8,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,10,1,10,1,10,3,10,143,8,10,1,10,1,10,3,10,147,8,10,1,10,
        1,10,3,10,151,8,10,1,10,1,10,1,10,1,11,1,11,3,11,158,8,11,1,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,172,8,
        14,1,15,1,15,1,15,1,15,3,15,178,8,15,1,15,1,15,1,15,1,16,1,16,1,
        16,5,16,186,8,16,10,16,12,16,189,9,16,1,17,1,17,1,17,1,18,1,18,1,
        18,3,18,197,8,18,1,18,1,18,1,19,1,19,1,19,5,19,204,8,19,10,19,12,
        19,207,9,19,1,20,1,20,3,20,211,8,20,1,20,1,20,1,21,1,21,1,21,1,21,
        1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,24,5,24,227,8,24,10,24,12,24,
        230,9,24,1,25,1,25,1,25,5,25,235,8,25,10,25,12,25,238,9,25,1,26,
        1,26,1,26,5,26,243,8,26,10,26,12,26,246,9,26,1,27,1,27,1,27,5,27,
        251,8,27,10,27,12,27,254,9,27,1,28,1,28,1,28,5,28,259,8,28,10,28,
        12,28,262,9,28,1,29,1,29,1,29,5,29,267,8,29,10,29,12,29,270,9,29,
        1,30,1,30,1,30,3,30,275,8,30,1,31,1,31,5,31,279,8,31,10,31,12,31,
        282,9,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,3,32,297,8,32,1,32,0,0,33,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        0,8,1,0,24,29,1,0,13,18,1,0,37,38,1,0,39,42,1,0,32,33,1,0,34,36,
        2,0,32,33,45,45,1,0,30,31,308,0,69,1,0,0,0,2,86,1,0,0,0,4,88,1,0,
        0,0,6,97,1,0,0,0,8,101,1,0,0,0,10,109,1,0,0,0,12,116,1,0,0,0,14,
        122,1,0,0,0,16,124,1,0,0,0,18,133,1,0,0,0,20,139,1,0,0,0,22,157,
        1,0,0,0,24,159,1,0,0,0,26,162,1,0,0,0,28,171,1,0,0,0,30,173,1,0,
        0,0,32,182,1,0,0,0,34,190,1,0,0,0,36,193,1,0,0,0,38,200,1,0,0,0,
        40,208,1,0,0,0,42,214,1,0,0,0,44,219,1,0,0,0,46,221,1,0,0,0,48,223,
        1,0,0,0,50,231,1,0,0,0,52,239,1,0,0,0,54,247,1,0,0,0,56,255,1,0,
        0,0,58,263,1,0,0,0,60,274,1,0,0,0,62,276,1,0,0,0,64,296,1,0,0,0,
        66,68,3,2,1,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,
        0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,5,0,0,1,73,1,1,0,0,0,74,
        87,3,6,3,0,75,87,3,12,6,0,76,87,3,16,8,0,77,87,3,18,9,0,78,87,3,
        20,10,0,79,87,3,30,15,0,80,81,3,36,18,0,81,82,5,52,0,0,82,87,1,0,
        0,0,83,87,3,40,20,0,84,87,3,4,2,0,85,87,5,52,0,0,86,74,1,0,0,0,86,
        75,1,0,0,0,86,76,1,0,0,0,86,77,1,0,0,0,86,78,1,0,0,0,86,79,1,0,0,
        0,86,80,1,0,0,0,86,83,1,0,0,0,86,84,1,0,0,0,86,85,1,0,0,0,87,3,1,
        0,0,0,88,92,5,48,0,0,89,91,3,2,1,0,90,89,1,0,0,0,91,94,1,0,0,0,92,
        90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,96,5,49,
        0,0,96,5,1,0,0,0,97,98,3,44,22,0,98,99,3,8,4,0,99,100,5,52,0,0,100,
        7,1,0,0,0,101,106,3,10,5,0,102,103,5,53,0,0,103,105,3,10,5,0,104,
        102,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,
        9,1,0,0,0,108,106,1,0,0,0,109,112,5,59,0,0,110,111,5,29,0,0,111,
        113,3,46,23,0,112,110,1,0,0,0,112,113,1,0,0,0,113,11,1,0,0,0,114,
        117,5,59,0,0,115,117,3,42,21,0,116,114,1,0,0,0,116,115,1,0,0,0,117,
        118,1,0,0,0,118,119,3,14,7,0,119,120,3,46,23,0,120,121,5,52,0,0,
        121,13,1,0,0,0,122,123,7,0,0,0,123,15,1,0,0,0,124,125,5,1,0,0,125,
        126,5,46,0,0,126,127,3,46,23,0,127,128,5,47,0,0,128,131,3,2,1,0,
        129,130,5,2,0,0,130,132,3,2,1,0,131,129,1,0,0,0,131,132,1,0,0,0,
        132,17,1,0,0,0,133,134,5,3,0,0,134,135,5,46,0,0,135,136,3,46,23,
        0,136,137,5,47,0,0,137,138,3,2,1,0,138,19,1,0,0,0,139,140,5,4,0,
        0,140,142,5,46,0,0,141,143,3,22,11,0,142,141,1,0,0,0,142,143,1,0,
        0,0,143,144,1,0,0,0,144,146,5,52,0,0,145,147,3,46,23,0,146,145,1,
        0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,150,5,52,0,0,149,151,3,
        28,14,0,150,149,1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,153,
        5,47,0,0,153,154,3,2,1,0,154,21,1,0,0,0,155,158,3,24,12,0,156,158,
        3,26,13,0,157,155,1,0,0,0,157,156,1,0,0,0,158,23,1,0,0,0,159,160,
        3,44,22,0,160,161,3,8,4,0,161,25,1,0,0,0,162,163,5,59,0,0,163,164,
        3,14,7,0,164,165,3,46,23,0,165,27,1,0,0,0,166,167,5,59,0,0,167,172,
        5,30,0,0,168,169,5,59,0,0,169,172,5,31,0,0,170,172,3,26,13,0,171,
        166,1,0,0,0,171,168,1,0,0,0,171,170,1,0,0,0,172,29,1,0,0,0,173,174,
        3,44,22,0,174,175,5,59,0,0,175,177,5,46,0,0,176,178,3,32,16,0,177,
        176,1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,180,5,47,0,0,180,
        181,3,4,2,0,181,31,1,0,0,0,182,187,3,34,17,0,183,184,5,53,0,0,184,
        186,3,34,17,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,
        188,1,0,0,0,188,33,1,0,0,0,189,187,1,0,0,0,190,191,3,44,22,0,191,
        192,5,59,0,0,192,35,1,0,0,0,193,194,5,59,0,0,194,196,5,46,0,0,195,
        197,3,38,19,0,196,195,1,0,0,0,196,197,1,0,0,0,197,198,1,0,0,0,198,
        199,5,47,0,0,199,37,1,0,0,0,200,205,3,46,23,0,201,202,5,53,0,0,202,
        204,3,46,23,0,203,201,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,
        206,1,0,0,0,206,39,1,0,0,0,207,205,1,0,0,0,208,210,5,19,0,0,209,
        211,3,46,23,0,210,209,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,
        213,5,52,0,0,213,41,1,0,0,0,214,215,5,59,0,0,215,216,5,50,0,0,216,
        217,3,46,23,0,217,218,5,51,0,0,218,43,1,0,0,0,219,220,7,1,0,0,220,
        45,1,0,0,0,221,222,3,48,24,0,222,47,1,0,0,0,223,228,3,50,25,0,224,
        225,5,44,0,0,225,227,3,50,25,0,226,224,1,0,0,0,227,230,1,0,0,0,228,
        226,1,0,0,0,228,229,1,0,0,0,229,49,1,0,0,0,230,228,1,0,0,0,231,236,
        3,52,26,0,232,233,5,43,0,0,233,235,3,52,26,0,234,232,1,0,0,0,235,
        238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,51,1,0,0,0,238,236,
        1,0,0,0,239,244,3,54,27,0,240,241,7,2,0,0,241,243,3,54,27,0,242,
        240,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,
        53,1,0,0,0,246,244,1,0,0,0,247,252,3,56,28,0,248,249,7,3,0,0,249,
        251,3,56,28,0,250,248,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,
        253,1,0,0,0,253,55,1,0,0,0,254,252,1,0,0,0,255,260,3,58,29,0,256,
        257,7,4,0,0,257,259,3,58,29,0,258,256,1,0,0,0,259,262,1,0,0,0,260,
        258,1,0,0,0,260,261,1,0,0,0,261,57,1,0,0,0,262,260,1,0,0,0,263,268,
        3,60,30,0,264,265,7,5,0,0,265,267,3,60,30,0,266,264,1,0,0,0,267,
        270,1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,59,1,0,0,0,270,268,
        1,0,0,0,271,272,7,6,0,0,272,275,3,60,30,0,273,275,3,62,31,0,274,
        271,1,0,0,0,274,273,1,0,0,0,275,61,1,0,0,0,276,280,3,64,32,0,277,
        279,7,7,0,0,278,277,1,0,0,0,279,282,1,0,0,0,280,278,1,0,0,0,280,
        281,1,0,0,0,281,63,1,0,0,0,282,280,1,0,0,0,283,297,5,56,0,0,284,
        297,5,55,0,0,285,297,5,57,0,0,286,297,5,58,0,0,287,297,5,22,0,0,
        288,297,5,23,0,0,289,297,5,59,0,0,290,297,3,36,18,0,291,297,3,42,
        21,0,292,293,5,46,0,0,293,294,3,46,23,0,294,295,5,47,0,0,295,297,
        1,0,0,0,296,283,1,0,0,0,296,284,1,0,0,0,296,285,1,0,0,0,296,286,
        1,0,0,0,296,287,1,0,0,0,296,288,1,0,0,0,296,289,1,0,0,0,296,290,
        1,0,0,0,296,291,1,0,0,0,296,292,1,0,0,0,297,65,1,0,0,0,26,69,86,
        92,106,112,116,131,142,146,150,157,171,177,187,196,205,210,228,236,
        244,252,260,268,274,280,296
    ]

class miniparser ( Parser ):

    grammarFileName = "miniparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'while'", "'for'", 
                     "'do'", "'switch'", "'case'", "'default'", "'const'", 
                     "'printf'", "'scanf'", "'sizeof'", "'int'", "'float'", 
                     "'double'", "'char'", "'bool'", "'void'", "'return'", 
                     "'break'", "'continue'", "'true'", "'false'", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'='", "'++'", "'--'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'>='", "'<='", "'>'", "'<'", "'&&'", "'||'", "'!'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "FOR", "DO", "SWITCH", 
                      "CASE", "DEFAULT", "CONST", "PRINTF", "SCANF", "SIZEOF", 
                      "INT", "FLOAT", "DOUBLE", "CHAR", "BOOL", "VOID", 
                      "RETURN", "BREAK", "CONTINUE", "TRUE", "FALSE", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "ASSIGN", "INCREMENT", "DECREMENT", "PLUS", "MINUS", 
                      "MULT", "DIV", "MOD", "EQUAL", "NOT_EQUAL", "GREATER_EQUAL", 
                      "LESS_EQUAL", "GREATER", "LESS", "AND", "OR", "NOT", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "SEMICOLON", "COMMA", "COLON", "FLOAT_LITERAL", 
                      "INTEGER_LITERAL", "STRING_LITERAL", "CHAR_LITERAL", 
                      "IDENTIFIER", "LINE_COMMENT", "BLOCK_COMMENT", "WHITESPACE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_variableDeclaration = 3
    RULE_variableList = 4
    RULE_variable = 5
    RULE_assignment = 6
    RULE_assignmentOperator = 7
    RULE_ifStatement = 8
    RULE_whileStatement = 9
    RULE_forStatement = 10
    RULE_forInit = 11
    RULE_variableDeclarationFor = 12
    RULE_assignmentNoSemi = 13
    RULE_forUpdate = 14
    RULE_functionDefinition = 15
    RULE_parameterList = 16
    RULE_parameter = 17
    RULE_functionCall = 18
    RULE_argumentList = 19
    RULE_returnStatement = 20
    RULE_arrayAccess = 21
    RULE_type = 22
    RULE_expression = 23
    RULE_logicalOr = 24
    RULE_logicalAnd = 25
    RULE_equality = 26
    RULE_relational = 27
    RULE_additive = 28
    RULE_multiplicative = 29
    RULE_unary = 30
    RULE_postfix = 31
    RULE_primary = 32

    ruleNames =  [ "program", "statement", "block", "variableDeclaration", 
                   "variableList", "variable", "assignment", "assignmentOperator", 
                   "ifStatement", "whileStatement", "forStatement", "forInit", 
                   "variableDeclarationFor", "assignmentNoSemi", "forUpdate", 
                   "functionDefinition", "parameterList", "parameter", "functionCall", 
                   "argumentList", "returnStatement", "arrayAccess", "type", 
                   "expression", "logicalOr", "logicalAnd", "equality", 
                   "relational", "additive", "multiplicative", "unary", 
                   "postfix", "primary" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    FOR=4
    DO=5
    SWITCH=6
    CASE=7
    DEFAULT=8
    CONST=9
    PRINTF=10
    SCANF=11
    SIZEOF=12
    INT=13
    FLOAT=14
    DOUBLE=15
    CHAR=16
    BOOL=17
    VOID=18
    RETURN=19
    BREAK=20
    CONTINUE=21
    TRUE=22
    FALSE=23
    PLUS_ASSIGN=24
    MINUS_ASSIGN=25
    MULT_ASSIGN=26
    DIV_ASSIGN=27
    MOD_ASSIGN=28
    ASSIGN=29
    INCREMENT=30
    DECREMENT=31
    PLUS=32
    MINUS=33
    MULT=34
    DIV=35
    MOD=36
    EQUAL=37
    NOT_EQUAL=38
    GREATER_EQUAL=39
    LESS_EQUAL=40
    GREATER=41
    LESS=42
    AND=43
    OR=44
    NOT=45
    LPAREN=46
    RPAREN=47
    LBRACE=48
    RBRACE=49
    LBRACKET=50
    RBRACKET=51
    SEMICOLON=52
    COMMA=53
    COLON=54
    FLOAT_LITERAL=55
    INTEGER_LITERAL=56
    STRING_LITERAL=57
    CHAR_LITERAL=58
    IDENTIFIER=59
    LINE_COMMENT=60
    BLOCK_COMMENT=61
    WHITESPACE=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(miniparser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.StatementContext)
            else:
                return self.getTypedRuleContext(miniparser.StatementContext,i)


        def getRuleIndex(self):
            return miniparser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = miniparser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 581245826908545050) != 0):
                self.state = 66
                self.statement()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(miniparser.EOF)
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

        def variableDeclaration(self):
            return self.getTypedRuleContext(miniparser.VariableDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(miniparser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(miniparser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(miniparser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(miniparser.ForStatementContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(miniparser.FunctionDefinitionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(miniparser.FunctionCallContext,0)


        def SEMICOLON(self):
            return self.getToken(miniparser.SEMICOLON, 0)

        def returnStatement(self):
            return self.getTypedRuleContext(miniparser.ReturnStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(miniparser.BlockContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = miniparser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.functionDefinition()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.functionCall()
                self.state = 81
                self.match(miniparser.SEMICOLON)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 84
                self.block()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 85
                self.match(miniparser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(miniparser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(miniparser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.StatementContext)
            else:
                return self.getTypedRuleContext(miniparser.StatementContext,i)


        def getRuleIndex(self):
            return miniparser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = miniparser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(miniparser.LBRACE)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 581245826908545050) != 0):
                self.state = 89
                self.statement()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(miniparser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(miniparser.TypeContext,0)


        def variableList(self):
            return self.getTypedRuleContext(miniparser.VariableListContext,0)


        def SEMICOLON(self):
            return self.getToken(miniparser.SEMICOLON, 0)

        def getRuleIndex(self):
            return miniparser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = miniparser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.type_()
            self.state = 98
            self.variableList()
            self.state = 99
            self.match(miniparser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.VariableContext)
            else:
                return self.getTypedRuleContext(miniparser.VariableContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.COMMA)
            else:
                return self.getToken(miniparser.COMMA, i)

        def getRuleIndex(self):
            return miniparser.RULE_variableList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableList" ):
                listener.enterVariableList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableList" ):
                listener.exitVariableList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableList" ):
                return visitor.visitVariableList(self)
            else:
                return visitor.visitChildren(self)




    def variableList(self):

        localctx = miniparser.VariableListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variableList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.variable()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 102
                self.match(miniparser.COMMA)
                self.state = 103
                self.variable()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(miniparser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(miniparser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(miniparser.ExpressionContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = miniparser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(miniparser.IDENTIFIER)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 110
                self.match(miniparser.ASSIGN)
                self.state = 111
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentOperator(self):
            return self.getTypedRuleContext(miniparser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(miniparser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(miniparser.SEMICOLON, 0)

        def IDENTIFIER(self):
            return self.getToken(miniparser.IDENTIFIER, 0)

        def arrayAccess(self):
            return self.getTypedRuleContext(miniparser.ArrayAccessContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = miniparser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 114
                self.match(miniparser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 115
                self.arrayAccess()
                pass


            self.state = 118
            self.assignmentOperator()
            self.state = 119
            self.expression()
            self.state = 120
            self.match(miniparser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(miniparser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(miniparser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(miniparser.MINUS_ASSIGN, 0)

        def MULT_ASSIGN(self):
            return self.getToken(miniparser.MULT_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(miniparser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(miniparser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return miniparser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = miniparser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                self._errHandler.recoverInline(self)
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


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(miniparser.IF, 0)

        def LPAREN(self):
            return self.getToken(miniparser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(miniparser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(miniparser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.StatementContext)
            else:
                return self.getTypedRuleContext(miniparser.StatementContext,i)


        def ELSE(self):
            return self.getToken(miniparser.ELSE, 0)

        def getRuleIndex(self):
            return miniparser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = miniparser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(miniparser.IF)
            self.state = 125
            self.match(miniparser.LPAREN)
            self.state = 126
            self.expression()
            self.state = 127
            self.match(miniparser.RPAREN)
            self.state = 128
            self.statement()
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 129
                self.match(miniparser.ELSE)
                self.state = 130
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(miniparser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(miniparser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(miniparser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(miniparser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(miniparser.StatementContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = miniparser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(miniparser.WHILE)
            self.state = 134
            self.match(miniparser.LPAREN)
            self.state = 135
            self.expression()
            self.state = 136
            self.match(miniparser.RPAREN)
            self.state = 137
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(miniparser.FOR, 0)

        def LPAREN(self):
            return self.getToken(miniparser.LPAREN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.SEMICOLON)
            else:
                return self.getToken(miniparser.SEMICOLON, i)

        def RPAREN(self):
            return self.getToken(miniparser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(miniparser.StatementContext,0)


        def forInit(self):
            return self.getTypedRuleContext(miniparser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(miniparser.ExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(miniparser.ForUpdateContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = miniparser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(miniparser.FOR)
            self.state = 140
            self.match(miniparser.LPAREN)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303939584) != 0):
                self.state = 141
                self.forInit()


            self.state = 144
            self.match(miniparser.SEMICOLON)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1116998273601634304) != 0):
                self.state = 145
                self.expression()


            self.state = 148
            self.match(miniparser.SEMICOLON)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 149
                self.forUpdate()


            self.state = 152
            self.match(miniparser.RPAREN)
            self.state = 153
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarationFor(self):
            return self.getTypedRuleContext(miniparser.VariableDeclarationForContext,0)


        def assignmentNoSemi(self):
            return self.getTypedRuleContext(miniparser.AssignmentNoSemiContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = miniparser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forInit)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.variableDeclarationFor()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.assignmentNoSemi()
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


    class VariableDeclarationForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(miniparser.TypeContext,0)


        def variableList(self):
            return self.getTypedRuleContext(miniparser.VariableListContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_variableDeclarationFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationFor" ):
                listener.enterVariableDeclarationFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationFor" ):
                listener.exitVariableDeclarationFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarationFor" ):
                return visitor.visitVariableDeclarationFor(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarationFor(self):

        localctx = miniparser.VariableDeclarationForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variableDeclarationFor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.type_()
            self.state = 160
            self.variableList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentNoSemiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(miniparser.IDENTIFIER, 0)

        def assignmentOperator(self):
            return self.getTypedRuleContext(miniparser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(miniparser.ExpressionContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_assignmentNoSemi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentNoSemi" ):
                listener.enterAssignmentNoSemi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentNoSemi" ):
                listener.exitAssignmentNoSemi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentNoSemi" ):
                return visitor.visitAssignmentNoSemi(self)
            else:
                return visitor.visitChildren(self)




    def assignmentNoSemi(self):

        localctx = miniparser.AssignmentNoSemiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignmentNoSemi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(miniparser.IDENTIFIER)
            self.state = 163
            self.assignmentOperator()
            self.state = 164
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(miniparser.IDENTIFIER, 0)

        def INCREMENT(self):
            return self.getToken(miniparser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(miniparser.DECREMENT, 0)

        def assignmentNoSemi(self):
            return self.getTypedRuleContext(miniparser.AssignmentNoSemiContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = miniparser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forUpdate)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(miniparser.IDENTIFIER)
                self.state = 167
                self.match(miniparser.INCREMENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(miniparser.IDENTIFIER)
                self.state = 169
                self.match(miniparser.DECREMENT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.assignmentNoSemi()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(miniparser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(miniparser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(miniparser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(miniparser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(miniparser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(miniparser.ParameterListContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = miniparser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.type_()
            self.state = 174
            self.match(miniparser.IDENTIFIER)
            self.state = 175
            self.match(miniparser.LPAREN)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0):
                self.state = 176
                self.parameterList()


            self.state = 179
            self.match(miniparser.RPAREN)
            self.state = 180
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.ParameterContext)
            else:
                return self.getTypedRuleContext(miniparser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.COMMA)
            else:
                return self.getToken(miniparser.COMMA, i)

        def getRuleIndex(self):
            return miniparser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = miniparser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.parameter()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 183
                self.match(miniparser.COMMA)
                self.state = 184
                self.parameter()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(miniparser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(miniparser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return miniparser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = miniparser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.type_()
            self.state = 191
            self.match(miniparser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(miniparser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(miniparser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(miniparser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(miniparser.ArgumentListContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = miniparser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(miniparser.IDENTIFIER)
            self.state = 194
            self.match(miniparser.LPAREN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1116998273601634304) != 0):
                self.state = 195
                self.argumentList()


            self.state = 198
            self.match(miniparser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.ExpressionContext)
            else:
                return self.getTypedRuleContext(miniparser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.COMMA)
            else:
                return self.getToken(miniparser.COMMA, i)

        def getRuleIndex(self):
            return miniparser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = miniparser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.expression()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 201
                self.match(miniparser.COMMA)
                self.state = 202
                self.expression()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(miniparser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(miniparser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(miniparser.ExpressionContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = miniparser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(miniparser.RETURN)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1116998273601634304) != 0):
                self.state = 209
                self.expression()


            self.state = 212
            self.match(miniparser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(miniparser.IDENTIFIER, 0)

        def LBRACKET(self):
            return self.getToken(miniparser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(miniparser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(miniparser.RBRACKET, 0)

        def getRuleIndex(self):
            return miniparser.RULE_arrayAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess" ):
                listener.enterArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess" ):
                listener.exitArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccess" ):
                return visitor.visitArrayAccess(self)
            else:
                return visitor.visitChildren(self)




    def arrayAccess(self):

        localctx = miniparser.ArrayAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arrayAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(miniparser.IDENTIFIER)
            self.state = 215
            self.match(miniparser.LBRACKET)
            self.state = 216
            self.expression()
            self.state = 217
            self.match(miniparser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(miniparser.INT, 0)

        def FLOAT(self):
            return self.getToken(miniparser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(miniparser.DOUBLE, 0)

        def CHAR(self):
            return self.getToken(miniparser.CHAR, 0)

        def BOOL(self):
            return self.getToken(miniparser.BOOL, 0)

        def VOID(self):
            return self.getToken(miniparser.VOID, 0)

        def getRuleIndex(self):
            return miniparser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = miniparser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                self._errHandler.recoverInline(self)
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOr(self):
            return self.getTypedRuleContext(miniparser.LogicalOrContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = miniparser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.logicalOr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.LogicalAndContext)
            else:
                return self.getTypedRuleContext(miniparser.LogicalAndContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.OR)
            else:
                return self.getToken(miniparser.OR, i)

        def getRuleIndex(self):
            return miniparser.RULE_logicalOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOr" ):
                listener.enterLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOr" ):
                listener.exitLogicalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)




    def logicalOr(self):

        localctx = miniparser.LogicalOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_logicalOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.logicalAnd()
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 224
                self.match(miniparser.OR)
                self.state = 225
                self.logicalAnd()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.EqualityContext)
            else:
                return self.getTypedRuleContext(miniparser.EqualityContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.AND)
            else:
                return self.getToken(miniparser.AND, i)

        def getRuleIndex(self):
            return miniparser.RULE_logicalAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)




    def logicalAnd(self):

        localctx = miniparser.LogicalAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_logicalAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.equality()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 232
                self.match(miniparser.AND)
                self.state = 233
                self.equality()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.RelationalContext)
            else:
                return self.getTypedRuleContext(miniparser.RelationalContext,i)


        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.EQUAL)
            else:
                return self.getToken(miniparser.EQUAL, i)

        def NOT_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.NOT_EQUAL)
            else:
                return self.getToken(miniparser.NOT_EQUAL, i)

        def getRuleIndex(self):
            return miniparser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = miniparser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.relational()
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37 or _la==38:
                self.state = 240
                _la = self._input.LA(1)
                if not(_la==37 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 241
                self.relational()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.AdditiveContext)
            else:
                return self.getTypedRuleContext(miniparser.AdditiveContext,i)


        def GREATER(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.GREATER)
            else:
                return self.getToken(miniparser.GREATER, i)

        def LESS(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.LESS)
            else:
                return self.getToken(miniparser.LESS, i)

        def GREATER_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.GREATER_EQUAL)
            else:
                return self.getToken(miniparser.GREATER_EQUAL, i)

        def LESS_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.LESS_EQUAL)
            else:
                return self.getToken(miniparser.LESS_EQUAL, i)

        def getRuleIndex(self):
            return miniparser.RULE_relational

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = miniparser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.additive()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8246337208320) != 0):
                self.state = 248
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8246337208320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 249
                self.additive()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(miniparser.MultiplicativeContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.PLUS)
            else:
                return self.getToken(miniparser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.MINUS)
            else:
                return self.getToken(miniparser.MINUS, i)

        def getRuleIndex(self):
            return miniparser.RULE_additive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)




    def additive(self):

        localctx = miniparser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.multiplicative()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 256
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 257
                self.multiplicative()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniparser.UnaryContext)
            else:
                return self.getTypedRuleContext(miniparser.UnaryContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.MULT)
            else:
                return self.getToken(miniparser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.DIV)
            else:
                return self.getToken(miniparser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.MOD)
            else:
                return self.getToken(miniparser.MOD, i)

        def getRuleIndex(self):
            return miniparser.RULE_multiplicative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative" ):
                listener.enterMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative" ):
                listener.exitMultiplicative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative(self):

        localctx = miniparser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.unary()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0):
                self.state = 264
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 265
                self.unary()
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(miniparser.UnaryContext,0)


        def NOT(self):
            return self.getToken(miniparser.NOT, 0)

        def PLUS(self):
            return self.getToken(miniparser.PLUS, 0)

        def MINUS(self):
            return self.getToken(miniparser.MINUS, 0)

        def postfix(self):
            return self.getTypedRuleContext(miniparser.PostfixContext,0)


        def getRuleIndex(self):
            return miniparser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = miniparser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32, 33, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 35197256990720) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 272
                self.unary()
                pass
            elif token in [22, 23, 46, 55, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.postfix()
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


    class PostfixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(miniparser.PrimaryContext,0)


        def INCREMENT(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.INCREMENT)
            else:
                return self.getToken(miniparser.INCREMENT, i)

        def DECREMENT(self, i:int=None):
            if i is None:
                return self.getTokens(miniparser.DECREMENT)
            else:
                return self.getToken(miniparser.DECREMENT, i)

        def getRuleIndex(self):
            return miniparser.RULE_postfix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix" ):
                listener.enterPostfix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix" ):
                listener.exitPostfix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix" ):
                return visitor.visitPostfix(self)
            else:
                return visitor.visitChildren(self)




    def postfix(self):

        localctx = miniparser.PostfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_postfix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.primary()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 277
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(miniparser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(miniparser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(miniparser.STRING_LITERAL, 0)

        def CHAR_LITERAL(self):
            return self.getToken(miniparser.CHAR_LITERAL, 0)

        def TRUE(self):
            return self.getToken(miniparser.TRUE, 0)

        def FALSE(self):
            return self.getToken(miniparser.FALSE, 0)

        def IDENTIFIER(self):
            return self.getToken(miniparser.IDENTIFIER, 0)

        def functionCall(self):
            return self.getTypedRuleContext(miniparser.FunctionCallContext,0)


        def arrayAccess(self):
            return self.getTypedRuleContext(miniparser.ArrayAccessContext,0)


        def LPAREN(self):
            return self.getToken(miniparser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(miniparser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(miniparser.RPAREN, 0)

        def getRuleIndex(self):
            return miniparser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = miniparser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_primary)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(miniparser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.match(miniparser.FLOAT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 285
                self.match(miniparser.STRING_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 286
                self.match(miniparser.CHAR_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 287
                self.match(miniparser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 288
                self.match(miniparser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 289
                self.match(miniparser.IDENTIFIER)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 290
                self.functionCall()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 291
                self.arrayAccess()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 292
                self.match(miniparser.LPAREN)
                self.state = 293
                self.expression()
                self.state = 294
                self.match(miniparser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





