parser grammar miniparser;

options {
    tokenVocab = minilexer;
}

// ====================================================
// PROGRAMA
// ====================================================

program
    : statement* EOF
    ;

// ====================================================
// STATEMENTS
// ====================================================

statement
    : variableDeclaration
    | assignment
    | ifStatement
    | whileStatement
    | forStatement
    | functionDefinition
    | functionCall SEMICOLON
    | returnStatement
    | block
    | SEMICOLON
    ;

// ====================================================
// BLOQUE
// ====================================================

block
    : LBRACE statement* RBRACE
    ;

// ====================================================
// VARIABLES
// ====================================================

variableDeclaration
    : type variableList SEMICOLON
    ;

variableList
    : variable (COMMA variable)*
    ;

variable
    : IDENTIFIER (ASSIGN expression)?
    ;

// ====================================================
// ASIGNACIÓN
// ====================================================

assignment
    : (IDENTIFIER | arrayAccess)
      assignmentOperator
      expression
      SEMICOLON
    ;

assignmentOperator
    : ASSIGN
    | PLUS_ASSIGN
    | MINUS_ASSIGN
    | MULT_ASSIGN
    | DIV_ASSIGN
    | MOD_ASSIGN
    ;

// ====================================================
// IF
// ====================================================

ifStatement
    : IF LPAREN expression RPAREN statement (ELSE statement)?
    ;

// ====================================================
// WHILE
// ====================================================

whileStatement
    : WHILE LPAREN expression RPAREN statement
    ;

// ====================================================
// FOR (CORREGIDO Y ESTABLE)
// ====================================================

forStatement
    : FOR LPAREN
        forInit? SEMICOLON
        expression? SEMICOLON
        forUpdate?
      RPAREN
      statement
    ;

// INIT del FOR
forInit
    : variableDeclarationFor
    | assignmentNoSemi
    ;

// declaración sin punto y coma
variableDeclarationFor
    : type variableList
    ;

// asignación sin ;
assignmentNoSemi
    : IDENTIFIER assignmentOperator expression
    ;

// UPDATE del FOR (CLAVE)
forUpdate
    : IDENTIFIER INCREMENT
    | IDENTIFIER DECREMENT
    | assignmentNoSemi
    ;

// ====================================================
// FUNCIONES
// ====================================================

functionDefinition
    : type IDENTIFIER LPAREN parameterList? RPAREN block
    ;

parameterList
    : parameter (COMMA parameter)*
    ;

parameter
    : type IDENTIFIER
    ;

// ====================================================
// FUNCIONES CALL
// ====================================================

functionCall
    : IDENTIFIER LPAREN argumentList? RPAREN
    ;

argumentList
    : expression (COMMA expression)*
    ;

// ====================================================
// RETURN
// ====================================================

returnStatement
    : RETURN expression? SEMICOLON
    ;

// ====================================================
// ARRAY
// ====================================================

arrayAccess
    : IDENTIFIER LBRACKET expression RBRACKET
    ;

// ====================================================
// TYPES
// ====================================================

type
    : INT
    | FLOAT
    | DOUBLE
    | CHAR
    | BOOL
    | VOID
    ;

// ====================================================
// EXPRESSIONS
// ====================================================

expression
    : logicalOr
    ;

logicalOr
    : logicalAnd (OR logicalAnd)*
    ;

logicalAnd
    : equality (AND equality)*
    ;

equality
    : relational ((EQUAL | NOT_EQUAL) relational)*
    ;

relational
    : additive ((GREATER | LESS | GREATER_EQUAL | LESS_EQUAL) additive)*
    ;

additive
    : multiplicative ((PLUS | MINUS) multiplicative)*
    ;

multiplicative
    : unary ((MULT | DIV | MOD) unary)*
    ;

unary
    : (NOT | PLUS | MINUS) unary
    | postfix
    ;

postfix
    : primary (INCREMENT | DECREMENT)*
    ;

primary
    : INTEGER_LITERAL
    | FLOAT_LITERAL
    | STRING_LITERAL
    | CHAR_LITERAL
    | TRUE
    | FALSE
    | IDENTIFIER
    | functionCall
    | arrayAccess
    | LPAREN expression RPAREN
    ;