:- consult('buildings.pl').
:- dynamic(build_price/2).

% цена каждого здания
% ресурсы
build_price(plantation, 1500).
build_price(wood, 750).
build_price(coconut, 800).
build_price(farm, 900).
build_price(mine, 1200).

% промышленность
build_price(boat, 14500).
build_price(cans, 6500).
build_price(car, 22000).
build_price(cheese, 10500).
build_price(chocolate, 6500).
build_price(cigars, 13600).
build_price(clothes, 18000).
build_price(electronics, 25000).
build_price(fabric, 10500).
build_price(furniture, 10000).
build_price(industry_leather, 4800).
build_price(jewellery, 9500).
build_price(juice, 12000).
build_price(medicine, 28000).
build_price(plastmass, 10500).
build_price(planks, 4700).
build_price(rum, 9600).
build_price(steel, 9500).
build_price(weapon, 18000).

% жилые
build_price(conventillo, 4850).
build_price(bunkhouse, 1500).
build_price(flophouse, 2150).
build_price(tenement, 2650).
build_price(countryhouse, 1100).
build_price(apartments, 3750).
build_price(house, 1850).
build_price(mansion, 1550).
build_price(modern_apartment, 8650).
build_price(modern_mansion, 2050).
build_price(highest_modern_mansion, 3000).

% развлечения
build_price(tavern, 1200).
build_price(circus, 4800).
build_price(funfair_pier, 7350).
build_price(restaurant, 2600).
build_price(amusement_park, 18400).
build_price(stadium, 21000).

% роскошные развлечения
build_price(theater, 5300).
build_price(cabaret, 5000).
build_price(casino, 9200).
build_price(opera, 9880).
build_price(gourmet, 16000).
build_price(yacht, 11800).

% СМИ и образование
build_price(newspaper, 1800).
build_price(radiostation, 2400).
build_price(tvstation, 8200).
build_price(school, 11500).
build_price(college, 16500).

% здравоохранение
build_price(clinic, 3000).
build_price(hospital, 7800).
build_price(research_hospital, 7800).

% наука
build_price(library, 3600).
build_price(science_lab, 16000).
build_price(space_program, 42000).

% магазины
build_price(grocery, 1200).
build_price(mall, 7250).

% войска
build_price(fort, 4000).
build_price(barracks, 6000).
build_price(armybase, 20000).
build_price(aircraft_carrier, 35000).
build_price(drons, 12000).

% электричество
electricity_price(coal, 12000).      
electricity_price(oil, 12000).      
electricity_price(sun, 18000). 
electricity_price(uranium, 32000).