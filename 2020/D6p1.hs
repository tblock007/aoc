import D6input
import qualified Data.Set as Set
import qualified Data.List as List

blankLineSplit :: [String] -> [[String]]
blankLineSplit lines = 
    let matchingBlankLineStatus s1 s2 = (s1 == "") == (s2 == "")
        grouped = List.groupBy matchingBlankLineStatus lines
        isNotBlankLineGroup g = (head g) /= ""
     in filter isNotBlankLineGroup grouped

countUniqueLetters :: [String] -> Int
countUniqueLetters = 
    Set.size . (foldr Set.union Set.empty) . (List.map Set.fromList)

solve :: Int
solve = sum $ map countUniqueLetters $ blankLineSplit input

main :: IO ()
main = print $ solve