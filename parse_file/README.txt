--------------------------
python code to parse and output simplified test data. Checks for errors and
shows any that are found.




--------------------------
-- files (and functions):
# all functions and classes should have decently informative comments

parse_file.py           # main
    output_info()
    do_stuff()
    print_issues()
    
parse_functions.py      # contains the majority of function defs
    (+ other debug and helper functions)
    open_file()
    get_params()
    test_inv()
    param_indexes()
    test_indexes()
    get_pcmout_bert()
    get_linetest_in()
    
parse_classes.py        # contains class definitions and some simple helper functions
    (+ other simple helper functions)
    class Parameters
        get_list()
        printout()
    class Channel
        (getters for bits, errs, sync, inv, etc.)
        (fail test functions for bits, errs, sync, inv, etc.)
        get_dict()
        datafields()
        printout()
    class Test
        get_name()
        issues()
        get_inv()




--------------------------
note things:

- most of the functions are unused dubug or show functions

- the silent, debug, and onetest global variables in parse_functions.py
    - silent disables all the printout functions (so u can actually see your
    stuff when debugging)
    - debug makes a bunch of random things i havent messed with in a while so idk
    and onetest should just do stuff but for the first test in report (for ex, only
    bert_test_8)

- if there's a data parsing issue (actual test data values are not showing correct), 
its probably in get_pcmout_bert() or get_linetest_in() (in parse_functions.py). If not those, it's probably  
an issue with the do_stuff() function or one of it's helpers like param_indexes() or 
test_indexes().
    - (the code's general process involves searching for the parameter lines in the file
    and saving the indexes to a list, which is part of how it knows when to start and stop taking
    data)
    - overall, if the report format changes and causes issues, it would involve the
    param_indexes(), test_indexes(), get_params(), get_pcmout_bert(), get_linetest_in()
    (all in parse_functions.py), or the do_stuff() (essentially the main function, in 
    parse_file.py)

- for the classes and global list variables
    - global tests list -- contains instances of class Test for each individual 
    test at each rate
    - global params list -- contains instances of class Parameters for each test
    - class Parameters -- contains all test parameter data (test name, data polarity,
    auto polarity, rate, etc.)
    - class Channel -- contains individual data values and most of the test for errors
    functions
    - class Test -- general data structure that holds everything for each test at 
    each rate (parameters, list of channel classes w data, polarity values)

- if a new data field (like errs, bits, sync, etc.) is added, it would need to be added
into the add_to() function in parse_functions.py, as well as another member variable in 
the Channel class

- if "LINETEST IN" or "PCMOUT BERT" is changed, or a new thing is added, it would
need to be addressed in the do_stuff() (main function) and the get_pcmout_bert(), 
get_linetest_in() functions since those strings are used when parsing








--------------------------
potential issues im now realizing could make things complicated:

- when the code looks through the file and saves each test name and parameters, it
saves name and pattern separately. there might be some case with a dictionary or something
where, if two tests with the same name but different patterns are right next to each
other in the report order, it might use the same name for both and could cause problems.

- it SHOULD account for comments (like the space under test parameters with some extra
info that happens in one or so tests) but it's possible certain characters or amout of space 
could mess stuff up maybe?






