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


    # Visit a parse tree produced by miniparser#globalDeclaration.
    def visitGlobalDeclaration(self, ctx:miniparser.GlobalDeclarationContext):
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


    # Visit a parse tree produced by miniparser#type.
    def visitType(self, ctx:miniparser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#block.
    def visitBlock(self, ctx:miniparser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#statement.
    def visitStatement(self, ctx:miniparser.StatementContext):
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


    # Visit a parse tree produced by miniparser#incrementStatement.
    def visitIncrementStatement(self, ctx:miniparser.IncrementStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#decrementStatement.
    def visitDecrementStatement(self, ctx:miniparser.DecrementStatementContext):
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


    # Visit a parse tree produced by miniparser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:miniparser.DoWhileStatementContext):
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


    # Visit a parse tree produced by miniparser#switchStatement.
    def visitSwitchStatement(self, ctx:miniparser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#caseStatement.
    def visitCaseStatement(self, ctx:miniparser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#defaultStatement.
    def visitDefaultStatement(self, ctx:miniparser.DefaultStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#returnStatement.
    def visitReturnStatement(self, ctx:miniparser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#breakStatement.
    def visitBreakStatement(self, ctx:miniparser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#continueStatement.
    def visitContinueStatement(self, ctx:miniparser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#literal.
    def visitLiteral(self, ctx:miniparser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#expression.
    def visitExpression(self, ctx:miniparser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:miniparser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:miniparser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#equalityExpression.
    def visitEqualityExpression(self, ctx:miniparser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#relationalExpression.
    def visitRelationalExpression(self, ctx:miniparser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#additiveExpression.
    def visitAdditiveExpression(self, ctx:miniparser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:miniparser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#unaryExpression.
    def visitUnaryExpression(self, ctx:miniparser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#postfixExpression.
    def visitPostfixExpression(self, ctx:miniparser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#primaryExpression.
    def visitPrimaryExpression(self, ctx:miniparser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#functionCall.
    def visitFunctionCall(self, ctx:miniparser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#printfStatement.
    def visitPrintfStatement(self, ctx:miniparser.PrintfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#scanfStatement.
    def visitScanfStatement(self, ctx:miniparser.ScanfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#argumentList.
    def visitArgumentList(self, ctx:miniparser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#printfArguments.
    def visitPrintfArguments(self, ctx:miniparser.PrintfArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#scanfArguments.
    def visitScanfArguments(self, ctx:miniparser.ScanfArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#scanfArgument.
    def visitScanfArgument(self, ctx:miniparser.ScanfArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#arrayAccess.
    def visitArrayAccess(self, ctx:miniparser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniparser#sizeofExpression.
    def visitSizeofExpression(self, ctx:miniparser.SizeofExpressionContext):
        return self.visitChildren(ctx)



del miniparser