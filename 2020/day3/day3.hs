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

countTrees :: [[Char]] -> Int -> Int -> Int
countTrees grid x y 
  | y >= gridHeight grid = 0
  | isTree grid wrappedX y = 1 + countTrees grid (wrappedX+3) (y+1) 
  | otherwise = 0 + countTrees grid (wrappedX+3) (y+1)
  where wrappedX = wrap (gridWidth grid) x

problemOne :: [[Char]] -> Int
problemOne grid = countTrees grid 0 0

problemTwo :: [[Char]] -> Int
problemTwo = undefined

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
