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
farm(crocodile, natural_leather).   % крокодил - кожа
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
industry(industry_leather, skin) % кожа из шкур
industry(rum, sugar).       % ром из сахара
industry(cans, fish_meat).       % консервы из рыбы или ананаса или мяса или какао
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
industry(clothes, natural_leather).
industry(clothes, industry_leather).

% электростанции (МВт, потребляемый ресурс)
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
residential(modern_apartment, 28, 80). % Многоквартирная высотка
residential(mansion, 4, 85).        % Поместье
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

% образование (уровень образования).
education(uneducated).      % не является зданием. Просто факт об отсутствии образования
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

% военные здания (названия, сила одного человека)
military(fort, 1).              % Форт
military(barracks, 2).          % Казармы
military(armybase, 10).          % Военная база
military(aircraft_carrier, 8).  % Авианосец
military(drons, 5).             % Эскадра дронов