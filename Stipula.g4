grammar Stipula;

// Struttura del linguaggio

stipula :  'stipula' contractId=ID '{' assetsDecl? fieldsDecl? agreement functionDecl+ '}' EOF ;

assetsDecl : 'assets' assetId+=ID (',' assetId+=ID)* ;

fieldsDecl : 'fields' fieldInit (',' fieldInit)* ;

fieldInit : fieldId=ID ('=' value=(BOOL | TIMEDELTA | NUMBER | DATESTRING | STRING))? ;

agreement : 'agreement' '(' partyId+=ID (',' partyId+=ID)* ')' '(' fieldId+=ID (',' fieldId+=ID)* ')' '{' agree+ '}' '=>' '@' stateId=ID ;

agree : partyId+=ID (',' partyId+=ID)* ':' fieldId+=ID (',' fieldId+=ID)* ;

functionDecl : '@' startStateId=ID partyId=ID ':' functionId=ID '(' (fieldId+=ID (',' fieldId+=ID)*)? ')' '['(assetId+=ID (',' assetId+=ID)*)? ']' ('(' precondition=expression ')')? '{' functionBody '}' '=>' '@' endStateId=ID ;

functionBody : statement* eventDecl* ;

statement : ifThenElse | assetOperation | fieldOperation ;

ifThenElse : 'if' '(' condition=expression ')' '{' ifBody=functionBody '}' 'else' ( '{' elseBody=functionBody '}' | ifThenElse) ;

assetOperation : left=expression '-o' (right=ID ',')? destination=ID ;

fieldOperation : left=expression '->' right=ID ;

eventDecl : trigger=timeExpression '>>' '@' startStateId=ID '{' statement* '}' '=>' '@' endStateId=ID ;



// Espressioni temporali

timeExpression : NOW (PLUS right=timeExpression1)? | DATESTRING | ID ;

timeExpression1 : left=(TIMEDELTA | ID) (PLUS right=timeExpression1)? ;



// Operazioni

expression : left=expression1 (operator=(AND | OR) right=expression)? ;

expression1 : NOT? expression2 ;

expression2 : left=expression3 (operator=(EQ | NEQ | GE | LE | GEQ | LEQ) right=expression2)? ;

expression3 : left=expression4 (operator=(PLUS | MINUS) right=expression3)? ;

expression4 : left=expression5 (operator=(TIMES | DIVISION) right=expression4)? ;

expression5 : MINUS? expression6 ;

expression6 : NOW | BOOL | TIMEDELTA | NUMBER | DATESTRING | STRING | ID | '(' expression ')' ;



// Lexer rules

NOT : '!' ;
AND : '&&' ;
OR : '||' ;

EQ : '==' ;
NEQ : '!=' ;
LE : '<' ;
GE : '>' ;
LEQ : '<=' ;
GEQ : '>=' ;

PLUS : '+' ;
MINUS : '-' ;
TIMES : '*' ;
DIVISION : '/' ;

NOW : 'now' ;

BOOL : TRUE | FALSE ;
TRUE : 'true' ;
FALSE : 'false' ;
TIMEDELTA : INTEGER [YMDhm]? | NUMBER 's' ;
NUMBER : INTEGER ('.' [0-9]*)? ;
INTEGER : '0' | [1-9] [0-9]* ;
DATESTRING : '"' [0-9] [0-9] [0-9] [0-9] '-' ('0' [1-9] | '1' [0-2]) '-' ('0' [1-9] | [1-2] [0-9] | '3' [0-1]) '"' | '\'' [0-9] [0-9] [0-9] [0-9] '-' ('0' [1-9] | '1' [0-2]) '-' ('0' [1-9] | [1-2] [0-9] | '3' [0-1]) '\'' ;
STRING : '\'' ~('\'')+ '\'' | '"' ~('"')+ '"' ;

ID : [a-zA-Z] ([a-zA-Z] | [0-9] | '_')* ;

WS : [ \t\r\n] -> skip;

LINECOMMENT : '//' ~[\r\n]* -> skip ;
BLOCKCOMMENT : '/*' ('*' ~'/' | ~'*')* '*/' -> skip ;
