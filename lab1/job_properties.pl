:- consult('buildings.pl').
:- consult('wealth_props.pl').

% здесь описаны характеристики рабочих мест для каждого здания 
%               (здание, достаток, образование, кол-во рабочих мест, качество работы)

% ресурсы
job(plantation, poor, uneducated, 8, 40).
job(lumberjack_camp, poor, uneducated, 6, 40).
job(coconut_combine, poor, uneducated, 6, 40).
job(farm, poor, uneducated, 4, 40).
job(mine, poor, uneducated, 5, 40).

% промышленность
job(boat, well-off, school, 5, 55).
job(cans, well-off, uneducated, 8, 50).
job(car, well-off, school, 10, 65).
job(cheese, well-off, uneducated, 4, 60).
job(chocolate, well-off, school, 5, 60).
job(cigars, well-off, school, 5, 65).
job(clothes, well-off, uneducated, 4, 60).
job(electronics, well-off, school, 8, 50).
job(fabric, well-off, uneducated, 10, 55).
job(furniture, well-off, uneducated, 5, 60).
job(jewellery, well-off, school, 4, 70).
job(juice, well-off, uneducated, 5, 55).
job(medicine, well-off, school, 6, 70).
job(plastmass, well-off, uneducated, 5, 55).
job(steel, well-off, school, 8, 55).
job(weapon, well-off, uneducated, 8, 60).

% электричество
job(coal, well-off, school, 6, 60).      
job(oil, 12000, well-off, school, 6, 60).      
job(sun, 18000, well-off, school, 3, 65). 
job(uranium, super_rich, college, 4, 80).

% развлечения
job(tavern, poor, uneducated, 3, 40).
job(circus, poor, uneducated, 6, 45).
job(funfair_pier, poor, uneducated, 6, 45).
job(restaurant, poor, uneducated, 4, 45).
job(amusement_park, poor, uneducated, 6, 50).
job(stadium, poor, uneducated, 50).

% роскошные развлечения
job(theater, well-off, school, 6, 50).
job(cabaret, well-off, school, 4, 50).
job(casino, well-off, school, 6, 60).
job(opera, well-off, school, 8, 60).
job(gourmet, well-off, school, 6, 65).
job(yacht, poor, uneducated, 4, 75).

% СМИ и образование
job(newspaper, well-off, school, 4, 60).
job(radiostation, well-off, school, 2, 65).
job(tvstation, well-off, school, 4, 70).
job(school, well-off, school, 4, 50).
job(college, rich, college, 3, 70).

% здравоохранение
job(clinic, well-off, college, 2, 70).
job(hospital, rich, college, 4, 65).
job(research_hospital, rich, college, 4, 65).

% наука
job(library, well-off, school, 3, 60).
job(science_lab, rich, college, 5, 70).
job(space_program, super_rich, college, 10, 80).

% магазины
job(grocery, poor, uneducated, 2, 55).
job(mall, poor, uneducated, 8, 55).

% религия
job(chaptel, poor, school, 2, 55).
job(church, well-off, school, 3, 65).
job(cathedral, rich, college, 4, 80).

% войска
job(pirate, well-off, uneducated, 4, 50).
job(fort, poor, school, 8, 35).
job(barracks, well-off, school, 8, 40).
job(armybase, well-off, school, 2, 65).
job(aircraft_carrier, rich, school, 4, 80).
job(drons, rich, school, 4, 75).