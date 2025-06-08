# Set root project folder name
$projectRoot = "./"

# List of main Python files
$mainFiles = @(
    "common_pins.py",
    "generate_pins.py",
    "valid_date_checker.py",
    "evaluator.py",
    "main.py",
    "requirements.txt",
    "README.md"
)

# Test directory and test file
$testDir = "tests"
$testFile = "test_cases.py"

# Create project root folder
New-Item -ItemType Directory -Path $projectRoot -Force | Out-Null

# Create Python files inside project root
foreach ($file in $mainFiles) {
    New-Item -ItemType File -Path "$projectRoot\$file" -Force | Out-Null
}

# Create tests folder and test file
New-Item -ItemType Directory -Path "$projectRoot\$testDir" -Force | Out-Null
New-Item -ItemType File -Path "$projectRoot\$testDir\$testFile" -Force | Out-Null

Write-Host "mpin_checker Project structure created at: $projectRoot"
