import D21input
import Control.Monad
import Data.List as List
import Data.Map.Strict as Map
import Data.Set as Set

type IngredientList = ([String], [String])
type PossStrings = Map.Map String (Set.Set String)

addRow :: IngredientList -> PossStrings -> PossStrings
addRow (_, []) acc = acc
addRow (is, (a:as)) acc = 
    Map.insertWith Set.intersection a (Set.fromList is) (addRow (is, as) acc)

addAssignment :: [String] -> (String, Set.Set String) -> [[String]]
addAssignment curr (_, is) =
    [next:curr | next <- (Set.toList is) List.\\ curr]

solve :: String
solve = let allergenMap = List.foldr addRow Map.empty input
            ingredients = reverse $ head $ foldM addAssignment [] (Map.toList allergenMap)
         in intercalate "," ingredients

main :: IO ()
main = print $ solve
