# randomness-in-languages
An example of random number generation in different programming [languages](/sources#languages)

## Pseudo Random Number Generators
Trials : 
1. 1,000,000 numbers in range 1-10
2. 1,000,000 numbers in range 1-1000
3. 1,000,000,000 numbers in range 1-10

For each of these trials we calculate the frequency of each number and output this to a file.


Example : 
For trial (1) we randomly calculated 1,000,000 numbers in range 1-10.  For number 3, we rolled it 54321 times.  This means the frequency of #3 was 54321/1000000 which is equivalent to `0.054321`.  The output in our file `language_10_1000000` would be
```
...
3:0.054321
...
```

# hacktoberfest
A hactoberfest-friendly project

## Contribute
Create an example of generating a million random numbers and calculating the percentage for each bucket.  

For more details check out [CONTRIBUTING.md]()