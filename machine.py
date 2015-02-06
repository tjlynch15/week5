

class CoinDispenser:

	coins = [25, 10,5,1]

	def make_change (self, amount):

		change = []

		change.append(amount//CoinDispenser.coins[0])
		remainder = amount % CoinDispenser.coins[0]

		change.append(remainder//CoinDispenser.coins[1])
		remainder = remainder % CoinDispenser.coins[1]

		change.append(remainder//CoinDispenser.coins[2])
		remainder = remainder % CoinDispenser.coins[2]

		change.append(remainder//CoinDispenser.coins[3])

		return change
	
