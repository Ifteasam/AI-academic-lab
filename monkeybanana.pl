do(state(middle, onbox, middle, hasnot),
    grasp,
    state(middle, onbox, middle, has) ).
 
% monkey climbs box
do(state(L, onfloor, L, Banana),
    climb,
    state(L, onbox,   L, Banana) ).
 
% monkey pushes box from P1 to P2
do(state(L1, onfloor, L1, Banana),
    push(L1, L2),
    state(L2, onfloor, L2, Banana) ).
 
% monkey moves from P1 to P2
do(state(L1, onfloor, Box, Banana),
    walk(L1, L2),
    state(L2, onfloor, Box, Banana) ).
 
% define (recursively) how the monkey can get the banana
canget(state(_,_,_,has)).
canget(State1) :- do(State1, Action, State2), canget(State2),write(Action).

%get plan:- list of actions

canget(state(_,_,_,has), []). %monkey already has it.. Goal state
canget(State1,Plan):- do(State1, Action, State2), canget(State2, Partialplan),
    add(Action, Partialplan, Plan).

add(X,L,[X|L]).
