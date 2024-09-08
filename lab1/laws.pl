:- consult('build_cost.pl').
:- dynamic(law/2).

% законы, изменяющие базу знаний (название, стоимость закона)

law(industrialization, 10000). % Индустриализация. Снижает цены на промышленные здания в 2 раза.
law(agricultural_subsidies, 3000). % Аграрные субсидии. Снижает цены на плантации и фермы в 2 раза.

industrialization() :-
    findall((Name, Price), (build_price(Name, Price), (industry(Name, _); industry(Name, _, _))), Industries),
    sort(Industries, UIndustries),
    forall(
        member((Name, Price), UIndustries),
        (
            (law(industrialization, 10000),
            retract(build_price(Name, Price)),
            NewPrice is Price / 2,
            assert(build_price(Name, NewPrice)));

            (\+ law(industrialization, 10000),
            retract(build_price(Name, Price)),
            NewPrice is Price * 2,
            assert(build_price(Name, NewPrice)))
        )
    ),
    (retract(law(industrialization, 10000)); assert(law(industrialization, 10000))).

agricultural_subsidies() :-
    (law(agricultural_subsidies, 3000),
    retract(build_price(plantation, 1500)),
    assert(build_price(plantation, 750)),
    retract(build_price(farm, 900)),
    assert(build_price(farm, 450));

    \+ law(agricultural_subsidies, 3000),
    retract(build_price(plantation, 750)),
    assert(build_price(plantation, 1500)),
    retract(build_price(farm, 450)),
    assert(build_price(farm, 900))),

    (retract(law(agricultural_subsidies, 3000)); assert(law(agricultural_subsidies, 3000))).