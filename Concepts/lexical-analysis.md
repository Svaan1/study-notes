02.07.2025 18:38
Tags: #concept

---
# Lexical Analysis


It basically reads the code and tries to match valid tokens, a token is valid if it passes finds a final state in a finite state machine, its like trying to find a valid language symbol.

Responsibilities:
- Identifies valid tokens, returning its data and where is it located
- Removes comments and whitespaces
- Informs if there is still code to be read

Examples of tokens and its corresponding lexema

| Token           | Description                                           | Lexeme                                     |
| --------------- | ----------------------------------------------------- | ------------------------------------------ |
| CONSTANT        | Constant value                                        | CONST                                      |
| IF_STATEMENT    | Condition                                             | IF                                         |
| IDENTIFIER      | Identifies a type of data, a variable, function, etc. | temperature, employeeCode, offerPercentage |
| NUMBER          | Any number                                            | 100, 50.54, 0                              |
| CHARACTER_CHAIN | Chain alphabetical characters                         | ´Hello World´                              |
| ASSIGNMENT      | Used to assign values to variables                    | :=                                         |
| END_OF_COMMAND  | States the end of any command                         | ;                                          |

## Constant Values
Tokens rarely hold additional information, so to simplify its definitions, we define tokens as constant values, usually enumerators, and store any additional data in a symbol table if any fetch is needed.

### Examples of token attributes
#### Identifier Attributes
- Name
- Type (string, bool, int, etc)
#### Number Attributes
- Value
- Type (int, float, double, etc)

#### Relational Operand Attributes
- Type (<, >, ≤, ≥, =, <>)

## Recognizing Tokens
To identify a valid token we use finite state machines, starting from an initial zero value, and iterate trough the characters of a chain.

With each character we traverse, the state of the state machine is altered depending on the type of the character. When a final state is reached a valid token is identified and stored.

However there are additional safety checks that have to be made in between the process, such as checking for reserved keywords, these checks have to be made before identifying a complete identifier token as valid. 

```ad-info
Reserved keywords can also be inserted into the symbol table before-hand to simplify the lexical analysis.
```

While traversing the characters, we also use a double pointer, one to keep track of the initial location of the identifier, and the other to traverse ahead and search for the next characters until the end of the current token is reached, which then brings the first pointer to the start of the next token.

![[recognizing-tokens.png]]

We can also insert a special character at the end of the source code to simplify the token search.

## Symbol Table
Holds reserved keywords and data of the stored identifiers from the source code, such as its name, value, type, etc. 

```ad-info
Types can also be specified after the identifier is created, as the name of the identifier can be declared before the type.
```