from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
import sys
from antlr4.tree.Tree import TerminalNode
from minilexer import minilexer
from miniparser import miniparser
from semantic import SemanticAnalyzer


# =====================================================
# Clasificación de tokens
# =====================================================

def categoria(token_name):

    keywords = {
        "IF", "ELSE", "WHILE", "FOR", "DO",
        "INT", "FLOAT", "DOUBLE", "CHAR",
        "BOOL", "VOID",
        "RETURN", "BREAK", "CONTINUE",
        "TRUE", "FALSE"
    }

    assignment = {
        "ASSIGN",
        "PLUS_ASSIGN",
        "MINUS_ASSIGN",
        "MULT_ASSIGN",
        "DIV_ASSIGN",
        "MOD_ASSIGN"
    }

    arithmetic = {
        "PLUS",
        "MINUS",
        "MULT",
        "DIV",
        "MOD",
        "INCREMENT",
        "DECREMENT"
    }

    relational = {
        "EQUAL",
        "NOT_EQUAL",
        "GREATER",
        "LESS",
        "GREATER_EQUAL",
        "LESS_EQUAL"
    }

    logical = {
        "AND",
        "OR",
        "NOT"
    }

    delimiters = {
        "LPAREN",
        "RPAREN",
        "LBRACE",
        "RBRACE",
        "LBRACKET",
        "RBRACKET",
        "SEMICOLON",
        "COMMA"
    }

    if token_name in keywords:
        return "KEYWORD"

    elif token_name == "IDENTIFIER":
        return "IDENTIFIER"

    elif token_name in assignment:
        return "ASSIGNMENT_OPERATOR"

    elif token_name in arithmetic:
        return "ARITHMETIC_OPERATOR"

    elif token_name in relational:
        return "RELATIONAL_OPERATOR"

    elif token_name in logical:
        return "LOGICAL_OPERATOR"

    elif token_name in delimiters:
        return "DELIMITER"

    elif token_name in {
        "INTEGER_LITERAL",
        "FLOAT_LITERAL",
        "STRING_LITERAL",
        "CHAR_LITERAL"
    }:
        return "LITERAL"

    elif token_name in {
        "LINE_COMMENT",
        "BLOCK_COMMENT"
    }:
        return "COMMENT"

    elif token_name == "ERROR_CHAR":
        return "LEXICAL_ERROR"

    return token_name


# =====================================================
# Listener de errores sintácticos
# =====================================================

class SyntaxErrorListener(ErrorListener):

    def __init__(self):
        super().__init__()
        self.errores = 0

    def syntaxError(self,
                    recognizer,
                    offendingSymbol,
                    line,
                    column,
                    msg,
                    e):

        self.errores += 1

        print("\n===================================")
        print("ERROR SINTACTICO")
        print("===================================")

        print(f"Linea   : {line}")
        print(f"Columna : {column}")

        if offendingSymbol:
            print(f"Token   : {offendingSymbol.text}")

        print(f"Mensaje : {msg}")


class MyErrorStrategy(DefaultErrorStrategy):

    def reportError(self, recognizer, e):

        print("\nIntentando recuperarse del error...")
        super().reportError(recognizer, e)


# =====================================================
# ARCHIVO DE ENTRADA
# =====================================================

archivo = "input.txt"


# =====================================================
# ANALISIS LEXICO
# =====================================================

print("\n")
print("=" * 60)
print("TABLA DE TOKENS")
print("=" * 60)

entrada = FileStream(archivo, encoding="utf-8")
lexer = minilexer(entrada)

tokens = lexer.getAllTokens()

print(f'{"LEXEMA":25} {"TOKEN"}')
print("-" * 60)

errores_lexicos = 0

for token in tokens:

    nombre = lexer.symbolicNames[token.type]

    if nombre == "ERROR_CHAR":

        errores_lexicos += 1

        print(f'{token.text:25} LEXICAL_ERROR')
        print(f'   -> Error léxico en línea {token.line}, columna {token.column}')

    else:

        print(f'{token.text:25} {categoria(nombre)}')

print("-" * 60)

if errores_lexicos > 0:

    print(f"\nSe encontraron {errores_lexicos} error(es) léxicos.")
    print("El análisis se detuvo.")
    sys.exit(1)

print("No se encontraron errores léxicos.")

# =====================================================
# ARBOL SINTACTICO
# =====================================================



def imprimirArbol(nodo, nivel=0, padre=None, ultimo=True):

    # Construye la sangría
    sangria = ""
    for i in range(nivel - 1):
        sangria += "│   "

    if nivel > 0:
        if ultimo:
            sangria += "└── "
        else:
            sangria += "├── "

    # Nombre del nodo
    if isinstance(nodo, TerminalNode):
        nombre = nodo.getText()
    else:
        nombre = type(nodo).__name__.replace("Context", "")

    # Imprime la relación padre -> hijo
    if padre is None:
        print(nombre)
    else:
        print(f"{sangria}{padre} → {nombre}")

    # Recorrer hijos
    cantidad = nodo.getChildCount()

    for i in range(cantidad):
        hijo = nodo.getChild(i)
        imprimirArbol(
            hijo,
            nivel + 1,
            nombre,
            i == cantidad - 1
        )
# =====================================================
# ANALISIS SINTACTICO
# =====================================================

print("\n")
print("=" * 60)
print("ANALISIS SINTACTICO")
print("=" * 60)

entrada = FileStream(archivo, encoding="utf-8")
lexer = minilexer(entrada)
tokens = CommonTokenStream(lexer)

parser = miniparser(tokens)

listener = SyntaxErrorListener()

parser.removeErrorListeners()
parser.addErrorListener(listener)
parser._errHandler = MyErrorStrategy()

tree = parser.program()

print("\n")
print("=" * 60)
print("ÁRBOL SINTÁCTICO")
print("=" * 60)

imprimirArbol(tree)

if listener.errores > 0:

    print(f"\nSe encontraron {listener.errores} error(es) sintácticos.")
    print("El análisis se detuvo.")
    sys.exit(1)

print("\nNo se encontraron errores sintácticos.")


# =====================================================
# ANALISIS SEMANTICO
# =====================================================

print("\n")
print("=" * 60)
print("ANALISIS SEMANTICO")
print("=" * 60)

semantic = SemanticAnalyzer()

semantic.visit(tree)

semantic.printErrors()

if len(semantic.errors) > 0:

    print("\nEl análisis se detuvo debido a errores semánticos.")
    sys.exit(1)



print("\n========================================")
print("COMPILACION FINALIZADA CORRECTAMENTE")
print("========================================")