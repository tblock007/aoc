import D12input

-- 0 is north, 1 is east, 2 is south, 3 is west
dd :: [(Int, Int)]
dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]

rotateRight :: String -> Int -> Int
rotateRight "90" d = mod (d + 1) 4
rotateRight "180" d = mod (d + 2) 4
rotateRight "270" d = mod (d + 3) 4

rotateLeft :: String -> Int -> Int
rotateLeft "90" = rotateRight "270"
rotateLeft "180" = rotateRight "180"
rotateLeft "270" = rotateRight "90"

moveForward :: Int -> (Int, Int, Int) -> (Int, Int, Int)
moveForward n (x, y, d) =
    let (dx, dy) = dd !! d
     in (x + n*dx, y + n*dy, d)

execute :: [(String, String)] -> (Int, Int, Int) -> (Int, Int, Int)
execute [] state = state
execute ((c,v):cvs) (x,y,d)
    | c == "N" = execute cvs (x, y+n, d)
    | c == "S" = execute cvs (x, y-n, d)
    | c == "E" = execute cvs (x+n, y, d)
    | c == "W" = execute cvs (x-n, y, d)
    | c == "L" = execute cvs (x, y, rotateLeft v d)
    | c == "R" = execute cvs (x, y, rotateRight v d)
    | c == "F" = execute cvs (moveForward n (x, y, d))
        where n = read v :: Int

solve :: Int
solve = let (x, y, _) = execute input (0, 0, 1)
         in (abs x + abs y)

main :: IO ()
main = print $ solve