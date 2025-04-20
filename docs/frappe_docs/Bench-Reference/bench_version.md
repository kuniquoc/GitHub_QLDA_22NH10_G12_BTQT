# bench version

## Usage
`bench version [OPTIONS]`

## Description
The `version` command displays compiled info about all the apps installed in the current bench directory. You can choose your preferred output format: plain text, JSON, or ASCII table.

### Options
- `-f`, `--format`: Choose the format for showing versions of the apps installed in the current bench. The available options are "plain", "table", "json", "legacy". This value defaults to "legacy".

### Examples
1. Get human-readable information about the installed apps on the current bench, with commit messages:
   ```
   bench version --format plain
   ```
2. Get bench version information in JSON format:
   ```
   bench version -f json
   ```