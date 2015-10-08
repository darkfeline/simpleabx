simpleabx
=========

Super simple ABX script written in Python 3.

Requires mpv.

Usage
-----

Run:

    $ python3 simpleabx.py a.mp3 b.flac

First, track A will play.  Press Enter to continue.

Next, track B will play.  Press Enter to continue.

Finally, track X will play.  X is randomly either A or B.  Enter a or b then
press Enter to continue.

simpleabx will echo the choice to stdout and return with exit code 0 if choice
was correct, 1 if choice was incorrect, and 2 if choice was invalid (not A or
B).

Thus, simpleabx can be used in a script:

    python3 simpleabx.py $file1 $file2 >> choices
    echo $? >> results
