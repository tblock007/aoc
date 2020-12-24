import D18input
import Data.Char

data Expr = Digit Char | Add Expr Expr | Mult Expr Expr deriving Show

eval :: Expr -> Int
eval (Digit c) = digitToInt c
eval (Add e1 e2) = (eval e1) + (eval e2)
eval (Mult e1 e2) = (eval e1) * (eval e2)

preprocess :: String -> String
preprocess = map flipBrackets . reverse . filter (/=' ')
    where flipBrackets c = if c == '('
                           then ')'
                           else if c == ')'
                                then '('
                                else c

findMatching :: String -> Int -> String
findMatching ('(':cs) rem = '(':(findMatching cs (rem + 1))
findMatching (')':cs) rem = if rem == 1 
                            then "" 
                            else ')':(findMatching cs (rem - 1))
findMatching (c:cs) rem = c:(findMatching cs rem)

headTerm :: String -> String
headTerm (c:cs)
    | c == '(' = findMatching cs 1
    | otherwise = [c]

stripTerm :: String -> (String, String)
stripTerm s = let t = headTerm s
                  l = if head s == '(' then (length t) + 2 else 1
               in (t, drop l s)

parse :: String -> Expr
parse (c:[]) = Digit c
parse s = case stripTerm s of
    (first, "") -> parse first
    (first, rest) -> let op = head rest
                         second = tail rest
                      in case op of
                          '+' -> Add (parse first) (parse second)
                          '*' -> Mult (parse first) (parse second)

solve :: Int
solve = sum $ map (eval . parse . preprocess) input

main :: IO ()
main = print $ solve