# Terminal-Dictionary
A simple dictionary that can be used to get definitions for words using linux terminal.
## Prerequisites
- python3
- requests
- json
- textwrap

modules can be install using pip. For example, to install requests
```
python3 -m pip install requests
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
