import D17input
import Data.List as List
import Data.Maybe as Maybe
import Data.Vector as Vector

import Control.Comonad
import Control.Monad as M

type Grid = Vector (Vector (Vector Char))
type Coords = (Int, Int, Int)

dim = 25
idim = 8

emptyPlane :: Vector (Vector Char)
emptyPlane = Vector.replicate dim (Vector.replicate dim '.')

plane :: [String] -> Vector (Vector Char)
plane strings = 
    let npad = div (dim - idim) 2
        hPadding = List.replicate npad '.'
        hPadded = List.map (\s -> hPadding List.++ s List.++ hPadding) strings
        emptyRow = List.replicate dim '.'
        vPadding = List.replicate npad emptyRow
        listGrid = vPadding List.++ hPadded List.++ vPadding
     in fromList $ List.map fromList listGrid

grid :: [String] -> Grid
grid strings = 
    let padding = Vector.replicate (div dim 2) emptyPlane
     in padding Vector.++ (Vector.singleton (plane strings)) Vector.++ padding

getOffsets :: Coords -> [Coords]
getOffsets (i,j,k) = [(x, y, z) | x <- [i-1, i, i+1],
                                  y <- [j-1, j, j+1],
                                  z <- [k-1, k, k+1],
                                  x /= i || y /= j || z /= k]

(!!!?) :: Grid -> Coords -> Maybe Char
(!!!?) g (i,j,k) = do
    xp <- g !? i
    yr <- xp !? j
    z <- yr !? k
    return z

countNeighbors :: Grid -> Coords -> Int
countNeighbors g pos = 
    let neighbors = Maybe.catMaybes $ List.map (g!!!?) $ getOffsets pos
     in List.sum $ List.map (\c -> if c == '#' then 1 else 0) neighbors

nextChar :: Grid -> Coords -> Char
nextChar g pos
    | curr == '.' && numNeighbors == 3 = '#'
    | curr == '#' && (numNeighbors > 3 || numNeighbors < 2) = '.'
    | otherwise = curr
        where curr = Maybe.fromJust (g !!!? pos)
              numNeighbors = countNeighbors g pos

updateGrid :: Grid -> Grid
updateGrid g = fromList $ List.map convertPlane [0..(Vector.length g)-1]
    where
        convertPlane :: Int -> Vector (Vector Char)
        convertPlane i =
            let num = Vector.length (g ! i)
                ijs = List.zip (repeat i) [0..num-1]
             in fromList $ List.map (convertRow) ijs

        convertRow :: (Int,Int) -> Vector Char
        convertRow (i,j) = 
            let num = Vector.length ((g ! i) ! j)
                ijks = List.zipWith (\(a,b) c -> (a,b,c)) (repeat (i,j)) [0..num-1]
             in fromList $ List.map (nextChar g) ijks

countOccupied :: Grid -> Int
countOccupied g = Vector.sum $ Vector.map sumPlane g
    where
        sumPlane plane = Vector.sum $ Vector.map sumRow plane
        sumRow row = Vector.sum $ Vector.map (\c -> if c == '#' then 1 else 0) row

solve :: Int
solve = countOccupied $ List.head $ List.drop 6 $ iterate updateGrid (grid input)

main :: IO ()
main = print $ solve

printGrid :: Grid -> IO ()
printGrid g = do
    M.forM_ g $ \p -> do
        M.forM_ p $ \r -> do
            putStr $ Vector.toList r
            putStr "\n"
        putStr "\n"
