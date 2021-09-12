# Contributing
1. Choose a language that has not been [completed](/sources#Languages)
2. Create the [program](#sources) that produces [output](#output)
3. Submit a [PR](#PR) as described below

# Submit A Pull Request
1. Fork this [repository](https://github.com/spencermwoo/randomness-in-programming-languages)
2. Clone your fork
 * `git clone https://github.com/<your_github_account>/randomness-in-programming-languages`

3. Create a new branch for the language 
 * `git checkout -b javascript`

4. Add your changes for the language
 * `git add sources/javascript.js`
 * `git add outputs/js_10_1000000`
 * `git add outputs/js_1000_1000000`
 * `git add outputs/js_10_1000000000`
 
5. Commit your changes
 * `git commit -m "Add javascript language"`

6. Push your changes to your branch
 * `git remote -v`
 * `git push origin javascript`

7. Send a PR from your branch to `master`

# Sources

## Pseudo Random Number Generators
**Trials:**
1. 1,000,000 numbers in range 1-10
2. 1,000,000 numbers in range 1-1000
3. 1,000,000,000 numbers in range 1-10

For each of these trials we calculate the frequency of each number and output this to a file.

**Output:**
For each of the above (3) trials, we output the probability occurance of each number.

Here is an [example pull request](https://github.com/spencermwoo/randomness-in-programming-languages/pull/1/files).

## Program
1. The program generates N random numbers in range R
2. Count the occurances of each number in R and divide by N to calculate the probability
3. Output the probability for each number in R into a file
4. The source file is named after the langauge
 * `javascript.js`
5. The output file is named after the language and trial
 * `js_10_1000000`

Here is an [example pull request](https://github.com/spencermwoo/randomness-in-programming-languages/pull/1/files).

## Output
The commit being PR'd should have 1 source file for the language and 3 output files in total (1 for each trial).

Here is an [example pull request](https://github.com/spencermwoo/randomness-in-programming-languages/pull/1/files).

# Additional Contributions
We also welcome any formatting changes or improvements to any existing source code.

If there's any questions feel free to ping me on github via @spencermwoo