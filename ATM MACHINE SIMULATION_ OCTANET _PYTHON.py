# ATM Machine Simulation
import time
print("***WELCOME TO WOW BANK***")
print("PLEASE INSERT YOUR CARD")
time.sleep(2)

# Definition of variables
balance = 5000
history = []
pin = "1234"
chances = 3

# Function to display account balance
def get_balance():
  global balance
  return balance

# Function to withdraw cash
def withdraw():
  global balance
  amount = float(input("Please Enter withdrawal amount: Rs."))
  if amount <= balance:
    balance -= amount
    history.append(f"Withdrawal: -{amount}")
    return True
  return False

# Function to deposit cash
def deposit():
  global balance
  amount = float(input("Please Enter deposit amount: Rs."))
  balance += amount
  history.append(f"Deposit: +{amount}")
  return True

# Function to change PIN
def change_pin():
  global pin
  old_pin = input("Enter old PIN: ")
  new_pin = input("Enter new PIN: ")
  if old_pin == pin:
    pin = new_pin
    return True
  return False

# Function to display transaction history
def get_history():
  return history

# Main program
while True:
  print("**************************************************************")
  print("""
                      1.BALANCE
                      2.WITHDRAW BALANCE
                      3.DEPOSIT BALANCE
                      4.CHANGE PIN
                      5.TRANSACTION HISTORY
                      6.EXIT
                  """)
  choice = input("Enter your choice (1-6): ")
  if choice == "1":
    pin_input = input("Enter your PIN: ")
    if pin_input == pin:
      print(f"Your Current Balance is: Rs.{get_balance()}")
    else:
      chances -= 1
      print(f"Invalid PIN! You have {chances} chances left.")
      if chances == 0:
        print("Three incorrect PIN attempts.\nAccount locked for security reasons.\nTry again in 24 hours")
        print("**************************************************************")
        break
  elif choice == "2":
    pin_input = input("Enter your PIN: ")
    if pin_input == pin:
      if withdraw():
        print("Withdrawal successful!")
        print(f"Your Updated Balance is: Rs.{get_balance()}")
      else:
        print("Insufficient funds!")
    else:
      chances -= 1
      print(f"Invalid PIN! You have {chances} chances left.")
      if chances == 0:
        print("Three incorrect PIN attempts.\nAccount locked for security reasons.\nTry again in 24 hours")
        print("**************************************************************")
        break
  elif choice == "3":
    pin_input = input("Enter your PIN: ")
    if pin_input == pin:
      deposit()
      print("Deposit successful!")
      print(f"Your Updated Balance is: Rs.{get_balance()}")
    else:
      chances -= 1
      print(f"Invalid PIN! You have {chances} chances left.")
      if chances == 0:
        print("Three incorrect PIN attempts.\nAccount locked for security reasons.\nTry again in 24 hours")
        print("**************************************************************")
        break
  elif choice == "4":
    pin_input = input("Enter your PIN: ")
    if pin_input == pin:
      if change_pin():
        print("PIN changed successfully!")
      else:
        print("Authentication failed!")
    else:
      chances -= 1
      print(f"Invalid PIN! You have {chances} chances left.")
      if chances == 0:
        print("Three incorrect PIN attempts.\nAccount locked for security reasons.\nTry again in 24 hours")
        print("**************************************************************")
        break
  elif choice == "5":
    pin_input = input("Enter your PIN: ")
    if pin_input == pin:
      for transaction in get_history():
        print(transaction)
    else:
      chances -= 1
      print(f"Invalid PIN! You have {chances} chances left.")
      if chances == 0:
        print("Three incorrect PIN attempts.\nAccount locked for security reasons.\nTry again in 24 hours")
        print("**************************************************************")
        break
  elif choice == "6":
                print("**THANKYOU FOR USING WOW BANK**")
                print("**************************************************************")
                break
  else:
    print("Invalid choice!")
