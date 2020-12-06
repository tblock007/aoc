import D3input

countTrees :: [String] -> Int -> Int
countTrees [] _ = 0
countTrees field col =
    let numTrees = if ((head field) !! col == '#') then 1 else 0
        numCols = length $ head field
    in numTrees + countTrees (tail field) (mod (col + rightSteps) numCols)

hasTreeInCol :: (Int, String) -> Int
hasTreeInCol (colIndex, row) = 
    let actualColIndex = colIndex `mod` (length row)
     in if (row !! actualColIndex == '#') then 1 else 0

hasTreeOnPath :: Int -> [String] -> [Int]
hasTreeOnPath step field =
    let indexed = zip [0,step..] field
     in map hasTreeInCol indexed

ct :: [String] -> Int -> Int
ct field step = foldr (+) 0 (hasTreeOnPath step field)


solve :: Int
solve = ct input rightSteps

main :: IO ()
main = print solve