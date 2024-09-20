:- consult('production.pl').
:- consult('build_price.pl').
:- consult('electricity_usage.pl').
:- consult('wealth_props.pl').
:- consult('laws.pl').
:- dynamic(build/3).

% построить здание (здание, id, кол-во рабочих)
new_building(Build, Id, Workers) :-
    Id >= 0, build_price(Build, _), \+ build(Build, Id, _),
    job(Build, _, _, N, _), Workers =< N,
    assert(build(Build, Id, Workers)).

% разрушить здание (здание, id)
destroy_building(Build, Id) :-
    retractallводство товаров в день
theory_pro(build(Build, Id, _)).

% изменить кол-во рабочих в здании
set_workers(Build, Id, Workers) :-
    destroy_build(Build, Id), new_build(Build, Id, Workers).

% рассчитывает сколько товаров производится в день, учитывая, сколько производственных зданий построено
prod_per_day(Build, Count) :-
    (plantation(Build); farm(_, Build); mine(Build); industry(Build, _); industry(Build, _, _)),
    findall(W, build(Build, _, W), Workers),
    sum_list(Workers, Sum),
    job(Build, _, _, _, _), prod_count(Build, Prod),
    Count is Prod * Sum.

% делает то же, что и предыдущее правило, за исключением того, что данное правило теоретически рассчитывает
% произd_per_day(Build, Workers, Count) :-
    (plantation(Build); farm(_, Build); mine(Build); industry(Build, _); industry(Build, _, _)),
    job(Build, _, _, _, _), !, prod_count(Build, Prod),
    Count is Prod * Workers.

% расчитывает какую продукция и сколько требуется продать, чтобы получить Profit, но при этом, продав товаров
% не больше, чем Max
calculate_profit(Profit, Max, Item, Count) :-
    price(Item, Price), Price * Max >= Profit, Count is round(Profit / Price * 10) / 10.

% расчитывает, сколько понадобится продать товаров (Item), чтобы получить Profit. Без ограничений
calculate_profit_one_item(Profit, Item, Count) :-
    price(Item, Price), Count is round(Profit / Price * 10) / 10.

% расчет зарплаты в месяц
salary(Build, Workers, Salary) :-
    (build_price(Build, Price); electricity(Build, Price)), job(Build, _, _, N, _),
    Salary is (Price / 100) * (Workers / N).

% возвращает подходящее здание в соответствии с введённым минимальным качеством жилья
suitable_house(People, Quality, Wealth, TotalPrice, TotalElectricity) :-
    findall(Res, (residential(Res, _, Q), Q >= Quality, build_wealth(Res, W), W=Wealth), List),
    nth0(0, List, House),
    residential(House, Capacity, _), build_price(House, Price), build_electricity(House, Electricity),
    Count is ceil(People / Capacity),
    format('Residentials: ~w ', House), format('(~d)\n', Count),
    TotalPrice is Price * Count, TotalElectricity is Electricity * Count.

% выводит информацию о необходимом количестве производственных зданий, работников и жилых домов, 
% в которых будут проживать работники. Количество производственных зданий и рабочих рассчитывается такое,
% чтобы доход от экспорта продукции этого здания был равен Purpose. Также учитывается минимальное качество
% жилья для рабочих
city_development(Purpose, LHouse) :-
    price(Item, Price), get_job(Item, Job),
    format('Resource: ~w\n\tRequirements\n', Item),
    prod_count(Item, N), job(Job, Wealth, _, Max, _), build_price(Job, BuildPrice),

    Workers is ceil(Purpose / (Price * N - BuildPrice / (100 * Max))),
    BuildCount is ceil(Workers / Max),
    format('Workers: ~d\n', Workers),
    format('~w buildings: ', Item), format('~d\n', BuildCount),

    suitable_house(Workers, LHouse, Wealth, HousesPrice, HousesElectricity),
    (\+build_electricity(Item, _) -> format('\nTotal Electricity: ~d\n', HousesElectricity);
    build_electricity(Item, Electricity) -> format('\nTotal Electricity: ~d\n', Electricity + HousesElectricity)),
    format('Total Price: ~d\n', BuildCount * BuildPrice + HousesPrice),
    write('-----------------------\n').
