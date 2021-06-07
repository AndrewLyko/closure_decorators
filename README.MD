# Closured & Decorators

# Closure
1. What is it?
 - access to variables/ functions/ classes from out of actual scope

2. How to create?
 - we need have min 2 function, outer and inner
 - outer function have to return declaration of inner function
 - inner function have to use something from outer function like variables, functions, classes

3. Pros:
 - persistence (trwalosc)

4. Cons:
 - leak of memory

## Scope - access/ visibility to variable/ function declaration, class definition
- LEGB

1. L - local, crated by function body
2. E - enclosing, function object '__closure__'
3. G - global, created by module (python file)
4. B - build in, examples: sum, maz, print, len

## 2 ways of find identifier :
1. lhs - left-hand side assignment  - check if variable exists locally if not create
2. rhs - right-hand side assignment - search through the scopes (LEGB)

## 2 basic data structure
1. Stack - FILO - first in, last out
2. Queue - FIFO - first in, first out 

## List indexing

"a"| "b"| "c"
--- | --- | ---
0 | 1 | 2

# Programming main rules:
- DRY - don't repeat yourself
- KISS - keep it simple, stupid!

## Higher order function
- function, which get declaration of function as parameter

## First class function
- all functions are objects

# Decorator:

## 3 variance
- function decorator 😌
- class decorator
- design pattern (the best way to solve problem)

## How to create:
1. Create function using closure
2. Add annotation with ad and name of decorator above decorated function


## Rules:
- you can use multiple decorators to decorate one function
- order of decoration is from the nearest decorated function to the furthest
- you cen pass parameters to decorator using double closure in decoration
- order of parameters in double closure:
    - parameters decorator
    - decorated function
    - parameters of decorated function

# Dictionary
-iPython - interactive python