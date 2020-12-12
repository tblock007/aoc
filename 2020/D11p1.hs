import D11input
import qualified Data.List as List
import qualified Data.Maybe as Maybe
import Data.Vector as Vector


type Grid = Vector (Vector Char)

grid :: [String] -> Grid
grid strings = fromList (List.map fromList strings)

getOffsets :: (Int, Int) -> [(Int, Int)]
getOffsets (i,j) = [(i-1,j-1), (i,j-1), (i+1,j-1),
                    (i-1,j), (i+1,j),
                    (i-1,j+1), (i,j+1), (i+1,j+1)]

(!!!) :: Grid -> (Int,Int) -> Maybe Char
(!!!) g (i,j) = do
    row <- g !? i
    c <- row !? j
    return c

countNeighbors :: Grid -> (Int, Int) -> Int
countNeighbors g (i,j) = 
    let neighbors = Maybe.catMaybes $ List.map (g!!!) $ getOffsets (i,j)
     in List.sum $ List.map (\c -> if c == '#' then 1 else 0) neighbors

nextChar :: Grid -> (Int,Int) -> Char
nextChar g pos
    | curr == '.' = '.'
    | curr == 'L' && numNeighbors == 0 = '#'
    | curr == '#' && numNeighbors >= 4 = 'L'
    | otherwise = curr
        where curr = Maybe.fromJust (g !!! pos)
              numNeighbors = countNeighbors g pos

updateGrid :: Grid -> Grid
updateGrid g = Vector.map convertRow $ fromList [0..(Vector.length g)-1]
    where
        convertRow i = 
            let numCols = Vector.length (g ! i)
                indices = Vector.zip (Vector.replicate numCols i) $ fromList [0..numCols-1]
             in Vector.map (nextChar g) indices

steadyState :: Grid -> Grid
steadyState g
    | g == u = u
    | otherwise = steadyState u
        where u = updateGrid g

countOccupied :: Grid -> Int
countOccupied g = Vector.sum $ Vector.map sumRow g
    where
        sumRow row = Vector.sum $ Vector.map (\c -> if c == '#' then 1 else 0) row

solve :: Int
solve = countOccupied $ steadyState (grid input)

main :: IO ()
main = print $ solve