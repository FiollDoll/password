from rich import print

admin = False
with open("AdminToken.txt", "w") as file:
	file.write("")
def start():
	global admin
	st = input("Write a cod: ")
	if st == "admin2007":
		print("Welcome, [green]admin[/green]")
		admin = True
		menu()
	elif st == "2007":
		print("Welcome, [green]user[/green]")
		menu()
	else:
		print("[red]Error[/red]")
		start()

def menu():
		print("New password: np\nMy passwords: mp\nclear: cls")
		m = input("")
		if m == "np":
			passw = input("Write your password: ")
			with open("passwords.txt", "a") as file:
				file.write(f"\n{passw}")
			menu()
		elif m == "mp":
			with open("passwords.txt") as file:
				print(file.read())
			menu()
		elif m == "cls":
			if admin == True:
				with open("passwords.txt", "w") as file:
					file.write(" ")
				menu()
			else:
				print("[red]Error[/red]")
				menu()
start()