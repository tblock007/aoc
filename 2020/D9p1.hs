import D9input
import qualified Data.List as List
import qualified Data.Maybe as Maybe
import qualified Data.Set as Set
import qualified Control.Monad as Monad

winLength :: Int
winLength = 25

windows :: [Integer] -> [[Integer]]
windows xs =
    let headSlice list
         | length list >= (winLength + 1) = 
             Just ((take (winLength + 1) list), tail list)
         | otherwise = Nothing
     in List.unfoldr headSlice xs

allPairSums :: [Integer] -> [Integer]
allPairSums list = do
    (i,x) <- zip [0..] list
    (j,y) <- zip [0..] list
    Monad.guard (i < j)
    return (x + y)

notSum :: [Integer] -> Maybe Integer
notSum list =
    let sums = Set.fromList $ allPairSums $ take winLength list
        value = head $ drop winLength list
     in if Set.member value sums then Nothing else Just value

solve :: Integer
solve = head $ Maybe.catMaybes $ map notSum $ windows input

main :: IO ()
main = print $ solve