# Terminal-Dictionary
A simple dictionary that can be used to get definitions for words using linux terminal.
## Prerequisites
The following Python libraries are required to run the program.
- requests
- json
- textwrap

modules can be install using pip. For example, to install textwrap, use the command:
```
python3 -m pip install textwrap
```
## Installation
**Clone the repo** 
```
git clone https://github.com/Ameenafz248/Terminal-Dictionary.git
```
**Give execution permission to define.py** 
```
chmod +x define.py
```
**Put the file in bin path**
For example
``` 
mkdir -p ~/.local/bin && mv define.py ~./local/bin/define
```
## Usage
```
define <WORD>
```
