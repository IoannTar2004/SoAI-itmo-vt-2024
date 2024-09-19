from request_pattern import RequestPattern
from pyswip import Prolog
import re
import os



def execute_prolog(request):
    facts = re.split('\\s*\\.\\s*', request)
    req = RequestPattern()
    for fact in facts:
        req.get(fact)


if __name__ == '__main__':
    # execute_prolog('Что может выращивать плантация')
    p = Prolog()
    # p.consult('a.pl')