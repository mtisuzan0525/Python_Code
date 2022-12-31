from Logic import *

teachers = Symbol("MrsTeacher")
police = Symbol("MrsPolice")
players = Symbol("MrsPlayer")

knowldege = And(
    Implication(Not(teachers), police),
    Or(police, players),
    Not(And(police, players)),
    police
)

print(model_check(knowldege, teachers))
