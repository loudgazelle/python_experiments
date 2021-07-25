# reverse.py
string manipulation - take the first argument provided and output it to the user in reverse order

if multiple arguments are provided it will print the first argument and exit, unless the arguments are surrounded by quotes in which case it'll reverse everything inside those quotes

## examples

### no input provided
output the usage
```
$ ./reverse.py
usage: reverse.py <'string in quotes'>
```

### multiple strings without quotes
output the first string and exit
```
$ ./reverse.py please reverse this text
esaelp
```

### multiple strings surrounded by quotes
output everything inside quotes, reversed
```
$ ./reverse.py 'please reverse this text'
txet siht esrever esaelp
```

### numbers without spaces
numbers are handled the same as strings
```
$ ./reverse.py '12345678910'
01987654321
```

### numbers with spaces
when surrounded by quotes numbers with spaces are handled the same as strings
```
$ ./reverse.py '1 2 3 4 5 6 7 8 9 10'
01 9 8 7 6 5 4 3 2 1
```
