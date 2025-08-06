03.07.2025 00:44
Tags: #concept

---
# Semantic Analysis

Receives the ATS structured code from the syntactic analyzer and validates the source code to check its semantic validity.

It checks if the code is semantically valid, usually involving checks type usage, declaration of variables, invalid operations and any other semantic errors that cannot be identified during the parsing. 

## Types of Semantic Analysis
### Static
It is done during compilation.
### Dynamic
Done during runtime

## Validations

### Types
- Checks the symbol table and makes sure that every identifier has defined types
### Arithmetic Expressions
- Makes sure every arithmetic expression is done using numbers and are type-compatible, optionally doing any possible implicit conversions\
### Assignments
- Make sure that every variable receives a value of its defined type
### Loops
- Makes sure that the loops end if possible
- Checks the range of for loops
### Logic Expressions
- Makes sure the logic expressions receive logic values, true or false