import sys 
def bankoper(initalBal,deposit,withdraw):
    totalBal = initalBal+deposit
    updatedBal = totalBal-withdraw

    return totalBal , updatedBal

if __name__ == "__main__":
    initalBal = int(input("Enter amount as initialBal:"))
    deposit= int(input("Enter amount as deposit:"))
    withdraw =int(input("Enter amount as withdraw:"))

    totalBal,updatedBal = bankoper(initalBal,deposit,withdraw)

    print ("Total Balance :",totalBal)
    print(" Updated Balance:",updatedBal)


