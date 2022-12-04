import Data.Char (ord)
import qualified Data.Set as Set

main :: IO ()
main = interact (writeOutput . solve . readInput)

chunk :: Int -> [a] -> [[a]]
chunk _ [] = []
chunk n xs = (take n xs):(chunk n (drop n xs))

readInput :: String -> [[String]]
readInput =  chunk 3 . lines

writeOutput :: Int -> String
writeOutput x = show x ++ "\n"

findCommon :: [String] -> Char
findCommon ss = Set.findMin $ foldr1 Set.intersection $ map Set.fromList ss

priority :: Char -> Int
priority c
      | c >= 'a' && c <= 'z' = ord c - ord 'a' + 1
      | c >= 'A' && c <= 'Z' = ord c - ord 'A' + 27

solve :: [[String]] -> Int
solve = sum . map (priority . findCommon)
