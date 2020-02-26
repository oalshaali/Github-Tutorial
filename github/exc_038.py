from exc_037 import Employee

class CEO(Employee):
	def __init__(self, name, years_experience, past_employers, onForbes, fortune500):
		super().__init__(name, years_experience, past_employers)
		self.onForbes = onForbes
		self.fortune500 = fortune500

	def needsPromotion(self):
		return(False)

def main():
	ceo1 = CEO(name = "Jeff Bezos", years_experience = 20, past_employers = ["Amazon"], onForbes = True, fortune500 = True)

	print(ceo1.needsPromotion())

if __name__ == '__main__':
	main()