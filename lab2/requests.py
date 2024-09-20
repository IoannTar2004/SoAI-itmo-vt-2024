import re
from pyswip import Prolog
from fact_dictionary import *

prolog = Prolog()
prolog.consult('../lab1/city.pl')


def print_result(title, result, key):
    print(title)
    for r in result:
        print("\t", r.get(key))


def get_query(pattern):
    try:
        return pattern
    except KeyError:
        return None


def what_can_produce_abstract(subject, bool, query, predicate_str):
    if bool:
        result = list(prolog.query(query))
        print_result(subject + f" {predicate_str}: ", result, "Result")
    else:
        print(f"Здание {subject} не {predicate_str}")


def what_can_grow(fact: str):
    subject = fact.split()[-1].lower()
    query = get_query(f"{russian_english.get(subject)}(Result)")
    what_can_produce_abstract(subject, subject in ["плантация", "лагерь_лесорубов", "кокосовый_комбайн"],
                              query, "может выращивать")


def what_can_give(fact: str):
    subject = fact.split()[-1].lower()
    query = f"farm({russian_english.get(subject)}, Result)"
    if subject in ["бык", "рыба", "овца", "крокодил", "свинья"]:
        result = list(prolog.query(query))
        print_result(subject + " даёт: ", result, "Result")
    else:
        print(f"{subject} ничего не даёт")


def what_can_mine(fact: str):
    subject = fact.split()[-1].lower()
    query = "mine(Result)"
    what_can_produce_abstract(subject, subject in ["шахта"], query, "может добывать")


def what_can_produce(fact: str):
    subject = fact.split()[-1].lower()
    if re.match("ферма_*", subject):
        match = re.search("ферма_(\\w+)", subject)
        animal = match.group(1)
        query = f"farm({russian_english.get(animal)}, Result)"
        what_can_produce_abstract(subject, russian_english.get(animal) is not None, query, "может производить")
    else:
        building = russian_english.get(subject)
        resource = english_russian.get(building)
        if building is not None:
            print(f"Здание {subject} производит {resource}")
        else:
            print(f"Здание {subject} не может производить")
