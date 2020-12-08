import D8input
import qualified Data.List as List
import qualified Data.Maybe as Maybe
import qualified Data.Set as Set
import qualified Data.Map.Strict as Map

-- Maps PC to the (op, arg) pair.
type Program = Map.Map Int (String, String)
-- Holds current PC and ACC values.
type ProgramState = (Int, Int)

getAccAtTerminate :: Program -> ProgramState -> Int -> Set.Set Int -> Maybe Int
getAccAtTerminate prog (pc, acc) end visited
    | pc == end = Just acc
    | Set.member pc visited = Nothing
    | otherwise = 
        let newVisited = Set.union visited (Set.singleton pc)
        in case Map.lookup pc prog of
            Nothing -> Nothing
            Just (op, arg) ->
                case op of
                    "nop" -> getAccAtTerminate prog (pc + 1, acc) end newVisited
                    "acc" -> getAccAtTerminate prog (pc + 1, acc + (read arg)) end newVisited
                    "jmp" -> getAccAtTerminate prog (pc + (read arg), acc) end newVisited

modifyProgram :: Program -> Int -> Maybe Program
modifyProgram prog pc =
    case Map.lookup pc prog of
        Nothing -> Nothing
        Just (op, arg) ->
            case op of
                "acc" -> Nothing
                "nop" -> Just $ Map.insert pc ("jmp", arg) prog
                "jmp" -> Just $ Map.insert pc ("nop", arg) prog

tryChange :: Program -> Int -> Maybe Int
tryChange prog pcToChange = do
    l <- Just (length prog)
    newProg <- modifyProgram prog pcToChange
    result <- getAccAtTerminate newProg (0, 0) l Set.empty
    return result

solve :: Int
solve = 
    let prog = Map.fromList $ zip [0..] input
     in head $ Maybe.catMaybes $ List.map (tryChange prog) [0..]

main :: IO ()
main = print $ solve