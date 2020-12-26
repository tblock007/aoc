import D21input
import Data.List as List
import Data.Map.Strict as Map
import Data.Set as Set

type IngredientList = ([String], [String])
type PossStrings = Map.Map String (Set.Set String)

addRow :: IngredientList -> PossStrings -> PossStrings
addRow (_, []) acc = acc
addRow (is, (a:as)) acc = 
    Map.insertWith Set.intersection a (Set.fromList is) (addRow (is, as) acc)

getPossAllergens :: PossStrings -> Set.Set String
getPossAllergens = Map.foldr Set.union Set.empty

getAllIngredients :: [IngredientList] -> [String]
getAllIngredients l = List.concat $ List.map fst l

solve :: Int
solve = let allergenMap = List.foldr addRow Map.empty input
            possAllergens = getPossAllergens allergenMap
            allIngredients = getAllIngredients input
            isPossAllergen = ((flip Set.member) possAllergens)
            allSafe = List.filter (not . isPossAllergen) allIngredients
         in List.length allSafe

main :: IO ()
main = print $ solve
