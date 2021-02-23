module Day4 where
import System.IO
import Data.List
import Data.Char


type Pair = (String, String)
type Batch = [Pair]

possibleKeys :: [String]
possibleKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

split :: Char -> [Char] -> [[Char]]
split _ [] = [""]
split delim (x:xs) 
  | x == delim = "" : rest 
  | otherwise = (x : head rest) : tail rest 
  where rest = split delim xs

allKeysAvailable :: Batch -> Bool
allKeysAvailable batch = and [k `elem` keys | k <- possibleKeys]
  where keys = fst $ unzip batch

-- gets batch in string representation: "ecl:gry pid:860033327 eyr:2020 hcl:#fffffdbyr:1937 iyr:2017 cid:147 hgt:183cm" 
-- returns a parsed Batch
stringToBatch :: String -> Batch
stringToBatch batch = [(x !! 0, x !! 1) | x <- listOfKeyValues] 
  where listOfKeyValues = map (split ':') $ split ' ' batch

-- gets: ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", "", "hcl:#cfa07d byr:1929"]
-- returns the first batch as a string 
extractBatchAsString :: [String] -> String
extractBatchAsString input = concat withWhiteSpaces 
  where linesOfBatch = takeWhile (/= "") input
        addWhiteSpaces [x] = x : []
        addWhiteSpaces (x:xs) = (x ++ " ") : addWhiteSpaces xs
        withWhiteSpaces = addWhiteSpaces linesOfBatch

removeBatchFromInput :: [String] -> [String]
removeBatchFromInput = drop 1 . dropWhile (/= "")

-- gets: ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", "", "hcl:#cfa07d byr:1929"]
-- empty string denote a new batch
inputToBatches :: [String] -> [Batch]
inputToBatches [] = []
inputToBatches input = batch : inputToBatches newInput 
  where batchAsString = extractBatchAsString input
        newInput = removeBatchFromInput input
        batch = stringToBatch batchAsString

-- A Batch is [[(byr, 2020), (iyr, 2020)], [(hcl, #cfa123)]]
problemOne :: [String] -> Int
problemOne input = length validBatches
  where batches = inputToBatches input
        validBatches = filter allKeysAvailable batches

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
