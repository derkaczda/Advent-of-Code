module Day4 where
import System.IO
import Data.List

split :: Char -> [Char] -> [[Char]]
split _ [] = [""]
split delim (x:xs) 
  | x == delim = "" : rest 
  | otherwise = (x : head rest) : tail rest 
  where rest = split delim xs

allKeysAvailable :: [String] -> Bool
allKeysAvailable input = and [k `elem` input | k <- keys]
  where keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

isBatchValid :: String -> Bool
isBatchValid batch = allKeysAvailable keys
  where key_values = split ' ' batch
        keys = concat $ map (take 1 . split ':') key_values
        countryAvailable = "cid" `elem` keys

getUntilBatchEnd :: [String] -> String
getUntilBatchEnd [] = ""
getUntilBatchEnd (x:xs)
  | x == "" = ""
  | otherwise = x ++ " " ++ getUntilBatchEnd xs

inputToBatch :: [String] -> [String] 
inputToBatch [] = [] 
inputToBatch input 
  | length batch == 0 = inputToBatch newInput
  | otherwise = [concat batch] ++ (inputToBatch newInput) 
  where batch_before = takeWhile (/= "") input
        batch = map (++ " ") batch_before
        newInput = drop (length batch + 1) input

problemOne :: [String] -> Int
problemOne input = sum [1 | v <- valids, v] 
  where batches = inputToBatch input 
        valids = map isBatchValid batches

problemTwo :: [String] -> Int
problemTwo = undefined

data Problem = One | Two

getProblem :: Problem -> ([String] -> Int)
getProblem One = problemOne
getProblem Two = problemTwo

day4 :: Problem -> IO ()
day4 problem = do
  withFile "day4/input.txt" ReadMode (\handle -> do
    content <- hGetContents handle
    let w = lines content 
    let result = getProblem problem w
    putStr (show result)
    )
