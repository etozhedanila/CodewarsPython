def count_change(money, coins):
	if len(coins) < 1:
		return 0
	if money < 0:
		return 0
	if money == 0:
		return 1
	if len(coins) > 1:
		return count_change(money - coins[0],coins) + count_change(money, coins[1::])
	else:
		return count_change(money - coins[0], coins)

print(count_change(4, [1,2]))
print(count_change(11, [5,7]))

