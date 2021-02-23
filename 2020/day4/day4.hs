module Day4 where
import System.IO
import Data.List
import Data.Char

split :: Char -> [Char] -> [[Char]]
split _ [] = [""]
split delim (x:xs) 
  | x == delim = "" : rest 
  | otherwise = (x : head rest) : tail rest 
  where rest = split delim xs

byrValid :: String -> Bool
byrValid value = length value == 4 && iValue >= 1920 && iValue <= 2002
  where iValue = read value

iyrValid :: String -> Bool
iyrValid value = length value == 4 && iValue >= 2010 && iValue <= 2020
  where iValue = read value

eyrValid :: String -> Bool
eyrValid value = length value == 4 && iValue >= 2020 && iValue <= 2030
  where iValue = read value

hgtValid :: String -> Bool
hgtValid value = metricValid && valuesValid 
  where sValue = takeWhile isDigit value
        parsedValue = read sValue
        metric = drop (length sValue) value
        metricValid = metric == "cm" || metric == "in"
        valuesValid = if metric == "cm" 
                         then parsedValue >= 150 && parsedValue <= 193 
                         else parsedValue >= 59 && parsedValue <= 76

hclValid :: String -> Bool
hclValid value = hashAvailable && and list && length list == 6 
  where possibleChars = ['0'..'9'] ++ ['a'..'f']
        hashAvailable = '#' == (value !! 0)
        list = [c `elem` possibleChars | c <- (drop 1 value)]

eclValid :: String -> Bool
eclValid value = value `elem` possibleValues 
  where possibleValues = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

pidValid :: String -> Bool
pidValid value = length value == 9 

keyValid :: String -> String -> Bool
keyValid key value
  | key == "byr" = byrValid value
  | key == "iyr" = iyrValid value
  | key == "eyr" = eyrValid value
  | key == "hgt" = hgtValid value
  | key == "hcl" = hclValid value
  | key == "ecl" = eclValid value
  | key == "pid" = pidValid value
  | otherwise = True

allKeysAvailable :: [[String]] -> Bool
allKeysAvailable input = and [keyValid (k !! 0) (k !! 1) | k <- input]

isBatchValid :: String -> Bool
isBatchValid batch = allKeysAvailable keys
  where key_values = split ' ' batch
        keys = map (split ':') key_values

getUntilBatchEnd :: [String] -> String
getUntilBatchEnd [] = ""
getUntilBatchEnd (x:xs)
  | x == "" = ""
  | otherwise = x ++ " " ++ getUntilBatchEnd xs


inputToBatch' :: [String] -> [[Pair]] 
inputToBatch' [] = [] 
inputToBatch' input 
  | length batch == 0 = inputToBatch newInput
  | otherwise = [concat batch] ++ (inputToBatch newInput) 
  where batch_before = takeWhile (/= "") input
        batch = map (++ " ") batch_before
        newInput = drop (length batch + 1) input

-- gets: ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", "", "hcl:#cfa07d byr:1929"]
-- returns the first batch as a string 
extractBatchAsString :: [String] -> String
extractBatchAsString input = concat linesOfBatch 
  where linesOfBatch = takeWhile (/= "") input


-- gets: ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", "", "hcl:#cfa07d byr:1929"]
-- empty string denote a new batch
inputToBatch :: [String] -> [Batch]
inputToBatch [] = []
inputToBatch input = undefined

type Pair = (String, String)
type Batch = [Pair]
-- A Batch is [[(byr, 2020), (iyr, 2020)], [(hcl, #cfa123)]]
problemOne :: [String] -> Int
problemOne input = sum [1 | v <- valids, v] 
  where batches = inputToBatch input 
        valids = map isBatchValid batches

problemTwo :: [String] -> Int
problemTwo input = sum [1 | v <- valids, v] 
  where batches = inputToBatch input
        valids = map isBatchValid batches

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
