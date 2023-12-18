import System.Environment
import System.IO
import Data.List (intercalate)

-- Function to invert colors
invertColor :: Int -> Int
invertColor colorValue = 255 - colorValue

-- Apply invertColor to a list
invertColors :: [Int] -> [Int]
invertColors = map invertColor

main :: IO ()
main = do
    -- Read the input file name from the command line arguments
    args <- getArgs
    case args of
        [inputFileName] -> do
            -- Read the input file
            inputFile <- openFile inputFileName ReadMode
            inputContents <- hGetContents inputFile
            let numbers = map read (words inputContents) :: [Int]
                invertedColors = invertColors numbers
                resultStrings = map show invertedColors
                outputString = unwords resultStrings

            -- Write the output to haskell_output.txt
            let outputFileName = "haskell_output.txt"
            outputFile <- openFile outputFileName WriteMode
            hPutStrLn outputFile outputString

            hClose inputFile
            hClose outputFile
        _ -> putStrLn "Usage: programName inputFileName"
