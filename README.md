# MPIN Checker Project

## Project Description

The **MPIN Checker** is a Python-based utility designed to validate and evaluate MPINs along with associated date inputs. The system allows users to enter MPINs and related date information, validates the formats, checks for common insecure MPINs, and assesses the strength of the MPIN provided. This project aims to ensure security compliance by preventing weak or commonly used MPINs and verifying valid date formats linked with the MPINs.

This project is modular, organized into multiple Python files each responsible for a specific part of the overall workflow — from generating MPINs, checking date validity, to evaluating MPIN strength.

---

## Modules Description

### 1. `common_pins.py`

This module contains a collection of commonly used or insecure MPINs. It provides functions to check whether a given MPIN is part of this list, thereby identifying potentially weak or predictable PINs. This helps in early rejection of insecure MPINs and prompts users to choose stronger ones.

Key Features:

- Maintains a list or set of known weak/common MPINs.
- Provides a fast lookup method to verify MPIN security status.

---

### 2. `generate_pins.py`

This module is responsible for generating valid MPINs based on certain criteria or rules. It may also provide utility functions to manipulate or create candidate MPINs for testing or evaluation.

Key Features:

- Functions to generate random or rule-based MPINs.
- May include formatting or normalization of PINs before validation.
- Used internally to simulate or validate MPIN input scenarios.

---

### 3. `valid_date_checker.py`

This module ensures that the date inputs associated with MPINs are valid. It parses input date strings, verifies correct formatting (e.g., `DD/MM/YYYY` or 'YYYY/MM/DD' ). This helps in rejecting invalid or malformed date entries during user input validation.

Key Features:

- Date parsing and format validation.
- Logical validation of day, month, and year values.
- Support for multiple date formats if necessary.

---

### 4. `evaluator.py`

The evaluator module is the core logic that assesses the MPIN strength and the overall validity of user inputs. It uses other modules (like checking against common pins and validating dates) and implements rules to categorize the security level of an MPIN.

Key Features:

- Integrates with `common_pins.py` and `valid_date_checker.py`.
- Provides strength ratings (e.g., weak, medium, strong) to MPINs.

---

### 5. `main.py`

The main entry point for the MPIN Checker project. This script orchestrates the input/output interactions with the user, calls necessary functions from the other modules, and controls the flow of the program.

Key Features:

- Handles user input prompts for MPIN and date values.
- Uses `evaluator.find_reasons()` to validate and rate the MPIN.
- Displays results and prompts for continuation or exit.
- Contains the main program loop.
- Logs every execution

---

## Usage

1. Run the `main.py` file to start the MPIN Checker.
2. Follow the input prompts to enter your MPIN and associated dates.
3. The system will validate your inputs, check MPIN strength, and display appropriate messages.
4. Optionally, use the modules individually for custom validation or generation as needed.

---

## Dependencies

- Python 3.x (tested on Python 3.13)
- Colorama
- Openpyxl

---

## Testing

There is a tester.py inside ./tests that runs automatically and tests 20 test cases.
It uses the main function for running tests and logs the outputs
*Ignore the terminal output when testing. You can verify the test results using the latest logs inside .tests/logs.xlsx*
