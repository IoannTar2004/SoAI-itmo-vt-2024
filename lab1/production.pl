:- consult('goods.pl').
:- consult('build_price.pl').
:- consult('job_properties.pl').

% Факты о кол-ве товара, произведенного в один день одним работником

prod_count(corn, 0.5).
prod_count(banana, 0.7).
prod_count(pineapple, 0.55).
prod_count(tobacco, 0.5).
prod_count(cotton, 0.313).
prod_count(coffee, 0.375).
prod_count(cacao, 0.313).
prod_count(sugar, 0.4).
prod_count(rubber, 0.3).
prod_count(wood, 0.75).
prod_count(coconut, 0.6).

prod_count(skin, 0.75).
prod_count(meat, 0.5).
prod_count(wool, 0.5).
prod_count(milk, 0.5).
prod_count(natural_leather, 0.3).
prod_count(fish_meat, 0.5).
prod_count(shellfish, 0.2).

prod_count(iron, 0.6).
prod_count(coal, 1).
prod_count(gold, 0.2).
prod_count(nickel, 0.3).
prod_count(aluminum, 0.5).
prod_count(uranium, 0.25).
prod_count(oil, 0.2).

prod_count(planks, 2).
prod_count(rum, 1).
prod_count(cans, 0.8).
prod_count(steel, 2).
prod_count(boat, 1).
prod_count(fabric, 0.7).
prod_count(furniture, 0.7).
prod_count(industrial_leather, 0.7).
prod_count(weapon, 0.7).
prod_count(cheese, 0.75).
prod_count(cigars, 0.55).
prod_count(car, 0.8).
prod_count(plastmass, 1).
prod_count(chocolate, 0.5).
prod_count(medicine, 1).
prod_count(juice, 0.84).
prod_count(jewellery, 0.5).
prod_count(electronics, 0.8).
prod_count(clothes, 0.9).

% сколько вырабатывает МВт каждый работник
electricity_prod(coal, 60).      % ТЭС на угле
electricity_prod(oil, 66).       % ТЭС на нефти
electricity_prod(sun, 166).       % Солнечная ЭС
electricity_prod(uranium, 266).   % АЭС