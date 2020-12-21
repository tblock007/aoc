import D14input
import Data.Bits
import qualified Data.Map.Strict as Map

fromBinary :: String -> Int
fromBinary s =
    let ds = map (\c -> if c == '1' then 1 else 0) s
     in foldl (\b a -> 2 * b + a) 0 ds

toReversedBinaryString :: Int -> String
toReversedBinaryString x
    | x == 0 = ""
    | otherwise = let d = if x `mod` 2 == 0 then '0' else '1'
                   in d:(toReversedBinaryString (x `div` 2))

applyMask :: String -> Int -> String
applyMask mask address =
    let s = (toReversedBinaryString address) ++ (repeat '0')
        m = reverse mask
        reversedResult = zipWith combineDigits s m
     in reverse reversedResult
        where combineDigits d1 d2
                | d2 == '1' || d2 == 'X' = d2
                | d2 == '0' = d1

expand :: String -> [String]
expand [] = [""]
expand (d:ds)
    | d == 'X' = map ('0':) (expand ds) ++ map ('1':) (expand ds)
    | otherwise = map (d:) (expand ds)

getAddresses :: String -> [Int]
getAddresses = map fromBinary . expand

insertMultiple :: [Int] -> Int -> Map.Map Int Int -> Map.Map Int Int
insertMultiple [] _ m = m
insertMultiple (k:ks) value m = Map.insert k value (insertMultiple ks value m)

execute :: [(String, String, String)] -> String -> Map.Map Int Int -> Map.Map Int Int
execute [] _ mem = mem
execute ((command, address, value):cs) mask mem
    | command == "mask" = execute cs value mem
    | command == "mem" = execute cs mask (insertMultiple addresses newValue mem)
        where addresses = getAddresses (applyMask mask (read address :: Int))
              newValue = read value :: Int

solve :: Int
solve = let mem = execute input "" Map.empty
         in Map.foldr (+) 0 mem

main :: IO ()
main = print $ solve