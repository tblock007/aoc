import D10input
import Data.List

countIf :: (a -> Bool) -> [a] -> Int
countIf f xs = length $ filter f xs

diffHist :: [Int] -> (Int, Int, Int)
diffHist list =
    let sorted = sort list
        diffs = map (\(x,y) -> y - x) $ zip sorted (tail sorted)
        ones = countIf (==1) diffs
        twos = countIf (==2) diffs
        threes = countIf (==3) diffs
     in (ones, twos, threes)

solve :: Int
solve =
    let (ones, twos, threes) = diffHist (0:input)
     in ones * (threes + 1)

main :: IO ()
main = print $ solve