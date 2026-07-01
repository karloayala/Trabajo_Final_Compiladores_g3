from miniparserVisitor import miniparserVisitor

class SemanticAnalyzer(miniparserVisitor):

    def __init__(self):
        self.symbolTable = {}
        self.errors = []

    # ====================================================
    # VARIABLES
    # ====================================================
    def visitVariableDeclaration(self, ctx):

        tipo = ctx.type_().getText()

        for var in ctx.variableList().variable():

            nombre = var.IDENTIFIER().getText()

            # duplicadas
            if nombre in self.symbolTable:
                self.errors.append(
                    f"Error Semántico: La variable '{nombre}' ya fue declarada."
                )
            else:
                self.symbolTable[nombre] = tipo

            # inicialización (si existe)
            if var.expression():
                tipoExpr = self.getExpressionType(var.expression())

                if tipoExpr != "desconocido" and tipoExpr != tipo:
                    self.errors.append(
                        f"Error Semántico: No se puede inicializar '{nombre}' ({tipo}) con '{tipoExpr}'."
                    )

        return self.visitChildren(ctx)

    # ====================================================
    # ASIGNACIONES
    # ====================================================
    def visitAssignment(self, ctx):

        if ctx.IDENTIFIER():
            nombre = ctx.IDENTIFIER().getText()
        else:
            nombre = ctx.arrayAccess().IDENTIFIER().getText()

        # no declarada
        if nombre not in self.symbolTable:
            self.errors.append(
                f"Error Semántico: La variable '{nombre}' no ha sido declarada."
            )
            return self.visitChildren(ctx)

        tipoVar = self.symbolTable[nombre]
        tipoExpr = self.getExpressionType(ctx.expression())

        if tipoExpr != "desconocido" and tipoExpr != tipoVar:
            self.errors.append(
                f"Error Semántico: No se puede asignar '{tipoExpr}' a '{tipoVar}' en '{nombre}'."
            )

        return self.visitChildren(ctx)

    # ====================================================
    # ARRAYS
    # ====================================================
    def visitArrayAccess(self, ctx):

        nombre = ctx.IDENTIFIER().getText()

        if nombre not in self.symbolTable:
            self.errors.append(
                f"Error Semántico: El arreglo '{nombre}' no ha sido declarado."
            )

        return self.visitChildren(ctx)

    # ====================================================
    # IF (CORREGIDO ESTILO C/C++)
    # ====================================================
    def visitIfStatement(self, ctx):

        tipoCond = self.getExpressionType(ctx.expression())

        # C/C++ permite int, float, bool como condición
        if tipoCond == "string":
            self.errors.append(
                f"Error Semántico: la condición del IF no puede ser tipo '{tipoCond}'."
            )

        return self.visitChildren(ctx)

    # ====================================================
    # WHILE
    # ====================================================
    def visitWhileStatement(self, ctx):

        tipoCond = self.getExpressionType(ctx.expression())

        if tipoCond == "string":
            self.errors.append(
                f"Error Semántico: la condición del WHILE no puede ser tipo '{tipoCond}'."
            )

        return self.visitChildren(ctx)

    # ====================================================
    # PRIMARY (uso de variables)
    # ====================================================
    def visitPrimary(self, ctx):

        if ctx.IDENTIFIER():

            nombre = ctx.IDENTIFIER().getText()

            if nombre not in self.symbolTable:
                self.errors.append(
                    f"Error Semántico: la variable '{nombre}' no ha sido declarada."
                )

        return self.visitChildren(ctx)

    # ====================================================
    # TIPADO DE EXPRESIONES
    # ====================================================
    def getExpressionType(self, ctx):

        texto = ctx.getText()

        # float
        if "." in texto:
            try:
                float(texto)
                return "float"
            except:
                pass

        # int
        if texto.isdigit():
            return "int"

        # char/string simplificado
        if texto.startswith('"') and texto.endswith('"'):
            return "string"

        if texto.startswith("'") and texto.endswith("'"):
            return "char"

        # variable
        if texto in self.symbolTable:
            return self.symbolTable[texto]

        # operadores relacionales → bool implícito
        if any(op in texto for op in [">", "<", ">=", "<=", "==", "!="]):
            return "bool"

        return "desconocido"

    # ====================================================
    # ERRORES
    # ====================================================
    def printErrors(self):

        print("\n====================================")
        print("ANÁLISIS SEMÁNTICO")
        print("====================================")

        if not self.errors:
            print("No se encontraron errores semánticos.")
        else:
            for e in self.errors:
                print(e)