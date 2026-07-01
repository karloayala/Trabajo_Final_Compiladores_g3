// Generated from c:/Users/eicek/Downloads/lexer (2)/lexer/miniparser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class miniparser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IF=1, ELSE=2, WHILE=3, FOR=4, DO=5, SWITCH=6, CASE=7, DEFAULT=8, CONST=9, 
		PRINTF=10, SCANF=11, SIZEOF=12, INT=13, FLOAT=14, DOUBLE=15, CHAR=16, 
		BOOL=17, VOID=18, RETURN=19, BREAK=20, CONTINUE=21, TRUE=22, FALSE=23, 
		PLUS_ASSIGN=24, MINUS_ASSIGN=25, MULT_ASSIGN=26, DIV_ASSIGN=27, MOD_ASSIGN=28, 
		ASSIGN=29, INCREMENT=30, DECREMENT=31, PLUS=32, MINUS=33, MULT=34, DIV=35, 
		MOD=36, EQUAL=37, NOT_EQUAL=38, GREATER_EQUAL=39, LESS_EQUAL=40, GREATER=41, 
		LESS=42, AND=43, OR=44, NOT=45, LPAREN=46, RPAREN=47, LBRACE=48, RBRACE=49, 
		LBRACKET=50, RBRACKET=51, SEMICOLON=52, COMMA=53, COLON=54, FLOAT_LITERAL=55, 
		INTEGER_LITERAL=56, STRING_LITERAL=57, CHAR_LITERAL=58, IDENTIFIER=59, 
		LINE_COMMENT=60, BLOCK_COMMENT=61, WHITESPACE=62, ERROR_CHAR=63;
	public static final int
		RULE_program = 0, RULE_globalDeclaration = 1, RULE_functionDefinition = 2, 
		RULE_parameterList = 3, RULE_parameter = 4, RULE_type = 5, RULE_block = 6, 
		RULE_statement = 7, RULE_variableDeclaration = 8, RULE_variableList = 9, 
		RULE_variable = 10, RULE_assignment = 11, RULE_assignmentOperator = 12, 
		RULE_incrementStatement = 13, RULE_decrementStatement = 14, RULE_ifStatement = 15, 
		RULE_whileStatement = 16, RULE_forStatement = 17, RULE_doWhileStatement = 18, 
		RULE_forInit = 19, RULE_variableDeclarationFor = 20, RULE_assignmentNoSemi = 21, 
		RULE_forUpdate = 22, RULE_switchStatement = 23, RULE_caseStatement = 24, 
		RULE_defaultStatement = 25, RULE_returnStatement = 26, RULE_breakStatement = 27, 
		RULE_continueStatement = 28, RULE_literal = 29, RULE_expression = 30, 
		RULE_logicalOrExpression = 31, RULE_logicalAndExpression = 32, RULE_equalityExpression = 33, 
		RULE_relationalExpression = 34, RULE_additiveExpression = 35, RULE_multiplicativeExpression = 36, 
		RULE_unaryExpression = 37, RULE_postfixExpression = 38, RULE_primaryExpression = 39, 
		RULE_functionCall = 40, RULE_printfStatement = 41, RULE_scanfStatement = 42, 
		RULE_argumentList = 43, RULE_printfArguments = 44, RULE_scanfArguments = 45, 
		RULE_scanfArgument = 46, RULE_arrayAccess = 47, RULE_sizeofExpression = 48;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "globalDeclaration", "functionDefinition", "parameterList", 
			"parameter", "type", "block", "statement", "variableDeclaration", "variableList", 
			"variable", "assignment", "assignmentOperator", "incrementStatement", 
			"decrementStatement", "ifStatement", "whileStatement", "forStatement", 
			"doWhileStatement", "forInit", "variableDeclarationFor", "assignmentNoSemi", 
			"forUpdate", "switchStatement", "caseStatement", "defaultStatement", 
			"returnStatement", "breakStatement", "continueStatement", "literal", 
			"expression", "logicalOrExpression", "logicalAndExpression", "equalityExpression", 
			"relationalExpression", "additiveExpression", "multiplicativeExpression", 
			"unaryExpression", "postfixExpression", "primaryExpression", "functionCall", 
			"printfStatement", "scanfStatement", "argumentList", "printfArguments", 
			"scanfArguments", "scanfArgument", "arrayAccess", "sizeofExpression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'else'", "'while'", "'for'", "'do'", "'switch'", "'case'", 
			"'default'", "'const'", "'printf'", "'scanf'", "'sizeof'", "'int'", "'float'", 
			"'double'", "'char'", "'bool'", "'void'", "'return'", "'break'", "'continue'", 
			"'true'", "'false'", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", "'++'", 
			"'--'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'>='", "'<='", 
			"'>'", "'<'", "'&&'", "'||'", "'!'", "'('", "')'", "'{'", "'}'", "'['", 
			"']'", "';'", "','", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IF", "ELSE", "WHILE", "FOR", "DO", "SWITCH", "CASE", "DEFAULT", 
			"CONST", "PRINTF", "SCANF", "SIZEOF", "INT", "FLOAT", "DOUBLE", "CHAR", 
			"BOOL", "VOID", "RETURN", "BREAK", "CONTINUE", "TRUE", "FALSE", "PLUS_ASSIGN", 
			"MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "ASSIGN", 
			"INCREMENT", "DECREMENT", "PLUS", "MINUS", "MULT", "DIV", "MOD", "EQUAL", 
			"NOT_EQUAL", "GREATER_EQUAL", "LESS_EQUAL", "GREATER", "LESS", "AND", 
			"OR", "NOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
			"SEMICOLON", "COMMA", "COLON", "FLOAT_LITERAL", "INTEGER_LITERAL", "STRING_LITERAL", 
			"CHAR_LITERAL", "IDENTIFIER", "LINE_COMMENT", "BLOCK_COMMENT", "WHITESPACE", 
			"ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "miniparser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public miniparser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(miniparser.EOF, 0); }
		public List<FunctionDefinitionContext> functionDefinition() {
			return getRuleContexts(FunctionDefinitionContext.class);
		}
		public FunctionDefinitionContext functionDefinition(int i) {
			return getRuleContext(FunctionDefinitionContext.class,i);
		}
		public List<GlobalDeclarationContext> globalDeclaration() {
			return getRuleContexts(GlobalDeclarationContext.class);
		}
		public GlobalDeclarationContext globalDeclaration(int i) {
			return getRuleContext(GlobalDeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 516608L) != 0)) {
				{
				setState(100);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(98);
					functionDefinition();
					}
					break;
				case 2:
					{
					setState(99);
					globalDeclaration();
					}
					break;
				}
				}
				setState(104);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(105);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GlobalDeclarationContext extends ParserRuleContext {
		public VariableDeclarationContext variableDeclaration() {
			return getRuleContext(VariableDeclarationContext.class,0);
		}
		public GlobalDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_globalDeclaration; }
	}

	public final GlobalDeclarationContext globalDeclaration() throws RecognitionException {
		GlobalDeclarationContext _localctx = new GlobalDeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_globalDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			variableDeclaration();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDefinitionContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public TerminalNode LPAREN() { return getToken(miniparser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(miniparser.RPAREN, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ParameterListContext parameterList() {
			return getRuleContext(ParameterListContext.class,0);
		}
		public FunctionDefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDefinition; }
	}

	public final FunctionDefinitionContext functionDefinition() throws RecognitionException {
		FunctionDefinitionContext _localctx = new FunctionDefinitionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_functionDefinition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			type();
			setState(110);
			match(IDENTIFIER);
			setState(111);
			match(LPAREN);
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 516096L) != 0)) {
				{
				setState(112);
				parameterList();
				}
			}

			setState(115);
			match(RPAREN);
			setState(116);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterListContext extends ParserRuleContext {
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(miniparser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(miniparser.COMMA, i);
		}
		public ParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterList; }
	}

	public final ParameterListContext parameterList() throws RecognitionException {
		ParameterListContext _localctx = new ParameterListContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_parameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			parameter();
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(119);
				match(COMMA);
				setState(120);
				parameter();
				}
				}
				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			type();
			setState(127);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(miniparser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(miniparser.FLOAT, 0); }
		public TerminalNode DOUBLE() { return getToken(miniparser.DOUBLE, 0); }
		public TerminalNode CHAR() { return getToken(miniparser.CHAR, 0); }
		public TerminalNode BOOL() { return getToken(miniparser.BOOL, 0); }
		public TerminalNode VOID() { return getToken(miniparser.VOID, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 516096L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(miniparser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(miniparser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(LBRACE);
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 576742230505549434L) != 0)) {
				{
				{
				setState(132);
				statement();
				}
				}
				setState(137);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(138);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public VariableDeclarationContext variableDeclaration() {
			return getRuleContext(VariableDeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public DoWhileStatementContext doWhileStatement() {
			return getRuleContext(DoWhileStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public SwitchStatementContext switchStatement() {
			return getRuleContext(SwitchStatementContext.class,0);
		}
		public ReturnStatementContext returnStatement() {
			return getRuleContext(ReturnStatementContext.class,0);
		}
		public BreakStatementContext breakStatement() {
			return getRuleContext(BreakStatementContext.class,0);
		}
		public ContinueStatementContext continueStatement() {
			return getRuleContext(ContinueStatementContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(miniparser.SEMICOLON, 0); }
		public IncrementStatementContext incrementStatement() {
			return getRuleContext(IncrementStatementContext.class,0);
		}
		public DecrementStatementContext decrementStatement() {
			return getRuleContext(DecrementStatementContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public PrintfStatementContext printfStatement() {
			return getRuleContext(PrintfStatementContext.class,0);
		}
		public ScanfStatementContext scanfStatement() {
			return getRuleContext(ScanfStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_statement);
		try {
			setState(158);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				variableDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(141);
				assignment();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(142);
				ifStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(143);
				whileStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(144);
				doWhileStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(145);
				forStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(146);
				switchStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(147);
				returnStatement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(148);
				breakStatement();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(149);
				continueStatement();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(150);
				functionCall();
				setState(151);
				match(SEMICOLON);
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(153);
				incrementStatement();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(154);
				decrementStatement();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(155);
				block();
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(156);
				printfStatement();
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(157);
				scanfStatement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VariableDeclarationContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public VariableListContext variableList() {
			return getRuleContext(VariableListContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(miniparser.SEMICOLON, 0); }
		public TerminalNode CONST() { return getToken(miniparser.CONST, 0); }
		public VariableDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDeclaration; }
	}

	public final VariableDeclarationContext variableDeclaration() throws RecognitionException {
		VariableDeclarationContext _localctx = new VariableDeclarationContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_variableDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CONST) {
				{
				setState(160);
				match(CONST);
				}
			}

			setState(163);
			type();
			setState(164);
			variableList();
			setState(165);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VariableListContext extends ParserRuleContext {
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(miniparser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(miniparser.COMMA, i);
		}
		public VariableListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableList; }
	}

	public final VariableListContext variableList() throws RecognitionException {
		VariableListContext _localctx = new VariableListContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_variableList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			variable();
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(168);
				match(COMMA);
				setState(169);
				variable();
				}
				}
				setState(174);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VariableContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public TerminalNode LBRACKET() { return getToken(miniparser.LBRACKET, 0); }
		public TerminalNode INTEGER_LITERAL() { return getToken(miniparser.INTEGER_LITERAL, 0); }
		public TerminalNode RBRACKET() { return getToken(miniparser.RBRACKET, 0); }
		public TerminalNode ASSIGN() { return getToken(miniparser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_variable);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(IDENTIFIER);
			setState(179);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LBRACKET) {
				{
				setState(176);
				match(LBRACKET);
				setState(177);
				match(INTEGER_LITERAL);
				setState(178);
				match(RBRACKET);
				}
			}

			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(181);
				match(ASSIGN);
				setState(182);
				expression();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public AssignmentOperatorContext assignmentOperator() {
			return getRuleContext(AssignmentOperatorContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(miniparser.SEMICOLON, 0); }
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public ArrayAccessContext arrayAccess() {
			return getRuleContext(ArrayAccessContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(185);
				match(IDENTIFIER);
				}
				break;
			case 2:
				{
				setState(186);
				arrayAccess();
				}
				break;
			}
			setState(189);
			assignmentOperator();
			setState(190);
			expression();
			setState(191);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentOperatorContext extends ParserRuleContext {
		public TerminalNode ASSIGN() { return getToken(miniparser.ASSIGN, 0); }
		public TerminalNode PLUS_ASSIGN() { return getToken(miniparser.PLUS_ASSIGN, 0); }
		public TerminalNode MINUS_ASSIGN() { return getToken(miniparser.MINUS_ASSIGN, 0); }
		public TerminalNode MULT_ASSIGN() { return getToken(miniparser.MULT_ASSIGN, 0); }
		public TerminalNode DIV_ASSIGN() { return getToken(miniparser.DIV_ASSIGN, 0); }
		public TerminalNode MOD_ASSIGN() { return getToken(miniparser.MOD_ASSIGN, 0); }
		public AssignmentOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentOperator; }
	}

	public final AssignmentOperatorContext assignmentOperator() throws RecognitionException {
		AssignmentOperatorContext _localctx = new AssignmentOperatorContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_assignmentOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1056964608L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IncrementStatementContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public TerminalNode INCREMENT() { return getToken(miniparser.INCREMENT, 0); }
		public TerminalNode SEMICOLON() { return getToken(miniparser.SEMICOLON, 0); }
		public IncrementStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_incrementStatement; }
	}

	public final IncrementStatementContext incrementStatement() throws RecognitionException {
		IncrementStatementContext _localctx = new IncrementStatementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_incrementStatement);
		try {
			setState(201);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(195);
				match(IDENTIFIER);
				setState(196);
				match(INCREMENT);
				setState(197);
				match(SEMICOLON);
				}
				break;
			case INCREMENT:
				enterOuterAlt(_localctx, 2);
				{
				setState(198);
				match(INCREMENT);
				setState(199);
				match(IDENTIFIER);
				setState(200);
				match(SEMICOLON);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DecrementStatementContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public TerminalNode DECREMENT() { return getToken(miniparser.DECREMENT, 0); }
		public TerminalNode SEMICOLON() { return getToken(miniparser.SEMICOLON, 0); }
		public DecrementStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decrementStatement; }
	}

	public final DecrementStatementContext decrementStatement() throws RecognitionException {
		DecrementStatementContext _localctx = new DecrementStatementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_decrementStatement);
		try {
			setState(209);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(203);
				match(IDENTIFIER);
				setState(204);
				match(DECREMENT);
				setState(205);
				match(SEMICOLON);
				}
				break;
			case DECREMENT:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				match(DECREMENT);
				setState(207);
				match(IDENTIFIER);
				setState(208);
				match(SEMICOLON);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(miniparser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(miniparser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(miniparser.RPAREN, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(miniparser.ELSE, 0); }
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_ifStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(IF);
			setState(212);
			match(LPAREN);
			setState(213);
			expression();
			setState(214);
			match(RPAREN);
			setState(215);
			statement();
			setState(218);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(216);
				match(ELSE);
				setState(217);
				statement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatementContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(miniparser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(miniparser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(miniparser.RPAREN, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_whileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(WHILE);
			setState(221);
			match(LPAREN);
			setState(222);
			expression();
			setState(223);
			match(RPAREN);
			setState(224);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStatementContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(miniparser.FOR, 0); }
		public TerminalNode LPAREN() { return getToken(miniparser.LPAREN, 0); }
		public List<TerminalNode> SEMICOLON() { return getTokens(miniparser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(miniparser.SEMICOLON, i);
		}
		public TerminalNode RPAREN() { return getToken(miniparser.RPAREN, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ForInitContext forInit() {
			return getRuleContext(ForInitContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ForUpdateContext forUpdate() {
			return getRuleContext(ForUpdateContext.class,0);
		}
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_forStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			match(FOR);
			setState(227);
			match(LPAREN);
			setState(229);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 576460752303939584L) != 0)) {
				{
				setState(228);
				forInit();
				}
			}

			setState(231);
			match(SEMICOLON);
			setState(233);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1116998273601638400L) != 0)) {
				{
				setState(232);
				expression();
				}
			}

			setState(235);
			match(SEMICOLON);
			setState(237);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 576460755524648960L) != 0)) {
				{
				setState(236);
				forUpdate();
				}
			}

			setState(239);
			match(RPAREN);
			setState(240);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DoWhileStatementContext extends ParserRuleContext {
		public TerminalNode DO() { return getToken(miniparser.DO, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode WHILE() { return getToken(miniparser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(miniparser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(miniparser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(miniparser.SEMICOLON, 0); }
		public DoWhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doWhileStatement; }
	}

	public final DoWhileStatementContext doWhileStatement() throws RecognitionException {
		DoWhileStatementContext _localctx = new DoWhileStatementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_doWhileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			match(DO);
			setState(243);
			statement();
			setState(244);
			match(WHILE);
			setState(245);
			match(LPAREN);
			setState(246);
			expression();
			setState(247);
			match(RPAREN);
			setState(248);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForInitContext extends ParserRuleContext {
		public VariableDeclarationForContext variableDeclarationFor() {
			return getRuleContext(VariableDeclarationForContext.class,0);
		}
		public AssignmentNoSemiContext assignmentNoSemi() {
			return getRuleContext(AssignmentNoSemiContext.class,0);
		}
		public ForInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forInit; }
	}

	public final ForInitContext forInit() throws RecognitionException {
		ForInitContext _localctx = new ForInitContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_forInit);
		try {
			setState(252);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
			case DOUBLE:
			case CHAR:
			case BOOL:
			case VOID:
				enterOuterAlt(_localctx, 1);
				{
				setState(250);
				variableDeclarationFor();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(251);
				assignmentNoSemi();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VariableDeclarationForContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public VariableListContext variableList() {
			return getRuleContext(VariableListContext.class,0);
		}
		public VariableDeclarationForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDeclarationFor; }
	}

	public final VariableDeclarationForContext variableDeclarationFor() throws RecognitionException {
		VariableDeclarationForContext _localctx = new VariableDeclarationForContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_variableDeclarationFor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			type();
			setState(255);
			variableList();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentNoSemiContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public AssignmentOperatorContext assignmentOperator() {
			return getRuleContext(AssignmentOperatorContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentNoSemiContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentNoSemi; }
	}

	public final AssignmentNoSemiContext assignmentNoSemi() throws RecognitionException {
		AssignmentNoSemiContext _localctx = new AssignmentNoSemiContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_assignmentNoSemi);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(IDENTIFIER);
			setState(258);
			assignmentOperator();
			setState(259);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForUpdateContext extends ParserRuleContext {
		public AssignmentNoSemiContext assignmentNoSemi() {
			return getRuleContext(AssignmentNoSemiContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public TerminalNode INCREMENT() { return getToken(miniparser.INCREMENT, 0); }
		public TerminalNode DECREMENT() { return getToken(miniparser.DECREMENT, 0); }
		public ForUpdateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forUpdate; }
	}

	public final ForUpdateContext forUpdate() throws RecognitionException {
		ForUpdateContext _localctx = new ForUpdateContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_forUpdate);
		try {
			setState(270);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(261);
				assignmentNoSemi();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(262);
				match(IDENTIFIER);
				setState(263);
				match(INCREMENT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(264);
				match(INCREMENT);
				setState(265);
				match(IDENTIFIER);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(266);
				match(IDENTIFIER);
				setState(267);
				match(DECREMENT);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(268);
				match(DECREMENT);
				setState(269);
				match(IDENTIFIER);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SwitchStatementContext extends ParserRuleContext {
		public TerminalNode SWITCH() { return getToken(miniparser.SWITCH, 0); }
		public TerminalNode LPAREN() { return getToken(miniparser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(miniparser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(miniparser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(miniparser.RBRACE, 0); }
		public List<CaseStatementContext> caseStatement() {
			return getRuleContexts(CaseStatementContext.class);
		}
		public CaseStatementContext caseStatement(int i) {
			return getRuleContext(CaseStatementContext.class,i);
		}
		public DefaultStatementContext defaultStatement() {
			return getRuleContext(DefaultStatementContext.class,0);
		}
		public SwitchStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchStatement; }
	}

	public final SwitchStatementContext switchStatement() throws RecognitionException {
		SwitchStatementContext _localctx = new SwitchStatementContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_switchStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			match(SWITCH);
			setState(273);
			match(LPAREN);
			setState(274);
			expression();
			setState(275);
			match(RPAREN);
			setState(276);
			match(LBRACE);
			setState(280);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CASE) {
				{
				{
				setState(277);
				caseStatement();
				}
				}
				setState(282);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(284);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DEFAULT) {
				{
				setState(283);
				defaultStatement();
				}
			}

			setState(286);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CaseStatementContext extends ParserRuleContext {
		public TerminalNode CASE() { return getToken(miniparser.CASE, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode COLON() { return getToken(miniparser.COLON, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public CaseStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_caseStatement; }
	}

	public final CaseStatementContext caseStatement() throws RecognitionException {
		CaseStatementContext _localctx = new CaseStatementContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_caseStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			match(CASE);
			setState(289);
			literal();
			setState(290);
			match(COLON);
			setState(294);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 576742230505549434L) != 0)) {
				{
				{
				setState(291);
				statement();
				}
				}
				setState(296);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefaultStatementContext extends ParserRuleContext {
		public TerminalNode DEFAULT() { return getToken(miniparser.DEFAULT, 0); }
		public TerminalNode COLON() { return getToken(miniparser.COLON, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public DefaultStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defaultStatement; }
	}

	public final DefaultStatementContext defaultStatement() throws RecognitionException {
		DefaultStatementContext _localctx = new DefaultStatementContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_defaultStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			match(DEFAULT);
			setState(298);
			match(COLON);
			setState(302);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 576742230505549434L) != 0)) {
				{
				{
				setState(299);
				statement();
				}
				}
				setState(304);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStatementContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(miniparser.RETURN, 0); }
		public TerminalNode SEMICOLON() { return getToken(miniparser.SEMICOLON, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStatement; }
	}

	public final ReturnStatementContext returnStatement() throws RecognitionException {
		ReturnStatementContext _localctx = new ReturnStatementContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_returnStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(305);
			match(RETURN);
			setState(307);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1116998273601638400L) != 0)) {
				{
				setState(306);
				expression();
				}
			}

			setState(309);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BreakStatementContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(miniparser.BREAK, 0); }
		public TerminalNode SEMICOLON() { return getToken(miniparser.SEMICOLON, 0); }
		public BreakStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakStatement; }
	}

	public final BreakStatementContext breakStatement() throws RecognitionException {
		BreakStatementContext _localctx = new BreakStatementContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_breakStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(311);
			match(BREAK);
			setState(312);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContinueStatementContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(miniparser.CONTINUE, 0); }
		public TerminalNode SEMICOLON() { return getToken(miniparser.SEMICOLON, 0); }
		public ContinueStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continueStatement; }
	}

	public final ContinueStatementContext continueStatement() throws RecognitionException {
		ContinueStatementContext _localctx = new ContinueStatementContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_continueStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			match(CONTINUE);
			setState(315);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INTEGER_LITERAL() { return getToken(miniparser.INTEGER_LITERAL, 0); }
		public TerminalNode FLOAT_LITERAL() { return getToken(miniparser.FLOAT_LITERAL, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(miniparser.STRING_LITERAL, 0); }
		public TerminalNode CHAR_LITERAL() { return getToken(miniparser.CHAR_LITERAL, 0); }
		public TerminalNode TRUE() { return getToken(miniparser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(miniparser.FALSE, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(317);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 540431955297042432L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public LogicalOrExpressionContext logicalOrExpression() {
			return getRuleContext(LogicalOrExpressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(319);
			logicalOrExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalOrExpressionContext extends ParserRuleContext {
		public List<LogicalAndExpressionContext> logicalAndExpression() {
			return getRuleContexts(LogicalAndExpressionContext.class);
		}
		public LogicalAndExpressionContext logicalAndExpression(int i) {
			return getRuleContext(LogicalAndExpressionContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(miniparser.OR); }
		public TerminalNode OR(int i) {
			return getToken(miniparser.OR, i);
		}
		public LogicalOrExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOrExpression; }
	}

	public final LogicalOrExpressionContext logicalOrExpression() throws RecognitionException {
		LogicalOrExpressionContext _localctx = new LogicalOrExpressionContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_logicalOrExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(321);
			logicalAndExpression();
			setState(326);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(322);
				match(OR);
				setState(323);
				logicalAndExpression();
				}
				}
				setState(328);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalAndExpressionContext extends ParserRuleContext {
		public List<EqualityExpressionContext> equalityExpression() {
			return getRuleContexts(EqualityExpressionContext.class);
		}
		public EqualityExpressionContext equalityExpression(int i) {
			return getRuleContext(EqualityExpressionContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(miniparser.AND); }
		public TerminalNode AND(int i) {
			return getToken(miniparser.AND, i);
		}
		public LogicalAndExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalAndExpression; }
	}

	public final LogicalAndExpressionContext logicalAndExpression() throws RecognitionException {
		LogicalAndExpressionContext _localctx = new LogicalAndExpressionContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_logicalAndExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(329);
			equalityExpression();
			setState(334);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(330);
				match(AND);
				setState(331);
				equalityExpression();
				}
				}
				setState(336);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EqualityExpressionContext extends ParserRuleContext {
		public List<RelationalExpressionContext> relationalExpression() {
			return getRuleContexts(RelationalExpressionContext.class);
		}
		public RelationalExpressionContext relationalExpression(int i) {
			return getRuleContext(RelationalExpressionContext.class,i);
		}
		public List<TerminalNode> EQUAL() { return getTokens(miniparser.EQUAL); }
		public TerminalNode EQUAL(int i) {
			return getToken(miniparser.EQUAL, i);
		}
		public List<TerminalNode> NOT_EQUAL() { return getTokens(miniparser.NOT_EQUAL); }
		public TerminalNode NOT_EQUAL(int i) {
			return getToken(miniparser.NOT_EQUAL, i);
		}
		public EqualityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equalityExpression; }
	}

	public final EqualityExpressionContext equalityExpression() throws RecognitionException {
		EqualityExpressionContext _localctx = new EqualityExpressionContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_equalityExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(337);
			relationalExpression();
			setState(342);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==EQUAL || _la==NOT_EQUAL) {
				{
				{
				setState(338);
				_la = _input.LA(1);
				if ( !(_la==EQUAL || _la==NOT_EQUAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(339);
				relationalExpression();
				}
				}
				setState(344);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelationalExpressionContext extends ParserRuleContext {
		public List<AdditiveExpressionContext> additiveExpression() {
			return getRuleContexts(AdditiveExpressionContext.class);
		}
		public AdditiveExpressionContext additiveExpression(int i) {
			return getRuleContext(AdditiveExpressionContext.class,i);
		}
		public List<TerminalNode> GREATER() { return getTokens(miniparser.GREATER); }
		public TerminalNode GREATER(int i) {
			return getToken(miniparser.GREATER, i);
		}
		public List<TerminalNode> LESS() { return getTokens(miniparser.LESS); }
		public TerminalNode LESS(int i) {
			return getToken(miniparser.LESS, i);
		}
		public List<TerminalNode> GREATER_EQUAL() { return getTokens(miniparser.GREATER_EQUAL); }
		public TerminalNode GREATER_EQUAL(int i) {
			return getToken(miniparser.GREATER_EQUAL, i);
		}
		public List<TerminalNode> LESS_EQUAL() { return getTokens(miniparser.LESS_EQUAL); }
		public TerminalNode LESS_EQUAL(int i) {
			return getToken(miniparser.LESS_EQUAL, i);
		}
		public RelationalExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationalExpression; }
	}

	public final RelationalExpressionContext relationalExpression() throws RecognitionException {
		RelationalExpressionContext _localctx = new RelationalExpressionContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_relationalExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(345);
			additiveExpression();
			setState(350);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8246337208320L) != 0)) {
				{
				{
				setState(346);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 8246337208320L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(347);
				additiveExpression();
				}
				}
				setState(352);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AdditiveExpressionContext extends ParserRuleContext {
		public List<MultiplicativeExpressionContext> multiplicativeExpression() {
			return getRuleContexts(MultiplicativeExpressionContext.class);
		}
		public MultiplicativeExpressionContext multiplicativeExpression(int i) {
			return getRuleContext(MultiplicativeExpressionContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(miniparser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(miniparser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(miniparser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(miniparser.MINUS, i);
		}
		public AdditiveExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additiveExpression; }
	}

	public final AdditiveExpressionContext additiveExpression() throws RecognitionException {
		AdditiveExpressionContext _localctx = new AdditiveExpressionContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_additiveExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(353);
			multiplicativeExpression();
			setState(358);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(354);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(355);
				multiplicativeExpression();
				}
				}
				setState(360);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicativeExpressionContext extends ParserRuleContext {
		public List<UnaryExpressionContext> unaryExpression() {
			return getRuleContexts(UnaryExpressionContext.class);
		}
		public UnaryExpressionContext unaryExpression(int i) {
			return getRuleContext(UnaryExpressionContext.class,i);
		}
		public List<TerminalNode> MULT() { return getTokens(miniparser.MULT); }
		public TerminalNode MULT(int i) {
			return getToken(miniparser.MULT, i);
		}
		public List<TerminalNode> DIV() { return getTokens(miniparser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(miniparser.DIV, i);
		}
		public List<TerminalNode> MOD() { return getTokens(miniparser.MOD); }
		public TerminalNode MOD(int i) {
			return getToken(miniparser.MOD, i);
		}
		public MultiplicativeExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicativeExpression; }
	}

	public final MultiplicativeExpressionContext multiplicativeExpression() throws RecognitionException {
		MultiplicativeExpressionContext _localctx = new MultiplicativeExpressionContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_multiplicativeExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(361);
			unaryExpression();
			setState(366);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 120259084288L) != 0)) {
				{
				{
				setState(362);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 120259084288L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(363);
				unaryExpression();
				}
				}
				setState(368);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryExpressionContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(miniparser.NOT, 0); }
		public UnaryExpressionContext unaryExpression() {
			return getRuleContext(UnaryExpressionContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(miniparser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(miniparser.MINUS, 0); }
		public PostfixExpressionContext postfixExpression() {
			return getRuleContext(PostfixExpressionContext.class,0);
		}
		public UnaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryExpression; }
	}

	public final UnaryExpressionContext unaryExpression() throws RecognitionException {
		UnaryExpressionContext _localctx = new UnaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_unaryExpression);
		try {
			setState(376);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(369);
				match(NOT);
				setState(370);
				unaryExpression();
				}
				break;
			case PLUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(371);
				match(PLUS);
				setState(372);
				unaryExpression();
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 3);
				{
				setState(373);
				match(MINUS);
				setState(374);
				unaryExpression();
				}
				break;
			case SIZEOF:
			case TRUE:
			case FALSE:
			case LPAREN:
			case FLOAT_LITERAL:
			case INTEGER_LITERAL:
			case STRING_LITERAL:
			case CHAR_LITERAL:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 4);
				{
				setState(375);
				postfixExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PostfixExpressionContext extends ParserRuleContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public List<TerminalNode> INCREMENT() { return getTokens(miniparser.INCREMENT); }
		public TerminalNode INCREMENT(int i) {
			return getToken(miniparser.INCREMENT, i);
		}
		public List<TerminalNode> DECREMENT() { return getTokens(miniparser.DECREMENT); }
		public TerminalNode DECREMENT(int i) {
			return getToken(miniparser.DECREMENT, i);
		}
		public PostfixExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_postfixExpression; }
	}

	public final PostfixExpressionContext postfixExpression() throws RecognitionException {
		PostfixExpressionContext _localctx = new PostfixExpressionContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_postfixExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(378);
			primaryExpression();
			setState(382);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==INCREMENT || _la==DECREMENT) {
				{
				{
				setState(379);
				_la = _input.LA(1);
				if ( !(_la==INCREMENT || _la==DECREMENT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(384);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryExpressionContext extends ParserRuleContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public ArrayAccessContext arrayAccess() {
			return getRuleContext(ArrayAccessContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public TerminalNode LPAREN() { return getToken(miniparser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(miniparser.RPAREN, 0); }
		public SizeofExpressionContext sizeofExpression() {
			return getRuleContext(SizeofExpressionContext.class,0);
		}
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_primaryExpression);
		try {
			setState(394);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(385);
				functionCall();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(386);
				arrayAccess();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(387);
				literal();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(388);
				match(IDENTIFIER);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(389);
				match(LPAREN);
				setState(390);
				expression();
				setState(391);
				match(RPAREN);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(393);
				sizeofExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public TerminalNode LPAREN() { return getToken(miniparser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(miniparser.RPAREN, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(396);
			match(IDENTIFIER);
			setState(397);
			match(LPAREN);
			setState(399);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1116998273601638400L) != 0)) {
				{
				setState(398);
				argumentList();
				}
			}

			setState(401);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintfStatementContext extends ParserRuleContext {
		public TerminalNode PRINTF() { return getToken(miniparser.PRINTF, 0); }
		public TerminalNode LPAREN() { return getToken(miniparser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(miniparser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(miniparser.SEMICOLON, 0); }
		public PrintfArgumentsContext printfArguments() {
			return getRuleContext(PrintfArgumentsContext.class,0);
		}
		public PrintfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printfStatement; }
	}

	public final PrintfStatementContext printfStatement() throws RecognitionException {
		PrintfStatementContext _localctx = new PrintfStatementContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_printfStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(403);
			match(PRINTF);
			setState(404);
			match(LPAREN);
			setState(406);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1116998273601638400L) != 0)) {
				{
				setState(405);
				printfArguments();
				}
			}

			setState(408);
			match(RPAREN);
			setState(409);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScanfStatementContext extends ParserRuleContext {
		public TerminalNode SCANF() { return getToken(miniparser.SCANF, 0); }
		public TerminalNode LPAREN() { return getToken(miniparser.LPAREN, 0); }
		public ScanfArgumentsContext scanfArguments() {
			return getRuleContext(ScanfArgumentsContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(miniparser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(miniparser.SEMICOLON, 0); }
		public ScanfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanfStatement; }
	}

	public final ScanfStatementContext scanfStatement() throws RecognitionException {
		ScanfStatementContext _localctx = new ScanfStatementContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_scanfStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(411);
			match(SCANF);
			setState(412);
			match(LPAREN);
			setState(413);
			scanfArguments();
			setState(414);
			match(RPAREN);
			setState(415);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(miniparser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(miniparser.COMMA, i);
		}
		public ArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentList; }
	}

	public final ArgumentListContext argumentList() throws RecognitionException {
		ArgumentListContext _localctx = new ArgumentListContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(417);
			expression();
			setState(422);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(418);
				match(COMMA);
				setState(419);
				expression();
				}
				}
				setState(424);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintfArgumentsContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(miniparser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(miniparser.COMMA, i);
		}
		public PrintfArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printfArguments; }
	}

	public final PrintfArgumentsContext printfArguments() throws RecognitionException {
		PrintfArgumentsContext _localctx = new PrintfArgumentsContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_printfArguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(425);
			expression();
			setState(430);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(426);
				match(COMMA);
				setState(427);
				expression();
				}
				}
				setState(432);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScanfArgumentsContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(miniparser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(miniparser.COMMA, i);
		}
		public List<ScanfArgumentContext> scanfArgument() {
			return getRuleContexts(ScanfArgumentContext.class);
		}
		public ScanfArgumentContext scanfArgument(int i) {
			return getRuleContext(ScanfArgumentContext.class,i);
		}
		public ScanfArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanfArguments; }
	}

	public final ScanfArgumentsContext scanfArguments() throws RecognitionException {
		ScanfArgumentsContext _localctx = new ScanfArgumentsContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_scanfArguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(433);
			expression();
			setState(438);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(434);
				match(COMMA);
				setState(435);
				scanfArgument();
				}
				}
				setState(440);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScanfArgumentContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public ArrayAccessContext arrayAccess() {
			return getRuleContext(ArrayAccessContext.class,0);
		}
		public ScanfArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanfArgument; }
	}

	public final ScanfArgumentContext scanfArgument() throws RecognitionException {
		ScanfArgumentContext _localctx = new ScanfArgumentContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_scanfArgument);
		try {
			setState(443);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(441);
				match(IDENTIFIER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(442);
				arrayAccess();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayAccessContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public TerminalNode LBRACKET() { return getToken(miniparser.LBRACKET, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(miniparser.RBRACKET, 0); }
		public ArrayAccessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayAccess; }
	}

	public final ArrayAccessContext arrayAccess() throws RecognitionException {
		ArrayAccessContext _localctx = new ArrayAccessContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_arrayAccess);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(445);
			match(IDENTIFIER);
			setState(446);
			match(LBRACKET);
			setState(447);
			expression();
			setState(448);
			match(RBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SizeofExpressionContext extends ParserRuleContext {
		public TerminalNode SIZEOF() { return getToken(miniparser.SIZEOF, 0); }
		public TerminalNode LPAREN() { return getToken(miniparser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(miniparser.RPAREN, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(miniparser.IDENTIFIER, 0); }
		public SizeofExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sizeofExpression; }
	}

	public final SizeofExpressionContext sizeofExpression() throws RecognitionException {
		SizeofExpressionContext _localctx = new SizeofExpressionContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_sizeofExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(450);
			match(SIZEOF);
			setState(451);
			match(LPAREN);
			setState(454);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
			case DOUBLE:
			case CHAR:
			case BOOL:
			case VOID:
				{
				setState(452);
				type();
				}
				break;
			case IDENTIFIER:
				{
				setState(453);
				match(IDENTIFIER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(456);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001?\u01cb\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u00070\u0001\u0000\u0001\u0000"+
		"\u0005\u0000e\b\u0000\n\u0000\f\u0000h\t\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002r\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0005\u0003z\b\u0003\n\u0003\f\u0003}\t\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0005\u0006\u0086\b\u0006\n\u0006\f\u0006\u0089\t\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0003\u0007\u009f\b\u0007\u0001\b\u0003\b\u00a2\b\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0005\t\u00ab"+
		"\b\t\n\t\f\t\u00ae\t\t\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00b4\b"+
		"\n\u0001\n\u0001\n\u0003\n\u00b8\b\n\u0001\u000b\u0001\u000b\u0003\u000b"+
		"\u00bc\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f"+
		"\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00ca"+
		"\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0003\u000e\u00d2\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00db\b\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00e6\b\u0011\u0001\u0011\u0001"+
		"\u0011\u0003\u0011\u00ea\b\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00ee"+
		"\b\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0013\u0001\u0013\u0003\u0013\u00fd\b\u0013\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0003\u0016\u010f\b\u0016\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u0117\b\u0017\n"+
		"\u0017\f\u0017\u011a\t\u0017\u0001\u0017\u0003\u0017\u011d\b\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0005"+
		"\u0018\u0125\b\u0018\n\u0018\f\u0018\u0128\t\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0005\u0019\u012d\b\u0019\n\u0019\f\u0019\u0130\t\u0019\u0001"+
		"\u001a\u0001\u001a\u0003\u001a\u0134\b\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0005\u001f\u0145\b\u001f\n\u001f\f\u001f\u0148\t\u001f\u0001 "+
		"\u0001 \u0001 \u0005 \u014d\b \n \f \u0150\t \u0001!\u0001!\u0001!\u0005"+
		"!\u0155\b!\n!\f!\u0158\t!\u0001\"\u0001\"\u0001\"\u0005\"\u015d\b\"\n"+
		"\"\f\"\u0160\t\"\u0001#\u0001#\u0001#\u0005#\u0165\b#\n#\f#\u0168\t#\u0001"+
		"$\u0001$\u0001$\u0005$\u016d\b$\n$\f$\u0170\t$\u0001%\u0001%\u0001%\u0001"+
		"%\u0001%\u0001%\u0001%\u0003%\u0179\b%\u0001&\u0001&\u0005&\u017d\b&\n"+
		"&\f&\u0180\t&\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'"+
		"\u0001\'\u0001\'\u0003\'\u018b\b\'\u0001(\u0001(\u0001(\u0003(\u0190\b"+
		"(\u0001(\u0001(\u0001)\u0001)\u0001)\u0003)\u0197\b)\u0001)\u0001)\u0001"+
		")\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001+\u0001+\u0001+\u0005"+
		"+\u01a5\b+\n+\f+\u01a8\t+\u0001,\u0001,\u0001,\u0005,\u01ad\b,\n,\f,\u01b0"+
		"\t,\u0001-\u0001-\u0001-\u0005-\u01b5\b-\n-\f-\u01b8\t-\u0001.\u0001."+
		"\u0003.\u01bc\b.\u0001/\u0001/\u0001/\u0001/\u0001/\u00010\u00010\u0001"+
		"0\u00010\u00030\u01c7\b0\u00010\u00010\u00010\u0000\u00001\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e"+
		" \"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`\u0000\b\u0001\u0000\r\u0012\u0001"+
		"\u0000\u0018\u001d\u0002\u0000\u0016\u00177:\u0001\u0000%&\u0001\u0000"+
		"\'*\u0001\u0000 !\u0001\u0000\"$\u0001\u0000\u001e\u001f\u01d8\u0000f"+
		"\u0001\u0000\u0000\u0000\u0002k\u0001\u0000\u0000\u0000\u0004m\u0001\u0000"+
		"\u0000\u0000\u0006v\u0001\u0000\u0000\u0000\b~\u0001\u0000\u0000\u0000"+
		"\n\u0081\u0001\u0000\u0000\u0000\f\u0083\u0001\u0000\u0000\u0000\u000e"+
		"\u009e\u0001\u0000\u0000\u0000\u0010\u00a1\u0001\u0000\u0000\u0000\u0012"+
		"\u00a7\u0001\u0000\u0000\u0000\u0014\u00af\u0001\u0000\u0000\u0000\u0016"+
		"\u00bb\u0001\u0000\u0000\u0000\u0018\u00c1\u0001\u0000\u0000\u0000\u001a"+
		"\u00c9\u0001\u0000\u0000\u0000\u001c\u00d1\u0001\u0000\u0000\u0000\u001e"+
		"\u00d3\u0001\u0000\u0000\u0000 \u00dc\u0001\u0000\u0000\u0000\"\u00e2"+
		"\u0001\u0000\u0000\u0000$\u00f2\u0001\u0000\u0000\u0000&\u00fc\u0001\u0000"+
		"\u0000\u0000(\u00fe\u0001\u0000\u0000\u0000*\u0101\u0001\u0000\u0000\u0000"+
		",\u010e\u0001\u0000\u0000\u0000.\u0110\u0001\u0000\u0000\u00000\u0120"+
		"\u0001\u0000\u0000\u00002\u0129\u0001\u0000\u0000\u00004\u0131\u0001\u0000"+
		"\u0000\u00006\u0137\u0001\u0000\u0000\u00008\u013a\u0001\u0000\u0000\u0000"+
		":\u013d\u0001\u0000\u0000\u0000<\u013f\u0001\u0000\u0000\u0000>\u0141"+
		"\u0001\u0000\u0000\u0000@\u0149\u0001\u0000\u0000\u0000B\u0151\u0001\u0000"+
		"\u0000\u0000D\u0159\u0001\u0000\u0000\u0000F\u0161\u0001\u0000\u0000\u0000"+
		"H\u0169\u0001\u0000\u0000\u0000J\u0178\u0001\u0000\u0000\u0000L\u017a"+
		"\u0001\u0000\u0000\u0000N\u018a\u0001\u0000\u0000\u0000P\u018c\u0001\u0000"+
		"\u0000\u0000R\u0193\u0001\u0000\u0000\u0000T\u019b\u0001\u0000\u0000\u0000"+
		"V\u01a1\u0001\u0000\u0000\u0000X\u01a9\u0001\u0000\u0000\u0000Z\u01b1"+
		"\u0001\u0000\u0000\u0000\\\u01bb\u0001\u0000\u0000\u0000^\u01bd\u0001"+
		"\u0000\u0000\u0000`\u01c2\u0001\u0000\u0000\u0000be\u0003\u0004\u0002"+
		"\u0000ce\u0003\u0002\u0001\u0000db\u0001\u0000\u0000\u0000dc\u0001\u0000"+
		"\u0000\u0000eh\u0001\u0000\u0000\u0000fd\u0001\u0000\u0000\u0000fg\u0001"+
		"\u0000\u0000\u0000gi\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000"+
		"ij\u0005\u0000\u0000\u0001j\u0001\u0001\u0000\u0000\u0000kl\u0003\u0010"+
		"\b\u0000l\u0003\u0001\u0000\u0000\u0000mn\u0003\n\u0005\u0000no\u0005"+
		";\u0000\u0000oq\u0005.\u0000\u0000pr\u0003\u0006\u0003\u0000qp\u0001\u0000"+
		"\u0000\u0000qr\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000st\u0005"+
		"/\u0000\u0000tu\u0003\f\u0006\u0000u\u0005\u0001\u0000\u0000\u0000v{\u0003"+
		"\b\u0004\u0000wx\u00055\u0000\u0000xz\u0003\b\u0004\u0000yw\u0001\u0000"+
		"\u0000\u0000z}\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000{|\u0001"+
		"\u0000\u0000\u0000|\u0007\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000"+
		"\u0000~\u007f\u0003\n\u0005\u0000\u007f\u0080\u0005;\u0000\u0000\u0080"+
		"\t\u0001\u0000\u0000\u0000\u0081\u0082\u0007\u0000\u0000\u0000\u0082\u000b"+
		"\u0001\u0000\u0000\u0000\u0083\u0087\u00050\u0000\u0000\u0084\u0086\u0003"+
		"\u000e\u0007\u0000\u0085\u0084\u0001\u0000\u0000\u0000\u0086\u0089\u0001"+
		"\u0000\u0000\u0000\u0087\u0085\u0001\u0000\u0000\u0000\u0087\u0088\u0001"+
		"\u0000\u0000\u0000\u0088\u008a\u0001\u0000\u0000\u0000\u0089\u0087\u0001"+
		"\u0000\u0000\u0000\u008a\u008b\u00051\u0000\u0000\u008b\r\u0001\u0000"+
		"\u0000\u0000\u008c\u009f\u0003\u0010\b\u0000\u008d\u009f\u0003\u0016\u000b"+
		"\u0000\u008e\u009f\u0003\u001e\u000f\u0000\u008f\u009f\u0003 \u0010\u0000"+
		"\u0090\u009f\u0003$\u0012\u0000\u0091\u009f\u0003\"\u0011\u0000\u0092"+
		"\u009f\u0003.\u0017\u0000\u0093\u009f\u00034\u001a\u0000\u0094\u009f\u0003"+
		"6\u001b\u0000\u0095\u009f\u00038\u001c\u0000\u0096\u0097\u0003P(\u0000"+
		"\u0097\u0098\u00054\u0000\u0000\u0098\u009f\u0001\u0000\u0000\u0000\u0099"+
		"\u009f\u0003\u001a\r\u0000\u009a\u009f\u0003\u001c\u000e\u0000\u009b\u009f"+
		"\u0003\f\u0006\u0000\u009c\u009f\u0003R)\u0000\u009d\u009f\u0003T*\u0000"+
		"\u009e\u008c\u0001\u0000\u0000\u0000\u009e\u008d\u0001\u0000\u0000\u0000"+
		"\u009e\u008e\u0001\u0000\u0000\u0000\u009e\u008f\u0001\u0000\u0000\u0000"+
		"\u009e\u0090\u0001\u0000\u0000\u0000\u009e\u0091\u0001\u0000\u0000\u0000"+
		"\u009e\u0092\u0001\u0000\u0000\u0000\u009e\u0093\u0001\u0000\u0000\u0000"+
		"\u009e\u0094\u0001\u0000\u0000\u0000\u009e\u0095\u0001\u0000\u0000\u0000"+
		"\u009e\u0096\u0001\u0000\u0000\u0000\u009e\u0099\u0001\u0000\u0000\u0000"+
		"\u009e\u009a\u0001\u0000\u0000\u0000\u009e\u009b\u0001\u0000\u0000\u0000"+
		"\u009e\u009c\u0001\u0000\u0000\u0000\u009e\u009d\u0001\u0000\u0000\u0000"+
		"\u009f\u000f\u0001\u0000\u0000\u0000\u00a0\u00a2\u0005\t\u0000\u0000\u00a1"+
		"\u00a0\u0001\u0000\u0000\u0000\u00a1\u00a2\u0001\u0000\u0000\u0000\u00a2"+
		"\u00a3\u0001\u0000\u0000\u0000\u00a3\u00a4\u0003\n\u0005\u0000\u00a4\u00a5"+
		"\u0003\u0012\t\u0000\u00a5\u00a6\u00054\u0000\u0000\u00a6\u0011\u0001"+
		"\u0000\u0000\u0000\u00a7\u00ac\u0003\u0014\n\u0000\u00a8\u00a9\u00055"+
		"\u0000\u0000\u00a9\u00ab\u0003\u0014\n\u0000\u00aa\u00a8\u0001\u0000\u0000"+
		"\u0000\u00ab\u00ae\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001\u0000\u0000"+
		"\u0000\u00ac\u00ad\u0001\u0000\u0000\u0000\u00ad\u0013\u0001\u0000\u0000"+
		"\u0000\u00ae\u00ac\u0001\u0000\u0000\u0000\u00af\u00b3\u0005;\u0000\u0000"+
		"\u00b0\u00b1\u00052\u0000\u0000\u00b1\u00b2\u00058\u0000\u0000\u00b2\u00b4"+
		"\u00053\u0000\u0000\u00b3\u00b0\u0001\u0000\u0000\u0000\u00b3\u00b4\u0001"+
		"\u0000\u0000\u0000\u00b4\u00b7\u0001\u0000\u0000\u0000\u00b5\u00b6\u0005"+
		"\u001d\u0000\u0000\u00b6\u00b8\u0003<\u001e\u0000\u00b7\u00b5\u0001\u0000"+
		"\u0000\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8\u0015\u0001\u0000"+
		"\u0000\u0000\u00b9\u00bc\u0005;\u0000\u0000\u00ba\u00bc\u0003^/\u0000"+
		"\u00bb\u00b9\u0001\u0000\u0000\u0000\u00bb\u00ba\u0001\u0000\u0000\u0000"+
		"\u00bc\u00bd\u0001\u0000\u0000\u0000\u00bd\u00be\u0003\u0018\f\u0000\u00be"+
		"\u00bf\u0003<\u001e\u0000\u00bf\u00c0\u00054\u0000\u0000\u00c0\u0017\u0001"+
		"\u0000\u0000\u0000\u00c1\u00c2\u0007\u0001\u0000\u0000\u00c2\u0019\u0001"+
		"\u0000\u0000\u0000\u00c3\u00c4\u0005;\u0000\u0000\u00c4\u00c5\u0005\u001e"+
		"\u0000\u0000\u00c5\u00ca\u00054\u0000\u0000\u00c6\u00c7\u0005\u001e\u0000"+
		"\u0000\u00c7\u00c8\u0005;\u0000\u0000\u00c8\u00ca\u00054\u0000\u0000\u00c9"+
		"\u00c3\u0001\u0000\u0000\u0000\u00c9\u00c6\u0001\u0000\u0000\u0000\u00ca"+
		"\u001b\u0001\u0000\u0000\u0000\u00cb\u00cc\u0005;\u0000\u0000\u00cc\u00cd"+
		"\u0005\u001f\u0000\u0000\u00cd\u00d2\u00054\u0000\u0000\u00ce\u00cf\u0005"+
		"\u001f\u0000\u0000\u00cf\u00d0\u0005;\u0000\u0000\u00d0\u00d2\u00054\u0000"+
		"\u0000\u00d1\u00cb\u0001\u0000\u0000\u0000\u00d1\u00ce\u0001\u0000\u0000"+
		"\u0000\u00d2\u001d\u0001\u0000\u0000\u0000\u00d3\u00d4\u0005\u0001\u0000"+
		"\u0000\u00d4\u00d5\u0005.\u0000\u0000\u00d5\u00d6\u0003<\u001e\u0000\u00d6"+
		"\u00d7\u0005/\u0000\u0000\u00d7\u00da\u0003\u000e\u0007\u0000\u00d8\u00d9"+
		"\u0005\u0002\u0000\u0000\u00d9\u00db\u0003\u000e\u0007\u0000\u00da\u00d8"+
		"\u0001\u0000\u0000\u0000\u00da\u00db\u0001\u0000\u0000\u0000\u00db\u001f"+
		"\u0001\u0000\u0000\u0000\u00dc\u00dd\u0005\u0003\u0000\u0000\u00dd\u00de"+
		"\u0005.\u0000\u0000\u00de\u00df\u0003<\u001e\u0000\u00df\u00e0\u0005/"+
		"\u0000\u0000\u00e0\u00e1\u0003\u000e\u0007\u0000\u00e1!\u0001\u0000\u0000"+
		"\u0000\u00e2\u00e3\u0005\u0004\u0000\u0000\u00e3\u00e5\u0005.\u0000\u0000"+
		"\u00e4\u00e6\u0003&\u0013\u0000\u00e5\u00e4\u0001\u0000\u0000\u0000\u00e5"+
		"\u00e6\u0001\u0000\u0000\u0000\u00e6\u00e7\u0001\u0000\u0000\u0000\u00e7"+
		"\u00e9\u00054\u0000\u0000\u00e8\u00ea\u0003<\u001e\u0000\u00e9\u00e8\u0001"+
		"\u0000\u0000\u0000\u00e9\u00ea\u0001\u0000\u0000\u0000\u00ea\u00eb\u0001"+
		"\u0000\u0000\u0000\u00eb\u00ed\u00054\u0000\u0000\u00ec\u00ee\u0003,\u0016"+
		"\u0000\u00ed\u00ec\u0001\u0000\u0000\u0000\u00ed\u00ee\u0001\u0000\u0000"+
		"\u0000\u00ee\u00ef\u0001\u0000\u0000\u0000\u00ef\u00f0\u0005/\u0000\u0000"+
		"\u00f0\u00f1\u0003\u000e\u0007\u0000\u00f1#\u0001\u0000\u0000\u0000\u00f2"+
		"\u00f3\u0005\u0005\u0000\u0000\u00f3\u00f4\u0003\u000e\u0007\u0000\u00f4"+
		"\u00f5\u0005\u0003\u0000\u0000\u00f5\u00f6\u0005.\u0000\u0000\u00f6\u00f7"+
		"\u0003<\u001e\u0000\u00f7\u00f8\u0005/\u0000\u0000\u00f8\u00f9\u00054"+
		"\u0000\u0000\u00f9%\u0001\u0000\u0000\u0000\u00fa\u00fd\u0003(\u0014\u0000"+
		"\u00fb\u00fd\u0003*\u0015\u0000\u00fc\u00fa\u0001\u0000\u0000\u0000\u00fc"+
		"\u00fb\u0001\u0000\u0000\u0000\u00fd\'\u0001\u0000\u0000\u0000\u00fe\u00ff"+
		"\u0003\n\u0005\u0000\u00ff\u0100\u0003\u0012\t\u0000\u0100)\u0001\u0000"+
		"\u0000\u0000\u0101\u0102\u0005;\u0000\u0000\u0102\u0103\u0003\u0018\f"+
		"\u0000\u0103\u0104\u0003<\u001e\u0000\u0104+\u0001\u0000\u0000\u0000\u0105"+
		"\u010f\u0003*\u0015\u0000\u0106\u0107\u0005;\u0000\u0000\u0107\u010f\u0005"+
		"\u001e\u0000\u0000\u0108\u0109\u0005\u001e\u0000\u0000\u0109\u010f\u0005"+
		";\u0000\u0000\u010a\u010b\u0005;\u0000\u0000\u010b\u010f\u0005\u001f\u0000"+
		"\u0000\u010c\u010d\u0005\u001f\u0000\u0000\u010d\u010f\u0005;\u0000\u0000"+
		"\u010e\u0105\u0001\u0000\u0000\u0000\u010e\u0106\u0001\u0000\u0000\u0000"+
		"\u010e\u0108\u0001\u0000\u0000\u0000\u010e\u010a\u0001\u0000\u0000\u0000"+
		"\u010e\u010c\u0001\u0000\u0000\u0000\u010f-\u0001\u0000\u0000\u0000\u0110"+
		"\u0111\u0005\u0006\u0000\u0000\u0111\u0112\u0005.\u0000\u0000\u0112\u0113"+
		"\u0003<\u001e\u0000\u0113\u0114\u0005/\u0000\u0000\u0114\u0118\u00050"+
		"\u0000\u0000\u0115\u0117\u00030\u0018\u0000\u0116\u0115\u0001\u0000\u0000"+
		"\u0000\u0117\u011a\u0001\u0000\u0000\u0000\u0118\u0116\u0001\u0000\u0000"+
		"\u0000\u0118\u0119\u0001\u0000\u0000\u0000\u0119\u011c\u0001\u0000\u0000"+
		"\u0000\u011a\u0118\u0001\u0000\u0000\u0000\u011b\u011d\u00032\u0019\u0000"+
		"\u011c\u011b\u0001\u0000\u0000\u0000\u011c\u011d\u0001\u0000\u0000\u0000"+
		"\u011d\u011e\u0001\u0000\u0000\u0000\u011e\u011f\u00051\u0000\u0000\u011f"+
		"/\u0001\u0000\u0000\u0000\u0120\u0121\u0005\u0007\u0000\u0000\u0121\u0122"+
		"\u0003:\u001d\u0000\u0122\u0126\u00056\u0000\u0000\u0123\u0125\u0003\u000e"+
		"\u0007\u0000\u0124\u0123\u0001\u0000\u0000\u0000\u0125\u0128\u0001\u0000"+
		"\u0000\u0000\u0126\u0124\u0001\u0000\u0000\u0000\u0126\u0127\u0001\u0000"+
		"\u0000\u0000\u01271\u0001\u0000\u0000\u0000\u0128\u0126\u0001\u0000\u0000"+
		"\u0000\u0129\u012a\u0005\b\u0000\u0000\u012a\u012e\u00056\u0000\u0000"+
		"\u012b\u012d\u0003\u000e\u0007\u0000\u012c\u012b\u0001\u0000\u0000\u0000"+
		"\u012d\u0130\u0001\u0000\u0000\u0000\u012e\u012c\u0001\u0000\u0000\u0000"+
		"\u012e\u012f\u0001\u0000\u0000\u0000\u012f3\u0001\u0000\u0000\u0000\u0130"+
		"\u012e\u0001\u0000\u0000\u0000\u0131\u0133\u0005\u0013\u0000\u0000\u0132"+
		"\u0134\u0003<\u001e\u0000\u0133\u0132\u0001\u0000\u0000\u0000\u0133\u0134"+
		"\u0001\u0000\u0000\u0000\u0134\u0135\u0001\u0000\u0000\u0000\u0135\u0136"+
		"\u00054\u0000\u0000\u01365\u0001\u0000\u0000\u0000\u0137\u0138\u0005\u0014"+
		"\u0000\u0000\u0138\u0139\u00054\u0000\u0000\u01397\u0001\u0000\u0000\u0000"+
		"\u013a\u013b\u0005\u0015\u0000\u0000\u013b\u013c\u00054\u0000\u0000\u013c"+
		"9\u0001\u0000\u0000\u0000\u013d\u013e\u0007\u0002\u0000\u0000\u013e;\u0001"+
		"\u0000\u0000\u0000\u013f\u0140\u0003>\u001f\u0000\u0140=\u0001\u0000\u0000"+
		"\u0000\u0141\u0146\u0003@ \u0000\u0142\u0143\u0005,\u0000\u0000\u0143"+
		"\u0145\u0003@ \u0000\u0144\u0142\u0001\u0000\u0000\u0000\u0145\u0148\u0001"+
		"\u0000\u0000\u0000\u0146\u0144\u0001\u0000\u0000\u0000\u0146\u0147\u0001"+
		"\u0000\u0000\u0000\u0147?\u0001\u0000\u0000\u0000\u0148\u0146\u0001\u0000"+
		"\u0000\u0000\u0149\u014e\u0003B!\u0000\u014a\u014b\u0005+\u0000\u0000"+
		"\u014b\u014d\u0003B!\u0000\u014c\u014a\u0001\u0000\u0000\u0000\u014d\u0150"+
		"\u0001\u0000\u0000\u0000\u014e\u014c\u0001\u0000\u0000\u0000\u014e\u014f"+
		"\u0001\u0000\u0000\u0000\u014fA\u0001\u0000\u0000\u0000\u0150\u014e\u0001"+
		"\u0000\u0000\u0000\u0151\u0156\u0003D\"\u0000\u0152\u0153\u0007\u0003"+
		"\u0000\u0000\u0153\u0155\u0003D\"\u0000\u0154\u0152\u0001\u0000\u0000"+
		"\u0000\u0155\u0158\u0001\u0000\u0000\u0000\u0156\u0154\u0001\u0000\u0000"+
		"\u0000\u0156\u0157\u0001\u0000\u0000\u0000\u0157C\u0001\u0000\u0000\u0000"+
		"\u0158\u0156\u0001\u0000\u0000\u0000\u0159\u015e\u0003F#\u0000\u015a\u015b"+
		"\u0007\u0004\u0000\u0000\u015b\u015d\u0003F#\u0000\u015c\u015a\u0001\u0000"+
		"\u0000\u0000\u015d\u0160\u0001\u0000\u0000\u0000\u015e\u015c\u0001\u0000"+
		"\u0000\u0000\u015e\u015f\u0001\u0000\u0000\u0000\u015fE\u0001\u0000\u0000"+
		"\u0000\u0160\u015e\u0001\u0000\u0000\u0000\u0161\u0166\u0003H$\u0000\u0162"+
		"\u0163\u0007\u0005\u0000\u0000\u0163\u0165\u0003H$\u0000\u0164\u0162\u0001"+
		"\u0000\u0000\u0000\u0165\u0168\u0001\u0000\u0000\u0000\u0166\u0164\u0001"+
		"\u0000\u0000\u0000\u0166\u0167\u0001\u0000\u0000\u0000\u0167G\u0001\u0000"+
		"\u0000\u0000\u0168\u0166\u0001\u0000\u0000\u0000\u0169\u016e\u0003J%\u0000"+
		"\u016a\u016b\u0007\u0006\u0000\u0000\u016b\u016d\u0003J%\u0000\u016c\u016a"+
		"\u0001\u0000\u0000\u0000\u016d\u0170\u0001\u0000\u0000\u0000\u016e\u016c"+
		"\u0001\u0000\u0000\u0000\u016e\u016f\u0001\u0000\u0000\u0000\u016fI\u0001"+
		"\u0000\u0000\u0000\u0170\u016e\u0001\u0000\u0000\u0000\u0171\u0172\u0005"+
		"-\u0000\u0000\u0172\u0179\u0003J%\u0000\u0173\u0174\u0005 \u0000\u0000"+
		"\u0174\u0179\u0003J%\u0000\u0175\u0176\u0005!\u0000\u0000\u0176\u0179"+
		"\u0003J%\u0000\u0177\u0179\u0003L&\u0000\u0178\u0171\u0001\u0000\u0000"+
		"\u0000\u0178\u0173\u0001\u0000\u0000\u0000\u0178\u0175\u0001\u0000\u0000"+
		"\u0000\u0178\u0177\u0001\u0000\u0000\u0000\u0179K\u0001\u0000\u0000\u0000"+
		"\u017a\u017e\u0003N\'\u0000\u017b\u017d\u0007\u0007\u0000\u0000\u017c"+
		"\u017b\u0001\u0000\u0000\u0000\u017d\u0180\u0001\u0000\u0000\u0000\u017e"+
		"\u017c\u0001\u0000\u0000\u0000\u017e\u017f\u0001\u0000\u0000\u0000\u017f"+
		"M\u0001\u0000\u0000\u0000\u0180\u017e\u0001\u0000\u0000\u0000\u0181\u018b"+
		"\u0003P(\u0000\u0182\u018b\u0003^/\u0000\u0183\u018b\u0003:\u001d\u0000"+
		"\u0184\u018b\u0005;\u0000\u0000\u0185\u0186\u0005.\u0000\u0000\u0186\u0187"+
		"\u0003<\u001e\u0000\u0187\u0188\u0005/\u0000\u0000\u0188\u018b\u0001\u0000"+
		"\u0000\u0000\u0189\u018b\u0003`0\u0000\u018a\u0181\u0001\u0000\u0000\u0000"+
		"\u018a\u0182\u0001\u0000\u0000\u0000\u018a\u0183\u0001\u0000\u0000\u0000"+
		"\u018a\u0184\u0001\u0000\u0000\u0000\u018a\u0185\u0001\u0000\u0000\u0000"+
		"\u018a\u0189\u0001\u0000\u0000\u0000\u018bO\u0001\u0000\u0000\u0000\u018c"+
		"\u018d\u0005;\u0000\u0000\u018d\u018f\u0005.\u0000\u0000\u018e\u0190\u0003"+
		"V+\u0000\u018f\u018e\u0001\u0000\u0000\u0000\u018f\u0190\u0001\u0000\u0000"+
		"\u0000\u0190\u0191\u0001\u0000\u0000\u0000\u0191\u0192\u0005/\u0000\u0000"+
		"\u0192Q\u0001\u0000\u0000\u0000\u0193\u0194\u0005\n\u0000\u0000\u0194"+
		"\u0196\u0005.\u0000\u0000\u0195\u0197\u0003X,\u0000\u0196\u0195\u0001"+
		"\u0000\u0000\u0000\u0196\u0197\u0001\u0000\u0000\u0000\u0197\u0198\u0001"+
		"\u0000\u0000\u0000\u0198\u0199\u0005/\u0000\u0000\u0199\u019a\u00054\u0000"+
		"\u0000\u019aS\u0001\u0000\u0000\u0000\u019b\u019c\u0005\u000b\u0000\u0000"+
		"\u019c\u019d\u0005.\u0000\u0000\u019d\u019e\u0003Z-\u0000\u019e\u019f"+
		"\u0005/\u0000\u0000\u019f\u01a0\u00054\u0000\u0000\u01a0U\u0001\u0000"+
		"\u0000\u0000\u01a1\u01a6\u0003<\u001e\u0000\u01a2\u01a3\u00055\u0000\u0000"+
		"\u01a3\u01a5\u0003<\u001e\u0000\u01a4\u01a2\u0001\u0000\u0000\u0000\u01a5"+
		"\u01a8\u0001\u0000\u0000\u0000\u01a6\u01a4\u0001\u0000\u0000\u0000\u01a6"+
		"\u01a7\u0001\u0000\u0000\u0000\u01a7W\u0001\u0000\u0000\u0000\u01a8\u01a6"+
		"\u0001\u0000\u0000\u0000\u01a9\u01ae\u0003<\u001e\u0000\u01aa\u01ab\u0005"+
		"5\u0000\u0000\u01ab\u01ad\u0003<\u001e\u0000\u01ac\u01aa\u0001\u0000\u0000"+
		"\u0000\u01ad\u01b0\u0001\u0000\u0000\u0000\u01ae\u01ac\u0001\u0000\u0000"+
		"\u0000\u01ae\u01af\u0001\u0000\u0000\u0000\u01afY\u0001\u0000\u0000\u0000"+
		"\u01b0\u01ae\u0001\u0000\u0000\u0000\u01b1\u01b6\u0003<\u001e\u0000\u01b2"+
		"\u01b3\u00055\u0000\u0000\u01b3\u01b5\u0003\\.\u0000\u01b4\u01b2\u0001"+
		"\u0000\u0000\u0000\u01b5\u01b8\u0001\u0000\u0000\u0000\u01b6\u01b4\u0001"+
		"\u0000\u0000\u0000\u01b6\u01b7\u0001\u0000\u0000\u0000\u01b7[\u0001\u0000"+
		"\u0000\u0000\u01b8\u01b6\u0001\u0000\u0000\u0000\u01b9\u01bc\u0005;\u0000"+
		"\u0000\u01ba\u01bc\u0003^/\u0000\u01bb\u01b9\u0001\u0000\u0000\u0000\u01bb"+
		"\u01ba\u0001\u0000\u0000\u0000\u01bc]\u0001\u0000\u0000\u0000\u01bd\u01be"+
		"\u0005;\u0000\u0000\u01be\u01bf\u00052\u0000\u0000\u01bf\u01c0\u0003<"+
		"\u001e\u0000\u01c0\u01c1\u00053\u0000\u0000\u01c1_\u0001\u0000\u0000\u0000"+
		"\u01c2\u01c3\u0005\f\u0000\u0000\u01c3\u01c6\u0005.\u0000\u0000\u01c4"+
		"\u01c7\u0003\n\u0005\u0000\u01c5\u01c7\u0005;\u0000\u0000\u01c6\u01c4"+
		"\u0001\u0000\u0000\u0000\u01c6\u01c5\u0001\u0000\u0000\u0000\u01c7\u01c8"+
		"\u0001\u0000\u0000\u0000\u01c8\u01c9\u0005/\u0000\u0000\u01c9a\u0001\u0000"+
		"\u0000\u0000(dfq{\u0087\u009e\u00a1\u00ac\u00b3\u00b7\u00bb\u00c9\u00d1"+
		"\u00da\u00e5\u00e9\u00ed\u00fc\u010e\u0118\u011c\u0126\u012e\u0133\u0146"+
		"\u014e\u0156\u015e\u0166\u016e\u0178\u017e\u018a\u018f\u0196\u01a6\u01ae"+
		"\u01b6\u01bb\u01c6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}