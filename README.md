# PyPM
A process mining tool written in Python3.  

It generates a Petri net using the [Alpha Algorithm](https://en.wikipedia.org/wiki/Alpha_algorithm) from event logs.

---
## Requirements
1. `Python3`
2. `graphviz-2.38` (Only this version has been tested, other versions may also work), you need to add **graphviz** to your SYSTEM PATH. Just add the **/bin/** folder is enough.

---

## Usage
```
./main.py test/test0.txt
```
After running the command, it automatically generates a dot file, a png file shows the Petri Net and a txt file describing the footprint.
