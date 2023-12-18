'''
visitor.py
'''
from datetime import datetime
import re

from generated.StipulaVisitor import StipulaVisitor
from generated.StipulaParser import StipulaParser

from classes.exceptions.symbolexception import SymbolException
from classes.exceptions.fieldexception import FieldException
from classes.exceptions.expiredexception import ExpiredException
from classes.data import visitoroutput
from classes.data.functionvisitorentry import FunctionVisitorEntry
from classes.data.eventvisitorentry import EventVisitorEntry
from classes.data.visitoroutput import VisitorOutput
from classes.data.valuedependency import ValueDependency



class Visitor(StipulaVisitor):



    def __init__(self):
        StipulaVisitor.__init__(self)
        self.visitor_output = VisitorOutput()



    # Visit a parse tree produced by StipulaParser#stipula.
    def visitStipula(self, ctx:StipulaParser.StipulaContext):
        # Analizzo i field
        self.visitFieldDecl(ctx.fieldDecl())
        # Analizzo l'init
        self.visitInitStateDecl(ctx.initStateDecl())
        # Analizzo le funzioni
        for function_decl_context in ctx.functionDecl():
            self.visitFunctionDecl(function_decl_context)
        # Rimozione di eventi non raggiungibili e pulizia degli stati
        self.visitor_output.clear_events()
        # Calcolo dei tempi stipula
        self.visitor_output.compute_Ts()
        # Controllo della sequenza temporale
        self.visitor_output.clear_time()
        # Calcolo il dead-code
        self.visitor_output.compute_dead_code()
        return self.visitor_output



    # Visit a parse tree produced by StipulaParser#fieldDecl.
    def visitFieldDecl(self, ctx:StipulaParser.FieldDeclContext):
        self.visitor_output.field_id_set.update({field_id.text for field_id in ctx.fieldId})



    # Visit a parse tree produced by StipulaParser#initStateDecl.
    def visitInitStateDecl(self, ctx:StipulaParser.InitStateDeclContext):
        self.visitor_output.Q0 = ctx.stateId.text
        self.visitor_output.R[self.visitor_output.Q0] = set()



    # Visit a parse tree produced by StipulaParser#functionDecl.
    def visitFunctionDecl(self, ctx:StipulaParser.FunctionDeclContext):
        function_visitor_entry = FunctionVisitorEntry(ctx.startStateId.text, ctx.partyId.text, ctx.functionId.text, ctx.endStateId.text)
        self.visitor_output.add_visitor_entry(function_visitor_entry)
        # Analizzo gli eventi
        for event_decl_context in ctx.functionBody().eventDecl():
            self.visitor_output.add_event_definition(self.visitEventDecl(event_decl_context), function_visitor_entry)



    # Visit a parse tree produced by StipulaParser#eventDecl.
    def visitEventDecl(self, ctx:StipulaParser.EventDeclContext):
        # Le time expression devono essere nella forma `now + t`
        event_visitor_entry = EventVisitorEntry(ctx.startStateId.text, 'Ev', ctx.getSourceInterval()[0], ctx.endStateId.text)
        try:
            value_dependency = self.visitExpression(ctx.trigger)
            self.visitor_output.add_visitor_entry(event_visitor_entry)
            self.visitor_output.t[event_visitor_entry] = value_dependency.value
            self.visitor_output.dependency_t_dict[event_visitor_entry] = value_dependency.dependency_set
        except ExpiredException as exception:
            self.visitor_output.expired_code[event_visitor_entry] = exception.date_str
        return event_visitor_entry



    # Visit a parse tree produced by StipulaParser#expression.
    def visitExpression(self, ctx:StipulaParser.ExpressionContext):
        # Nelle time expression non sono ammessi `&&` e `||`
        if ctx.operator:
            raise SymbolException(ctx.operator.text)
        # Nelle time expression non è ammesso questo livello
        if ctx.right:
            raise SymbolException(ctx.right.getText())
        return self.visitExpression1(ctx.left)



    # Visit a parse tree produced by StipulaParser#expression1.
    def visitExpression1(self, ctx:StipulaParser.Expression1Context):
        # Nelle time expression non è ammesso `!`
        if ctx.NOT():
            raise SymbolException(ctx.NOT().getText())
        return self.visitExpression2(ctx.expression2())



    # Visit a parse tree produced by StipulaParser#expression2.
    def visitExpression2(self, ctx:StipulaParser.Expression2Context):
        # Nelle time expression non sono ammessi `==`, `!=`, `>`, `<`, `>=` e `<=`
        if ctx.operator:
            raise SymbolException(ctx.operator.text)
        # Nelle time expression non è ammesso questo livello
        if ctx.right:
            raise SymbolException(ctx.right.getText())
        return self.visitExpression3(ctx.left)



    # Visit a parse tree produced by StipulaParser#expression3.
    def visitExpression3(self, ctx:StipulaParser.Expression3Context):
        left_value_dependency = self.visitExpression4(ctx.left)
        right_value_dependency = ValueDependency(0, set())
        if ctx.operator:
            if ctx.right:
                right_value_dependency = self.visitExpression3(ctx.right)
            match ctx.operator.type:
                case StipulaParser.PLUS:
                    left_value_dependency.value += right_value_dependency.value
                case StipulaParser.MINUS:
                    left_value_dependency.value -= right_value_dependency.value
        return ValueDependency(left_value_dependency.value, left_value_dependency.dependency_set.union(right_value_dependency.dependency_set))



    # Visit a parse tree produced by StipulaParser#expression4.
    def visitExpression4(self, ctx:StipulaParser.Expression4Context):
        left_value_dependency = self.visitExpression5(ctx.left)
        right_value_dependency = ValueDependency(1, set())
        if ctx.operator:
            if ctx.right:
                right_value_dependency = self.visitExpression4(ctx.right)
            match ctx.operator.type:
                case StipulaParser.TIMES:
                    left_value_dependency.value *= right_value_dependency.value
                case StipulaParser.DIVISION:
                    left_value_dependency.value /= right_value_dependency.value
        return ValueDependency(left_value_dependency.value, left_value_dependency.dependency_set.union(right_value_dependency.dependency_set))



    # Visit a parse tree produced by StipulaParser#expression5.
    def visitExpression5(self, ctx:StipulaParser.Expression5Context):
        value_dependency = self.visitExpression6(ctx.expression6())
        return ValueDependency((-1 if ctx.MINUS() else 1) * value_dependency.value, value_dependency.dependency_set)



    # Visit a parse tree produced by StipulaParser#expression6.
    def visitExpression6(self, ctx:StipulaParser.Expression6Context):
        # Nelle time expression non sono ammessi valori booleani
        if ctx.BOOL():
            raise SymbolException(ctx.BOOL().getText())
        # Nelle time expression non sono ammesse stringhe
        if ctx.STRING():
            if not re.match(r'\"\d{2}\/\d{2}\/\d{4}\"$', ctx.STRING().getText()):
                raise SymbolException(ctx.STRING().getText())
            # Il delta è calcolato in secondi
            second_delta = (datetime.strptime(ctx.STRING().getText(), '"%d/%m/%Y"') - datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
            if second_delta < 0:
                raise ExpiredException(ctx.STRING().getText()[1:-1])
            return ValueDependency(second_delta, set())
        # `now` si considera 0
        if ctx.NOW():
            return ValueDependency(0, set())
        if ctx.NUMBER():
            return ValueDependency(float(ctx.NUMBER().getText()), set())
        # Gestione dei parametri di funzione e dei field
        if ctx.ID():
            if ctx.ID().getText() not in self.visitor_output.field_id_set:
                raise SymbolException(ctx.ID().getText())
            return ValueDependency(0, {ctx.ID().getText()})
        if ctx.expression():
            return self.visitExpression(ctx.expression())
