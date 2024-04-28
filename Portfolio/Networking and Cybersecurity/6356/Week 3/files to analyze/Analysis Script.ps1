# Specify the path to the directory containing PNG files
$directoryPath = "C:\Users\BlueBravo\OneDrive - West Texas A and M University\Masters\SP2024\CIDM 6356 DF\Week 3\files to analyze"

# Specify the path for the output CSV file
$outputCsvPath = "C:\Users\BlueBravo\OneDrive - West Texas A and M University\Masters\SP2024\CIDM 6356 DF\Week 3\files to analyze\output.csv"

# Get all PNG files in the specified directory
$pngFiles = Get-ChildItem -Path $directoryPath -Filter *.png

# Initialize an array to store hash results
$hashResults = @()

# Loop through each PNG file and calculate the hash
foreach ($file in $pngFiles) {
    $hash = Get-FileHash -Path $file.FullName
    $hashResults += [PSCustomObject]@{
        FileName = $file.Name
        Hash     = $hash.Hash
    }
}

# Output the results to a CSV file
$hashResults | Export-Csv -Path $outputCsvPath -NoTypeInformation

Write-Host "Hash calculation completed. Results saved to: $outputCsvPath"
