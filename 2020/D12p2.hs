import D12input

type WRelCoords = (Int, Int)
type SAbsCoords = (Int, Int)

rotateRight :: String -> WRelCoords -> WRelCoords
rotateRight "90" (x,y) = (y,-x)
rotateRight "180" (x,y) = (-x,-y)
rotateRight "270" (x,y) = (-y,x)

rotateLeft :: String -> WRelCoords -> WRelCoords
rotateLeft "90" = rotateRight "270"
rotateLeft "180" = rotateRight "180"
rotateLeft "270" = rotateRight "90"

moveForward :: Int -> WRelCoords -> SAbsCoords -> SAbsCoords
moveForward n (dx, dy) (x, y) = (x + n*dx, y + n*dy)

execute :: [(String, String)] -> (WRelCoords, SAbsCoords) -> (WRelCoords, SAbsCoords)
execute [] state = state
execute ((c,v):cvs) ((dx, dy), (x, y))
    | c == "N" = execute cvs ((dx, dy+n), (x, y))
    | c == "S" = execute cvs ((dx, dy-n), (x, y))
    | c == "E" = execute cvs ((dx+n, dy), (x, y))
    | c == "W" = execute cvs ((dx-n, dy), (x, y))
    | c == "L" = execute cvs (rotateLeft v (dx,dy), (x, y))
    | c == "R" = execute cvs (rotateRight v (dx,dy), (x, y))
    | c == "F" = execute cvs ((dx, dy), moveForward n (dx, dy) (x, y))
        where n = read v :: Int

solve :: Int
solve = let (_, (x, y)) = execute input ((10, 1), (0, 0))
         in (abs x + abs y)

main :: IO ()
main = print $ solve