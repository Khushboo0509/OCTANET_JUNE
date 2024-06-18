#**************ATM INTERFACE****************
import time
print("Please insert your card")
time.sleep(5)
password=1234
pin=int(input("Enter Your Atm pin:"))
balance=5000
if(pin==password):
 while True:
  print("""********WELCOME*******
       1:Check Balance
       2:Deposit
       3:Withdraw
       4:Exit""")
  try:
   choice=int(input("Enter Your Choice:"))
  except:
   print("Wrong choice!!Enter Again")
   continue
  if choice==1:
    print(f"Your Total balance is {balance}")
  elif choice==2:
    try:
      deposit_amt=float(input("Enter amount to deposit:"))
      if(deposit_amt>0):
        balance+=deposit_amt
        print(f"Amount is credited in your account {deposit_amt}")
        print(f"Updated balance is {balance}")
    except:
      print("Invalid Amount")     
  elif choice==3:
    try:
      withdraw_amt=float(input("Enter amount for withdraw:"))
      if(balance>=withdraw_amt and withdraw_amt>0):
         balance-=withdraw_amt
         print(f"Amount is debited from your account {withdraw_amt}")
         print(f"Updated balance is {balance}")
      else:
         print("Insufficient balance")   
    except:
      print("Invalid Amount")     
  elif choice==4:
    print("THANK YOU FOR USING OUR ATM")
    break   

else:
 print("Wrong pin entered!!Try Again")