import D1input

cartesianProduct :: [Int] -> [Int] -> [(Int, Int)]
cartesianProduct xs ys = [(x, y) | x <- xs, y <- ys]

findPair :: [Int] -> Int -> (Int, Int)
findPair entries target = 
    let pairs = cartesianProduct entries entries
    in head $ filter (\(x,y) -> x + y == target) pairs

solve :: Int
solve =
    let (x,y) = findPair input targetSum
    in x * y

main :: IO ()
main = print solve