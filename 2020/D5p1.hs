import D5input

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

solve :: Int
solve = foldr max (-1) $ map seatId input

main :: IO ()
main = print $ solve