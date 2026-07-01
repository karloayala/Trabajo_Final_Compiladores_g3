import sys
from antlr4 import *
from antlr4.tree.Trees import Trees 
from antlr4.error.ErrorListener import ErrorListener
from miniparser import miniparser
# Aseguramos nombres de lexer estables basados en los tokens importados
try:
    from minilexer import minilexer
except ImportError:
    from miniparser import miniparser as minilexer 

from semantic import SemanticAnalyzer

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Línea {line}:{column} -> {msg}")

def print_pretty_tree(tree, parser, prefix="", is_last=True):
    """
    Imprime el árbol sintáctico con líneas estructuradas garantizadas.
    """
    # 1. Obtener el nombre del nodo de forma segura
    if hasattr(tree, 'getRuleIndex'):
        node_text = parser.ruleNames[tree.getRuleIndex()]
    else:
        node_text = str(tree)
    
    # 2. Colapsar cascadas de expresiones con un solo hijo para limpiar la vista
    while tree.getChildCount() == 1 and hasattr(tree.getChild(0), 'getRuleIndex'):
        tree = tree.getChild(0)
        node_text = parser.ruleNames[tree.getRuleIndex()]

    # 3. Construir de forma explícita el marcador visual
    if not prefix:
        marker = ""
    else:
        marker = "└── " if is_last else "├── "
        
    print(f"{prefix}{marker}{node_text}")
    
    # 4. Calcular el prefijo que se pasará obligatoriamente a los hijos
    if not prefix:
        next_prefix = ""
    else:
        next_prefix = prefix + ("    " if is_last else "│   ")
        
    # 5. Llamada recursiva pasando SIEMPRE el prefijo calculado
    child_count = tree.getChildCount()
    for i in range(child_count):
        child = tree.getChild(i)
        is_child_last = (i == child_count - 1)
        
        # Corrección crucial: se pasa el prefijo correcto según el nivel actual
        child_prefix = next_prefix if prefix else ("    " if is_last else "│   ")
        
        print_pretty_tree(child, parser, child_prefix, is_child_last)


def main():
    # Leer el archivo de entrada
    input_file = "input.txt"
    try:
        input_stream = FileStream(input_file, encoding='utf-8')
    except IOError:
        print(f"Error: No se pudo abrir el archivo '{input_file}'")
        return

    # 1. Análisis Léxico
    lexer = miniparser(input_stream) if 'minilexer' not in sys.modules else minilexer(input_stream)
    lexer_error_listener = CustomErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_error_listener)

    stream = CommonTokenStream(lexer)
    
    # 2. Análisis Sintáctico
    parser = miniparser(stream)
    parser_error_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_error_listener)

    tree = parser.program()
    
    # Imprimir el árbol con líneas de progreso conectoras
    print("====================================")
    print("ÁRBOL SINTÁCTICO GENERADO")
    print("====================================")
    print_pretty_tree(tree, parser)
    print("====================================\n")

    # Reportar Errores Léxicos y Sintácticos
    print("====================================")
    print("ANÁLISIS LÉXICO Y SINTÁCTICO")
    print("====================================")
    
    if lexer_error_listener.errors:
        print("Errores Léxicos encontrados:")
        for err in lexer_error_listener.errors:
            print(err)
    else:
        print("Análisis Léxico finalizado sin errores críticos.")

    if parser_error_listener.errors:
        print("\nErrores Sintácticos encontrados:")
        for err in parser_error_listener.errors:
            print(err)
    else:
        print("Análisis Sintáctico finalizado con éxito.")

    # 3. Análisis Semántico (Solo corre si la sintaxis básica no está totalmente rota)
    analyzer = SemanticAnalyzer()
    analyzer.visit(tree)
    analyzer.printErrors()

if __name__ == '__main__':
    main()