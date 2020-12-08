import D8input
import qualified Data.Maybe as Maybe
import qualified Data.Set as Set
import qualified Data.Map.Strict as Map

-- Maps PC to the (op, arg) pair.
type Program = Map.Map Int (String, String)
-- Holds current PC and ACC values.
type ProgramState = (Int, Int)

getAccAtRepeat :: Program -> ProgramState -> Set.Set Int -> Maybe Int
getAccAtRepeat prog (pc, acc) visited
    | Set.member pc visited = Just acc
    | otherwise = 
        let newVisited = Set.union visited (Set.singleton pc)
        in case Map.lookup pc prog of
            Nothing -> Nothing
            Just (op, arg) ->
                case op of
                    "nop" -> getAccAtRepeat prog (pc + 1, acc) newVisited
                    "acc" -> getAccAtRepeat prog (pc + 1, acc + (read arg)) newVisited
                    "jmp" -> getAccAtRepeat prog (pc + (read arg), acc) newVisited

solve :: Int
solve = Maybe.fromJust $ getAccAtRepeat (Map.fromList $ zip [0..] input) (0, 0) Set.empty

main :: IO ()
main = print $ solve