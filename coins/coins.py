# name of student: Amar Nagim

import time

# input van de gebruiker
toPay = int(float(input('Amount to pay: '))* 100) #
payed = int(float(input('Payed amount: ')) * 100) #
change = payed - toPay #

# variables 
fivehundred = 0
threehundred = 0
twohundred = 0
fifty = 0
twenty = 0
ten = 0
five = 0
two = 0
one = 0


# if statements voor de waardeverandering
if change > 0:
  coinValue = 500

  while change > 0 and coinValue > 0:
    nrCoins = change // coinValue

    if nrCoins > 0:
      print(f'Return maximal {nrCoins} coins of {coinValue} cents!')
      nrCoinsReturned = int(input(f'How many coins of {str(coinValue)} cents did you return?'))
      if coinValue == 500:
       fivehundred += nrCoinsReturned
      elif coinValue == 300:
       threehundred += nrCoinsReturned
      elif coinValue == 50:
       fifty += nrCoinsReturned
      elif coinValue == 20:
       twenty += nrCoinsReturned
      elif coinValue == 10:
       ten += nrCoinsReturned
      elif coinValue == 5:
       five += nrCoinsReturned 
      elif coinValue == 2:
       coinValue = 1

      else:
       coinValue = 0  

      change -= nrCoinsReturned * coinValue 

if coinValue == 500:
  coinValue = 300
elif coinValue == 300:
  coinValue = 200 
elif coinValue == 200:
  coinValue = 50          
elif coinValue == 50:
  coinValue = 20     
elif coinValue == 20:
  coinValue = 10    
elif coinValue == 10:
  coinValue = 5
elif coinValue == 5:
  coinValue = 2
elif coinValue == 2:
  coinValue = 1  
else:
  coinValue = 0          








# Eindprints

if change > 0:
  print(f'Change not returned: {str(change)} cents')
  print('Money given back:')

  print(f""" 
  
  5 eurocenten         : {str(fivehundred)}
  3 eurocenten         : {str(threehundred)}
  2 eurocenten         : {str(twohundred)}
  50 eurocenten         : {str(fifty)}
  20 eurocenten         : {str(twenty)}
  10 eurocenten         : {str(ten)}
  5 eurocenten         : {str(five)}
  2 eurocenten         : {str(two)}
  1 eurocenten         : {str(one)}
  """)

else:
  print(f""" 
  
  500 eurocenten         : {str(fivehundred)}
  300 eurocenten         : {str(threehundred)}
  200 eurocenten         : {str(twohundred)}
  50 eurocenten         : {str(fifty)}
  20 eurocenten         : {str(twenty)}
  10 eurocenten         : {str(ten)}
  5 eurocenten         : {str(five)}
  2 eurocenten         : {str(two)}
  1 eurocenten         : {str(one)}
  """)
  print('done')


  












