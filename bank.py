import sys 
def bankoper(initalBal,deposit,withdraw):
    totalBal = initalBal+deposit
    updatedBal = totalBal-withdraw

    return totalBal , updatedBal

if __name__ == "__main__":
    initalBal = int(sys.argv[1])
    deposit= int(sys.argv[2])
    withdraw =int(sys.argv[3])

    totalBal,updatedBal = bankoper(initalBal,deposit,withdraw)

    print ("Total Balance :",totalBal)
    print(" Updated Balance:",updatedBal)


