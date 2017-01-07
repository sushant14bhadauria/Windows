array = {}

def start():
	
	x_o = int(input('Choice\n 1.Cross \n or\n 2.Circle \n for Player1'))
	
	
	def put_coordinates(Player):

		x_coordinates = int(input('Input x coordinate' + str(Player)))
		y_coordinates = int(input('Input y coordinate' + str(Player)))

		array[x_coordinates,y_coordinates] = Player

		print(array)

		switch_chance(Player)


	def switch_chance(Player):
		if (Player == 'o'):
			Player = 'x'
			put_coordinates(Player)

		else:
			Player = 'o'
			put_coordinates(Player)


	if(x_o == 1):
		Player1 = 'x'
		Player2 = 'o'

		put_coordinates(Player1)

	else:
		Player1 = 'o'
		Player2 = 'x'

		put_coordinates(Player1)

start()
	
	




