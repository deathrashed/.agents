---
name: shell-scripting
description: Create, debug, and optimize shell scripts (bash, zsh, sh) for automation, system administration, file processing, and CLI workflows. Use when writing shell scripts, automating tasks, processing files, system administration, or working with command-line tools.
---

# Shell Scripting Skill

This skill provides expertise in creating, debugging, and optimizing shell scripts for automation, system administration, and CLI workflows.

## Overview

Shell scripting enables automation of:
- File operations and batch processing
- System administration tasks
- Command-line tool orchestration
- Text processing and data manipulation
- Workflow automation
- CI/CD pipeline scripts

## Shell Types

### Bash (Bourne Again Shell)
- Most common on Linux and macOS
- Default on many systems
- Extensive features and compatibility

### Zsh (Z Shell)
- Default on macOS (since Catalina)
- Enhanced features over bash
- Better tab completion and globbing

### Sh (POSIX Shell)
- Most portable
- Minimal features
- Best for maximum compatibility

## Basic Script Structure

```bash
#!/bin/bash
# Shebang line - specifies interpreter

# Script metadata
# Author: Your Name
# Description: What the script does
# Usage: ./script.sh [options]

# Set script options
set -e          # Exit on error
set -u          # Exit on undefined variable
set -o pipefail # Exit on pipe failure

# Variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_NAME="$(basename "$0")"

# Functions
function usage() {
    echo "Usage: $SCRIPT_NAME [options]"
}

# Main script logic
main() {
    echo "Script execution starts here"
}

# Run main function
main "$@"
```

## Variables and Data Types

### Variable Assignment

```bash
# Basic assignment
NAME="value"
NUMBER=42

# Command substitution
CURRENT_DIR=$(pwd)
DATE=$(date +%Y-%m-%d)
FILE_COUNT=$(ls -1 | wc -l)

# Read-only variables
readonly CONSTANT="immutable value"

# Export for subprocesses
export ENV_VAR="value"
```

### Arrays

```bash
# Declare array
declare -a ARRAY=("item1" "item2" "item3")

# Access elements
echo "${ARRAY[0]}"      # First element
echo "${ARRAY[@]}"      # All elements
echo "${#ARRAY[@]}"     # Array length

# Append
ARRAY+=("item4")

# Iterate
for item in "${ARRAY[@]}"; do
    echo "$item"
done
```

### Associative Arrays (Bash 4+)

```bash
declare -A DICT
DICT["key1"]="value1"
DICT["key2"]="value2"

echo "${DICT[key1]}"
```

## Control Flow

### Conditionals

```bash
# If statement
if [ condition ]; then
    commands
elif [ condition ]; then
    commands
else
    commands
fi

# Test operators
[ -f file ]        # File exists and is regular
[ -d dir ]         # Directory exists
[ -r file ]        # File is readable
[ -w file ]        # File is writable
[ -x file ]        # File is executable
[ -z string ]      # String is empty
[ -n string ]      # String is not empty
[ str1 = str2 ]    # Strings equal
[ str1 != str2 ]   # Strings not equal
[ num1 -eq num2 ]  # Numbers equal
[ num1 -gt num2 ]  # Number greater than
```

### Loops

```bash
# For loop
for i in {1..10}; do
    echo "$i"
done

# For loop with array
for file in *.txt; do
    echo "Processing $file"
done

# While loop
while [ condition ]; do
    commands
done

# Until loop
until [ condition ]; do
    commands
done

# C-style for loop
for ((i=0; i<10; i++)); do
    echo "$i"
done
```

## Functions

```bash
# Function definition
function my_function() {
    local var1="$1"  # First argument
    local var2="$2"  # Second argument
    
    # Function body
    echo "Processing $var1 and $var2"
    return 0
}

# Call function
my_function "arg1" "arg2"

# Return value
if my_function "arg1" "arg2"; then
    echo "Function succeeded"
fi
```

## Input/Output

### Reading Input

```bash
# Read from stdin
read -p "Enter name: " name
read -s -p "Password: " password  # Hidden input

# Read from file
while IFS= read -r line; do
    echo "$line"
done < file.txt

# Read arguments
SCRIPT_NAME="$0"
FIRST_ARG="$1"
ALL_ARGS="$@"
ARG_COUNT="$#"
```

### Output

```bash
# Print
echo "Text"
echo -e "Text with\nnewline"  # Enable escape sequences
echo -n "No newline"          # No trailing newline

# Printf (formatted)
printf "Name: %s, Age: %d\n" "$name" "$age"

# Redirect
command > file.txt        # Overwrite
command >> file.txt       # Append
command 2> error.log      # Stderr
command &> all.log        # Both stdout and stderr
```

## Text Processing

### sed (Stream Editor)

```bash
# Replace text
sed 's/old/new/g' file.txt

# Delete lines
sed '/pattern/d' file.txt

# Print specific lines
sed -n '10,20p' file.txt
```

### awk

```bash
# Print columns
awk '{print $1, $3}' file.txt

# Conditional processing
awk '$3 > 100 {print $1, $3}' file.txt

# Field separator
awk -F',' '{print $1}' file.csv
```

### grep

```bash
# Search
grep "pattern" file.txt
grep -r "pattern" directory/  # Recursive
grep -i "pattern" file.txt     # Case insensitive
grep -v "pattern" file.txt     # Invert match
grep -E "regex" file.txt       # Extended regex
```

## File Operations

### File Tests

```bash
[ -f file ]    # Regular file
[ -d dir ]     # Directory
[ -L link ]    # Symbolic link
[ -r file ]    # Readable
[ -w file ]    # Writable
[ -x file ]    # Executable
[ -s file ]    # Non-empty
[ -e path ]    # Exists
```

### File Manipulation

```bash
# Copy
cp source.txt dest.txt
cp -r source_dir/ dest_dir/  # Recursive

# Move/Rename
mv old.txt new.txt

# Remove
rm file.txt
rm -rf directory/  # Recursive, force

# Create
touch file.txt
mkdir -p path/to/dir  # Create parent dirs

# Read
cat file.txt
head -n 10 file.txt
tail -n 10 file.txt
less file.txt
```

## Process Management

### Running Commands

```bash
# Background process
command &

# Wait for background
wait $PID

# Run in subshell
(cd /tmp && ls)

# Command substitution
RESULT=$(command)
RESULT=`command`  # Older syntax
```

### Process Control

```bash
# Get PID
PID=$$

# Kill process
kill $PID
kill -9 $PID      # Force kill
killall process_name

# Check if running
if pgrep -f "pattern"; then
    echo "Process is running"
fi
```

## Error Handling

```bash
# Exit on error
set -e

# Exit on undefined variable
set -u

# Exit on pipe failure
set -o pipefail

# Trap errors
trap 'echo "Error on line $LINENO"' ERR

# Cleanup on exit
trap 'rm -f /tmp/tempfile' EXIT

# Check command success
if ! command; then
    echo "Command failed"
    exit 1
fi
```

## Best Practices

1. **Always use shebang**: `#!/bin/bash` or `#!/usr/bin/env bash`
2. **Set error handling**: `set -euo pipefail`
3. **Quote variables**: `"$var"` not `$var`
4. **Use local variables**: `local var="value"` in functions
5. **Validate input**: Check arguments and file existence
6. **Use meaningful names**: Clear variable and function names
7. **Add comments**: Document complex logic
8. **Handle errors**: Check return codes and handle failures
9. **Use functions**: Break code into reusable functions
10. **Test incrementally**: Test as you build

## Common Patterns

### Script Template

```bash
#!/usr/bin/env bash
set -euo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "$0")"

function usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS]

Description of what the script does.

OPTIONS:
    -h, --help      Show this help message
    -v, --verbose   Enable verbose output
    -f, --file FILE Specify input file

EXAMPLES:
    $SCRIPT_NAME -f input.txt
    $SCRIPT_NAME --verbose

EOF
}

function log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" >&2
}

function main() {
    local verbose=false
    local input_file=""
    
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -h|--help)
                usage
                exit 0
                ;;
            -v|--verbose)
                verbose=true
                shift
                ;;
            -f|--file)
                input_file="$2"
                shift 2
                ;;
            *)
                echo "Unknown option: $1" >&2
                usage
                exit 1
                ;;
        esac
    done
    
    [[ -z "$input_file" ]] && { echo "Error: Input file required" >&2; exit 1; }
    [[ ! -f "$input_file" ]] && { echo "Error: File not found: $input_file" >&2; exit 1; }
    
    log "Processing $input_file"
    # Main logic here
}

main "$@"
```

### Logging Function

```bash
function log() {
    local level="$1"
    shift
    local message="$*"
    local timestamp=$(date +'%Y-%m-%d %H:%M:%S')
    
    case "$level" in
        INFO)
            echo "[$timestamp] [INFO] $message" >&2
            ;;
        WARN)
            echo "[$timestamp] [WARN] $message" >&2
            ;;
        ERROR)
            echo "[$timestamp] [ERROR] $message" >&2
            ;;
    esac
}

log INFO "Script started"
log WARN "This is a warning"
log ERROR "This is an error"
```

## Resources

- [Bash Guide](https://mywiki.wooledge.org/BashGuide)
- [Advanced Bash Scripting Guide](https://tldp.org/LDP/abs/html/)
- [ShellCheck](https://www.shellcheck.net/) - Shell script linter
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/)
