⍝ Parse input.
input ← ⊃⎕NGET'G:\Folders\Programming\aoc\2021\apl\d3\input3.txt' 1
m ← ⍎¨1000 12⍴⊃,/input

⍝ Converts an array ⍵ representing binary digits to a decimal value.
b2d ← { +/(2*(≢⍵)-⍳≢⍵)×⍵ }
⍝ Determines the most common bit in the matrix ⍵ at a specified position ⍺.
mc ← { ⌊0.5+÷(≢⍵)÷+⌿⍵[;⍺] }
⍝ Filters out rows of the matrix ⍵[2] based on the more common bit in position ⍵[1]. Returns an incremented ⍵[1] to facilitate repeated function application. 
filterh ← { (n m) ← ⍵ ⋄ 1=≢m:(n,⊂m) ⋄ (n+1),⊂(m[;n]=(n mc m))⌿m }
⍝ Like filterh above, but for the less common bit.
filterl ← { (n m) ← ⍵ ⋄ 1=≢m:(n,⊂m) ⋄ (n+1),⊂(m[;n]=1-(n mc m))⌿m }

⍝ Part 1
gammab ← (⍳12) mc m
(b2d gammab) × (b2d 1-gammab)

⍝ Part 2
o2b ← ⊃2⌷(filterh⍣12) (1 m)
co2b ← ⊃2⌷(filterl⍣12) (1 m)  
(b2d o2b[1;]) × (b2d co2b[1;])