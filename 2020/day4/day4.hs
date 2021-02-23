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
keyValid key 
  | key == "byr" = byrValid
  | key == "iyr" = iyrValid
  | key == "eyr" = eyrValid
  | key == "hgt" = hgtValid
  | key == "hcl" = hclValid
  | key == "ecl" = eclValid
  | key == "pid" = pidValid
  | otherwise = const True

allKeysAvailable :: Batch -> Bool
allKeysAvailable batch = and [k `elem` keys | k <- possibleKeys]
  where keys = fst $ unzip batch

allKeysValid :: Batch -> Bool
allKeysValid batch = and [keyValid k v | (k, v) <- batch]

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
problemTwo input = length batchesWithValidKeys
  where batches = inputToBatches input 
        batchesWithAllKeys = filter allKeysAvailable batches
        batchesWithValidKeys = filter allKeysValid batchesWithAllKeys

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
