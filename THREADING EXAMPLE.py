'''
Example of how to control a loop using the terminal while having the loop run continuously in the background using threading
by Andrew Shaw
'''

from time import sleep
from threading import Thread

counter = 0

tFlag1 = 1 # This is a flag variable that will tell the cycle thread when to stop counting
tFlag2 = 1 # Variable that tells the prompt thread that the cycle thread has stopped.

def promptThread():
      global tFlag1
      while tFlag2 == True:
            print('Enter "stop" to stop or "count" for the counter')
            qVar = input() # qvar stores the variable that the user inputs for a command
            if qVar == 'stop':
                  tFlag1 = False # This triggers the promptThread's Flag to go false
                  while tFlag2 == True: # Waits for cycleThread to return a Flag saying it's done
                        print('Stopping') # It does this over and over to show that it's stopping
                        sleep(1)
                  print('Stopped')
                  break # This breaks the top level while loop after getting a flag from the cycleThread
            elif qVar == 'count':
                  print('The counter is at {}'.format(counter))
      print('\n\nCounting has been successfully stopped')

def cycleThread():
      global tFlag2
      global counter
      print()
      print('Counting has started\n\n')
      while tFlag1 == True: # Check to make sure there isn't a flag from the promptThread to stop, then continue the cycle
            counter += 1
            sleep(.5)
      # When a flag to stop is recieved from promptThread, the previous while loop stops and moves to here
      tFlag2 = False # Flag to promptThread that everything is done here and to stop it's own thread.

promptThread = Thread(target=promptThread)
cycleThread = Thread(target=cycleThread)

print('Press enter to start')
input()

promptThread.start()
cycleThread.start()
promptThread.join()
cycleThread.join()

print()
print('\n\nProgram ended with the counter at {}\n\n'.format(counter))
