### Docker commands to run this script:
# First time (creating and running the container)
# docker run -it 026dd7906e
# -i interactive | -t add console
# Next times
# docker start -a -i mystifying_swartz
# -a attach mode for start command | -i interactive

from random import randint

min_number = int(input('Please enter the min number: '))
max_number = int(input('Please enter the max number: '))

if (max_number < min_number): 
  print('Invalid input - shutting down...')
else:
  rnd_number = randint(min_number, max_number)
  print(rnd_number)
