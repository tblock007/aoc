⍝ Parse input.
input ← ⍎¨↑⊃⎕NGET'G:\Folders\Programming\aoc\2021\apl\d9\input9.txt' 1

⍝ Part 1
⍝ Returns 1 if the middle element of the 3x3 matrix ⍵ is the smallest of its direct neighbors, ignoring 0s.
isMin ← { 
    c←⍵
    (⍺[1]↑[1]c) ← 10
    (⍺[2]↑[2]c) ← 10
    (c[2;2]≠9) ∧ c[2;2]=⌊/(c[1;2], c[2;1], c[2;2], c[2;3], c[3;2])
}
mask ← (isMin⌺3 3) input
+/+/mask+mask×input

⍝ Part 2
⍝ Returns the index of the first occurrence of ⍵ (ravel order) in matrix ⍺. Returns (1+1⊃⍴⍺ 1) if the element is not found.
indexm ← { (h w)←⍴⍺ ⋄ i←(,⍺)⍳⍵ ⋄ (w|i)=0:(⌈i÷w),w ⋄ (⌈i÷w),(w|i) }
⍝ Returns all directly neighboring indices of ⍵ that do not have 1 in the corresponding value of ⍺.
neighbors ← {
    c ← (⊂⍵)+¨((¯1 0) (1 0) (0 ¯1) (0 1))
    c ← ((0<1∘⌷¨c)∧(0<2∘⌷¨c)∧((1⊃⍴⍺)≥1∘⌷¨c)∧((2⊃⍴⍺)≥2∘⌷¨c))/c
    (~⍺[c])/c
}
⍝ Fills all regions for all indices in ⍺ based on a "visited" mask in ⍵. Returns the size(s) of the region(s) filled, and the updated matrix.
fill ← {
    (≢⊆⍺)=0:(0 ⍵)
    m ← ⍵
    m[⊆⍺] ← 1
    nns←⊃∪/(⊆m)neighbors¨⊆⍺
    (n mm) ← nns∇m
    (n+≢⊆⍺) mm
}
⍝ Fills all regions in ⍵ and returns an array of the size of all regions filled.
countFills ← {
    m ← ⍵
    i ← m indexm 0
    i[1]>1⊃⍴m: ⍬
    (n mm) ← i fill m
    n,∇mm
}
b ← countFills 9=input
×/3↑b[⍒b]