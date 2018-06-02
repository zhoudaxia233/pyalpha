# PyPM
A process mining tool written in Python3.  

It generates a Petri net using the [Alpha Algorithm](https://en.wikipedia.org/wiki/Alpha_algorithm) from event logs.

---
## Requirements
`Python3` only, you don't need ANY third-party libraries.

---

## Usage
```
./main.py test/test0.txt
```
After running the command, it automatically generates a dot file, then you can copy the content inside and paste it [here](http://www.webgraphviz.com/) to get the Petri Net image.
>Update: Now it also generates a footprint.txt file.