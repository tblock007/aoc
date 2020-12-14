import D13input

eEuclid :: (Int, Int, Int) -> (Int, Int, Int) -> (Int, Int, Int)
eEuclid (r, s, t) (r', s', t')
    | r' == 0 = (r, s, t)
    | otherwise = let q = r `div` r'
                   in eEuclid (r', s', t') (r `mod` r', s - q * s', t - q * t')   

bezout :: (Int, Int) -> (Int, Int)
bezout (a, b) = let (_, s, t) = eEuclid (a, 1, 0) (b, 0, 1)
                 in (s, t)

waitTime :: Int -> Int -> Int
waitTime t b = (-t) `mod` b

primesAndRemainders :: [Int] -> [(Int,Int)]
primesAndRemainders bs = 
    let pairs = filter (\(_, x) -> x /= 1) (zip [0..] bs)
     in map (\p@(i,b) -> (b, uncurry waitTime p)) pairs

chineseRemainder :: ([Int], [Int]) -> Int
chineseRemainder (ps, rs) =
    let n = foldr (*) 1 ps
        ns = map (div n) ps
        ms = map (fst . bezout) (zip ns ps)
        x = sum $ zipWith3 (\a b c -> a * b * c) rs ms ns
     in x `mod` n

solve :: Int
solve = chineseRemainder $ unzip $ primesAndRemainders input

main :: IO ()
main = print $ solve