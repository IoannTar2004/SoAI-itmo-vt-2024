from requests import *


class RequestPattern:
    patterns = {
        "Что может выращивать": what_can_grow
    }

    def get(self, request: str):
        for obj in list(self.patterns.keys()):
            if request.startswith(obj):
                return self.patterns[obj]
        return None
