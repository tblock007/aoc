import D16input
import Control.Monad
import Data.List as List
import Data.Set as Set

-- The input has been modified so that rules are implicitly
-- keyed by Int instead of String. The six fields starting with
-- "departure" are keyed 0 to 5.
type Rule = ((Int, Int), (Int, Int))

check :: Int -> Rule -> Bool
check n ((a,b), (c,d)) = 
    ((n >= a) && (n <= b)) || ((n >= c) && (n <= d))

isValid :: [Rule] -> Int -> Bool
isValid rs n = let checkResults = List.map (check n) rs
                in List.foldr (||) False checkResults

isTicketValid :: [Rule] -> [Int] -> Bool
isTicketValid rs ns = List.foldr (&&) True $ List.map (isValid rs) ns

allSatisfy :: [Int] -> Rule -> Bool
allSatisfy ns r = List.foldr (&&) True $ List.map ((flip check) r) ns

isValidAtPosition :: [[Int]] -> Rule -> [Bool]
isValidAtPosition os@([]:_) r = []
isValidAtPosition os r =
    let col = List.map head os
        rest = List.map tail os
        valid = allSatisfy col r
     in valid : (isValidAtPosition rest r)
        
getValidPositions :: [[Int]] -> Rule -> [Int]
getValidPositions os r = 
    let flags = isValidAtPosition os r
     in List.map fst $ List.filter snd $ zip [0..] flags

addAssignment :: [Int] -> [Int] -> [[Int]]
addAssignment curr validPositions = 
    [next:curr | next <- (validPositions List.\\ curr)]

solve :: Int
solve =
    let filteredOthers = List.filter (isTicketValid irules) others
        positions = List.map (getValidPositions filteredOthers) irules
        assignment = reverse $ head $ foldM addAssignment [] positions
        fields = List.map (ticket !!) $ take 6 assignment
     in List.foldr (*) 1 fields

main :: IO ()
main = print $ solve
