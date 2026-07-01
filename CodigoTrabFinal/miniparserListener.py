# Generated from miniparser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .miniparser import miniparser
else:
    from miniparser import miniparser

# This class defines a complete listener for a parse tree produced by miniparser.
class miniparserListener(ParseTreeListener):

    # Enter a parse tree produced by miniparser#program.
    def enterProgram(self, ctx:miniparser.ProgramContext):
        pass

    # Exit a parse tree produced by miniparser#program.
    def exitProgram(self, ctx:miniparser.ProgramContext):
        pass


    # Enter a parse tree produced by miniparser#globalDeclaration.
    def enterGlobalDeclaration(self, ctx:miniparser.GlobalDeclarationContext):
        pass

    # Exit a parse tree produced by miniparser#globalDeclaration.
    def exitGlobalDeclaration(self, ctx:miniparser.GlobalDeclarationContext):
        pass


    # Enter a parse tree produced by miniparser#functionDefinition.
    def enterFunctionDefinition(self, ctx:miniparser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by miniparser#functionDefinition.
    def exitFunctionDefinition(self, ctx:miniparser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by miniparser#parameterList.
    def enterParameterList(self, ctx:miniparser.ParameterListContext):
        pass

    # Exit a parse tree produced by miniparser#parameterList.
    def exitParameterList(self, ctx:miniparser.ParameterListContext):
        pass


    # Enter a parse tree produced by miniparser#parameter.
    def enterParameter(self, ctx:miniparser.ParameterContext):
        pass

    # Exit a parse tree produced by miniparser#parameter.
    def exitParameter(self, ctx:miniparser.ParameterContext):
        pass


    # Enter a parse tree produced by miniparser#type.
    def enterType(self, ctx:miniparser.TypeContext):
        pass

    # Exit a parse tree produced by miniparser#type.
    def exitType(self, ctx:miniparser.TypeContext):
        pass


    # Enter a parse tree produced by miniparser#block.
    def enterBlock(self, ctx:miniparser.BlockContext):
        pass

    # Exit a parse tree produced by miniparser#block.
    def exitBlock(self, ctx:miniparser.BlockContext):
        pass


    # Enter a parse tree produced by miniparser#statement.
    def enterStatement(self, ctx:miniparser.StatementContext):
        pass

    # Exit a parse tree produced by miniparser#statement.
    def exitStatement(self, ctx:miniparser.StatementContext):
        pass


    # Enter a parse tree produced by miniparser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:miniparser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by miniparser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:miniparser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by miniparser#variableList.
    def enterVariableList(self, ctx:miniparser.VariableListContext):
        pass

    # Exit a parse tree produced by miniparser#variableList.
    def exitVariableList(self, ctx:miniparser.VariableListContext):
        pass


    # Enter a parse tree produced by miniparser#variable.
    def enterVariable(self, ctx:miniparser.VariableContext):
        pass

    # Exit a parse tree produced by miniparser#variable.
    def exitVariable(self, ctx:miniparser.VariableContext):
        pass


    # Enter a parse tree produced by miniparser#assignment.
    def enterAssignment(self, ctx:miniparser.AssignmentContext):
        pass

    # Exit a parse tree produced by miniparser#assignment.
    def exitAssignment(self, ctx:miniparser.AssignmentContext):
        pass


    # Enter a parse tree produced by miniparser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:miniparser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by miniparser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:miniparser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by miniparser#incrementStatement.
    def enterIncrementStatement(self, ctx:miniparser.IncrementStatementContext):
        pass

    # Exit a parse tree produced by miniparser#incrementStatement.
    def exitIncrementStatement(self, ctx:miniparser.IncrementStatementContext):
        pass


    # Enter a parse tree produced by miniparser#decrementStatement.
    def enterDecrementStatement(self, ctx:miniparser.DecrementStatementContext):
        pass

    # Exit a parse tree produced by miniparser#decrementStatement.
    def exitDecrementStatement(self, ctx:miniparser.DecrementStatementContext):
        pass


    # Enter a parse tree produced by miniparser#ifStatement.
    def enterIfStatement(self, ctx:miniparser.IfStatementContext):
        pass

    # Exit a parse tree produced by miniparser#ifStatement.
    def exitIfStatement(self, ctx:miniparser.IfStatementContext):
        pass


    # Enter a parse tree produced by miniparser#whileStatement.
    def enterWhileStatement(self, ctx:miniparser.WhileStatementContext):
        pass

    # Exit a parse tree produced by miniparser#whileStatement.
    def exitWhileStatement(self, ctx:miniparser.WhileStatementContext):
        pass


    # Enter a parse tree produced by miniparser#forStatement.
    def enterForStatement(self, ctx:miniparser.ForStatementContext):
        pass

    # Exit a parse tree produced by miniparser#forStatement.
    def exitForStatement(self, ctx:miniparser.ForStatementContext):
        pass


    # Enter a parse tree produced by miniparser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:miniparser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by miniparser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:miniparser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by miniparser#forInit.
    def enterForInit(self, ctx:miniparser.ForInitContext):
        pass

    # Exit a parse tree produced by miniparser#forInit.
    def exitForInit(self, ctx:miniparser.ForInitContext):
        pass


    # Enter a parse tree produced by miniparser#variableDeclarationFor.
    def enterVariableDeclarationFor(self, ctx:miniparser.VariableDeclarationForContext):
        pass

    # Exit a parse tree produced by miniparser#variableDeclarationFor.
    def exitVariableDeclarationFor(self, ctx:miniparser.VariableDeclarationForContext):
        pass


    # Enter a parse tree produced by miniparser#assignmentNoSemi.
    def enterAssignmentNoSemi(self, ctx:miniparser.AssignmentNoSemiContext):
        pass

    # Exit a parse tree produced by miniparser#assignmentNoSemi.
    def exitAssignmentNoSemi(self, ctx:miniparser.AssignmentNoSemiContext):
        pass


    # Enter a parse tree produced by miniparser#forUpdate.
    def enterForUpdate(self, ctx:miniparser.ForUpdateContext):
        pass

    # Exit a parse tree produced by miniparser#forUpdate.
    def exitForUpdate(self, ctx:miniparser.ForUpdateContext):
        pass


    # Enter a parse tree produced by miniparser#switchStatement.
    def enterSwitchStatement(self, ctx:miniparser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by miniparser#switchStatement.
    def exitSwitchStatement(self, ctx:miniparser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by miniparser#caseStatement.
    def enterCaseStatement(self, ctx:miniparser.CaseStatementContext):
        pass

    # Exit a parse tree produced by miniparser#caseStatement.
    def exitCaseStatement(self, ctx:miniparser.CaseStatementContext):
        pass


    # Enter a parse tree produced by miniparser#defaultStatement.
    def enterDefaultStatement(self, ctx:miniparser.DefaultStatementContext):
        pass

    # Exit a parse tree produced by miniparser#defaultStatement.
    def exitDefaultStatement(self, ctx:miniparser.DefaultStatementContext):
        pass


    # Enter a parse tree produced by miniparser#returnStatement.
    def enterReturnStatement(self, ctx:miniparser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by miniparser#returnStatement.
    def exitReturnStatement(self, ctx:miniparser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by miniparser#breakStatement.
    def enterBreakStatement(self, ctx:miniparser.BreakStatementContext):
        pass

    # Exit a parse tree produced by miniparser#breakStatement.
    def exitBreakStatement(self, ctx:miniparser.BreakStatementContext):
        pass


    # Enter a parse tree produced by miniparser#continueStatement.
    def enterContinueStatement(self, ctx:miniparser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by miniparser#continueStatement.
    def exitContinueStatement(self, ctx:miniparser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by miniparser#literal.
    def enterLiteral(self, ctx:miniparser.LiteralContext):
        pass

    # Exit a parse tree produced by miniparser#literal.
    def exitLiteral(self, ctx:miniparser.LiteralContext):
        pass


    # Enter a parse tree produced by miniparser#expression.
    def enterExpression(self, ctx:miniparser.ExpressionContext):
        pass

    # Exit a parse tree produced by miniparser#expression.
    def exitExpression(self, ctx:miniparser.ExpressionContext):
        pass


    # Enter a parse tree produced by miniparser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:miniparser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by miniparser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:miniparser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by miniparser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:miniparser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by miniparser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:miniparser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by miniparser#equalityExpression.
    def enterEqualityExpression(self, ctx:miniparser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by miniparser#equalityExpression.
    def exitEqualityExpression(self, ctx:miniparser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by miniparser#relationalExpression.
    def enterRelationalExpression(self, ctx:miniparser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by miniparser#relationalExpression.
    def exitRelationalExpression(self, ctx:miniparser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by miniparser#additiveExpression.
    def enterAdditiveExpression(self, ctx:miniparser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by miniparser#additiveExpression.
    def exitAdditiveExpression(self, ctx:miniparser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by miniparser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:miniparser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by miniparser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:miniparser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by miniparser#unaryExpression.
    def enterUnaryExpression(self, ctx:miniparser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by miniparser#unaryExpression.
    def exitUnaryExpression(self, ctx:miniparser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by miniparser#postfixExpression.
    def enterPostfixExpression(self, ctx:miniparser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by miniparser#postfixExpression.
    def exitPostfixExpression(self, ctx:miniparser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by miniparser#primaryExpression.
    def enterPrimaryExpression(self, ctx:miniparser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by miniparser#primaryExpression.
    def exitPrimaryExpression(self, ctx:miniparser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by miniparser#functionCall.
    def enterFunctionCall(self, ctx:miniparser.FunctionCallContext):
        pass

    # Exit a parse tree produced by miniparser#functionCall.
    def exitFunctionCall(self, ctx:miniparser.FunctionCallContext):
        pass


    # Enter a parse tree produced by miniparser#printfStatement.
    def enterPrintfStatement(self, ctx:miniparser.PrintfStatementContext):
        pass

    # Exit a parse tree produced by miniparser#printfStatement.
    def exitPrintfStatement(self, ctx:miniparser.PrintfStatementContext):
        pass


    # Enter a parse tree produced by miniparser#scanfStatement.
    def enterScanfStatement(self, ctx:miniparser.ScanfStatementContext):
        pass

    # Exit a parse tree produced by miniparser#scanfStatement.
    def exitScanfStatement(self, ctx:miniparser.ScanfStatementContext):
        pass


    # Enter a parse tree produced by miniparser#argumentList.
    def enterArgumentList(self, ctx:miniparser.ArgumentListContext):
        pass

    # Exit a parse tree produced by miniparser#argumentList.
    def exitArgumentList(self, ctx:miniparser.ArgumentListContext):
        pass


    # Enter a parse tree produced by miniparser#printfArguments.
    def enterPrintfArguments(self, ctx:miniparser.PrintfArgumentsContext):
        pass

    # Exit a parse tree produced by miniparser#printfArguments.
    def exitPrintfArguments(self, ctx:miniparser.PrintfArgumentsContext):
        pass


    # Enter a parse tree produced by miniparser#scanfArguments.
    def enterScanfArguments(self, ctx:miniparser.ScanfArgumentsContext):
        pass

    # Exit a parse tree produced by miniparser#scanfArguments.
    def exitScanfArguments(self, ctx:miniparser.ScanfArgumentsContext):
        pass


    # Enter a parse tree produced by miniparser#scanfArgument.
    def enterScanfArgument(self, ctx:miniparser.ScanfArgumentContext):
        pass

    # Exit a parse tree produced by miniparser#scanfArgument.
    def exitScanfArgument(self, ctx:miniparser.ScanfArgumentContext):
        pass


    # Enter a parse tree produced by miniparser#arrayAccess.
    def enterArrayAccess(self, ctx:miniparser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by miniparser#arrayAccess.
    def exitArrayAccess(self, ctx:miniparser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by miniparser#sizeofExpression.
    def enterSizeofExpression(self, ctx:miniparser.SizeofExpressionContext):
        pass

    # Exit a parse tree produced by miniparser#sizeofExpression.
    def exitSizeofExpression(self, ctx:miniparser.SizeofExpressionContext):
        pass



del miniparser