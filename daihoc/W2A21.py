def Loop(Content, Times_left):
    print(Content)
    if Times_left != 0:
        Loop(Content, Times_left - 1)
Loop('Hello, world', 10)