__author__ = 'Sanhoj'


# import only system from os 
from os import system, name 

# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear') 

if __name__ == "__main__":
    # print out some text 
    print('hello geeks\n'*10) 

    # sleep for 2 seconds after printing output 
    sleep(4) 

    # now call function we defined above 
    clear() 
