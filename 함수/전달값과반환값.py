def deposit(balance,money):
    print('입금이 완료되었습니다. 잔액은 {}원입니다.'.format(balance+money))
    return balance + money
def withdraw(balance, money):
    if balance > money:
        print('출금이 완료되었습니다. 잔액은 {}입니다.'.format(balance-money))
    else:
        print('출금이 완료되지않았습니다. 잔액은 {}입니다.'.format(balance))
def withdraw_night(balance,money):
    commission = 100 #수수료 100
    return commission, balance - money - commission


balance =0
# print(deposit(balance,1000))
balance = deposit(balance,2000)
print(balance)

withdraw(balance,3500)

commission,balance = withdraw_night(balance,500)
print('수수료는 {}이고 잔액은 {}이다.'.format(commission,balance))