'''
visitor.py
'''
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from generated.StipulaVisitor import StipulaVisitor
from generated.StipulaParser import StipulaParser

from classes.exceptions.symbolexception import SymbolException
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
        self.visitFieldsDecl(ctx.fieldsDecl())
        # Analizzo l'init
        self.visitInitStateDecl(ctx.initStateDecl())
        # Analizzo le funzioni
        for function_decl_context in ctx.functionDecl():
            self.visitFunctionDecl(function_decl_context)
        # Rimuovo tutti gli eventi già scaduti
        self.visitor_output.compute_expired_code()
        # Calcolo RC
        self.visitor_output.compute_R()
        # Calcolo del warning-code
        self.visitor_output.compute_warning_code()
        # Calcolo l'unreachable-code
        self.visitor_output.compute_unreachable_code()
        return self.visitor_output



    # Visit a parse tree produced by StipulaParser#fieldDecl.
    def visitFieldsDecl(self, ctx:StipulaParser.FieldsDeclContext):
        for field_init_context in ctx.fieldInit():
            self.visitFieldInit(field_init_context)



    # Visit a parse tree produced by StipulaParser#fieldInit.
    def visitFieldInit(self, ctx:StipulaParser.FieldInitContext):
        value = None
        if ctx.value:
            match ctx.value.type:
                case StipulaParser.BOOL:
                    value = ctx.value.text == 'true'
                case StipulaParser.TIMEDELTA:
                    match ctx.value.text[-1]:
                        case 'Y':
                            value = (self.now_date_time + relativedelta(years=int(ctx.value.text[:-1]))) - self.now_date_time
                        case 'M':
                            value = (self.now_date_time + relativedelta(months=int(ctx.value.text[:-1]))) - self.now_date_time
                        case 'D':
                            value = timedelta(days=int(ctx.value.text[:-1]))
                        case 'h':
                            value = timedelta(hours=int(ctx.value.text[:-1]))
                        case 'm':
                            value = timedelta(minutes=int(ctx.value.text[:-1]))
                        case 's':
                            value = timedelta(seconds=float(ctx.value.text[:-1]))
                        case _:
                            value = timedelta(minutes=int(ctx.value.text))
                case StipulaParser.NUMBER:
                    value = float(ctx.value.text)
                case StipulaParser.DATESTRING:
                    value = datetime.fromisoformat(ctx.DATESTRING().getText()[1:-1]) - self.now_date_time
                case StipulaParser.STRING:
                    value = ctx.value.text[1:-1]
        self.visitor_output.set_field_id_value(ctx.fieldId.text, value)



    # Visit a parse tree produced by StipulaParser#initStateDecl.
    def visitInitStateDecl(self, ctx:StipulaParser.InitStateDeclContext):
        self.visitor_output.set_init_state_id(ctx.stateId.text)



    # Visit a parse tree produced by StipulaParser#functionDecl.
    def visitFunctionDecl(self, ctx:StipulaParser.FunctionDeclContext):
        function_visitor_entry = FunctionVisitorEntry(ctx.startStateId.text, ctx.partyId.text, ctx.functionId.text, ctx.endStateId.text, CodeReference(ctx.start.line, ctx.stop.line))
        field_id_set = set(ctx.fieldId)
        self.visitor_output.add_visitor_entry(function_visitor_entry)
        self.visitFunctionBody(ctx.functionBody(), function_visitor_entry, field_id_set)



    # Visit a parse tree produced by StipulaParser#functionBody.
    def visitFunctionBody(self, ctx:StipulaParser.FunctionBodyContext, function_visitor_entry, field_id_set):
        # Analizzo gli statement
        for statement_context in ctx.statement():
            self.visitStatement(statement_context)
        # Analizzo gli eventi
        for event_decl_context in ctx.eventDecl():
            self.visitor_output.set_event_definition(self.visitEventDecl(event_decl_context, field_id_set), function_visitor_entry)



    # Visit a parse tree produced by StipulaParser#statement.
    def visitStatement(self, ctx:StipulaParser.StatementContext):
        if ctx.fieldOperation():
            self.visitFieldOperation(ctx.fieldOperation())
    


    # Visit a parse tree produced by StipulaParser#fieldOperation.
    def visitFieldOperation(self, ctx:StipulaParser.FieldOperationContext):
        self.visitor_output.set_field_id_value(ctx.right.text, None)



    # Visit a parse tree produced by StipulaParser#eventDecl.
    def visitEventDecl(self, ctx:StipulaParser.EventDeclContext, field_id_set):
        # Le time expression devono essere nella forma `now + t`
        event_visitor_entry = EventVisitorEntry(ctx.startStateId.text, 'Ev', ctx.getSourceInterval()[0], ctx.endStateId.text, CodeReference(ctx.start.line, ctx.stop.line))
        value_dependency = self.visitTimeExpression(ctx.trigger, field_id_set)
        self.visitor_output.add_visitor_entry(event_visitor_entry)
        self.visitor_output.set_dependency_t(event_visitor_entry, value_dependency.dependency_tuple)
        self.visitor_output.set_t(event_visitor_entry, value_dependency.value)
        return event_visitor_entry



    # Visit a parse tree produced by StipulaParser#timeExpression.
    def visitTimeExpression(self, ctx:StipulaParser.TimeExpressionContext, field_id_set):
        if ctx.NOW():
            # Time expressione nella forma `now + t`
            right_value_dependency = ValueDependency(timedelta(seconds=0), ())
            if ctx.right:
                right_value_dependency = self.visitTimeExpression1(ctx.right, field_id_set)
            return ValueDependency(right_value_dependency.value, tuple(sorted([
                *right_value_dependency.dependency_tuple,
                visitoroutput.NOW
            ])))
        if ctx.DATESTRING():
            # Il delta è calcolato in secondi
            return ValueDependency(datetime.fromisoformat(ctx.DATESTRING().getText()[1:-1]) - self.now_date_time, ())
        if ctx.ID():
            # Gli id non possono essere presi dai parametri
            if ctx.ID().getText() in field_id_set:
                raise SymbolException(ctx.ID().getText())
            # Gli id devono essere di field del contratto
            if ctx.ID().getText() not in self.visitor_output.field_id_map:
                raise SymbolException(ctx.ID().getText())
            return ValueDependency(timedelta(seconds=0), (
                ctx.ID().getText(),
            ))



    # Visit a parse tree produced by StipulaParser#timeExpression1.
    def visitTimeExpression1(self, ctx:StipulaParser.TimeExpression1Context, field_id_set):
        match ctx.left.type:
            case StipulaParser.TIMEDELTA:
                # Bisogna leggere correttamente l'ordine di grandezza
                match ctx.left.text[-1]:
                    case 'Y':
                        left_value_dependency = ValueDependency((self.now_date_time + relativedelta(years=int(ctx.left.text[:-1]))) - self.now_date_time, ())
                    case 'M':
                        left_value_dependency = ValueDependency((self.now_date_time + relativedelta(months=int(ctx.left.text[:-1]))) - self.now_date_time, ())
                    case 'D':
                        left_value_dependency = ValueDependency(timedelta(days=int(ctx.left.text[:-1])), ())
                    case 'h':
                        left_value_dependency = ValueDependency(timedelta(hours=int(ctx.left.text[:-1])), ())
                    case 'm':
                        left_value_dependency = ValueDependency(timedelta(minutes=int(ctx.left.text[:-1])), ())
                    case 's':
                        left_value_dependency = ValueDependency(timedelta(seconds=float(ctx.left.text[:-1])), ())
                    case _:
                        left_value_dependency = ValueDependency(timedelta(minutes=int(ctx.left.text)), ())
            case StipulaParser.ID:
                # Gli id non possono essere presi dai parametri
                if ctx.left.text in field_id_set:
                    raise SymbolException(ctx.left.text)
                # Gli id devono essere i field del contratto
                if ctx.left.text not in self.visitor_output.field_id_map:
                    raise SymbolException(ctx.left.text)
                left_value_dependency = ValueDependency(timedelta(seconds=0), (
                    ctx.left.text,
                ))
        right_value_dependency = ValueDependency(timedelta(seconds=0), ())
        if ctx.right:
            right_value_dependency = self.visitTimeExpression1(ctx.right, field_id_set)
        return ValueDependency(left_value_dependency.value + right_value_dependency.value, tuple(sorted([
            *left_value_dependency.dependency_tuple,
            *right_value_dependency.dependency_tuple
        ])))
