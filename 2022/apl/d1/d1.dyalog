⍝ Parse input.
input ← ⊃⎕NGET'G:\Folders\Programming\aoc\2022\apl\d1\input.txt' 1
groups ← ⍎¨¨(⊢⊆⍨(0<≢)¨) input

⍝ Part 1
⌈/+/¨groups

⍝ Part 2
+/3↑{⍵[⍒⍵]}+/¨groups
