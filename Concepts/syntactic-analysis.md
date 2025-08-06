02.07.2025 19:26
Tags: #concept

---
# Syntactic Analysis

Uses identified tokens to Produces the syntactic tree

## Types of Syntactic Analysis
### Ascending
When the syntactic tree is created from the leaves to the root
### Descending
When the syntactic tree is created from the root to the leaves
### Predictive
Uses the lookahead token to identify which production rule to use.
### With regression
Tries to apply another production rule if the current one fails, more robust but also slower, due to exponential time increase, it is rarely used.
### Recursive
Better used in manual implementation of compilers, uses recursion.
### LLK
The first L means that it the code is traversed from the LEFT to the RIGHT, the second L means that the derivation is also done from the LEFT to the RIGHT, k means the number of tokens used as reference for the choice of the production rule used, ideally 1. so LL1. (uses a stack)

```ad-attention
A grammar is considered ambiguous if a sequence of tokens can result in more than one distinct derivation tree.
```

## Predictive Recursive Syntactic Analysis
Each production rule is defined as a subroutine, called recursively in the analysis of the source code. Uses the lookahead token to define which 
subroutine to call. Due to the recursive nature of this operation, the syntactic tree is done implicitly using the calling of the subroutines

Uses subroutines on the right side of the production rule to:
- Define which tokens are next and apply the next production rules if valid
- Treat non-terminal symbols if needed

Due to infinite recursion problems, some production rules may need to be refactored.
- Original : 
	- arithmetic_expression → arithmetic_expression + term
- Converted
	- arithmetic_expression → term arithmetic_expression_2
	- arithmetic_expression_2 0> + term arithmetic_expression_2 | null

## Descending Syntactic Analysis LL(1)
Uses a stack to apply a production rule.

1. Shift the non-terminal start symbol
2. For each input symbol:
	1. If the symbol at the top of the stack is non-terminal
		1. choose a production rule to apply to the the current input symbol
			1. If there is a production rule,
				1. remove the current non-terminal from the top of the stack
				2. add the new production rule from right to left in the stack
			2. if not, its a syntactic error
	2. If the symbol at the top of the stack is terminal.
		1. if the symbol at the top of the stack and the current input symbol matches, remove the symbol from the stack and go to the next input symbol
		2. if they don’t match, its a syntactic error
