import D6input
import qualified Data.Set as Set
import qualified Data.List as List

blankLineSplit :: [String] -> [[String]]
blankLineSplit lines = 
    let matchingBlankLineStatus s1 s2 = (s1 == "") == (s2 == "")
        grouped = List.groupBy matchingBlankLineStatus lines
        isNotBlankLineGroup g = (head g) /= ""
     in filter isNotBlankLineGroup grouped

countCommonLetters :: [String] -> Int
countCommonLetters ss = 
    let init = Set.fromList ['a'..'z']
        sets = List.map Set.fromList ss
        commonSet = foldr Set.intersection init sets
     in Set.size commonSet

solve :: Int
solve = sum $ map countCommonLetters $ blankLineSplit input

main :: IO ()
main = print $ solve