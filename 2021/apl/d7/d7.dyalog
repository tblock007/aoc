⍝ Parse input.
input ← ⍎⊃⊃⎕NGET'G:\Folders\Programming\aoc\2021\apl\d7\input7.txt' 1

⍝ Part 1
p ← input[⍋input][⌊0.5×≢input]
+/|p-input

⍝ Part 2
⍝ Returns the cost of moving from ⍺ to ⍵.
cost ← { d←|⍺-⍵ ⋄ 0.5×d×d+1 }
⍝ Returns the cost of moving all crabs from positions ⍺ to ⍵.
totalCost ← { +/⍵ cost¨ ⍺ }
⌊/(⊂input) totalCost¨ ¯1+⍳(1+⌈/input)