# freeCodeCamp Certification Paths

A series of lessons and projects to earn certificates using [freeCodeCamp](https://freecodecamp.org).

## Scientific Computing with Python(Beta) ➡️ [Github](https://github.com/sedstan/freeCodeCamp/tree/3f498cf8ee68c05e9e83802eeca5131bba7a1033/scientific-computing-with-python-beta/course)

Learning Python creating algorithms and applications.

### Scientific Computing Lessons

#### Learn String Manipulation by Building a Cipher

In this lesson, I learned fundamental programming concepts in Python, such as variables, functions, loops, and conditional statements.

#### Learn How to Work with Numbers and Strings by Implementing the Luhn Algorithm

In this lesson, I gained experience working with numerical computations and string manipulation.

#### Learn Lambda Functions by Building an Expense Tracker

In this lesson, I gained experience working with lambda functions by building an
expense tracker. I was also introduced to: `sum()`, `filter()`, lists and dictionaries.

#### Learn Python List Comprehension by Building a Case Converter

In this lesson, I gained experience in understanding how List Commprehension constructs a new Python list from an iterable type without using a loop or the `.append()` method.

A program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.

Two phases: 1. Use a loop to implement the program. 2. Use List Comprehension instead of a loop to acheive the same results.

#### Learn Regular Expression by Building a Password Generator

In this lesson, I learned how to import modules from the Python standard library. I also learned how to use Regular Expressions.

A function that takes 5 parameters, `length`, `nums`, `special_chars`, `uppercase`, `lowercase`, and returns a randomly generated password.

#### Learn Algorithm Design by Building a Shortest Path Algortithm

In this lesson, I gained experience building an algorithm using functions, loops, conditional statements and dictionary comprehension.

I saw an opportunty to refactor in the second file. Used ChatGPT as my Senior Python Developer to guide me. It told me the How and Why of the refactoring opportunities, without explicitly telling me where the refactors are. This allowed me to try and figure it out on my own before asking for futher assistance; understand why it is important to do this.

In `line 26` I removed the if-else statement. I learned that we don't need to conditional. It adds an extra step in getting to `paths[node]` - a copy of `paths[current]`.

Then I changed the unvisited list to a min-heap using the heap library. This optimises the algorithm by reducing the complexity since it is traversing the whole graph. It also removes unnecessary checks.

Next, I added parameters to the function allowing for more versatility:
    1. In line 40 I break the loop if the target is reached early.
    2. In line 55 I have the option to return only the distance and path to the target.

Then I refactor print statements for clarity. I added a new function to handle output for our returned distances and paths.

Lastly, I added validation for our algorithm.

#### Learn Recursion by Solving the Tower of Hanoi Puzzle

In this lesson I learnt about recursion by solving the Tower of Hanoi puzzle. The first  step involved writing using a series of `if-else` statements to the solution. The next step was to implement a recursive solution.

#### Learn Data Structures by Building the Merge Sort Algorithm

In this lesson I learnt how to interact with data structures by sorting a list of random numbers using the Merge Sort Algortihm.

## Relational Database ➡️ [Github](https://github.com/sedstan/freeCodeCamp/tree/3f498cf8ee68c05e9e83802eeca5131bba7a1033/relational-database/celestial-bodies-database)

Seleceted courses to learn PostgreSQL and Bash building scripts and databases.

### Relational Database Lessons

#### Celestial Bodies

Build a database using outerspace! This shows the complete dump of the database.

---

&nbsp;

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/e63eb68ab6eb43718b20c4e2569579f9)](https://app.codacy.com/gh/sedstan/freeCodeCamp/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
