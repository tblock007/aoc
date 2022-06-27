⍝ Parse input.
input ← ⊃⎕NGET'G:\Folders\Programming\aoc\2021\apl\d4\input4.txt' 1
nums ← ⍎⊃input
boards ← {5 5⍴⍎⍕input[⍵]}¨(¯4+6×⍳100)+⊂(⍳5)

⍝ Given an array of called numbers ⍺ and board ⍵, determines whether a bingo has occurred.
isWin ← { b←⍵∊⍺ ⋄ ∨/(∧/b),(∧⌿b) }
⍝ Computes the score of a winning board ⍵ with called numbers ⍺.
score ← { b←⍵∊⍺ ⋄ ⍺[≢⍺]×+/+/(1-b)×⍵ }
⍝ Array representing each step of the numbers called.
steps ← (⍳100)↑¨⊂nums
⍝ The number of steps required for each board to win.
winSteps ← { (steps isWin¨ ⊆⍵) ⍳ 1 }¨ boards

⍝ Part 1
(⊃steps[⌊/winSteps]) score (⊃boards[winSteps ⍳ ⌊/winSteps])

⍝ Part 2
(⊃steps[⌈/winSteps]) score (⊃boards[winSteps ⍳ ⌈/winSteps])