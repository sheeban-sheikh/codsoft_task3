import random
def password():
 while True: # Loop used because if user enters the length of password less than 8 it will try again
    user=int(input("Enter the desired length of password : "))
    letters="aAbBc@d!e#EfFg$GhHiI@jJkKlL&mMn@NoOp@PqQ$rRs#StTuU#VwWx@yY*Z"
    l=[]
    if user>=8:
      while user:
        password=random.choice(letters)
        l.append(password)
        user-=1
      new_password="".join(l)
      return new_password
    else:
        print("Atleast length should be 8.")
        print("Try Again!")
output=password()
print(f"Your Secret Password : {output}")
