import D16input

type Rule = (String, (Int, Int), (Int, Int))

check :: Int -> Rule -> Bool
check n (_, (a,b), (c,d)) = 
    ((n >= a) && (n <= b)) || ((n >= c) && (n <= d))

isValid :: [Rule] -> Int -> Bool
isValid rs n = any (check n) rs

solve :: Int
solve = sum $ filter (not . isValid rules) $ concat others

main :: IO ()
main = print $ solve