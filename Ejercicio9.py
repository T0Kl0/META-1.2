total = int(input("CUANTO SE PAGARA? "))
pp = float(input ('La propina es 18%, 20%, 25%'))

print ('SOLO SE ADMITEN 4 PERSONAS POR CONSUMO POR CONTIGENCIA')
personas = int(input('CUANTAS PERSONAS SERAN?'))
while personas >4:
    print ('SOLO ES POSIBLE 3 PERSONAS, PERDON')
    personas = int(input('CUANTAS PERSONAS SON?'))
if personas == 4:
    Total = total + (total * pp)
    print ('EL TOTAL A PAGAR ES DE: $',Total,'\nCADA PERSONA PAGARA UN PORCENTAJE')
    p1= float(input('PAGARE EL: '))
    por1 = Total * p1
    p2= float(input('PAGARE EL: '))
    por2 = Total * p2
    p3= float(input('PAGARE EL: '))
    por3 = Total * p3
    p4= float(input('PAGARE EL: '))
    por4 = Total * p4
    print ('EL TOTAL A PAGAR ES DE: $',Total ,'\nLa persona 1 pago el: ', p1*100,'%', ' o $',por1, '\nLa persona 2 pago el: ', p2*100, '%',' o $',por2, '\nLa persona 3 pago el: ', p3*100, '%',' o $',por3, '\nLa persona 4 pago el: ', p4*100, '%',' o $',por4  )
elif personas == 3:
     Total = total + (total * pp)
     print ('EL TOTAL A PAGAR ES DE: $',Total,'\nCADA PERSONA PAGARA UN PORCENTAJE')
     p1= float(input('PAGARE EL: '))
     por1 = Total * p1
     p2= float(input('PAGARE EL: '))
     por2 = Total * p2
     p3= float(input('PAGARE EL: '))
     por3 = Total * p3
     print ('EL TOTAL A PAGAR ES DE: $',Total ,'\nLa persona 1 pago el: ', p1*100,'%', ' o $',por1, '\nLa persona 2 pago el: ', p2*100, '%',' o $',por2, '\nLa persona 3 pago el: ', p3*100, '%',' o $',por3)
elif personas == 2:
     Total = total + (total * pp)
     print ('EL TOTAL A PAGAR ES DE: $',Total,'\nCADA PERSONA PAGARA UN PORCENTAJE')
     p1= float(input('PAGARE EL: '))
     por1 = Total * p1
     p2= float(input('PAGARE EL: '))
     por2 = Total * p2
     print ('EL TOTAL A PAGAR ES DE: $',Total ,'\nLa persona 1 pago el: ', p1*100,'%', ' o $',por1, '\nLa persona 2 pago el: ', p2*100, '%',' o $',por2)
elif personas == 1:
     Total = total + (total * pp)
     print ('EL TOTAL A PAGAR ES DE: $',Total,'\nCADA PERSONA PAGARA UN PORCENTAJE')
     print ('EL TOTAL A PAGAR ES DE: $',Total ,'\nLA PERSONA PAGARA: ',100, '$',Total)