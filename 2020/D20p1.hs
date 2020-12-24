import D20input
import Control.Monad
import qualified Data.List as List
import Data.Map.Strict (Map)
import qualified Data.Map.Strict as Map
import Data.Set (Set)
import qualified Data.Set as Set
import Data.Vector (Vector, (!))
import qualified Data.Vector as Vector

type Tile = [String]
type Edge = Int
type Edges = ((Edge, Edge, Edge, Edge), (Edge, Edge, Edge, Edge))

-- (i,r,m) represents tileId i rotated by r and mirrored iff m
type TileConfig = (Int, Int, Bool)

toInt :: String -> Int
toInt s =
    let ds = map (\c -> if c == '#' then 1 else 0) s
     in foldl (\b a -> 2 * b + a) 0 ds

getEdges :: Tile -> Edges
getEdges t =
    let e1 = head t
        e2 = map last t
        e3 = reverse $ last t
        e4 = reverse $ map head t
        re1 = reverse e1
        re2 = reverse e2
        re3 = reverse e3
        re4 = reverse e4
     in ((toInt e1, toInt e2, toInt e3, toInt e4),
         (toInt re1, toInt re2, toInt re3, toInt re4))

rotate :: Int -> Edges -> Edges
rotate 0 es = es
rotate 1 ((e1, e2, e3, e4), (re1, re2, re3, re4)) = 
    ((e2, e3, e4, e1), (re2, re3, re4, re1))
rotate n es = rotate (n - 1) (rotate 1 es)

mirror :: Bool -> Edges -> Edges
mirror False es = es
mirror True ((e1, e2, e3, e4), (re1, re2, re3, re4)) =
    ((re1, re4, re3, re2), (e1, e4, e3, e2))

isVertMatch :: Edges -> Edges -> Bool
isVertMatch top@(_,(_,_,re3,_)) bottom@((e1,_,_,_),_) = re3 == e1

isHorizMatch :: Edges -> Edges -> Bool
isHorizMatch left@(_,(_,re2,_,_)) right@((_,_,_,e4),_) = re2 == e4

fitsNext :: Vector Edges -> Edges -> Bool
fitsNext v es =
    let n = length v
        fitsUp =   if (n - dim) < 0
                   then True
                   else isVertMatch (v ! (n - dim)) es
        fitsLeft = if n `mod` dim == 0
                   then True
                   else isHorizMatch (v ! (n - 1)) es
     in fitsUp && fitsLeft

tileChoices :: [Tile] -> [(TileConfig, Edges)]
tileChoices tiles = do
    m <- [False, True]
    r <- [0..3]
    (i, es) <- List.zip [0..] (List.map getEdges tiles)
    return ((i, r, m), es)

type AccState = ([TileConfig], Vector Edges, Set Int)

addAssignment :: AccState -> [(TileConfig, Edges)] -> [AccState]
addAssignment (cs, es, seen) allConfigs = do
    (config@(t,r,m), rawNextEdges) <- allConfigs
    nextEdges <- pure $ rotate r (mirror m rawNextEdges)
    guard (not $ Set.member t seen)
    guard (fitsNext es nextEdges)
    updatedEdges <- pure $ Vector.snoc es nextEdges
    updatedSeen <- pure $ Set.insert t seen
    return (config:cs, updatedEdges, updatedSeen)

getValidAssignment :: [Tile] -> Int -> [TileConfig]
getValidAssignment ts d =  
    let tilePools = replicate (d*d) (tileChoices ts)
        init = ([], Vector.empty, Set.empty)
        (l,_,_) = head $ foldM addAssignment init tilePools
     in l

cornerIndices :: Int -> [Int]
cornerIndices d = [0, d-1, d*(d-1), d*d-1]

blankLineSplit :: [String] -> [[String]]
blankLineSplit lines = 
    let matchingBlankLineStatus s1 s2 = (s1 == "") == (s2 == "")
        grouped = List.groupBy matchingBlankLineStatus lines
        isNotBlankLineGroup g = (head g) /= ""
     in filter isNotBlankLineGroup grouped

solve :: Integer
solve = let tiles = blankLineSplit tilesRaw
            assignment = getValidAssignment tiles dim
            cornerTiles = List.map (assignment !!) (cornerIndices dim)
            tileIndices = List.map (\(t,_,_) -> toInteger (tileIds !! t)) cornerTiles
         in List.foldr (*) 1 tileIndices

main :: IO ()
main = print $ solve