class BankAccount:
	def __init__(self, account_type, amount):
		self.account_type = account_type
		self.amount = amount

	def deposit(self, deposit_amount):
		self.amount += deposit_amount

	def withdraw(self, withdrawal_amount):
		self.amount -= withdrawal_amount

	def fee(self, account_fee):
		self.amount -= account_fee

	def __str__(self):
		return "{} Amount: {}".format(self.account_type, self.amount)


denis = BankAccount("Savings", 100)


print(denis.account_type)
print(denis.amount)

denis.deposit(250)
print(denis.amount)

denis.withdraw(10)
print(denis.amount)

denis.fee(50)
print(denis.amount)

print(denis)

