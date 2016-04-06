x = 1
soma = 0
qnt = int(input(" quantos usuarios tem na turma ? " ))
while x<=qnt :
    n = int(input(" %d. Digite a idade :" % x ))
    soma = soma + n
    x = x + 1
    media = soma / qnt
print(" media : %5.2f" % (soma/qnt) )
    
if( media >= 0 and media <= 25 ):
    print(" turma jovem ")
if ( media >= 26 and media <=60 ):
    print( " turma adulta " )
if ( media > 60 ):
    print ( " turma idosa " )
    
