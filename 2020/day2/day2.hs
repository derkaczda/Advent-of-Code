module Day2 where
import System.IO

-- structure is : 2-9 c : ccccccccc
-- so we need to find the number between '-' and ' '
possibleRange :: [Char] -> (Int, Int)
possibleRange str = (read minNumber, read maxNumber) 
  where minNumber = takeWhile (/= '-') str
        maxNumber = ((takeWhile (/= ' ') . drop 1 . dropWhile (/= '-'))  str)

-- get the character to prove the password on
specialChar :: [Char] -> Char
specialChar str = ((head . drop 1 . dropWhile (/= ' ')) str)

countSpecialChar :: [Char] -> Int
countSpecialChar str = sum [1 | c <- sequence, c == character]
  where sequence = (dropWhile (/= ':') str)
        character = specialChar str

isPasswordCorrect :: [Char] -> Bool
isPasswordCorrect str = count >= minCount && count <= maxCount 
  where (minCount, maxCount) = possibleRange str
        count = countSpecialChar str

day2 :: [[Char]] -> Int
day2 passwords = sum [ 1 | p <- passwords, isPasswordCorrect p ]

main = do
  withFile "day2/input.txt" ReadMode (\handle -> do 
    content <- hGetContents handle 
    let w = lines content
    let numberCorrectPasswords = day2 w
    putStr (show numberCorrectPasswords)
    )
