% Rule to reverse a list
reverse_list([], []).
reverse_list([H|T], Reversed) :-
    reverse_list(T, ReversedT),
    append(ReversedT, [H], Reversed).

% Main rule to read from std_in, call reverse_list, and write to std_out
main :-
    read(InputList),
    reverse_list(InputList, OutputList),
    write(OutputList).