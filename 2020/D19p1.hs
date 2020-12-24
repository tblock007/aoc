import D19input
import qualified Data.IntMap.Lazy as Map
import qualified Data.List as List
import qualified Data.Maybe as Maybe

type Rule = [[Int]]

stripRule :: String -> Map.IntMap Rule -> Int -> [String]
stripRule "" _ _ = []
stripRule s m index
    | index == aRule = if head s == 'a' then [tail s] else []
    | index == bRule = if head s == 'b' then [tail s] else []
    | otherwise =
        let (Just r) = Map.lookup index m
         in concat $ List.map (stripRuleSeq s m) r

stripRuleSeq :: String -> Map.IntMap Rule -> [Int] -> [String]
stripRuleSeq s m [] = [s]
stripRuleSeq s m (i:is) = do
    suffix <- stripRule s m i
    stripRuleSeq suffix m is

matchesRule :: Map.IntMap Rule -> Int -> String -> Bool
matchesRule m i s =
    let tails = stripRule s m i
     in List.elem "" tails

solve :: Int
solve = let rulesMap = Map.fromList rules
         in length $ filter (matchesRule rulesMap 0) input

main :: IO ()
main = print $ solve