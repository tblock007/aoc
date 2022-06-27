⍝ Parse input.
input←⍎⊃⊃⎕NGET'G:\Folders\Programming\aoc\2021\apl\d6\input6.txt' 1

⍝ Computes the initial counts of lanternfish stages.
init ← (⊂(input+1)) {+/⍵=⍺}¨⍳9
⍝ Simulates and returns the state one step after the state represented by ⍵.
step ← { r ← 1⌽⍵ ⋄ r[7] +← r[9] ⋄ r }

⍝ Part 1
+/(step⍣80)init

⍝ Part 2
+/(step⍣256)init  ⍝ Note: ⎕PP←13 or higher may be necessary.