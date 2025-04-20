# Import Large CSV File

To import very large CSV files, use the `bench` utility's `import-csv` command. This method avoids timeouts that may occur when using the web interface.

## Example

```bash
bench --site test.erpnext.com import-csv ~/Downloads/Activity_Type.csv
```

## Options

- `--only-insert`: Do not overwrite existing records.
- `--submit-after-import`: Submit documents after importing.
- `--ignore-encoding-errors`: Ignore encoding errors while converting to Unicode.

For more details, run:

```bash
bench import-csv --help
```