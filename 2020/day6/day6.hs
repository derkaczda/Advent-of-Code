module Day6 where
import System.IO
import Data.List

data Problem = One | Two
type Group = [String]

blablkjdfklj


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

sameAnsweresAsFirstMember :: String -> Group -> String -> String
sameAnsweresAsFirstMember [] _ acc = acc
sameAnsweresAsFirstMember (x:xs) rest acc
  | allAgree = sameAnsweresAsFirstMember xs rest (x : acc)
  | otherwise = sameAnsweresAsFirstMember xs rest acc
  where allAgree = and [x `elem` y | y <- rest]

everyoneAnsweredYes :: Group -> String 
everyoneAnsweredYes group = sameAnsweresAsFirstMember (head group) (tail group) "" 

countGroup :: (Group -> String) -> Group -> Int 
countGroup f group = length $ f group

-- Get the lines of our input with blank lines 
-- as separators
problemOne :: [String] -> Int
problemOne input = sum $ map (countGroup answersOfGroup) groups
  where groups = convertToGroups input

problemTwo :: [String] -> Int
problemTwo input = sum $ map (countGroup everyoneAnsweredYes) groups
  where groups = convertToGroups input

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
