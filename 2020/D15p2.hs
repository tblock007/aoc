import D15input
import Control.Monad
import Control.Monad.ST
import Data.List as List
import Data.Vector.Unboxed.Mutable as MVector

initVector :: Int -> [(Int, Int)] -> ST s (MVector.MVector s Int)
initVector n init = do
    result <- MVector.replicate 30000000 (-1)
    forM_ init $ \(k, v) -> do 
        write result k v
    return result

run :: Int -> (MVector.MVector s Int) -> Int -> Int -> ST s Int
run n v last pos
    | pos == n = pure last
    | otherwise = do
        prevPos <- MVector.read v last
        diff <- pure $ if prevPos == (-1) then 0 else (pos - prevPos)
        MVector.write v last pos
        run n v diff (pos + 1)

getNth :: Int -> [(Int, Int)] -> Int -> Int -> Int
getNth n init last pos = 
    runST $ do
        v <- initVector n init
        run n v last pos

solve :: Int 
solve = getNth 30000000 (List.zip input [1..]) 0 (List.length input + 1)

main :: IO ()
main = print $ solve