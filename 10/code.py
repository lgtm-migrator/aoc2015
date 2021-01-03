"""
--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say.
They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence.
For example, ``211`` is read as "one two, two ones", which becomes ``1221`` (``1`` ``2``, ``2`` ``1``s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step.
For each step, take the previous value, and replace each run of digits (like ``111``)
with the number of digits (``3``) followed by the digit itself (``1``).

For example:

- ``1`` becomes ``11`` (``1`` copy of digit ``1``).
- ``11`` becomes ``21`` (``2`` copies of digit ``1``).
- ``21`` becomes ``1211`` (one ``2`` followed by one ``1``).
- ``1211`` becomes ``111221`` (one ``1``, one ``2``, and two ``1``s).
- ``111221`` becomes ``312211`` (three ``1``s, two ``2``s, and one ``1``).

Starting with the digits in your puzzle input, apply this process ``40`` times.
What is the length of the result?
"""

# stdlib
# ==========================
import re

print("Part One")
# ==========================

puzzle_input = "1321131112"

print(f"{len(puzzle_input)},")

for loop in range(50):

	new_value = []

	while puzzle_input:

		first, trailing = re.match(r"^([0-9])(\1+)?", puzzle_input).groups()
		length = len(trailing or '') + 1
		new_value.extend((str(length), first))

		puzzle_input = puzzle_input[length:]

	puzzle_input = ''.join(new_value)
	print(f"{len(puzzle_input)},")

	if loop == 39:
		print("After 40 cycles, the length is:", len(puzzle_input))  # 492982
		input(">>>")
	elif loop == 49:
		print("After 50 cycles, the length is:", len(puzzle_input))  # 6989950

# ==========================
print("\nPart Two")
# ==========================
"""
Neat, right? You might also enjoy hearing
`John Conway talking about this sequence <https://www.youtube.com/watch?v=ea7lJkEhytA>`_
(that's Conway of Conway's Game of Life fame).

Now, starting again with the digits in your puzzle input,
apply this process ``50`` times. What is the length of the new result?
"""
