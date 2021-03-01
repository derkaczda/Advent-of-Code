module Day6 where
import System.IO
import Data.List

data Problem = One | Two
type Group = [String]

-- get the puzzle input and return a list of groups 
convertToGroups :: [String] -> [Group]
convertToGroups [] = []
convertToGroups input = group : convertToGroups newInput 
  where group = takeWhile criterion input 
        newInput = drop (length group + 1) input
        criterion = (/= "")

removeDuplicateAnswers :: String -> String -> String
removeDuplicateAnswers [] acc = acc
removeDuplicateAnswers (x:xs) acc
  | x `elem` acc = removeDuplicateAnswers xs acc
  | otherwise =  removeDuplicateAnswers xs (x : acc)

answersOfGroup :: Group -> String
answersOfGroup group = removeDuplicateAnswers (concat group) "" 

countGroup :: Group -> Int 
countGroup group = length $ answersOfGroup group

-- Get the lines of our input with blank lines 
-- as separators
problemOne :: [String] -> Int
problemOne input = sum $ map countGroup groups
  where groups = convertToGroups input

problemTwo :: [String] -> Int
problemTwo = undefined

getProblem :: Problem -> ([String] -> Int)
getProblem One = problemOne
getProblem Two = problemTwo

day6 :: Problem -> IO ()
day6 problem = do 
  withFile "day6/input.txt" ReadMode (\handle -> do 
    content <- hGetContents handle
    let w = lines content
    let result = getProblem problem w 
    putStr (show result)
    )
