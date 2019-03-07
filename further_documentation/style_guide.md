# Style Guide
Contributions to this project ought to maintain the readability of this project's code and its style. Restantly, we have adopted the following style standards to ensure uniformity and clarity. Most of these standards are common within the field, but we have specified them here for the sake of elucidation.

## Git
**Commit messages**
All messages that describe the changes made in a given pull request ought to use the imperative form. Further, the first line of every commit message (the subject) should summarize the purpose of the changes within fifty characters, start with a capitalized letter, and end without a period. If necessary, more documentation can act as a body to the subject line. Written documentation should explain "why?" as opposed to "what?" or "how?" and ought to wrap at 72 characters.

**Branches**
One should only push partially untested code to test or development branches. The addition of any clustering algorithm or validity index to the program must result in the creation of a new branch where testing is conducted. Each such branch should maintain its own to-do list explaining bugs, problematic edge cases, and incomplete or nonfunctional code. Once tests have demonstrated the validity of the additional code, the code's branch may request to be integrated with the master branch.

## Code
**PEP 8**
All written code must comply with Python's PEP 8 conventions. Some notable rules:
    1) 4 spaces per indentation level
    2) all lines limited to 79 characters
    3) top-level functions and class definitions should have a border of two new lines below and above
    4) methods within a class should have a border of a single blank line below and above
    5) code can only utilize UTF-8 characters
    6) imports from different applications and libraries should be on different lines and imported in the following order: standard library imports, third party imports, local imports.
    7) files, functions/methods, and variables should be in `snake_case`
    8) classes should use `CapWords` as their naming convention
Further instructions, clarifications, and justifications exist in the [official Python documentation](https://www.python.org/dev/peps/pep-0008/#introduction).
An additional project level choice:
    - when breaking, we break before a binary operator (note that this is not mandatory as a part of PEP 8 but recommended)
    
**Documentation**
All classes, functions, and methods should have an informative docstring. Classes' documentation should explain the purpose of the class while maintaining abstraction. Methods' and functions' documentation should explain their preconditions, postconditions, and side effects. Typical explaination of parameters and return value ought to exist in the regular Python format. 
Generally, block and inline comments are discouraged as most code should be self-explanitory through its organization and naming. Of course, there are exceptional cases.
