bank(east,west).
bank(west,east).

move([X,X,Goat,Cabbage], wolf, [Y,Y,Goat,Cabbage]):- bank(X,Y).
move([X,Wolf,X,Cabbage], goat, [Y,Wolf,Y,Cabbage]):- bank(X,Y).
move([X,Wolf,Goat,X], cabbage, [Y,Wolf,Goat,Y]):- bank(X,Y).
move([X,Wolf,Goat,Cabbage], nothing, [Y,Wolf,Goat,Cabbage]):- bank(X,Y).

safety_check(X,X,_).
safety_check(X,_,X).

safe_status([Man,Wolf,Goat,Cabbage]):-
safety_check(Man,Goat,Wolf),
safety_check(Man,Goat,Cabbage).

solution([east,east,east,east ],[]).

solution(Config, [Move|OtherMoves]):-
move(Config,Move,NextConfig),
safe_status(NextConfig),
solution(NextConfig,OtherMoves).
