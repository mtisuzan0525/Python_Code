from Logic import *

teachers = Symbol("MrsTeacher")
police = Symbol("MrsPolice")
players = Symbol("MrsPlayer")
characters = [teachers, police, players]


classroom = Symbol("classroom")
policestation = Symbol("policestation")
feild = Symbol("feild")
rooms = [classroom, policestation, feild]

bat_ball = Symbol("bat_ball")
books = Symbol("books")
revolver = Symbol("revolver")

weapons = [bat_ball, books, revolver]

symbols = characters + rooms + weapons

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"{symbol}: YES")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room and a weapon.
knowledge = And(
    Or(teachers, police, players),
    Or(classroom, policestation, feild),
    Or(bat_ball, books, revolver)
)

# Initial cards
knowledge.add(And(
    Not(teachers), Not(policestation), Not(books)
))

# Unknown card
knowledge.add(Or(
    Not(players), Not(feild), Not(revolver)
))

# Known cards
knowledge.add(Not(police))
knowledge.add(Not(classroom))

check_knowledge(knowledge)
