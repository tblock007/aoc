import D2input

xor :: Bool -> Bool -> Bool
xor x y = (x && not y) || (not x && y)

isValid :: (Int, Int, Char, String) -> Bool
isValid (i1, i2, c, pw) = 
    let firstMatch = (pw !! (i1 - 1)) == c
        secondMatch = (pw !! (i2 - 1)) == c
    in xor firstMatch secondMatch

solve :: Int
solve = length $ filter isValid input

main :: IO ()
main = print solve