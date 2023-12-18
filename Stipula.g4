grammar Stipula;

// Struttura del linguaggio

stipula :  'stipula' contractId=ID '{' assetDecl? fieldDecl initStateDecl agreement functionDecl* '}' EOF ; 

assetDecl : 'asset' assetId+=ID (',' assetId+=ID)* ;

fieldDecl : 'field' fieldId+=ID (',' fieldId+=ID)* ;

initStateDecl : 'init' stateId=ID ;

agreement : 'agreement' '(' partyId+=ID (',' partyId+=ID)* ')' '(' fieldId+=ID (',' fieldId+=ID)* ')' '{' agree+ '}' '=>' '@' stateId+=ID ;

agree : partyId+=ID (',' partyId+=ID)* ':' fieldId+=ID (',' fieldId+=ID)* ;

functionDecl : '@' startStateId=ID partyId=ID ':' functionId=ID '(' (fieldId+=ID (',' fieldId+=ID)*)? ')' '['(assetId+=ID (',' assetId+=ID)*)? ']' '(' precondition=expression ')' '{' functionBody '}' '=>' '@' endStateId=ID ;

functionBody : statement* eventDecl* ;

statement : ifThenElse | assetOperation | fieldOperation ;

ifThenElse : 'if' '(' condition=expression ')' '{' ifBody=functionBody '}' 'else' ( '{' elseBody=functionBody '}' | ifThenElse) ;

assetOperation : left=expression '-o' (right=ID ',')? destination=ID ;

fieldOperation : left=expression '->' right=ID ;

eventDecl : trigger=expression '>>' '@' startStateId=ID '{' statement* '}' '=>' '@' endStateId=ID ;



// Operazioni

expression : left=expression1 (operator=(AND | OR) right=expression)? ;

expression1 : NOT? expression2 ;

expression2 : left=expression3 (operator=(EQ | NEQ | GE | LE | GEQ | LEQ) right=expression2)? ;

expression3 : left=expression4 (operator=(PLUS | MINUS) right=expression3)? ;

expression4 : left=expression5 (operator=(TIMES | DIVISION) right=expression4)? ;

expression5 : MINUS? expression6 ;

expression6 : NOW | BOOL | NUMBER | STRING | ID | '(' expression ')' ;



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
NUMBER : '0' | [1-9] [0-9]* | ('0' | [1-9] [0-9]*) '.' [0-9]* ;
STRING : '\'' ~('\'')+ '\'' | '"' ~('"')+ '"' ;

ID : [a-zA-Z] ([a-zA-Z] | [0-9] | '_')* ;

WS : [ \t\r\n] -> skip ;

LINECOMMENT : '//' ~[\r\n]* -> skip ;
BLOCKCOMMENT : '/*' ('*' ~'/' | ~'*')* '*/' -> skip ;