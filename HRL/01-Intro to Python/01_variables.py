# Hongjun Wu
# 20180208
# Python test files. This file test on variable and basic calculations.

price = 8.5
weight = 7.5

money = weight * price

# 卧槽toString原来是这么写的啊
print('You need to pay this amount: ' + money.__str__())

print('Now I will give you five bucks backs.')

money -= 5

print('Now just pay: ' + money.__str__())
