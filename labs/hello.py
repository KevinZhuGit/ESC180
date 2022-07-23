name1 = "Kevin Zhu"
name2 = "Sujit Peramanu"
greetee = input("What is your name? ")

print(f"Hello, {name1}\nHello, {name2}")

print("Hello " + name1, "\nHello ", name2)

print(f"Hello, {name1} and {name2}. Your names are {name1} and {name2}.\
     Hi there. Your names are still {name1} and {name2}.")

name1 = "Prof. Cluett"
name2 = "Prof. Thywissen"

if greetee == "Lord Voldemort":
    print("I'm not talking to you.")
else:
    print(f"Hello {greetee}.")


def test():
    global a
