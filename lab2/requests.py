import re
from pyswip import Prolog
from fact_dictionary import *

prolog = Prolog()
prolog.consult('../lab1/city.pl')


def print_result(title, result, key):
    print(title)
    for r in result:
        print("\t", english_russian[r.get(key)])


def what_can_produce_abstract(subject, bool, query, predicate_str):
    if bool:
        result = list(prolog.query(query))
        print_result(subject + f" {predicate_str}: ", result, "Result")
    else:
        print(f"Здание {subject} не {predicate_str}")


def what_can_grow(fact: str):
    subject = fact.split()[-1]
    query = f"{russian_english.get(subject)}(Result)"
    what_can_produce_abstract(subject, subject in ["плантация", "лагерь_лесорубов", "кокосовый_комбайн"],
                              query, "может выращивать")


def what_can_give(fact: str):
    subject = fact.split()[-1]
    query = f"farm({russian_english.get(subject)}, Result)"
    if subject in ["бык", "рыба", "овца", "крокодил", "свинья"]:
        result = list(prolog.query(query))
        print_result(subject + " даёт: ", result, "Result")
    else:
        print(f"{subject} ничего не даёт")


def what_can_mine(fact: str):
    subject = fact.split()[-1]
    query = "mine(Result)"
    what_can_produce_abstract(subject, subject in ["шахта"], query, "может добывать")


def what_can_produce(fact: str):
    subject = fact.split()[-1]
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


def what_resource_use(fact: str):
    def print_resource(subject, resource):
        print(f"Здание {subject} использует сырьё {resource}")

    subject = fact.split()[-1]
    if subject in ["тэц_на_угле", "тэц_на_нефти", "солнечная_эс", "аэс"]:
        print_resource(subject, russian_english[subject])
    if subject in ["сталелитейный_завод", "оружейный_завод", "автомобильный_завод", "шоколадная_фабрика",
                   "завод_электроники"]:
        query = f"industry({russian_english[subject]}, Res1, Res2)"
        result = list(prolog.query(query))
        resources = [english_russian[result[0]["Res1"]], english_russian[result[0]["Res2"]]]
        print_resource(subject, resources)
    else:
        try:
            query = f"industry({russian_english[subject]}, Res)"
            result = list(prolog.query(query))
            print_resource(subject, english_russian[result[0]["Res"]])
        except (KeyError, IndexError):
            print(f"Здание {subject} не использует никакое сырьё")


def build(fact: str):
    match = re.search("построить здание (\\w+) с id (\\d+) с работниками в количестве (\\d+)", fact)
    building, id, count = match.group(1), match.group(2), match.group(3)
    query = f"new_building({russian_english.get(building)}, {id}, {count})"
    result = list(prolog.query(query))
    print("Здание построено") if bool(result) else print("Здание не построено: проверьте корректность данных")


def destroy_building(fact: str):
    match = re.search("снести здание (\\w+) с id (\\d+)", fact)
    building, id = match.group(1), match.group(2)
    query = f"destroy_building({russian_english.get(building)}, {id})"
    result = list(prolog.query(query))
    print("Здание снесено")


def what_buildings_built(fact: str):
    result = list(prolog.query("build(Building, Id, Count)"))
    print("Информация о построенных зданиях")
    if len(result) > 0:
        for r in result:
            print(f"\t{r.get('Building')} - id: {r.get('Id')}, количество рабочих: {r.get('Count')}")
    else:
        print("Нет построенных зданий")


def city_development(fact: str):
    try:
        match = re.search("какая тактика развития, приносящая прибыль в день (\\d+), качество жилья рабочих (\\d+)", fact)
        purpose, quality = match.group(1), match.group(2)
        r = list(prolog.query(f"city_development({purpose}, {quality})"))
        print(r)
    except:
        print("Не понял вашего запроса")