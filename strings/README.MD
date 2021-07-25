README.MD
take the first argument provided and output it to the user in reverse order
if multiple arguments are provided it will print the first argument and exit, unless the arguments are surrounded by quotes in which case it'll reverse everything inside those quotes

## examples

### no input provided
```$ ./reverse.py
usage: reverse.py <'string in quotes'>
```

### multiple strings without quotes
```$ ./reverse.py please reverse this text
esaelp
```

### multiple strings surrounded by quotes
```$ ./reverse.py 'please reverse this text'
txet siht esrever esaelp
```

### numbers
```$ ./reverse.py '12345678910'
01987654321
```

### more numbers, with spaces
```$ ./reverse.py '1 2 3 4 5 6 7 8 9 10'
01 9 8 7 6 5 4 3 2 1
```
