debt = -20.0 
continuePaying = True 

while continuePaying:
 answer = input('payed? give positive amount or Q to quit') 
 if answer != 'Q':
  payed = float(answer) 
  debt = debt + payed
  print('debt is now ' + str(debt)) 
 continuePaying = answer != Q and debt < 0 
if debt < 0:
 print('still having a debt: ' + str(debt)) 

else:
 print('we are even')