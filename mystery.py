QUIT = 'q'

def main( ) :
   Mystery( )
   print()
   
def Mystery ( ):

   ch = input("Enter a char (q to quit): ")
   if (ch != QUIT):
      Mystery( )
      print(ch)
      
main ()
   
