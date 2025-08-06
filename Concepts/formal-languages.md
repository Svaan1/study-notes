20.02.2025 20:01
Tags: #concept #todo 

---
# Formal Languages

### Alphabet
Usually represented by Σ, an alphabet can be described as a finite set of symbols (atomic unit) of some kind.

Example:
- Σ={a,b,c … z} - roman alphabet
- Σ={0, 1} - binary alphabet
- Σ=(X) -m empty alphabet

```ad-warning
Sets like the natural numbers **cannot** be considered an alphabet, as alphabets cannot be infinite.
```
### Symbols
There is not a formal definition for a symbol. $MORE$
### Chains
A finite sequence of juxtaposed symbols.
#### Length
ω length of a chain notation — MORE —
| ω | means the length of the chain ω
#### Concatenation
if μ and ω are chains, then ω.μ  is the concatenation of the chain μ with the chain ω.
#### Sucessive Concatenation
Given ω=ab, μ=ba → ωμ=abba 

- $ω^3$ 
 ---– MORE --–
#### Unit Chain
chains made out of a single symbol

#### Prefixes
The chain abra has 5 possible prefixes: abra, abr, ab, a, empty-symbol

(Prefixo Proprio) every prefix that its not the chain itself

#### Suffix
The chain abra has 5 possible sufixes: abra, bra, ra, a and empty

(Sufixo Proprio) every suffix that its not the chain itself

#### Subchains
Chains created by removing the prefix and/or sufix of another chain

#### Set of every possible chain

Example:
- Σ={a, b}
- Σ*={empty, a, aa, ab, ba, bb, aaa…}
- Σ+={a, aa, ab, ba ,bb, aaa…}

#### Language
A formal language L over an alphabet Σ is any subset of Σ*, L ⊆ Σ*

