:- consult('goods.pl').
:- consult('build_cost.pl').
:- consult('job_properties.pl').

% Факты о кол-ве товара, произведенного в один день при полном штате работников.

prod_count(corn, 4).
prod_count(banana, 3).
prod_count(pineapple, 3).
prod_count(tobacco, 2.5).
prod_count(cotton, 2.5).
prod_count(coffee, 3).
prod_count(cacao, 2.5).
prod_count(sugar, 2).
prod_count(rubber, 2).
prod_count(wood, 4.5).
prod_count(coconut, 3).

prod_count(skin, 3).
prod_count(meat, 4).
prod_count(wool, 3.5).
prod_count(milk, 5).
prod_count(leather, 2).
prod_count(fish, 3).
prod_count(shellfish, 0.8).

prod_count(iron, 2).
prod_count(coal, 2).
prod_count(gold, 0.7).
prod_count(nickel, 1.5).
prod_count(aluminum, 2).
prod_count(uranium, 0.5).
prod_count(oil, 2.5).

prod_count(planks, 4).
prod_count(rum, 2.2).
prod_count(cans, 1.9).
prod_count(steel, 2).
prod_count(boat, 1).
prod_count(fabric, 3.2).
prod_count(weapon, 1).
prod_count(cheese, 3).
prod_count(cigars, 2.3).
prod_count(car, 1).
prod_count(chocolate, 4).
prod_count(medicine, 1.4).
prod_count(juice, 4.2).
prod_count(electronics, 1).
prod_count(clothes, 1.2).

electricity_prod(wind, 70).       % Ветряк
electricity_prod(coal, 360).      % ТЭС на угле
electricity_prod(oil, 400).       % ТЭС на нефти
electricity_prod(sun, 500).       % Солнечная ЭС
electricity_prod(uranium, 800).   % АЭС
