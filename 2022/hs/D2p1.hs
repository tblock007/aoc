main :: IO ()
main = interact (writeOutput . solve . readInput)

readInput :: String -> [(Char, Char)]
readInput =  map (\s -> (s!!0, s!!2)) . lines

writeOutput :: Int -> String
writeOutput x = show x ++ "\n"

data Hand = Rock | Paper | Scissors
data Result = Win | Draw | Lose

toHand :: Char -> Hand
toHand 'A' = Rock
toHand 'B' = Paper
toHand 'C' = Scissors
toHand 'X' = Rock
toHand 'Y' = Paper
toHand 'Z' = Scissors

resolveRound :: Hand -> Hand -> Result
resolveRound Rock Rock = Draw
resolveRound Rock Paper = Win
resolveRound Rock Scissors = Lose
resolveRound Paper Rock = Lose
resolveRound Paper Paper = Draw
resolveRound Paper Scissors = Win
resolveRound Scissors Rock = Win
resolveRound Scissors Paper = Lose
resolveRound Scissors Scissors = Draw

scoreHand :: Hand -> Int
scoreHand Rock = 1
scoreHand Paper = 2
scoreHand Scissors = 3

scoreResult :: Result -> Int
scoreResult Win = 6
scoreResult Draw = 3
scoreResult Lose = 0

scoreRound :: (Char, Char) -> Int
scoreRound (o,y) = (scoreResult r) + (scoreHand your)
      where opp = toHand o
            your = toHand y
            r = resolveRound opp your

solve :: [(Char, Char)] -> Int
solve = sum . map scoreRound
