import D10input
import qualified Data.Vector as Vector
import qualified Data.Set as Set

countWays :: Set.Set Int -> Int -> Int
countWays s n = 
    let countAux i
          | i == 0 = 1
          | Set.member i s = 
                let w1 = memo Vector.! (i - 1)
                    w2 = if i > 1 then memo Vector.! (i - 2) else 0
                    w3 = if i > 2 then memo Vector.! (i - 3) else 0
                 in w1 + w2 + w3
          | otherwise = 0        
        memo = Vector.generate (n+1) countAux
     in memo Vector.! n

solve :: Int
solve =
    let end = (maximum input) + 3
        values = Set.fromList (0:end:input)
     in countWays values end

main :: IO ()
main = print $ solve