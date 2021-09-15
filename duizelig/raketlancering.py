# Amar Nagim
# Vanaf 30 terugtellen tot de raketlancering. Print elke tel en print de lancering.

import time
    
print(f'De raketlancering zal over 30 seconden plaatsvinden:')
time.sleep(1)

countDown = 31

while countDown > 0:
    countDown -= 1
    time.sleep(1)
    print(countDown)

if countDown == 0:
    print('Raket is gelanceert.')



 
