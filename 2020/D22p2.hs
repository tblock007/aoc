import D22input
import Data.Foldable (toList)
import Data.HashSet as Set
import qualified Data.List as List
import qualified Data.Maybe as Maybe
import Data.Sequence ((|>), ViewL((:<)), ViewR((:>)))
import qualified Data.Sequence as Seq

data Player = P1 | P2 deriving (Show, Eq)

type GameState = (Seq.Seq Int, Seq.Seq Int)
type Memo = Set.HashSet ([Int], [Int])

seen :: GameState -> Memo -> Bool
seen (d1, d2) memo = 
    Set.member (Data.Foldable.toList d1, Data.Foldable.toList d2) memo

memoize :: GameState -> Memo -> Memo
memoize (d1, d2) memo = 
    Set.insert (Data.Foldable.toList d1, Data.Foldable.toList d2) memo

playRound :: GameState -> GameState
playRound (d1, d2) =
    let h1 = Seq.viewl d1
        h2 = Seq.viewl d2
     in case (h1, h2) of
         (Seq.EmptyL, _) -> (d1, d2)
         (_, Seq.EmptyL) -> (d1, d2)
         (c1 :< c1s, c2 :< c2s) ->
             if (c1 <= Seq.length c1s) && (c2 <= Seq.length c2s)
             then if (winnerOf (Seq.take c1 c1s, Seq.take c2 c2s) Set.empty) == P2
                  then (c1s, c2s |> c2 |> c1)
                  else (c1s |> c1 |> c2, c2s)
             else if (c1 < c2)
                  then (c1s, c2s |> c2 |> c1)
                  else (c1s |> c1 |> c2, c2s)

winnerOf :: GameState -> Memo -> Player
winnerOf s@(d1, d2) memo
    | seen s memo = P1
    | Seq.length d1 == 0 = P2
    | Seq.length d2 == 0 = P1
    | otherwise = winnerOf (playRound s) (memoize s memo)

steadyState :: Eq a => (a -> a) -> a -> a
steadyState f x
    | f x == x = x
    | otherwise = steadyState f (f x)

winningScore :: Seq.Seq Int -> Int
winningScore s = let l = Seq.length s
                  in sum $ zipWith (*) [l,l-1..1] (Data.Foldable.toList s)

solve :: Int
solve = let initialState = (Seq.fromList p1, Seq.fromList p2)
            (end1, end2) = steadyState playRound initialState
         in max (winningScore end1) (winningScore end2)

main :: IO ()
main = print $ solve
