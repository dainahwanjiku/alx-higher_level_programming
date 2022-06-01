#!/usr/bin/python3
print(*["%c" % a for a in range(97, 123)
            if "%c" % a not in 'qe'.format(a)], sep='', end='')
