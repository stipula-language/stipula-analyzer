# Generated from Stipula.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .StipulaParser import StipulaParser
else:
    from StipulaParser import StipulaParser

# This class defines a complete generic visitor for a parse tree produced by StipulaParser.

class StipulaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StipulaParser#stipula.
    def visitStipula(self, ctx:StipulaParser.StipulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#assetDecl.
    def visitAssetDecl(self, ctx:StipulaParser.AssetDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#fieldDecl.
    def visitFieldDecl(self, ctx:StipulaParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#initStateDecl.
    def visitInitStateDecl(self, ctx:StipulaParser.InitStateDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#agreement.
    def visitAgreement(self, ctx:StipulaParser.AgreementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#agree.
    def visitAgree(self, ctx:StipulaParser.AgreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#functionDecl.
    def visitFunctionDecl(self, ctx:StipulaParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#functionBody.
    def visitFunctionBody(self, ctx:StipulaParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#statement.
    def visitStatement(self, ctx:StipulaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#ifThenElse.
    def visitIfThenElse(self, ctx:StipulaParser.IfThenElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#assetOperation.
    def visitAssetOperation(self, ctx:StipulaParser.AssetOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#fieldOperation.
    def visitFieldOperation(self, ctx:StipulaParser.FieldOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#eventDecl.
    def visitEventDecl(self, ctx:StipulaParser.EventDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#timeExpression.
    def visitTimeExpression(self, ctx:StipulaParser.TimeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#timeExpression1.
    def visitTimeExpression1(self, ctx:StipulaParser.TimeExpression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#expression.
    def visitExpression(self, ctx:StipulaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#expression1.
    def visitExpression1(self, ctx:StipulaParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#expression2.
    def visitExpression2(self, ctx:StipulaParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#expression3.
    def visitExpression3(self, ctx:StipulaParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#expression4.
    def visitExpression4(self, ctx:StipulaParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#expression5.
    def visitExpression5(self, ctx:StipulaParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StipulaParser#expression6.
    def visitExpression6(self, ctx:StipulaParser.Expression6Context):
        return self.visitChildren(ctx)



del StipulaParser