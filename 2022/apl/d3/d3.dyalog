⍝ Parse input.
input ← ⊃⎕NGET'G:\Folders\Programming\aoc\2022\apl\d3\input.txt' 1

⍝ Common
p ← 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'∘⍳

⍝ Part 1
hl ← 2÷⍨≢
priority ← p∘⊃(hl↑⊢)∩(hl↓⊢)
+/priority¨input

⍝ Part 2
chunk ← {(1+⌊⍺÷⍨¯1+⍳≢⍵)⊆⍵}
+/p¨(⊃∘⊃∩/)¨3 chunk input
