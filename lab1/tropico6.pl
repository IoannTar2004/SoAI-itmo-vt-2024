% Фракции
fraction(religious).        % верующие
fraction(military).         % военные
fraction(capitalists).      % капиталисты
fraction(communists).       % коммунисты
fraction(ecologists).       % экологи
fraction(industrialists).   % промышленники
fraction(conservatives).    % консерваторы
fraction(intellectuals).    % интеллигенция

% Противоборствующие фракции
opposing_franctions(religious, military).
opposing_franctions(capitalists, communists).
opposing_franctions(ecologists, industrialists).
opposing_franctions(conservatives, intellectuals).

% достаток граждан
wealth(broke).        % разорившийся
wealth(poor).         % бедный
wealth(well-off).     % обеспеченный
wealth(rich).         % богатый
wealth(super_rich).   % несметно богатый

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
farm(fish, fish_meat). farm(fish, seafood).  % рыба - рыба, морепродукты

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
industry(fabric, wool).     % оружие из стали и никеля

industry(gun, steel, nickel)
industry(cheese, milk).     % сыр из молока
industry(cigarres, tobacco).    % сигары из табака
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
electricity(360, coal).      % ТЭС на угле
electricity(400, oil).       % ТЭС на нефти
electricity(800, uranium).   % АЭС
electricity(500, sun).       % Солнечная ЭС
electricity(70, wind).       % Ветряк

% жилые здания (вместимость, качество жилья)
residential(2, 10).   % Лачуга с качеством 10. Вмещает 2 людей.
residential(40, 28).      % Коммуналка с качеством 28. Вмещает 40 людей.
residential(12, 32).      % Барак с качеством 32. Вмещает 12 людей.
residential(18, 38).      % Ночлежка с качеством 38. Вмещает 18 людей.
residential(32, 40).      % Многокватрирный дом с качеством 38. Вмещает 18 людей.