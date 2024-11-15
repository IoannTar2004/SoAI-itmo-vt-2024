from request_pattern import RequestPattern
import re


def execute_prolog(request):
    facts = re.split('\\s*\\.\\s*', request)
    req = RequestPattern()
    for fact in facts:
        func = req.get(fact)
        func(fact.lower()) if func is not None else print("Не понял вашего запроса.")


def start():
    print("Что вы хотите узнать?")
    while True:
        request = input()
        if request == "halt":
            break
        execute_prolog(request)

