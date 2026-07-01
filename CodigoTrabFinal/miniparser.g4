grammar miniparser;

// Regla Inicial
program : (globalDeclaration | functionDefinition)* EOF ;

globalDeclaration : (CONST)? type_ variableList SEMICOLON ;

functionDefinition : type_ IDENTIFIER LPAREN parameterList? RPAREN block ;

parameterList : parameter (COMMA parameter)* ;
parameter : type_ IDENTIFIER ;

type_ : INT | FLOAT | DOUBLE | CHAR | BOOL | VOID ;

block : LBRACE statement* RBRACE ;

statement
    : variableDeclaration
    | assignment
    | incrementStatement
    | decrementStatement
    | ifStatement
    | whileStatement
    | forStatement
    | doWhileStatement
    | switchStatement
    | returnStatement
    | breakStatement
    | continueStatement
    | printfStatement
    | scanfStatement
    | block
    ;

variableDeclaration : type_ variableList SEMICOLON ;
variableList : variable (COMMA variable)* ;
variable : IDENTIFIER (LBRACKET INTEGER_LITERAL RBRACKET)? (ASSIGN expression)? ;

assignment : (IDENTIFIER | arrayAccess) assignmentOperator expression SEMICOLON ;
assignmentOperator : ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN ;

incrementStatement : IDENTIFIER INCREMENT SEMICOLON ;
decrementStatement : IDENTIFIER DECREMENT SEMICOLON ;

ifStatement : IF LPAREN expression RPAREN statement (ELSE statement)? ;
whileStatement : WHILE LPAREN expression RPAREN statement ;
doWhileStatement : DO statement WHILE LPAREN expression RPAREN SEMICOLON ;

forStatement : FOR LPAREN forInit? SEMICOLON expression? SEMICOLON forUpdate? RPAREN statement ;
forInit : variableDeclarationFor | assignmentNoSemi ;
variableDeclarationFor : type_ IDENTIFIER ASSIGN expression ;
assignmentNoSemi : IDENTIFIER ASSIGN expression ;
forUpdate : IDENTIFIER (INCREMENT | DECREMENT | assignmentOperator expression) ;

switchStatement : SWITCH LPAREN expression RPAREN LBRACE caseStatement* defaultStatement? RBRACE ;
caseStatement : CASE literal COLON statement* ;
defaultStatement : DEFAULT COLON statement* ;

returnStatement : RETURN expression? SEMICOLON ;
breakStatement : BREAK SEMICOLON ;
continueStatement : CONTINUE SEMICOLON ;

literal : INTEGER_LITERAL | FLOAT_LITERAL | STRING_LITERAL | CHAR_LITERAL | TRUE | FALSE ;

expression : logicalOrExpression ;
logicalOrExpression : logicalAndExpression (OR logicalAndExpression)* ;
logicalAndExpression : equalityExpression (AND equalityExpression)* ;
equalityExpression : relationalExpression ((EQUAL | NOT_EQUAL) relationalExpression)* ;
relationalExpression : additiveExpression ((GREATER | LESS | GREATER_EQUAL | LESS_EQUAL) additiveExpression)* ;
additiveExpression : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)* ;
multiplicativeExpression : unaryExpression ((MULT | DIV | MOD) unaryExpression)* ;
unaryExpression : NOT unaryExpression | MINUS unaryExpression | postfixExpression ;
postfixExpression : primaryExpression ;

primaryExpression
    : functionCall
    | arrayAccess
    | literal
    | IDENTIFIER
    | LPAREN expression RPAREN
    | sizeofExpression
    ;

functionCall : IDENTIFIER LPAREN argumentList? RPAREN ;
printfStatement : PRINTF LPAREN printfArguments? RPAREN SEMICOLON ;
scanfStatement : SCANF LPAREN scanfArguments RPAREN SEMICOLON ;

argumentList : expression (COMMA expression)* ;
printfArguments : expression (COMMA expression)* ;
scanfArguments : expression (COMMA scanfArgument)* ;
scanfArgument : IDENTIFIER | arrayAccess ;

arrayAccess : IDENTIFIER LBRACKET expression RBRACKET ;
sizeofExpression : SIZEOF LPAREN (type_ | expression) RPAREN ;

// TOKENS LÉXICOS
IF : 'if' ;
ELSE : 'else' ;
WHILE : 'while' ;
FOR : 'for' ;
DO : 'do' ;
SWITCH : 'switch' ;
CASE : 'case' ;
DEFAULT : 'default' ;
CONST : 'const' ;
PRINTF : 'printf' ;
SCANF : 'scanf' ;
SIZEOF : 'sizeof' ;
INT : 'int' ;
FLOAT : 'float' ;
DOUBLE : 'double' ;
CHAR : 'char' ;
BOOL : 'bool' ;
VOID : 'void' ;
RETURN : 'return' ;
BREAK : 'break' ;
CONTINUE : 'continue' ;
TRUE : 'true' ;
FALSE : 'false' ;

PLUS_ASSIGN : '+=' ;
MINUS_ASSIGN : '-=' ;
MULT_ASSIGN : '*=' ;
DIV_ASSIGN : '/=' ;
MOD_ASSIGN : '%=' ;
ASSIGN : '=' ;
INCREMENT : '++' ;
DECREMENT : '--' ;
PLUS : '+' ;
MINUS : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
EQUAL : '==' ;
NOT_EQUAL : '!=' ;
GREATER_EQUAL : '>=' ;
LESS_EQUAL : '<=' ;
GREATER : '>' ;
LESS : '<' ;
AND : '&&' ;
OR : '||' ;
NOT : '!' ;

LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LBRACKET : '[' ;
RBRACKET : ']' ;
SEMICOLON : ';' ;
COMMA : ',' ;
COLON : ':' ;

FLOAT_LITERAL : [0-9]+ '.' [0-9]+ ;
INTEGER_LITERAL : [0-9]+ ;
STRING_LITERAL : '"' .*? '"' ;
CHAR_LITERAL : '\'' . '\'' ;
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]* ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
WHITESPACE : [ \t\r\n]+ -> skip ;
ERROR_CHAR : . ;