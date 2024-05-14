move(1,A,B,_):-
    write('move top disk from '),
    write(A),
    write(' to '),
    write(B),
    nl.
move(N,X,Y,Z):-
    M is N-1,
    move(M,X,Z,Y),
    move(1,X,Y,_),
    move(M,Z,Y,X).
