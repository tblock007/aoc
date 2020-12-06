import D4input
import Data.List

containsAll :: [String] -> [String] -> Bool
containsAll tags (c:[]) = elem c tags
containsAll tags (c:cs)
    | elem c tags = containsAll tags cs
    | otherwise = False

isValid :: [String] -> Bool
isValid lines =
    let joined = intercalate " " lines
        tags = map (take 3) (words joined)
    in tags `containsAll` codes

countValid :: [String] -> Int
countValid [] = 0
countValid lines =
    let next = takeWhile (/="") lines
        remainder = tail $ dropWhile (/="") lines
        valid = if (isValid next) then 1 else 0
    in valid + countValid remainder

solve :: Int
solve = countValid input

main :: IO ()
main = print $ solve