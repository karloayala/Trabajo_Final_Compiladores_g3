from miniparserVisitor import miniparserVisitor

class SemanticAnalyzer(miniparserVisitor):
    def __init__(self):
        # Pila de entornos para resolución de alcance (Scope Resolution)
        self.scopes = [{}]  # El índice 0 es el ámbito global
        self.errors = []

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def declare_variable(self, nombre, tipo):
        # Validación de declaraciones en el ámbito actual
        current_scope = self.scopes[-1]
        if nombre in current_scope:
            self.errors.append(f"Error Semántico: La variable '{nombre}' ya fue declarada en este ámbito.")
            return False
        current_scope[nombre] = tipo
        return True

    def lookup_variable(self, nombre):
        # Buscar de adentro hacia afuera (Resolución de alcance jerárquica)
        for scope in reversed(self.scopes):
            if nombre in scope:
                return scope[nombre]
        return None

    # =====================================
    # Manejo de Funciones y Bloques
    # =====================================
    def visitFunctionDefinition(self, ctx):
        nombre_func = ctx.IDENTIFIER().getText()
        tipo_retorno = ctx.type_().getText()
        # Declarar la función en el ámbito global antes de entrar a su cuerpo
        self.scopes[0][nombre_func] = f"function->{tipo_retorno}"
        
        self.enter_scope()
        # Registrar parámetros si existen
        if ctx.parameterList():
            for param in ctx.parameterList().parameter():
                p_tipo = param.type_().getText()
                p_nombre = param.IDENTIFIER().getText()
                self.declare_variable(p_nombre, p_tipo)
                
        # Visitar el cuerpo del bloque sin crear otro scope duplicado
        result = self.visitChildren(ctx.block())
        self.exit_scope()
        return result

    def visitBlock(self, ctx):
        # Si viene de un if/while/for, requiere un nuevo ámbito local
        # Para evitar duplicar el scope de funciones, solo creamos si el padre no es FunctionDefinition
        if ctx.parentCtx.__class__.__name__ != 'FunctionDefinitionContext':
            self.enter_scope()
            result = self.visitChildren(ctx)
            self.exit_scope()
            return result
        return self.visitChildren(ctx)

    # =====================================
    # Declaración de variables
    # =====================================
    def visitVariableDeclaration(self, ctx):
        tipo = ctx.type_().getText()
        if ctx.variableList():
            for var in ctx.variableList().variable():
                nombre = var.IDENTIFIER().getText()
                self.declare_variable(nombre, tipo)
        return self.visitChildren(ctx)

    def visitVariableDeclarationFor(self, ctx):
        tipo = ctx.type_().getText()
        nombre = ctx.IDENTIFIER().getText()
        self.declare_variable(nombre, tipo)
        return self.visitChildren(ctx)

    # =====================================
    # Verificación de Declaración y Tipos
    # =====================================
    def visitAssignment(self, ctx):
        if ctx.IDENTIFIER():
            nombre = ctx.IDENTIFIER().getText()
        elif ctx.arrayAccess():
            nombre = ctx.arrayAccess().IDENTIFIER().getText()
        else:
            return self.visitChildren(ctx)

        tipo_var = self.lookup_variable(nombre)
        if not tipo_var:
            self.errors.append(f"Error Semántico: La variable '{nombre}' no ha sido declarada.")
        
        return self.visitChildren(ctx)

    def visitArrayAccess(self, ctx):
        nombre = ctx.IDENTIFIER().getText()
        tipo_var = self.lookup_variable(nombre)
        if not tipo_var:
            self.errors.append(f"Error Semántico: El arreglo '{nombre}' no ha sido declarado.")
        return self.visitChildren(ctx)

    def visitPrimaryExpression(self, ctx):
        if ctx.IDENTIFIER():
            nombre = ctx.IDENTIFIER().getText()
            if not self.lookup_variable(nombre):
                self.errors.append(f"Error Semántico: El identificador '{nombre}' no está declarado.")
        return self.visitChildren(ctx)

    def visitFunctionCall(self, ctx):
        nombre = ctx.IDENTIFIER().getText()
        if not self.lookup_variable(nombre):
            self.errors.append(f"Error Semántico: La función '{nombre}' no ha sido declarada.")
        return self.visitChildren(ctx)

    # =====================================
    # Mostrar errores
    # =====================================
    def printErrors(self):
        print("\n====================================")
        print("ANÁLISIS SEMÁNTICO")
        print("====================================")
        if len(self.errors) == 0:
            print("No se encontraron errores semánticos. ¡Excelente!")
        else:
            for error in self.errors:
                print(error)