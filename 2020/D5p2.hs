import D5input
import qualified Data.Set as Set

toBinary :: String -> Int -> Int
toBinary [] _ = 0
toBinary (c:cs) p2 =
    let contribution = if c == 'B' || c == 'R' then p2 else 0
    in contribution + toBinary cs (p2 `div` 2)

seatId :: String -> Int
seatId s =
    let row = toBinary (take 7 s) 64
        col = toBinary (drop 7 s) 4
     in row * 8 + col

maxSeat :: Int
maxSeat = foldr max (-1) $ map seatId input

minSeat :: Int
minSeat = foldr min 1000000 $ map seatId input

solve :: Int
solve =
    let passIds = Set.fromList $ map seatId input
        allIds = Set.fromList [minSeat..maxSeat]
     in Set.elemAt 0 (allIds Set.\\ passIds)

main :: IO ()
main = print $ solve