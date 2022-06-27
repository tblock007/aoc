⍝ Parse input.
input ← ⍎¨⊃⎕NGET'G:\Folders\Programming\aoc\2021\apl\d1\input1.txt' 1

⍝ Counts the number of increasing steps in a sequence ⍵.
countUp ← { +/(1↓⍵)>(¯1↓⍵) }
⍝ Produces a new sequence via sum of sliding windows of width 3 over the sequence ⍵.
window ← { +/1↓¯1↓(⊢⌺3)⍵ }    

⍝ Part 1
countUp input         ⍝ part 1

⍝ Part 2
countUp window input  ⍝ part 2
