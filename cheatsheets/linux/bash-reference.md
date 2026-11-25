# Bash Reference

## Variables

```bash
# Define variable
name="Nick"

# Access variable
echo "$name"

# Command substitution
current_user=$(whoami)

# Environment variable
export PATH="$PATH:/custom/path"

# Read input
read -r -p "Enter value: " value

# Unset variable
unset name
```

Use quotes around variable expansions to avoid unintended word splitting and glob expansion.

## Quoting

| Syntax | Behaviour |
|---|---|
| `'text'` | Literal string |
| `"text"` | Allows variable and command expansion |
| `$(command)` | Command substitution |
| `\` | Escape next character |
| `$'text'` | ANSI-C escape processing |

## Conditionals

```bash
if [ "$value" = "test" ]; then
    echo "Match"
else
    echo "No match"
fi
```

### Numeric comparisons

| Operator | Meaning |
|---|---|
| `-eq` | Equal |
| `-ne` | Not equal |
| `-gt` | Greater than |
| `-ge` | Greater than or equal |
| `-lt` | Less than |
| `-le` | Less than or equal |

### String comparisons

```bash
[ "$a" = "$b" ]
[ "$a" != "$b" ]
[ -z "$value" ]
[ -n "$value" ]
```

### File tests

| Test | Meaning |
|---|---|
| `-e file` | Exists |
| `-f file` | Regular file |
| `-d path` | Directory |
| `-r file` | Readable |
| `-w file` | Writable |
| `-x file` | Executable |
| `-s file` | Exists and is not empty |

## Loops

### For loop

```bash
for item in one two three; do
    echo "$item"
done
```

### Iterate over files

```bash
for file in /var/log/*.log; do
    [ -f "$file" ] || continue
    echo "$file"
done
```

### While loop

```bash
while read -r line; do
    echo "$line"
done < input.txt
```

### C-style loop

```bash
for ((i=1; i<=5; i++)); do
    echo "$i"
done
```

## Functions

```bash
greet() {
    local name="$1"
    echo "Hello, $name"
}

greet "Nick"
```

## Arguments

| Variable | Meaning |
|---|---|
| `$0` | Script name |
| `$1` | First argument |
| `$2` | Second argument |
| `$#` | Number of arguments |
| `$@` | All arguments as separate words |
| `$*` | All arguments as a single word when quoted |
| `$?` | Previous command exit status |
| `$$` | Current shell PID |

## Input and output

```bash
# Read user input
read -r value

# Redirect output
command > output.txt

# Append output
command >> output.txt

# Redirect errors
command 2> error.txt

# Redirect both streams
command > output.txt 2>&1

# Pipe output
command1 | command2

# Here document
cat <<EOF
This is a
multiline message.
EOF
```

## Useful built-ins

| Command | Description |
|---|---|
| `echo` | Print text |
| `printf` | Formatted output |
| `read` | Read input |
| `export` | Export environment variable |
| `source file` | Execute file in current shell |
| `alias` | Create command alias |
| `type command` | Identify command type |
| `command -v name` | Locate command |
| `set -e` | Exit on certain command failures |
| `set -u` | Treat unset variables as errors |
| `set -o pipefail` | Propagate pipeline failures |

## Safer script defaults

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

main() {
    echo "Script started"
}

main "$@"
```

These settings improve error handling but do not eliminate every Bash edge case. Test scripts with representative inputs.

## Exit codes

```bash
# Capture exit code
command
status=$?

# Exit successfully
exit 0

# Exit with failure
exit 1

# Check previous command
if command; then
    echo "Success"
else
    echo "Failure"
fi
```

## Debugging

```bash
# Syntax check
bash -n script.sh

# Trace execution
bash -x script.sh

# Enable tracing inside script
set -x

# Disable tracing
set +x

# Display shell options
set -o
```

## Regular expressions

```bash
# Match a pattern
grep "pattern" file

# Extended regular expressions
grep -E "error|warning" file

# Case-insensitive matching
grep -i "pattern" file

# Invert matching
grep -v "pattern" file

# Match whole words
grep -w "admin" file

# Match digits
grep -E '[0-9]+' file

# Match IPv4-shaped strings (not full IP validation)
grep -E '[0-9]{1,3}(\.[0-9]{1,3}){3}' file
```

## References

- [GNU Bash Manual](https://www.gnu.org/software/bash/manual/)
- [ShellCheck](https://www.shellcheck.net/)
- [Bash Hackers Wiki](https://flokoe.github.io/bash-hackers-wiki/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
