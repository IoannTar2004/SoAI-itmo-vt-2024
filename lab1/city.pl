:- consult('production.pl').
:- consult('build_cost.pl').
:- dynamic(build/3).

new_build(Build, Id, Workers) :-
    Id >= 0, build_price(Build, _), \+ build(Build, Id, _),
    job(Build, _, _, N, _), Workers =< N,
    assert(build(Build, Id, Workers)).

destroy_build(Build, Id) :-
    retractall(build(Build, Id, _)).

set_workers(Build, Id, Workers) :-
    destroy_build(Build, Id), new_build(Build, Id, Workers).

prod_per_day(Build, Count) :-
    (plantation(Build); farm(_, Build); mine(Build); industry(Build, _); industry(Build, _, _)),
    findall(W, build(Build, _, W), Workers),
    sum_list(Workers, Sum),
    job(Build, _, _, N, _), prod_count(Build, Prod),
    Count is Prod * (Sum / N).