import D3input

countTrees :: [String] -> Int -> Int
countTrees [] _ = 0
countTrees field col =
    let numTrees = if ((head field) !! col == '#') then 1 else 0
        numCols = length $ head field
    in numTrees + countTrees (tail field) (mod (col + rightSteps) numCols)

solve :: Int
solve = countTrees input 0

main :: IO ()
main = print solve