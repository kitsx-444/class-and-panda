# Currency Pair Performance Reporter

### What is this program
This is a pair performance reporter that uses classes and pandas combined.

### Concepts learned:
1. How to combine pandas and classes
2. the .method() and .sum() pandas functions.

### What does it output
It firstly uses data from a list of dictionaries that contain pips and outcomes of multiple trades of the same pair. It outputs the win rate, total pips and average pips across the whole list of dictionaries.

### How to Run
Requires pandas (`pip install pandas`)
Run: `python pair_performance.py`

### Output Example:
```
   pips outcome    pair
0    40     win  EURUSD
1   -20    loss  EURUSD
2   -10    loss  EURUSD
3   -32    loss  EURUSD
4   100     win  EURUSD
5    50     win  EURUSD
6   -20    loss  EURUSD
7   -30    loss  EURUSD
Your Win Rate: 37.5%
('Total Pips: 78', 'Average Pips: 9.75')
```
