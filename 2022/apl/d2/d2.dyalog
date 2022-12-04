⍝ Parse input.
input ← ⊃⎕NGET'G:\Folders\Programming\aoc\2022\apl\d2\input.txt' 1

⍝ Part 1
rs ← 6 6 ⍴ 3 6 0 3 6 0 0 3 6 0 3 6 6 0 3 6 0 3
score1 ← {(rs⌷⍨'ABCXYZ'⍳1 0 1/⍵) + ('XYZ'⍳3⌷⍵)}
+/score¨input

⍝ Part 2
hs ← 6 6 ⍴ 3 1 2 3 1 2 1 2 3 1 2 3 2 3 1 2 3 1
score2 ← {(0 3 6['XYZ'⍳3⌷⍵]) + (hs⌷⍨'ABCXYZ'⍳1 0 1/⍵)}
+/score2¨input
