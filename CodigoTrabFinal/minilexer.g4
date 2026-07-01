lexer grammar minilexer;
//====================================================
// PALABRAS RESERVADAS (KEYWORDS)
//====================================================

IF          : 'if';
ELSE        : 'else';
WHILE       : 'while';
FOR         : 'for';
DO          : 'do';
SWITCH      : 'switch';
CASE        : 'case';
DEFAULT     : 'default';
CONST       : 'const';
PRINTF      : 'printf';
SCANF       : 'scanf';
SIZEOF      : 'sizeof';

INT         : 'int';
FLOAT       : 'float';
DOUBLE      : 'double';
CHAR        : 'char';
BOOL        : 'bool';
VOID        : 'void';

RETURN      : 'return';
BREAK       : 'break';
CONTINUE    : 'continue';

TRUE        : 'true';
FALSE       : 'false';

//====================================================
// OPERADORES DE ASIGNACIÓN
//====================================================

PLUS_ASSIGN     : '+=';
MINUS_ASSIGN    : '-=';
MULT_ASSIGN     : '*=';
DIV_ASSIGN      : '/=';
MOD_ASSIGN      : '%=';

ASSIGN          : '=';

//====================================================
// OPERADORES ARITMÉTICOS
//====================================================

INCREMENT       : '++';
DECREMENT       : '--';

PLUS            : '+';
MINUS           : '-';
MULT            : '*';
DIV             : '/';
MOD             : '%';

//====================================================
// OPERADORES RELACIONALES
//====================================================

EQUAL           : '==';
NOT_EQUAL       : '!=';

GREATER_EQUAL   : '>=';
LESS_EQUAL      : '<=';

GREATER         : '>';
LESS            : '<';

//====================================================
// OPERADORES LÓGICOS
//====================================================

AND             : '&&';
OR              : '||';
NOT             : '!';

//====================================================
// DELIMITADORES
//====================================================

LPAREN          : '(';
RPAREN          : ')';

LBRACE          : '{';
RBRACE          : '}';

LBRACKET        : '[';
RBRACKET        : ']';

SEMICOLON       : ';';
COMMA           : ',';
COLON           : ':';
//====================================================
// LITERALES
//====================================================

FLOAT_LITERAL
    : [0-9]+ '.' [0-9]+
    ;

INTEGER_LITERAL
    : [0-9]+
    ;

STRING_LITERAL
    : '"' ( '\\' . | ~["\\] )* '"'
    ;

CHAR_LITERAL
    : '\'' ( '\\' . | ~['\\] ) '\''
    ;

//====================================================
// IDENTIFICADORES
//====================================================

IDENTIFIER
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

//====================================================
// COMENTARIOS
//====================================================

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

//====================================================
// ESPACIOS EN BLANCO
//====================================================

WHITESPACE
    : [ \t\r\n]+ -> skip
    ;

//====================================================
// ERROR LÉXICO
//====================================================

ERROR_CHAR
    : .
    ;