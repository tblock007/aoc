import D9input
import qualified Data.List as List
import qualified Control.Monad as Monad

-- answer from part 1
invalid :: Integer
invalid = 133015568

partialSum :: [Integer] -> [Integer]
partialSum = scanl (+) 0

summingRangeIndices :: Integer -> [Integer] -> [(Int, Int)]
summingRangeIndices t list = do
    (i, ps1) <- zip [0..] (partialSum list)
    (j, ps2) <- zip [0..] (partialSum list)
    Monad.guard (i < j)
    Monad.guard (ps2 - ps1 == t)
    return (i,j)

summingRange :: Integer -> [Integer] -> [Integer]
summingRange t list =
    let (i,j) = head $ summingRangeIndices t list
     in List.take (j - i) $ drop i list

solve :: Integer
solve =
    let range = summingRange invalid input
     in (minimum range) + (maximum range)

main :: IO ()
main = print $ solve