'switch ( X ) {
'case 1:
'foo (10) ;
'break ;
'case 2:
'foo2 ( X ) ;
'break ;
'case 3:
'foo (5) ;
'break ;
'otherwise :
'print ( ’ Erro ’)
'}

x=int(input)
if x==1:
    foo(10)
elif x==2:
    foo2(5)
elif x==3:
    foo3(5)
elif x>3:
    print('ERRO')