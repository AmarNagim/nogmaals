# Amar Nagim
# Herhaal een input() tot het resultaat daarvan gelijk is aan ‘quit’ Print het aantal iteraties per iteratie.

count = int('1')

def input1():
 global word
 word = input(f'Poging {count}; Vul hier het woord quit in: ').lower()
 print('')

input1()

print('')

while word != 'quit':
    print('Ik begreep u niet.')
    count += 1
    input1()
    

if word == 'quit':
    print('Je hebt het woord \'quit\' geschreven!')
    print('Einde script.')
    
    
