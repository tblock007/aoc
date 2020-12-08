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

insertParents :: String -> [(Int, String)] -> Map.Map String [String] -> Map.Map String [String]
insertParents _ [] m = m
insertParents p ((n,c):ncs) m = 
    Map.insertWith (++) c [p] (insertParents p ncs m)

parentMap :: Map.Map String [(Int, String)] -> Map.Map String [String]
parentMap containMap = Map.foldrWithKey insertParents Map.empty containMap

getAncestors :: Map.Map String [String] -> String -> Set.Set String
getAncestors m color =
    case Map.lookup color m of
        Nothing -> Set.empty
        Just colors -> 
            let parents = Set.fromList colors
                ancestors = foldr Set.union Set.empty (List.map (getAncestors m) colors)
             in Set.union parents ancestors

solve :: Int
solve = Set.size $ (getAncestors $ parentMap $ mapify input) "shiny gold"

main :: IO ()
main = print $ solve