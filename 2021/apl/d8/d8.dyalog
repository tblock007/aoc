⍝ Parse input.
input ← ⊃⎕NGET'G:\Folders\Programming\aoc\2021\apl\d8\input8.txt' 1

⍝ Part 1
⍝ Extracts the output strings (last four strings) from a line of input ⍵.
outputStrings ← { (t ← ' ' (≠⊆⊢) ⍵)[12 13 14 15] }
⍝ Counts the number of 1s, 4s, 7s, and 8s in a line of input ⍵.
count1478 ← { +/(≢¨outputStrings ⍵)∊(2 4 3 7) }
+/count1478¨input

⍝ Part 2
⍝ Returns the digit corresponding to a seven-segment string ⍵. Returns 10 if the string does not correspond to a digit.
decodeDigit ← { ¯1+('abcefg' 'cf' 'acdeg' 'acdfg' 'bcdf' 'abdfg' 'abdefg' 'acf' 'abcdefg' 'abcdfg')⍳⊂⍵[⍋⍵] }
⍝ Extracts all seven-segment strings from a line of input ⍵, removing the '|' character.
allStrings ← { t ← ' ' (≠⊆⊢) ⍵ ⋄ t[(⍳10), 12 13 14 15] }
⍝ Returns all permutations of the array ⍵.
perms ← { 1≥⍴⍵:1 1⍴⍵ ⋄ ↑⍪/⍵(,∘∇)¨(⍵∘~¨⍵) }
⍝ Applies a permutation ⍺, represented using integers 1..n to a seven-segment string ⍵.
applyPerm ← { (⊂⍺) {'abcdefg'[⍺['abcdefg'⍳⍵]]}¨ ⍵ }
⍝ Returns 1 if all strings in ⍵ decode to a digit.
check ← { ^/10≠decodeDigit¨ ⍵ }
⍝ Converts an array of digits to its decimal value. e.g., 4 7 2 7 → 4727
toDec ← { +/⍵×10*(≢⍵)-⍳≢⍵ }
⍝ Decodes a line of input ⍵, returning the four digit value.
decode ← {
    ps ← ↓perms ⍳7
    codes ← allStrings ⍵
    pi ← ⍸ check¨ (⊂codes) applyPerm⍨¨ ps
    toDec (decodeDigit¨ (⊃ps[pi]) applyPerm codes)[11 12 13 14]
}
+/decode¨input