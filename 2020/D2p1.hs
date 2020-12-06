import D2input

isValid :: (Int, Int, Char, String) -> Bool
isValid (min, max, c, pw) = 
    let occurrences = length $ filter (==c) pw
    in (occurrences >= min && occurrences <= max)

solve :: Int
solve = length $ filter isValid input

main :: IO ()
main = print solve