# stipula-analyzer

## The Author
The code has been developed by Samuele Evangelisti in his Undergraduate Thesis using the 
theory developed by Cosimo Laneve in "Reachability Analysis in Micro-Stipula. PPDP 2024". 
For any consern about the code, please contact Samuele: samueleevangelisti@yahoo.it.

## Requirements

- Python >= 3.11.6
- Antlr4 >= 4.13.1

## Installation

### Linux
1. Install Python, you ca use:
   - Your distro package manager
   - The Python site (https://www.python.org/downloads/)
2. Install Antlr4, you can use:
   - Your distro package manager
   - Open a terminal in the repository directory and run `python -m pip install -r requirements.txt`

### Windows
1. Install python from the site (https://www.python.org/downloads/)
2. Install Antlr4, open a terminal in the repository directory and run `python -m pip install -r requirements.txt`

### MacOS
1. Install Python, brew package manager is recommended:
   1. Follow the installation istruction on the brew site (https://brew.sh/)
   2. Open a terminal and run `brew install python@3.11`
2. Install Antlr4, open a terminal in the repository directory and run `python3.11 -m pip install -r requirements.txt`

On MacOS you probably need to specify the python version, so you need to use `python3.11` instead of `python`.

## Run

To run an example, open a terminal in the repository directory and run 

`python analyzer.py [OPTIONS] TESTS/bet.stipula`  // python3.11 ... on MacOS

where OPTIONS are
   * -r, --readable to have a different (more readable) representation of clauses
   * -c, --compact to have a less verbose output (only the relevant infos are shown)
