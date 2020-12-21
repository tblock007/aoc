import D14input
import Data.Bits
import qualified Data.Map.Strict as Map

fromBinary :: String -> Int
fromBinary s =
    let ds = map (\c -> if c == '1' then 1 else 0) s
     in foldl (\b a -> 2 * b + a) 0 ds

type AndMask = Int
type OrMask = Int
data BitMask = BitMask AndMask OrMask deriving Show

fromString :: String -> BitMask
fromString s =
    let a = map (\c -> if c == 'X' then '1' else c) s
        o = map (\c -> if c == 'X' then '0' else c) s
     in BitMask (fromBinary a) (fromBinary o)

maskWith :: BitMask -> Int -> Int
maskWith (BitMask a o) x = x .&. a .|. o

execute :: [(String, String, String)] -> BitMask -> Map.Map String Int -> Map.Map String Int
execute [] _ mem = mem
execute ((command, address, value):cs) mask mem
    | command == "mask" = execute cs (fromString value) mem
    | command == "mem" = execute cs mask (Map.insert address newValue mem)
        where newValue = maskWith mask (read value :: Int)

solve :: Int
solve = let mem = execute input (fromString "") Map.empty
         in Map.foldr (+) 0 mem

main :: IO ()
main = print $ solve