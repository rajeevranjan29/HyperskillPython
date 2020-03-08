import copy

class CoffeeMachine:
	def __init__(self):
		self.available_coffee = 0
		self.dif_available = 0

		self.initialization_sentence_list = ["Starting to make a coffee",
		                                     "Grinding coffee beans",
		                                     "Boiling water",
		                                     "Mixing boiled water with crushed coffee beans",
		                                     "Pouring coffee into the cup",
		                                     "Pouring some milk into the cup",
		                                     "Coffee is ready!",
		                                     "\n"]

		self.ingredients_dict = {
			"water": {
				"qtd_per_cup": 200,
				"type": "ml",
				"stock": 400,
				"cups_available": 0,
				"dif_available": 0,
			},
			"milk": {
				"qtd_per_cup": 50,
				"type": "ml",
				"stock": 540,
				"cups_available": 0,
				"dif_available": 0,
			},
			"coffee beans": {
				"qtd_per_cup": 15,
				"type": "grams",
				"stock": 120,
				"cups_available": 0,
				"dif_available": 0,
			},
			"disposable cups": {
				"qtd_per_cup": 1,
				"type": "cups",
				"stock": 9,
				"cups_available": 0,
				"dif_available": 0,
			},
		}

		self.money = 550

		self.coffees_dict = {
			"1": {"name": "espresso",
			      "ingredients": {
				      "water": 250,
				      "coffee beans": 16,
				      "money": 4,
				      "disposable cups": 1
			      }},
			"2": {"name": "latte",
			      "ingredients": {
				      "water": 350,
				      "milk": 75,
				      "coffee beans": 20,
				      "money": 7,
				      "disposable cups": 1
			      }},
			"3": {"name": "cappuccino",
			      "ingredients": {
				      "water": 200,
				      "milk": 100,
				      "coffee beans": 12,
				      "money": 6,
				      "disposable cups": 1}},
		}

		self.actions = {
			"buy": self.buy_coffee,
			"fill": self.fill_machine,
			"take": self.take_money,
			"remaining": self.stock_print,
			"exit": self.end_program
		}

	# Stage #1
	def init_machine(self):
		"""
		Inicializa Maquina da café
		Imprime no console as frases de inicialização
		"""
		for sentence in self.initialization_sentence_list:
			print(sentence)

	# Stage #2
	def sell_coffee(self):
		"""
		Efetua a venda de copos de café. Solicita a quantidade para vender e imprime no console a quantidade
		de ingredientes necessários
		"""
		cups = int(input("Write how many cups of coffee you will need: "))
		print(f"For {cups} cups of coffee you will need:")
		print(f"{self.ingredients_dict['water'].get('qtd_per_cup') * cups} ml of water")
		print(f"{self.ingredients_dict['milk'].get('qtd_per_cup') * cups} ml of milk")
		print(f"{self.ingredients_dict['coofee beans'].get('qtd_per_cup') * cups} g of coofee beans")
		print("\n")

	# Stage #3
	def update_stock(self, ingredient, new_stock):
		"""
		Atualiza a quantidade em estoque do ingrediente
		:param ingredient: ingrediente (chave do ingredients_dict)
		:param new_stock: Nova quantidade de estoque
		:return:
		"""
		# Atualiza estoque do ingrediente
		self.ingredients_dict[ingredient]['stock'] += new_stock

		self.ingredients_dict[ingredient]['cups_available'] = self.ingredients_dict[ingredient].get('stock') // \
		                                                      self.ingredients_dict[ingredient].get('qtd_per_cup')

		self.ingredients_dict[ingredient]['dif_available'] = self.ingredients_dict[ingredient].get('stock') / \
		                                                     self.ingredients_dict[ingredient].get('qtd_per_cup')

	def init_stock(self):
		"""
		Inicializa estoque
		Solicita as quantidades para cada ingrediente e atualiza o 'ingredients_dict'
		"""
		for ingr, value in self.ingredients_dict.items():
			new_stock = int(input(f"Write how many {self.ingredients_dict[ingr].get('type')} of {ingr} the "
			                      f"coffee machine has: "))
			self.update_stock(ingr, new_stock)

	def check_can_do_coffee(self):
		"""
		Verifica se a maquina pode fazer cafe
		:return:
		"""
		# Atualiza o total de copos disponiveis e quanto ainda pode ser feito,
		# baseado na quantidade individual de cada ingrediente
		self.available_coffee = int(min([y.get('cups_available') for (x, y) in self.ingredients_dict.items()]))
		self.dif_available = int(min([y.get('dif_available') for (x, y) in self.ingredients_dict.items()]))

		# Cria um set para indicar se pode ou nao fazer mais cafe
		has_more_coffee = set(map(lambda x: x >= 1, [y.get('dif_available') for (x, y) in self.ingredients_dict.items()]))

		if self.available_coffee >= self.cups:
			# if has_more_coffee is True:
			if True in has_more_coffee:
				print(
					f"Yes, I can make that amount of coffee (and even {self.dif_available - self.cups} more than that)")
			else:
				print("Yes, I can make that amount of coffee")
		else:
			print(f"No, I can make only {self.dif_available} cups of coffee")

	def ask_for_coffee(self):
		self.cups = int(input("Write how many cups of coffee you will need: "))
		self.check_can_do_coffee()

	# Stage 4
	def ask_action(self):
		"""
		Solicita a ação a ser executada e chama a mesma
		:return:
		"""
		action = input(f"Write action ({', '.join(self.actions.keys())}): ")
		if action == 'exit':
			return 'exit'

		self.actions[action]()


	def stock_print(self):
		"""
		Imprime o estoque atual
		"""
		print("The coffee machine has:")
		for ingr, atribute in self.ingredients_dict.items():
			print(f"{atribute['stock']} of {ingr}")

		# Imprime money
		print(f'${self.money} of money')

		print("\n")

	def buy_coffee(self):
		"""
		Efetua a venda do café
		:param coffee: Tipo de Café (chave do dicionario coffees_dict)
		:return:
		"""
		print("What do you want to buy? ", end='')
		# print(f"{[str(key) + ' - ' + value['name'] for (key, value) in self.coffees_dict.items()]}", ", back - to main menu: ", end='')
		print(f"{', '.join([str(key) + ' - ' + value['name'] for (key, value) in self.coffees_dict.items()])}", ", back - to main menu: ", end='')
		coffee = input()

		# Se escolheu voltar
		if coffee == 'back':
			return

		# Verifica se tem estoque
		if self.check_stock(coffee):
			for ingr, atribute in self.ingredients_dict.items():
				self.ingredients_dict[ingr]['stock'] -= self.coffees_dict[coffee]['ingredients'].get(ingr, 0)

			# Adiciona dinheiro a maquina
			self.money += self.coffees_dict[coffee]['ingredients']['money']

		print("\n")

	def fill_machine(self):
		"""
		Atualiza o estoque
		Solicita as quantidades para cada ingrediente e atualiza o 'ingredients_dict'
		"""
		for ingr, value in self.ingredients_dict.items():
			new_stock = int(input(f"Write how many {self.ingredients_dict[ingr]['type']} of {ingr} do "
			                      f"you want to add: "))
			self.update_stock(ingr, new_stock)

		print("\n")

	def take_money(self):
		print(f"I gave you ${self.money}")

		self.money = 0

		print("\n")

	# Stage 5
	def end_program(self):
		pass

	def check_stock(self, coffee):
		""" Itera pelo estoque e retorna se pode ou não fazer mais café"""
		msg = 'I have enough resources, making you a coffee!'

		# Faz um deep Copy do dicionario
		tmp_ingredients_stock = copy.deepcopy(self.ingredients_dict)

		for ingr, atribute in tmp_ingredients_stock.items():
			tmp_ingredients_stock[ingr]['stock'] -= self.coffees_dict[coffee]['ingredients'].get(ingr, 0)

		for ingr, atribute in tmp_ingredients_stock.items():
			if tmp_ingredients_stock[ingr]['stock'] < 0:
				print(f'Sorry, not enough {ingr}!')
				return False

		print(msg)

		return True


if __name__ == '__main__':
	machine = CoffeeMachine()
	# machine.stock_print()
	# machine.init_machine()
	# machine.sell_coffee()
	# machine.init_stock()
	# machine.ask_for_coffee()

	# Stage 4
	# machine.stock_print()
	# machine.ask_action()
	# machine.stock_print()

	# Stage 5
	while True:
		choice = machine.ask_action()

		if choice == 'exit':
			break
