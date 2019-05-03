# Coding Style Doc
Our coding style follows the standards articulated in [PEP-8](https://pep8.org/#imports).

This standard was chosen due to its wide adoption throughout the Python community. Furthermore, the scale of this project does not warrant the creation of a new coding style, thus, it makes more sense to use a wider adopted stardard.

## Style Overview
#### Code Layout
Indentations will consist of four spaces. Our maximum line length will be 79 characters to follow the convention used in the Python Standard Library. Binary operators will follow the Knuth convention such that when a operator falls at the end of a line it ought to be moved to the beginning of the following line. Lastly imports are ordered in the following way:
1. standard library imports
2. related third party imports
3. local application/library specific imports

#### String Quotes
Single quotes are used throughout the document with the exception of docstrings which will begin and end with three double quotes to follow the explict recommendation in PEP-8.

#### Comments
Block comments will begin with a # at the beginning of every line and a space seperating it from the content of the block comment. Additionally, block comment will be prefered over inline comments unless sufficiently warranted, e.g. single line of code covers an edge case. Lastly, prior to every function declaration there will be a docstring. In general, docstrings will be one line if the function is simple or multi-line if the function is more complicated. Regardless, the first line should be a single line summary of the function. If it is a multi-line docstring then there will be an empty line after the summary and then details about the inputs and outputs. The content of docstrings is explained in detail in [PEP-257](https://www.python.org/dev/peps/pep-0257/).

#### Naming Conventions
In our app, constants follow the convention of having their names be all capitalized, and variables and function names will be lowercase with underscores seperating words to improve readability. Additional naming conventions, such as those for classes, contained in PEP-8 are not discussed here given those objects are not used in our app.


Any additional questions, examples, or specifications can be found at [https://pep8.org/#imports](https://pep8.org/#imports).
