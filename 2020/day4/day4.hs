module Day4 where
import System.IO
import Data.List

-- some constants
c_birthyear :: [Char]
c_birthyear = "byr"
c_issueyear :: [Char]
c_issueyear = "iyr"
c_expirationyear :: [Char]
c_expirationyear = "eyr"
c_height :: [Char]
c_height = "hgt"
c_haircolor :: [Char]
c_haircolor = "hcl"
c_eyecolor :: [Char]
c_eyecolor = "ecl"
c_passportid :: [Char]
c_passportid = "pid"
c_countryid :: [Char]
c_countryid = "cid"

type Passport = ([Char], Int, Int, [Char], Int, Int, Int, Int)
birthYear :: Passport -> Int
birthYear (_, _, _, _, x, _, _, _) = x
issueYear :: Passport -> Int
issueYear (_, _, _, _, _, x, _, _) = x
expirationYear :: Passport -> Int
expirationYear (_, _, x, _, _, _, _, _) = x
height :: Passport -> Int
height (_, _, _, _, _, _, _, x) = x
hairColor :: Passport -> [Char]
hairColor (_, _, _, x, _, _, _, _) = x
eyeColor :: Passport -> [Char]
eyeColor (x, _, _, _, _, _, _, _) = x
passportId :: Passport -> Int
passportId (_, x, _, _, _, _, _, _) = x
countryId :: Passport -> Int
countryId (_, _, _, _, _, _, x, _) = x 

split :: Char -> [Char] -> [[Char]]
split _ [] = [""]
split delim (x:xs) 
  | x == delim = "" : rest 
  | otherwise = (x : head rest) : tail rest 
  where rest = split delim xs

batchToPassport :: String -> [[String]] 
batchToPassport batch = keys 
  where keys = map (split ':') (words batch)

inputToBatch :: [String] -> [[String]] 
inputToBatch [] = [] 
inputToBatch input 
  | length batch == 0 = inputToBatch newInput
  | otherwise = [batch] ++ (inputToBatch newInput) 
  where batch = takeWhile (/= "") input
        newInput = drop (length batch + 1) input


problemOne :: [String] -> Int
problemOne = undefined

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
    putStr (show w)
    )
