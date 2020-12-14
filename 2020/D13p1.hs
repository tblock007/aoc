import D13input

waitTime :: Int -> Int -> Int
waitTime t b = (-t) `mod` b

bestPair :: Int -> [Int] -> (Int, Int)
bestPair t bs = minimum (zip (map (waitTime t) bs) bs)

solve :: Int
solve = let (time, id) = bestPair earliest buses
         in (time * id)

main :: IO ()
main = print $ solve