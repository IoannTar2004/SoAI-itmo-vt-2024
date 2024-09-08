:- consult('goods.pl').

% земельные ресурсы: плантации, лесозаготовки
plantation(corn).       % кукуруза
plantation(banana).     % банан
plantation(pineapple).  % ананас
plantation(tobacco).    % табак
plantation(cotton).     % хлопок
plantation(coffee).     % кофе
plantation(cacao).      % какао
plantation(sugar).      % сахар
plantation(rubber).     % каучук

lumberjack_camp(wood).      % древесина
coconut_combine(coconut).   % кокос

% фермы
farm(bull, skin). farm(bull, meat).     % бык - шкуры, мясо
farm(pig, meat).    % свинья - мясо
farm(sheep, wool). farm(sheep, milk).   % овца - шерсть, молоко
farm(crocodile, leather).   % крокодил - кожа
farm(fish, fish_meat). farm(fish, shellfish).  % рыба - рыба, морепродукты

% шахты
mine(iron).     % железо
mine(coal).     % уголь
mine(gold).     % золото
mine(nickel).   % никель
mine(aluminum). % алюминий
mine(uranium).  % уран
mine(oil).      % нефть

% заводы (продукция, материалы...)
industry(planks, wood).     % доски из дерева
industry(rum, sugar).       % ром из сахара
industry(leather, skin).    % кожа из шкур
industry(cans, fish).       % консервы из рыбы или ананаса или мяса или какао
industry(cans, pineapple).
industry(cans, meat).
industry(cans, cacao).
industry(steel, iron, coal).% сталь из железа и угля
industry(boat, planks).     % лодки из досок или стали или алюминия
industry(boat, steel).      
industry(boat, aluminum).

industry(fabric, cotton).   % ткань из хлопка или шерсти
industry(fabric, wool).

industry(weapon, steel, nickel). % оружие из стали и никеля
industry(cheese, milk).     % сыр из молока
industry(cigars, tobacco).    % сигары из табака
industry(plastmass, oil).       % пластмассы из нефти
industry(furniture, planks).    % мебель из досок или пластмасс
industry(furniture, plastmass).

industry(car, steel, rubber).   % автомобили из стали и каучука
industry(chocolate, cacao, sugar).   % шоколад из какао и сахара

industry(jewellery, gold).  % украшения из золота
industry(medicine, oil).    % лекарства из нефти
industry(juice, banana).    % сок из бананов или ананасов или кокосов
industry(juice, pineapple).
industry(juice, coconut).
industry(electronics, plastmass, gold). % электроника из пластмасс и золота

industry(clothes, fabric).  % одежда из ткани или кожи
industry(clothes, leather).

% электростанции (МВт, потребляемый ресурс)
electricity(wind).      % Ветряк
electricity(coal).      % ТЭС на угле
electricity(oil).       % ТЭС на нефти
electricity(sun).       % Солнечная ЭС
electricity(uranium).   % АЭС

% жилые здания (название, вместимость, качество жилья)
residential(shack, 2, 10).          % Лачуга
residential(conventillo, 40, 28).   % Коммуналка
residential(bunkhouse, 12, 32).     % Барак
residential(flophouse, 18, 38).     % Ночлежка
residential(tenement, 32, 40).      % Многокватрирный дом
residential(countryhouse, 4, 48).   % Загородный дом
residential(apartments, 20, 52).    % Квартиры
residential(house, 6, 64).          % Дом
residential(mansion, 4, 68).        % Поместье
residential(modern_apartment, 4, 80). % Многоквартирная высотка
residential(modern_mansion, 4, 90).   % Современный особняк
residential(highest_modern_mansion, 4, 105).    % Современный особняк высочайшего класса

% Развлечения (название, качество обслуживания)
entertainment(tavern, 32).           % Таверна
entertainment(circus, 45).           % Цирк
entertainment(funfair_pier, 60).     % Весёлая пристань
entertainment(restaurant, 65).       % Ресторан
entertainment(amusement_park, 70).   % Парк аттракционов
entertainment(stadium, 80).          % Стадион

% Роскошные развлечения (название, качество обслуживания)
lux_entertainment(theater, 60).       % Театр
lux_entertainment(cabaret, 60).       % Кабаре
lux_entertainment(casino, 60).        % Казино
lux_entertainment(opera, 75).         % Оперный театр
lux_entertainment(gourmet, 60).       % Ресторан деликатесов
lux_entertainment(yacht, 90).         % Яхт-клуб

% СМИ (название, даваемый уровень свободы)
media(newspaper, 20).       % Газета
media(radiostation, 30).    % Радиостанция
media(tvstation, 50).       % Телестанция

% образование (уровень образования)
education(uneducated).
education(school).
education(college).

% здравоохранение (название, даваемый уровень здоровья, макс посетителей)
health(clinic, 60, 12).
health(hospital, 80, 24).
health(research_hospital, 80, 20).

% научные исследования (название, очков знаний за день)
science(library, 1).                % библиотека
science(research_hospital, 2).      % исследовательская больница
science(science_lab, 3).            % научная лаборатория
science(space_program, 4).          % космическая программа

% магазины (название, даваемый уровень удовлетворения пищей, макс посетителей)
store(grocery, 45, 16).     % продуктовый магазин
store(mall, 50, 40).        % торговый центр

% религия (название, даваемый уровень веры)
relig(chaptel, 45).         % Часовня
relig(church, 60).          % Церковь
relig(cathedral, 80).       % Собор

% рейды: пираты (украденные ресурсы\3, количество каждого ресурса соответственно)
pirate(banana, skin, iron, 2000, 3200, 1200).
pirate(coconut, sugar, wool, 1200, 1800, 1000).
pirate(coffee, corn, gold, 1000, 1600, 200).
pirate(coal, wood, pineapple, 1200, 1800, 2000).
pirate(fish, nickel, tobacco, 1000, 550, 1800).
pirate(aluminum, cacao, shellfish, 700, 1000, 1200).
pirate(milk, rubber, uranium, 1100, 1600, 105).
pirate(cotton, meat, oil, 1500, 1600, 500).

% военные здания (названия, сила одного человека)
military(palace, 1).            % Дворец
military(fort, 1).              % Форт
military(barracks, 2).          % Казармы
military(armybase, 5).          % Военная база
military(aircraft_carrier, 6).  % Авианосец
military(drons, 3).             % Эскадра дронов