"""
Author: Fernando Collado
Github: ForFer
"""

"""
When you select a contiguous block of text in a PDF viewer, the selection is
highlighted with a blue rectangle. In a new kind of PDF viewer, the
selection of each word is independent of the other words; this means that each
rectangular selection area forms independently around each highlighted
word. 

In this type of PDF viewer, the width of the rectangular selection area is
equal to the number of letters in the word times the width of a letter, and the
height is the maximum height of any letter in the word.

Consider a word consisting of lowercase English alphabetic letters, where each
letter 1mm is wide. Given the height of each letter in millimeters (mm), find the
total area that will be highlighted by blue rectangle in mm² when the given word
is selected in our new PDF viewer.

Input Format

The first line contains 26 space-separated integers describing the respective
heights of each consecutive lowercase English letter.
The second line contains a single word, consisting of lowercase English
alphabetic letters.

Output Format

Print a single integer denoting the area of highlighted rectangle when the
given word is selected. The unit of measurement for this is square
millimeters (), but you must only print the integer.

Sample Input

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

Sample Output

9

"""
import string as s
heights = list(map(int, input().split()))
word = input().strip()

maxHeight = 0
for letter in word:
    index = s.ascii_lowercase.index(letter)
    if(heights[index]>maxHeight):
        maxHeight = heights[index]

print(maxHeight*len(word))

