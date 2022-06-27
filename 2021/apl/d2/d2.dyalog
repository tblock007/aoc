⍝ Parse input.
input ← ⊃⎕NGET'G:\Folders\Programming\aoc\2021\apl\d2\input2.txt' 1

⍝ Converts a string like "up 3" into a complex value.
toC ← {
    ⍵[1]='u': ⍎'0J¯',⍵[1+≢'up ']
    ⍵[1]='d': ⍎'0J',⍵[1+≢'down ']
    ⍎⍵[1+≢'forward ']
}
⍝ The directions provided in the input, represented as complex numbers.
i ← toC¨input
⍝ Returns a × b for complex number a+ib.
pxd ← { ×/9 11○⍵ }

⍝ Part 1
pxd +/i

⍝ Part 2
aim ← 0J1×11○+\i
pxd +/(i+i×aim)[⍸0=11○i]  
