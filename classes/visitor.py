'''
visitor.py
'''
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from generated.StipulaVisitor import StipulaVisitor
from generated.StipulaParser import StipulaParser

from classes.exceptions.symbolexception import SymbolException
from classes.exceptions.expiredexception import ExpiredException
from classes.data import visitoroutput
from classes.data.functionvisitorentry import FunctionVisitorEntry
from classes.data.eventvisitorentry import EventVisitorEntry
from classes.data.visitoroutput import VisitorOutput
from classes.data.valuedependency import ValueDependency
from classes.data.codereference import CodeReference



class Visitor(StipulaVisitor):



    def __init__(self):
        StipulaVisitor.__init__(self)
        self.now_date_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
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
        # Costruzione di R a partire da C
        self.visitor_output.compute_R()
        # Rimozione di eventi non raggiungibili e pulizia degli stati
        self.visitor_output.clear_events()
        # TODO DSE queste altre parti bisogna sistemarle
        # # Calcolo dei tempi stipula
        # self.visitor_output.compute_T()
        # # Controllo della sequenza temporale
        # self.visitor_output.clear_time()
        # # Calcolo il dead-code
        # self.visitor_output.compute_dead_code()
        return self.visitor_output



    # Visit a parse tree produced by StipulaParser#fieldDecl.
    def visitFieldDecl(self, ctx:StipulaParser.FieldDeclContext):
        for field_init_context in ctx.fieldInit():
            self.visitFieldInit(field_init_context)



    # Visit a parse tree produced by StipulaParser#fieldInit.
    def visitFieldInit(self, ctx:StipulaParser.FieldInitContext):
        self.visitor_output.add_field_id(ctx.fieldId.text)



    # Visit a parse tree produced by StipulaParser#initStateDecl.
    def visitInitStateDecl(self, ctx:StipulaParser.InitStateDeclContext):
        self.visitor_output.Q0 = ctx.stateId.text



    # Visit a parse tree produced by StipulaParser#functionDecl.
    def visitFunctionDecl(self, ctx:StipulaParser.FunctionDeclContext):
        function_visitor_entry = FunctionVisitorEntry(ctx.startStateId.text, ctx.partyId.text, ctx.functionId.text, ctx.endStateId.text, CodeReference(ctx.start.line, ctx.stop.line))
        self.visitor_output.add_visitor_entry(function_visitor_entry)
        # Analizzo gli eventi
        for event_decl_context in ctx.functionBody().eventDecl():
            self.visitor_output.add_event_definition(self.visitEventDecl(event_decl_context), function_visitor_entry)



    # Visit a parse tree produced by StipulaParser#eventDecl.
    def visitEventDecl(self, ctx:StipulaParser.EventDeclContext):
        # Le time expression devono essere nella forma `now + t`
        event_visitor_entry = EventVisitorEntry(ctx.startStateId.text, 'Ev', ctx.getSourceInterval()[0], ctx.endStateId.text, CodeReference(ctx.start.line, ctx.stop.line))
        try:
            value_dependency = self.visitTimeExpression(ctx.trigger)
            self.visitor_output.add_visitor_entry(event_visitor_entry)
            self.visitor_output.add_dependency_t(event_visitor_entry, value_dependency.dependency_set)
            self.visitor_output.set_t(event_visitor_entry, value_dependency.value)
        except ExpiredException as exception:
            self.visitor_output.set_expired_code(event_visitor_entry, exception.date_str)
        return event_visitor_entry



    # Visit a parse tree produced by StipulaParser#timeExpression.
    def visitTimeExpression(self, ctx:StipulaParser.TimeExpressionContext):
        if ctx.NOW():
            # Time expressione nella forma `now + t`
            right_value_dependency = ValueDependency(timedelta(seconds=0), set())
            if ctx.right:
                right_value_dependency = self.visitTimeExpression1(ctx.right)
            return ValueDependency(right_value_dependency.value, right_value_dependency.dependency_set.union({visitoroutput.NOW}))
        if ctx.DATESTRING():
            # Il delta è calcolato in secondi
            time_delta = datetime.fromisoformat(ctx.DATESTRING().getText()[1:-1]) - self.now_date_time
            if time_delta < timedelta(seconds=0):
                raise ExpiredException(ctx.DATESTRING().getText()[1:-1])
            return ValueDependency(time_delta, set())
        if ctx.ID():
            # Gli id devono essere di field del contratto
            if ctx.ID().getText() not in self.visitor_output.field_id_set:
                raise SymbolException(ctx.ID().getText())
            return ValueDependency(timedelta(seconds=0), {ctx.ID().getText()})



    # Visit a parse tree produced by StipulaParser#timeExpression1.
    def visitTimeExpression1(self, ctx:StipulaParser.TimeExpression1Context):
        match ctx.left.type:
            case StipulaParser.TIMEDELTA:
                # Bisogna leggere correttamente l'ordine di grandezza
                match ctx.left.text[-1]:
                    case 'Y':
                        left_value_dependency = ValueDependency((self.now_date_time + relativedelta(years=int(ctx.left.text[:-1]))) - self.now_date_time, set())
                    case 'M':
                        left_value_dependency = ValueDependency((self.now_date_time + relativedelta(months=int(ctx.left.text[:-1]))) - self.now_date_time, set())
                    case 'D':
                        left_value_dependency = ValueDependency(timedelta(days=int(ctx.left.text[:-1])), set())
                    case 'h':
                        left_value_dependency = ValueDependency(timedelta(hours=int(ctx.left.text[:-1])), set())
                    case 'm':
                        left_value_dependency = ValueDependency(timedelta(minutes=int(ctx.left.text[:-1])), set())
                    case 's':
                        left_value_dependency = ValueDependency(timedelta(seconds=float(ctx.left.text[:-1])), set())
                    case _:
                        left_value_dependency = ValueDependency(timedelta(minutes=int(ctx.left.text)), set())
            case StipulaParser.ID:
                # Gli id devono essere i field del contratto
                if ctx.left.text not in self.visitor_output.field_id_set:
                    raise SymbolException(ctx.left.text)
                left_value_dependency = ValueDependency(timedelta(seconds=0), {ctx.left.text})
        right_value_dependency = ValueDependency(timedelta(seconds=0), set())
        if ctx.right:
            right_value_dependency = self.visitTimeExpression1(ctx.right)
        return ValueDependency(left_value_dependency.value + right_value_dependency.value, left_value_dependency.dependency_set.union(right_value_dependency.dependency_set))
