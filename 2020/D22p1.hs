import D22input
import Data.Foldable (toList)
import qualified Data.List as List
import qualified Data.Maybe as Maybe
import Data.Sequence ((|>), ViewL((:<)), ViewR((:>)))
import qualified Data.Sequence as Seq

type GameState = (Seq.Seq Int, Seq.Seq Int)

playRound :: GameState -> GameState
playRound (d1, d2) =
    let h1 = Seq.viewl d1
        h2 = Seq.viewl d2
     in case (h1, h2) of
         (Seq.EmptyL, _) -> (d1, d2)
         (_, Seq.EmptyL) -> (d1, d2)
         (c1 :< c1s, c2 :< c2s) ->
             if c1 < c2
             then (c1s, c2s |> c2 |> c1)
             else (c1s |> c1 |> c2, c2s)

steadyState :: Eq a => (a -> a) -> a -> a
steadyState f x
    | f x == x = x
    | otherwise = steadyState f (f x)

winningScore :: Seq.Seq Int -> Int
winningScore s = let l = Seq.length s
                  in sum $ zipWith (*) [l,l-1..1] (toList s)

solve :: Int
solve = let initialState = (Seq.fromList p1, Seq.fromList p2)
            (end1, end2) = steadyState playRound initialState
         in max (winningScore end1) (winningScore end2)

main :: IO ()
main = print $ solve
