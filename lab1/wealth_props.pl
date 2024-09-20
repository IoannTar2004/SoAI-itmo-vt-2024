:- consult('buildings.pl').

% достаток граждан
wealth(broke).        % разорившийся
wealth(poor).         % бедный
wealth(well-off).     % обеспеченный
wealth(rich).         % богатый
wealth(super_rich).   % несметно богатый

% здания, в которые могут прийти или жить граждане в зависимости от достатка

% жилые
build_wealth(shack, broke).
build_wealth(conventillo, poor).
build_wealth(bunkhouse, poor).
build_wealth(flophouse, poor).
build_wealth(tenement, poor).
build_wealth(countryhouse, well-off).
build_wealth(apartments, well-off).
build_wealth(house, well-off).
build_wealth(mansion, rich).
build_wealth(modern_apartment, well-off).
build_wealth(modern_mansion, rich).
build_wealth(highest_modern_mansion, super_rich).

% развлечения
build_wealth(tavern, poor).
build_wealth(circus, poor).
build_wealth(funfair_pier, poor).
build_wealth(restaurant, well-off).
build_wealth(amusement_park, poor).
build_wealth(stadium, poor).

% роскошные развлечения
build_wealth(theater, well-of).
build_wealth(cabaret, well-of).
build_wealth(casino, well-of).
build_wealth(opera, rich).
build_wealth(gourmet, rich).
build_wealth(yacht, rich).