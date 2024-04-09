import random
print("IDEAS")
print()
def add():
  f = open("my.ideas", "a+")
  idea = input("What is your idea? ")
  f.write(f"{idea}\n")
  f.close()

def show():
  f = open("my.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)

while True:
  menu = input("1: Add an idea\n2: Show a random idea\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    show()
  else:
    break


