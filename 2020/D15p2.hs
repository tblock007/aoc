import D15input
import Control.Monad
import Control.Monad.ST
import Data.Vector.Unboxed.Mutable as MVector
import Data.Vector as Vector

-- initVector :: [(Int, Int)] -> Vector.Vector s
initVector first = runST $ do
    result <- MVector.replicate 30 0
    -- forM_ first $ \(k, v) -> do 
    --     writeArray result k v
    return result

-- getNth :: Int -> UArray Int Int -> Int -> Int -> Int
-- getNth n memo last pos
--     | pos == n = last
--     | otherwise =
--         let updatedMemo = Map.insert last pos memo
--             diff = case Map.lookup last memo of
--                     Nothing -> 0
--                     Just i -> pos - i
--         in getNth n updatedMemo diff (pos + 1)

solve :: Int
solve = let v = initVector $ Prelude.zip input [1..] 
         in v ! 1

main :: IO ()
main = print $ solve