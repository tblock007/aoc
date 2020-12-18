import D17input
import Data.List as List
import Data.Maybe as Maybe
import Data.Vector as Vector

import Control.Monad as M

type Grid = Vector (Vector (Vector (Vector Char)))
type Space = Vector (Vector (Vector Char))
type Plane = Vector (Vector Char)
type Line = Vector Char
type Coords = (Int, Int, Int, Int)

dim = 20
idim = 8

emptySpace :: Space
emptySpace = Vector.replicate dim emptyPlane

emptyPlane :: Plane
emptyPlane = Vector.replicate dim (Vector.replicate dim '.')

plane :: [String] -> Plane
plane strings = 
    let npad = div (dim - idim) 2
        hPadding = List.replicate npad '.'
        hPadded = List.map (\s -> hPadding List.++ s List.++ hPadding) strings
        emptyLine = List.replicate dim '.'
        vPadding = List.replicate npad emptyLine
        listGrid = vPadding List.++ hPadded List.++ vPadding
     in fromList $ List.map fromList listGrid

grid :: [String] -> Grid
grid strings = 
    let spacePadding = Vector.replicate (div dim 2) emptyPlane
        paddedSpace = spacePadding Vector.++ (Vector.singleton (plane strings)) Vector.++ spacePadding
        padding = Vector.replicate (div dim 2) emptySpace
     in padding Vector.++ (Vector.singleton paddedSpace) Vector.++ padding

getOffsets :: Coords -> [Coords]
getOffsets (i,j,k,l) = [(w, x, y, z) | w <- [i-1, i, i+1],
                                       x <- [j-1, j, j+1],
                                       y <- [k-1, k, k+1],
                                       z <- [l-1, l, l+1],
                                       w /= i || x /= j || y /= k || z /= l]

(!!!?) :: Grid -> Coords -> Maybe Char
(!!!?) g (i,j,k,l) = do
    ws <- g !? i
    xp <- ws !? j
    yr <- xp !? k
    z <- yr !? l
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
updateGrid g = fromList $ List.map convertSpace [0..(Vector.length g)-1]
    where
        convertSpace :: Int -> Space
        convertSpace i =
            let num = Vector.length (g ! i)
                ijs = List.zip (repeat i) [0..num-1]
             in fromList $ List.map convertPlane ijs

        convertPlane :: (Int,Int) -> Plane
        convertPlane (i,j) =
            let num = Vector.length ((g ! i) ! j)
                ijks = List.zipWith (\(a,b) c -> (a,b,c)) (repeat (i,j)) [0..num-1]
             in fromList $ List.map convertLine ijks

        convertLine :: (Int,Int,Int) -> Line
        convertLine (i,j,k) = 
            let num = Vector.length (((g ! i) ! j) ! k)
                ijkls = List.zipWith (\(a,b,c) d -> (a,b,c,d)) (repeat (i,j,k)) [0..num-1]
             in fromList $ List.map (nextChar g) ijkls

countOccupied :: Grid -> Int
countOccupied g = Vector.sum $ Vector.map sumSpace g
    where
        sumSpace space = Vector.sum $ Vector.map sumPlane space
        sumPlane plane = Vector.sum $ Vector.map sumLine plane
        sumLine line = Vector.sum $ Vector.map (\c -> if c == '#' then 1 else 0) line

solve :: Int
solve = countOccupied $ List.head $ List.drop 6 $ iterate updateGrid (grid input)

main :: IO ()
main = print $ solve

-- printGrid :: Grid -> IO ()
-- printGrid g = do
--     M.forM_ g $ \p -> do
--         M.forM_ p $ \r -> do
--             putStr $ Vector.toList r
--             putStr "\n"
--         putStr "\n"
