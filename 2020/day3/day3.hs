module Day3 where
import System.IO

gridWidth :: [[Char]] -> Int
gridWidth grid = length (grid !! 0)

gridHeight :: [[Char]] -> Int
gridHeight = length

gridValue :: [[Char]] -> Int -> Int -> Char
gridValue grid x y = row !! x 
  where row = grid !! y 

isTree :: [[Char]] -> Int -> Int -> Bool
isTree grid x y = (gridValue grid x y) == '#' 

wrap :: Int -> Int -> Int
wrap max x = if x >= max then (x `mod` max) else x

countTrees :: [[Char]] -> Int -> Int -> (Int, Int)-> Int
countTrees grid x y (stepx, stepy) 
  | y >= gridHeight grid = 0
  | isTree grid wrappedX y = 1 + countTrees grid (wrappedX+stepx) (y+stepy) (stepx, stepy) 
  | otherwise = 0 + countTrees grid (wrappedX+stepx) (y+stepy) (stepx, stepy)
  where wrappedX = wrap (gridWidth grid) x

problemOne :: [[Char]] -> Int
problemOne grid = countTrees grid 0 0 (3, 1)

problemTwo :: [[Char]] -> Int
problemTwo grid = product [ countTrees grid 0 0 step | step <- steps ]
  where steps = [(1,1), (3,1), (5,1), (7,1), (1,2)]

getProblem :: Int -> ([[Char]] -> Int)
getProblem x = if x == 1 then problemOne else problemTwo

day3 :: Int -> IO ()
day3 problem = do 
  withFile "day3/input.txt" ReadMode (\handle -> do 
    content <- hGetContents handle
    let w = lines content 
    let numberOfTrees = getProblem problem w
    putStr (show numberOfTrees)
    )
