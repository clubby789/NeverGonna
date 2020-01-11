
# NeverGonna
 A terrible Python implementation of the Rick Astley-inspired esoteric language 'NeverGonna'
## What is it?
[https://esolangs.org/wiki/NeverGonna](https://esolangs.org/wiki/NeverGonna)

I was browsing the esolangs wiki and came across this. I thought it was interesting, and I couldn't find any implementations, so I decided to write my own.

Currently has minimal features and only an interpreter (can't run programs).
## Usage

    python main.py
## Language
Currently implemented is variable declaration, assignment, and printing (slightly changed from the original implementation, fully documented inside the file).

### Declaration
`NG> we're no strangers to <type>:<name>`
Currently implemented types: `str` and `int`
### Assignment
`NG> gotta make <name>:<value>`
`<value>` can be a string/int literal or another variable.
### Printing
`NG> i just wanna tell you`<value>
`<value>` can be a string/int literal or another variable. Strings are concatenated automatically and delimited by spaces.
