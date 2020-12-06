import D4input
import Data.Char
import Data.List

containsAll :: [String] -> [String] -> Bool
containsAll tags (c:[]) = elem c tags
containsAll tags (c:cs)
    | elem c tags = containsAll tags cs
    | otherwise = False

allTagsValid :: [String] -> [String] -> Bool
allTagsValid (t:[]) (v:[]) = isTagValid t v
allTagsValid (t:ts) (v:vs)
    | isTagValid t v = allTagsValid ts vs
    | otherwise = False

isHeightValid :: String -> Bool
isHeightValid s = let h = read (takeWhile isDigit s) :: Int
                      u = dropWhile isDigit s
                    in if u == "cm"
                        then h >= 150 && h <= 193
                        else h >= 59 && h <= 76

isHairColorValid :: String -> Bool
isHairColorValid (c:cs) =
    let isHexDigit d = isDigit d || (d >= 'a') || (d <= 'f')
        allHexDigits = foldr (&&) True (map isHexDigit cs)
     in (c == '#') && allHexDigits

isEyeColorValid :: String -> Bool 
isEyeColorValid = (flip elem) ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

isPidValid :: String -> Bool
isPidValid pid = (length pid == 9) && foldr (&&) True (map isDigit pid)

isTagValid :: String -> String -> Bool
isTagValid t v
    | t == "byr" = let y = read v in y >= 1920 && y <= 2002
    | t == "iyr" = let y = read v in y >= 2010 && y <= 2020
    | t == "eyr" = let y = read v in y >= 2020 && y <= 2030
    | t == "hgt" = isHeightValid v
    | t == "hcl" = isHairColorValid v
    | t == "ecl" = isEyeColorValid v
    | t == "pid" = isPidValid v
    | t == "cid" = True

isValid :: [String] -> Bool
isValid lines =
    let joined = intercalate " " lines
        tags = map (take 3) $ words joined
        values = map (drop 4) $ words joined
    in (tags `containsAll` codes) && (allTagsValid tags values)

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