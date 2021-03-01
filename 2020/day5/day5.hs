module Day5 where
import System.IO
import Data.List

data Problem = One | Two

bpartition :: (Char, Char) -> (Int, Int) -> String -> Int
bpartition (minChar, maxChar) (lowerBound, upperBound) (x:xs)
  | xs == [] = if minChar == x then lowerBound else upperBound
  | x == minChar = bpartition (minChar, maxChar) (lowerBound, upperBound - modifier) xs
  | otherwise = bpartition (minChar, maxChar) (lowerBound + modifier, upperBound) xs
  where modifier = ((upperBound - lowerBound) `div` 2) + 1


-- Get a single partition FFBBFFBFBFRLRLR
computeSeatID :: String -> Int
computeSeatID part = rowNumber * 8 + columnNumber
  where rowPartition = takeWhile rowCriterion part
        columnPartition = dropWhile rowCriterion part
        rowCriterion = (\x -> x /= 'L' && x /= 'R')
        rowNumber = bpartition ('F', 'B') (0, 127) rowPartition
        columnNumber = bpartition ('L', 'R') (0, 7) columnPartition

getAllMissingIds :: [Int] -> Int -> [Int] -> [Int]
getAllMissingIds [] last acc = acc
getAllMissingIds (x:xs) last acc
  | last == x = getAllMissingIds xs (last + 1) acc
  | otherwise = getAllMissingIds (x:xs) (last + 1) (last : acc)

-- get list of binary partitions
-- ["FFFBBBBRLL", "FFBFBFBFRL", ...]
problemOne :: [String] -> Int
problemOne input = maximum $ map computeSeatID input 

problemTwo :: [String] -> Int
problemTwo input = head allMissings 
  where allIds = sort $ map computeSeatID input
        allMissings = getAllMissingIds allIds (head allIds) []

getProblem :: Problem -> ([String] -> Int)
getProblem One = problemOne
getProblem Two = problemTwo

day5 :: Problem -> IO ()
day5 problem = do 
  withFile "day5/input.txt" ReadMode (\handle -> do 
    content <- hGetContents handle 
    let w = lines content
    let result = getProblem problem w
    putStr (show result)
    )
