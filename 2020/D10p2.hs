import D10input
import qualified Data.Vector as Vector
import qualified Data.Set as Set

countWays :: Set.Set Int -> Int -> Int
countWays s n = 
    let countForIMinus2 i
          | i == 0 || i == 1 = 0
          | i == 2 = 1
          | Set.member (i-2) s = 
                let w1 = memo Vector.! (i - 1)
                    w2 = memo Vector.! (i - 2)
                    w3 = memo Vector.! (i - 3)
                 in w1 + w2 + w3
          | otherwise = 0        
        memo = Vector.generate (n+3) countForIMinus2
     in memo Vector.! (n + 2)

solve :: Int
solve =
    let end = (maximum input) + 3
        values = Set.fromList (0:end:input)
     in countWays values end

main :: IO ()
main = print $ solve