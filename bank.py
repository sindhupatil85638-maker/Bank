def bankoper(initalBal,deposit,withdraw):
    totalBal = initalBal+deposit
    updatedBal = totalBal-withdraw

    return totalBal , updatedBal

if __name__ == "__main__":
    initalBal = int(input("Enter amount as initial Balance"))
    deposit= int(input("Enter amount as deposit"))
    withdraw =int(input("Enter amout as withdraw"))

    totalBal,updatedBal = bankoper(initalBal,deposit,withdraw)

    print ("Total Balance :",totalBal)
    print(" Updated Balance:",updatedBal)


