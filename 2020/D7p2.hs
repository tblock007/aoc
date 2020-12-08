import D7input
import qualified Data.List as List
import qualified Data.Map.Strict as Map
import qualified Data.Set as Set

parseChildren :: [String] -> [(Int, String)]
parseChildren [] = []
parseChildren s = 
    let number = read (head s)
        color = unwords (take 2 $ tail s)
     in (number, color) : parseChildren (drop 4 s) 

parse :: String -> (String, [(Int, String)])
parse s =
    let tokens = words s
        key = unwords (take 2 tokens)
        children = parseChildren (drop 4 tokens)
     in if length tokens == 7
        then (key, [])
        else (key, children)
        
mapify :: [String] -> Map.Map String [(Int, String)]
mapify ss = Map.fromList (List.map parse ss)

countBags :: Map.Map String [(Int, String)] -> (Int, String) -> Int
countBags m (number,color) = 
    let Just childCounts = Map.lookup color m
        descendantBags = sum (List.map (countBags m) childCounts)
     in number * (1 + descendantBags)   

solve :: Int
solve = countBags (mapify input) (1, "shiny gold") - 1

main :: IO ()
main = print $ solve