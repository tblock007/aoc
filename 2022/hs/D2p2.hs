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

toResult :: Char -> Result
toResult 'X' = Lose
toResult 'Y' = Draw
toResult 'Z' = Win

getHand :: Hand -> Result -> Hand
getHand Rock Win = Paper
getHand Rock Draw = Rock
getHand Rock Lose = Scissors
getHand Paper Win = Scissors
getHand Paper Draw = Paper
getHand Paper Lose = Rock
getHand Scissors Win = Rock 
getHand Scissors Draw = Scissors
getHand Scissors Lose = Paper

scoreHand :: Hand -> Int
scoreHand Rock = 1
scoreHand Paper = 2
scoreHand Scissors = 3

scoreResult :: Result -> Int
scoreResult Win = 6
scoreResult Draw = 3
scoreResult Lose = 0

scoreRound :: (Char, Char) -> Int
scoreRound (o,r) = (scoreResult res) + (scoreHand your)
      where opp = toHand o
            res = toResult r
            your = getHand opp res

solve :: [(Char, Char)] -> Int
solve = sum . map scoreRound
