# Debugging an ISBN Validator

A walkthrough of identifying and fixing bugs in a Python ISBN validator. The program validates ISBN-10 and ISBN-13 codes by verifying their check digits using the official ISBN checksum algorithms — and this project documents the process of getting it to handle all inputs correctly without crashing.

---

## Features

- Validates both **ISBN-10** and **ISBN-13** codes
- Supports the special **`X` check digit** for ISBN-10 codes
- Bugs fixed to gracefully handle all invalid inputs with clear error messages
- Can be used interactively via the command line or called directly as a function

---

## How It Works

ISBN codes use a checksum algorithm to detect errors. This tool extracts all digits except the last one, runs them through the appropriate algorithm, and compares the computed check digit against the one provided.

- **ISBN-10:** Each of the first 9 digits is multiplied by a decreasing weight (10 down to 2), the results are summed, and the check digit is derived from `11 - (sum % 11)`. A result of 10 is represented as `X`.
- **ISBN-13:** Each of the first 12 digits is multiplied alternately by 1 and 3, the results are summed, and the check digit is derived from `10 - (sum % 10)`.

---

## Requirements

- Python 3.x
- No external libraries required

---

## Usage

### Interactive Mode

Uncomment the `main()` call at the bottom of the file, then run:

```bash
python Debug_ISBN_Validator.py
```

You will be prompted to enter the ISBN code and its length as a comma-separated value:

```
Enter ISBN and length: 1530051126,10
Valid ISBN Code.
```

### Direct Function Calls

You can also call `validate_isbn()` directly in your own code:

```python
validate_isbn('1530051126', 10)     # Valid ISBN Code.
validate_isbn('9781530051120', 13)  # Valid ISBN Code.
```

---

## Input & Output Reference

| ISBN Input | Length | Output |
|---|---|---|
| `1530051126` | `10` | `Valid ISBN Code.` |
| `9781530051120` | `13` | `Valid ISBN Code.` |
| `080442957X` | `10` | `Valid ISBN Code.` |
| `1530051125` | `10` | `Invalid ISBN Code.` |
| `9781530051120` | `10` | `ISBN-10 code should be 10 digits long.` |
| `1530051126` | `13` | `ISBN-13 code should be 13 digits long.` |
| `15-0051126` | `10` | `Invalid character was found.` |
| `1530051126` | `9` | `Length should be 10 or 13.` |
| `1530051125` | `'A'` | `Length must be a number.` |
| `1530051125` | *(omitted)* | `Enter comma-separated values.` |

---

## Bugs Fixed: Error Handling

The following bugs were identified and fixed so the program handles all error cases without crashing:

| Scenario | Message |
|---|---|
| Input is not comma-separated | `Enter comma-separated values.` |
| Length is not a number | `Length must be a number.` |
| Length is not 10 or 13 | `Length should be 10 or 13.` |
| ISBN length does not match specified length | `ISBN-10 code should be 10 digits long.` / `ISBN-13 code should be 13 digits long.` |
| ISBN contains non-numeric characters (except `X` as check digit in ISBN-10) | `Invalid character was found.` |

---

## Project Structure

```
Error_Handling/
└── Debug_ISBN_Validator.py
    ├── validate_isbn(isbn, length)       # Main validation logic
    ├── calculate_check_digit_10(digits)  # ISBN-10 checksum algorithm
    ├── calculate_check_digit_13(digits)  # ISBN-13 checksum algorithm
    └── main()                            # CLI entry point
```

---

## Example Valid ISBN Codes for Testing

**ISBN-10:**
```
1530051126,10
9971502100,10
080442957X,10
```

**ISBN-13:**
```
9781530051120,13
9781947172104,13
```
