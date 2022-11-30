from decimal import Decimal

def task_01_money(rubles, coins, amount):
    return (rubles + (coins/100)) * amount

print(task_01_money(1, 2 ,3))

#def task_02_sign(number):
    #if number > 0:
        #return '+1'
    #if number < 0:
        #return '-1'
    #if :
        #return '0'
#print(task_02_sign(1))
#print(task_02_sign(-1))
#print(task_02_sign('jniiubnui'))
