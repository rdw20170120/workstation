# Python source

## Testing
I want to maximize test coverage,
within reason.
Most functions can be tested easily,
but some have side-effects
that make testing
more difficult and costly
in time and effort.
Testing side-effects
often means
making use of mock implementations.
I tend to put off (for now)
the effort to implement mocks
since I need to research
how best to do that
in Python.
I justify putting off those tests
in part because I feel that the code
gets tested for those side-effects
during real use.
Nonetheless,
I do still want to improve
my test coverage
by eventually adding proper tests
that address those side-effects.
On the other hand,
I do not want that lack of such tests
to skew my test coverage metrics.
The easy solution is to exclude
functions with side-effects
from my test coverage reporting.
However,
the current test coverage configuration
only supports such exclusion
at the granularity of an entire source file.
There probably exists a way to mark
a particular function
as being excluded from test coverage,
but I have not researched that yet.
Therefore,
it is useful to refactor functions
to separate them into source files
that I exclude versus those that I include
in my test coverage.
Some exclusions are likely to be permanent
as I have decided that the side-effects
are not worth the effort to test.
But I do want to eventually
implement tests for many side-effects
that are tractable.

Therefore,
my testing approach
involves separating functions
into three categories:
* functions without side-effects
* functions with side-effects that I will likely never test
* functions with side-effects that I will probably test someday

