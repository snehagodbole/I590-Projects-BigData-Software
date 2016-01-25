
import sys

#This function iterates from 1 to n and if n is multiple of 2 it returns fizz if multiple of 3 returns buzz and if both returns fizzbuzz
def fizzbuzz(n) :
    string="Entered Integer value is "
    string+=str(n)
    print string
    
    numbers=range(1,n+1)
    for i in numbers:
        if i%2 == 0:
            print 'fizz'

        if i%3 == 0:
            print 'buzz'
            
        if i%2 == 0 and i%3 == 0:
            print 'fizzbuzz'    
            
            

if __name__ == '__main__':
   argc = len(sys.argv)

if argc < 2:
    print "Please pass any integer value as command line argument e.g python C:/Users/sneha/AppData/Local/Temp/7zO40FD4C3D/fizzbuzz.py 10"

    sys.exit();
elif argc == 2:
    n=int(sys.argv[1])
    fizzbuzz(n)
