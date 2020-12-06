import D3input

takeEvery :: Int -> [a] -> [a]
takeEvery _ [] = []
takeEvery n (x:xs) = x : (takeEvery n (drop (n - 1) xs))

countTreesAux :: [String] -> Int -> Int -> Int
countTreesAux [] _ _ = 0
countTreesAux field col rightSteps =
    let numTrees = if ((head field) !! col == '#') then 1 else 0
        numCols = length $ head field
    in numTrees + countTreesAux (tail field) (mod (col + rightSteps) numCols) rightSteps

countTrees :: [String] -> (Int, Int) -> Int
countTrees field (x, y) = 
    let stridedField = takeEvery x field 
    in countTreesAux stridedField 0 y

solve :: Int
solve  = foldr (*) 1 (map (countTrees input) slopes)

main :: IO ()
main = print solve