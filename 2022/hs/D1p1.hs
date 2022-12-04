import Data.List (sort)

main :: IO ()
main = interact (writeOutput . solve . readInput)

splitBy :: String -> [String] -> [[String]]
splitBy _ [] = []
splitBy delim strs@(s:ss)
      | s == delim = splitBy delim ss
      | otherwise = c:splitBy delim rest
            where c = takeWhile (/= delim) strs
                  rest = dropWhile (/= delim) strs

readInput :: String -> [[Int]]
readInput =  map (map read) . splitBy "" . lines

writeOutput :: Int -> String
writeOutput x = show x ++ "\n"

solve :: [[Int]] -> Int
solve = maximum . map sum
