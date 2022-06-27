⍝ Parse input.
input ← ⊃⎕NGET'G:\Folders\Programming\aoc\2021\apl\d5\input5.txt' 1
i ← { r←⍵ ⋄ r[⍸⍵∊',->']←' ' ⋄ ⍎r }¨ input

⍝ Generates a sequential range from ⍺ to ⍵, handling the decreasing case as well.
range ← { 
    ⍺=⍵: ⍺
    ⍺<⍵: ,[0.5](⍺-1)+⍳(1+⍵-⍺)
    (⍺+⍵)-(⍵∇⍺)
}
⍝ Generates an array of indices touched by a line of input ⍵.
indices ← { (x1 y1 x2 y2)←⍵ ⋄ ↓⍉(x1 range x2)⍪(y1 range y2) }
⍝ Counts the number of overlaps for an array of entries ⍵.
countOverlap ← { +/+/⊃1<+/{m←1000 1000⍴0 ⋄ m[indices ⍵]←1 ⋄ m}¨⍵ }

⍝ Part 1
countOverlap ({(⍵[1]=⍵[3])∨(⍵[2]=⍵[4])}¨ i)/i

⍝ Part 2
countOverlap i