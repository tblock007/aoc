module D17input where

input :: [String]
input = ["######.#",
	"#.###.#.",
	"###.....",
	"#.####..",
	"##.#.###",
	".######.",
	"###.####",
	"######.#"]

pdim :: Int
pdim = 6

idim :: Int
idim = length input

dim :: Int
dim = pdim + idim + pdim