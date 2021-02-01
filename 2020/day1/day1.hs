module Day1 where
import System.IO    

dayOne :: [Int] -> Int
dayOne xs = head [ x * y | x <- xs, y <- xs, x + y == 2020 ]

dayOnePartTwo :: [Int] -> Int
dayOnePartTwo xs = head [ x * y * z | x <- xs, y <-xs , z <- xs, x+y+z == 2020 ]

main = do
    withFile "day1/input.txt" ReadMode (\handle -> do
        content <- hGetContents handle
        let result = dayOnePartTwo (map read (words content))
        putStr (show result)
        )
        
