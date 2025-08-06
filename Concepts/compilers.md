02.07.2025 17:04
Tags: #concept

---
# Compilers

## Basic Concepts
### Machine Code
Instructions are sent to the CPU via machine code, which is stored as binary data.

A machine code instruction looks roughly like this:

0101 | 1010 | 0110 | 0000 | 0100 | 0000 | 0000 | 0000
   5        A         6         0          4         0          0          0

Where
- `5A`: Code of the sum operation
- `6`: Number of the register where the sum will be executed
- `04000`: Memory address of one of the operands to be used in the sum

### Assembly Languages
Assembly languages facilitate the codification process by giving aliases to machine instructions, giving easier access to data, addresses and operations.

The instruction used as exemple above can be translated to the following assembly instruction:

`ADD 6, J`

### Assemblers
CPU vendors provide assemblers, applications that translate assembly language instructions to machine code ones.

### Low Level Languages
Coding machine instructions using programming languages where you have direct and mandatory use of volatile hardware components, such as memory addresses and registers are called low-level languages.

###  High Level Languages 
High level programming languages are the ones which try to abstract and take away this responsibility from the user, making the instructions look closer to natural languages, lowering the complexity and increasing user-friendliness, but at the same time, giving space for lack of control and unpredictability.

The conversion from a high level source code to machine code is done trough the use of either an interpreter or a compiler, maybe something somewhere in between.

(Source Code) → (Interpreter / Compiler) → (Machine Code)

### Interpreters
Interpreters convert source code to machine code in runtime, thus the interpreter needs to be present in the machine running the code, also creating a slower execution time, due to the overhead of the conversion alongside the application's logic.

### Compilers
Compilers convert source code to machine code instructions in a single operation, often creating a single operational system specific executable file. The executable is independent from the compiler and the source code is harder to decipher, as it will be stored directly as machine code.

### Operations of a Compiler

![[compiler-flow.png]]

- **Lexical Analysis**: Identify and parse tokens out of the code.
- **Syntactic Analysis**: Creates a valid syntactic tree out of the parsed tokens.
- **Semantic Analysis**: Validates structures such as undeclared variables, out of scope operations, missing parameters, etc.
- **Intermediate Code Generation**: Uses the syntactic tree to create a new data structure that closely resembles the target code structure, using three operand operations.
- **Code Optimization**: Removes and optimizes ambiguous and unnecessary code, such as unreachable code, redundant operations, algebraic operations, etc.
- **Target Code Generation**: Generates assembly or machine code using the intermediate code.

- **Symbols Table**: Keeps track of all identifiers and its specific type, content, size, memory address, etc.
- **Error Handling**: Displays or tries to handle any existing errors during compilation.

## Formal Specifications

### Regular Expressions
- Used to specify patterns of valid tokens in a language.
- Used in the **lexical** analysis.
- Can be easily recognized by a deterministic finite automaton .

### Grammars
- Grammars free of context can be used to determine how symbols can be combined into valid chains.
- Used in the **syntactic** analysis.

Notations:
	- **G** = (V, T, P, S)
	- **V**: non-terminal symbols
	- **T**: terminal symbols
	- **P**: production rules
	- **S**: non-terminal start symbol

Meanings:
	- **V**: used in the deriving of the source code
		- cmd_if
		- cmd_while
		- cmd_for
		- cmd_switch
	- **T**: alphabetical symbols used to describe the source code.
		- +, -, /, %
		- if, while, for, switch, etc.
		- identifiers
		- numbers
	- **P**: production rules of a grammar of a type 2 (free of context) language
		- cmd → cmd_if | cmd_while
		- cmd_if → if (op_logic) { cmds }
		- cmds → cmd(cmd)*
		- op_logic → == |  != | > | < | ≥ | ≤
	- **S**: non-terminal symbol where the application is created
		- S = application
		- application → declarations type main (parameters) command_block
