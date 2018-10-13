# pyalpha
A process mining tool written in Python3.  

It generates a Petri net using the [Alpha Algorithm](https://en.wikipedia.org/wiki/Alpha_algorithm) from event logs.

---
## Requirements
1. `Python3`
2. `pip`
3. `graphviz-2.38` (Only this version has been tested, other versions may also work).

On Ubuntu, simply type `sudo apt install graphviz`, and it will work!

On Windows, you may need this link [Graphviz 2.38 Stable Release](https://graphviz.gitlab.io/_pages/Download/windows/graphviz-2.38.msi). Also, you need to add **graphviz** to your SYSTEM PATH. Just add the **/bin/** folder is enough.

---

## Installation

Install `pyalpha`:

```bash
sudo pip3 install pyalpha
```

---

## Developing

Install `pyalpha` for development:

```bash
python3 setup.py develop
```

---

## Usage
### How to use pyalpha?
```bash
pyalpha name-of-your-file-which-contains-event-logs.txt  # e.g. tests/test0.txt
```
By default, it generates a dot file, a png file shows the Petri Net and a txt file describing the footprint.

### How to run unit tests?
e.g. If you want to run unit tests of `alpha_test.py`, just type the command below:  
```bash
python3 -m unittest tests.alpha_test
```

### How can I use my custom event logs?  
Please take a look at `.txt` files in folder `tests/`. Just follow the same style.
