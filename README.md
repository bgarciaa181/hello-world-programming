## ACT2 Reflection

Good variable names make the code clear and easy to read. Comments can become old or confusing if you change the code later, but clear names help you understand what the code does right away without losing time.

## ACT3 Plaintext
Python strings are immutable, so their memory size cannot be changed.
Using += in a loop creates a new string object in memory every time.
On the other hand, str.join() calculates the final size before creating the result.
This memory management makes str.join() much faster than += inside a loop.

## ACT 4 Explain what you would change if IVA became 23%
If the IVA changes to 23%, I would only go to config.py and change IVA from 1.21 to 1.23. I don't need to touch main.py because it updates automatically.

## ACT 5