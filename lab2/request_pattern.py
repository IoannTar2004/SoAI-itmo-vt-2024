from requests import *


class RequestPattern:
    patterns = {
        "что может выращивать": what_can_grow,
        "что даёт": what_can_give,
        "что может добывать шахта": what_can_mine,
        "что может производить": what_can_produce
    }

    def get(self, request: str):
        for obj in list(self.patterns.keys()):
            if request.lower().startswith(obj):
                return self.patterns[obj]
        return None
