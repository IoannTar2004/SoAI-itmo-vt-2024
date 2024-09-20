from requests import *


class RequestPattern:
    patterns = {
        "что может выращивать": what_can_grow,
        "что даёт": what_can_give,
        "что может добывать шахта": what_can_mine,
        "что может производить": what_can_produce,
        "какое сырьё использует": what_resource_use,
        "построить здание": build,
        "какие здания построены": what_buildings_built,
        "снести здание": destroy_building,
        "какая тактика развития": city_development
    }

    def get(self, request: str):
        for obj in list(self.patterns.keys()):
            if request.lower().startswith(obj):
                return self.patterns[obj]
        return None
