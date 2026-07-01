# Generated from miniparser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .miniparser import miniparser
else:
    from miniparser import miniparser

# This class defines a complete generic visitor for a parse tree produced by miniparser.

class miniparserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miniparser#program.
    def visitProgram(self, ctx:miniparser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#statement.
    def visitStatement(self, ctx:miniparser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#block.
    def visitBlock(self, ctx:miniparser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:miniparser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#variableList.
    def visitVariableList(self, ctx:miniparser.VariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#variable.
    def visitVariable(self, ctx:miniparser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#assignment.
    def visitAssignment(self, ctx:miniparser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:miniparser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#ifStatement.
    def visitIfStatement(self, ctx:miniparser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#whileStatement.
    def visitWhileStatement(self, ctx:miniparser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#forStatement.
    def visitForStatement(self, ctx:miniparser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#forInit.
    def visitForInit(self, ctx:miniparser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#variableDeclarationFor.
    def visitVariableDeclarationFor(self, ctx:miniparser.VariableDeclarationForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#assignmentNoSemi.
    def visitAssignmentNoSemi(self, ctx:miniparser.AssignmentNoSemiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#forUpdate.
    def visitForUpdate(self, ctx:miniparser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#functionDefinition.
    def visitFunctionDefinition(self, ctx:miniparser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#parameterList.
    def visitParameterList(self, ctx:miniparser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#parameter.
    def visitParameter(self, ctx:miniparser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#functionCall.
    def visitFunctionCall(self, ctx:miniparser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#argumentList.
    def visitArgumentList(self, ctx:miniparser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#returnStatement.
    def visitReturnStatement(self, ctx:miniparser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#arrayAccess.
    def visitArrayAccess(self, ctx:miniparser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#type.
    def visitType(self, ctx:miniparser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#expression.
    def visitExpression(self, ctx:miniparser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#logicalOr.
    def visitLogicalOr(self, ctx:miniparser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#logicalAnd.
    def visitLogicalAnd(self, ctx:miniparser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#equality.
    def visitEquality(self, ctx:miniparser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#relational.
    def visitRelational(self, ctx:miniparser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#additive.
    def visitAdditive(self, ctx:miniparser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#multiplicative.
    def visitMultiplicative(self, ctx:miniparser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#unary.
    def visitUnary(self, ctx:miniparser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#postfix.
    def visitPostfix(self, ctx:miniparser.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#primary.
    def visitPrimary(self, ctx:miniparser.PrimaryContext):
        return self.visitChildren(ctx)



del miniparser