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

getSequence :: [Char] -> [Char]
getSequence = removeWhiteSpace . dropWhile (/= ':')
  where removeWhiteSpace = (drop 1)

countSpecialChar :: [Char] -> Int
countSpecialChar str = sum [1 | c <- seq, c == character]
  where seq = getSequence str
        character = specialChar str

isPasswordCorrect :: [Char] -> Bool
isPasswordCorrect str = count >= minCount && count <= maxCount 
  where (minCount, maxCount) = possibleRange str
        count = countSpecialChar str

problemOne :: [[Char]] -> Int
problemOne = countValidPasswords isPasswordCorrect

xor :: Bool -> Bool -> Bool
xor a b = (a || b) && not (a && b)

-- a valid password for the Toboggan Corporate Policies (see problem two description)
validPasswordTCP :: [Char] -> Bool
validPasswordTCP str = ((seq !! posOne) == character)  `xor` ((seq !! posTwo) == character)
  where (posOne, posTwo) = possibleRange str
        seq = getSequence str
        character = specialChar str

countValidPasswords :: ([Char] -> Bool) -> [[Char]] -> Int
countValidPasswords test passwords = sum [ 1 | p <- passwords, test p ]

problemTwo :: [[Char]] -> Int
problemTwo = countValidPasswords validPasswordTCP 

day2 :: Int -> IO ()
day2 problem = do
  withFile "day2/input.txt" ReadMode (\handle -> do 
    content <- hGetContents handle 
    let w = lines content
    let numberCorrectPasswords = (if problem == 1 then problemOne else problemTwo) w
    putStr (show numberCorrectPasswords)
    )
