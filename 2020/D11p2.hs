import D11input
import qualified Data.List as List
import qualified Data.Map.Strict as Map
import qualified Data.Maybe as Maybe
import Data.Vector as Vector


type Grid = Vector (Vector Char)

grid :: [String] -> Grid
grid strings = fromList (List.map fromList strings)

getNeighborInDirectionAux :: Grid -> (Int, Int) -> (Int, Int) -> Maybe (Int, Int)
getNeighborInDirectionAux g pos@(i,j) dir@(di,dj) =
    case g !!! pos of
        Nothing -> Nothing
        Just '.' -> getNeighborInDirectionAux g (i+di,j+dj) dir
        Just _ -> Just pos

getNeighborInDirection :: Grid -> (Int, Int) -> (Int, Int) -> Maybe (Int, Int)
getNeighborInDirection g pos@(i,j) dir@(di,dj) = 
    getNeighborInDirectionAux g (i+di,j+dj) dir

getNeighborsInView :: Grid -> (Int, Int) -> [(Int, Int)]
getNeighborsInView g pos =
    let dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
     in Maybe.catMaybes $ List.map (getNeighborInDirection g pos) dirs

neighborMap :: Map.Map (Int, Int) [(Int, Int)]
neighborMap =
    let numRows = List.length input
        numCols = List.length $ List.head input
        positions = [(i,j) | i <- [0..numRows-1], j <- [0..numCols-1]]
        neighbors = List.map (getNeighborsInView (grid input)) positions
     in Map.fromList $ List.zip positions neighbors

getNeighborOffsets :: (Int, Int) -> [(Int, Int)]
getNeighborOffsets pos = Maybe.fromJust $ Map.lookup pos neighborMap

(!!!) :: Grid -> (Int,Int) -> Maybe Char
(!!!) g (i,j) = do
    row <- g !? i
    c <- row !? j
    return c

countNeighbors :: Grid -> (Int, Int) -> Int
countNeighbors g (i,j) = 
    let neighbors = Maybe.catMaybes $ List.map (g!!!) $ getNeighborOffsets (i,j)
     in List.sum $ List.map (\c -> if c == '#' then 1 else 0) neighbors

nextChar :: Grid -> (Int,Int) -> Char
nextChar g pos
    | curr == '.' = '.'
    | curr == 'L' && numNeighbors == 0 = '#'
    | curr == '#' && numNeighbors >= 5 = 'L'
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