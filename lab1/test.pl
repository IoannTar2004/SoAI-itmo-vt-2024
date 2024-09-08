building(a, 1000).
building(a, 1000).
building(b, 1000).

total_cost(Total, Name) :-
    findall(Price, building(Name, Price), Prices),  % Собираем все стоимости зданий
    sum_list(Prices, Total).  

is_expensive(Threshold) :-
    total_cost(Total),
    Total > Threshold.