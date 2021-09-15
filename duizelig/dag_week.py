# Amar Nagim
# Vraag een dag van de week op (ma,di,wo,do,vr,za,zo) Print alle dagen tot aan de opgegeven dag.

import time
import sys

print('')
print('Ik ga alle dagen van de week die voor de dag die jij invoert opnoemen:')
print('')
day = input('Voer hier een dag van de week in: ').lower()

while day == 'maandag':
    print('maandag')
    sys.exit()

while day == 'dinsdag':
    print('maandag en dinsdag')
    sys.exit()    

while day == 'woensdag':
    print('maandag, dinsdag en woensdag')
    sys.exit()       

while day == 'donderdag':
    print('maandag, dinsdag, woensdag en donderdag')
    sys.exit()       

while day == 'vrijdag':
    print('maandag, dinsdag, woensdag, donderdag en vrijdag')
    sys.exit() 

while day == 'zaterdag':
    print('maandag, dinsdag, woensdag, donderdag, vrijdag en zaterdag')
    sys.exit() 

while day == 'zondag':
    print('maandag, dinsdag, woensdag, donderdag, vrijdag, zaterdag en zondag')
    sys.exit()  
