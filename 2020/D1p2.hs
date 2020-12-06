import D1input

cartesianProduct :: [Int] -> [Int] -> [Int] -> [(Int, Int, Int)]
cartesianProduct xs ys zs = [(x, y, z) | x <- xs, y <- ys, z <- zs]

findTriple :: [Int] -> Int -> (Int, Int, Int)
findTriple entries target = 
    let triples = cartesianProduct entries entries entries
    in head $ filter (\(x,y,z) -> x + y + z == target) triples

solve :: Int
solve =
    let (x,y,z) = findTriple input targetSum
    in x * y * z

main :: IO ()
main = print solve