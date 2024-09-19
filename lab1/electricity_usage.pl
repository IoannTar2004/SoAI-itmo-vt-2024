:- consult('goods.pl').
:- consult('buildings.pl').

% здания потребляющие электроэнергию в МВт
% промышленность
build_electricity(boat, 50).
build_electricity(cans, 80).
build_electricity(furniture, 105).
build_electricity(plastmass, 25).
build_electricity(car, 50).
build_electricity(electronics, 60).
build_electricity(clothes, 25).
build_electricity(medicine, 80).
build_electricity(juice, 30).

% жилые
build_electricity(conventillo, 20).
build_electricity(bunkhouse, 8).
build_electricity(flophouse, 10).
build_electricity(tenement, 32).
build_electricity(countryhouse, 2).
build_electricity(apartments, 18).
build_electricity(house, 3).
build_electricity(mansion, 5).
build_electricity(modern_apartment, 50).
build_electricity(modern_apartment, 18).
build_electricity(highest_modern_apartment, 18).

% развлечения
build_electricity(funfair_pier, 20).
build_electricity(amusement_park, 50).
build_electricity(stadium, 60).
build_electricity(casino, 25).
build_electricity(gourmet, 15).

% СМИ и образование
build_electricity(radiostation, 10).
build_electricity(tvstation, 45).
build_electricity(school, 8).
build_electricity(college, 15).

% наука
build_electricity(research_hospital, 35).
build_electricity(science_lab, 75).
build_electricity(space_program, 100).

% общественные службы
build_electricity(hospital, 35).
build_electricity(mall, 60).

% войска
build_electricity(drones, 50).