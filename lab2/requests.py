import re
from pyswip import Prolog

prolog = Prolog()
prolog.consult('../lab1/city.pl')


def what_can_grow(fact: str):
    subject = fact.split()[-1].lower()
    subjects = {
        "плантация": "plantation(CanGrow)",
        "лагерь лесорубов": "lumberjack_camp(CanGrow)",
        "кокосовый комбайн": "coconut_combine(CanGrow)"
    }
    print(list(prolog.query(subjects[subject])))


