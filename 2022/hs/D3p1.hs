import Data.Char (ord)
import qualified Data.Set as Set

main :: IO ()
main = interact (writeOutput . solve . readInput)

readInput :: String -> [String]
readInput =  lines

writeOutput :: Int -> String
writeOutput x = show x ++ "\n"

split :: String -> (String, String)
split s = (take h s, drop h s)
    where h = div (length s) 2

findDuplicate :: String -> Char
findDuplicate s = Set.findMin $ Set.intersection (Set.fromList s1) (Set.fromList s2)
      where (s1, s2) = split s

priority :: Char -> Int
priority c
      | c >= 'a' && c <= 'z' = ord c - ord 'a' + 1
      | c >= 'A' && c <= 'Z' = ord c - ord 'A' + 27

solve :: [String] -> Int
solve = sum . map (priority . findDuplicate)
