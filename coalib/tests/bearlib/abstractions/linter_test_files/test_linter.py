# This little program tests whether each line only continues a single char and
# is one of the primitive math operations ``+``, ``-``, ``*`` and ``/``.
# When user specifies to actually fix the file, this program removes invalid
# lines.
#
# Invocation:
# python3 test_linter.py [--use_stderr] [--correct] file-to-lint

import sys


if __name__ == "__main__":
    if "--use_stderr" in sys.argv:
        output_file = sys.stderr
    else:
        output_file = sys.stdout

    correct = "--correct" in sys.argv

    filename = sys.argv[-1]
    with open(filename, mode="r") as fl:
        content = fl.read()

    for i, line in enumerate(content.splitlines()):
        if line[0] not in ("+", "-", "*", "/"):
            if not correct:
                print("L{}C{}-L{}C{}: Invalid char ('{}') | "
                      "MAJOR SEVERITY".format(i, 0, i, 1, line[0]),
                      file=output_file)
            # If `correct` is True just leave out the line since it's invalid.
        else:
            if correct:
                print(line, file=output_file)
