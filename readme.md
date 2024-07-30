
# Password-Protected ZIP File Cracking

This project demonstrates how to crack a password-protected ZIP file using a brute force method with a list of passwords from the Ashley Madison password leak data. The implementation is done in both Python and Rust, and the performance of each is compared.

## Project Structure

```
.
├── Ashley_Madison.txt                # Password list from Ashley Madison leak
├── make_zip.py                       # Script to create a password-protected ZIP file
├── protected.zip                     # Example password-protected ZIP file
├── py_prog                           # Python implementation directory
│   ├── data
│   │   ├── Ashley_Madison.txt -> ../../Ashley_Madison.txt   # Symlink to the password list
│   │   └── protected.zip -> ../../protected.zip             # Symlink to the ZIP file
│   ├── main.ipynb                    # Jupyter notebook with Python implementation
│   └── payload
│       └── payload.txt               # Example payload inside the ZIP file
└── rust_prog                         # Rust implementation directory
    ├── Cargo.lock                    # Cargo lock file
    ├── Cargo.toml                    # Cargo configuration file
    ├── data
    │   ├── Ashley_Madison.txt -> ../../Ashley_Madison.txt   # Symlink to the password list
    │   └── protected.zip -> ../../protected.zip             # Symlink to the ZIP file
    └── src
        └── main.rs                   # Rust implementation source code
```

## Python Implementation

The Python implementation is provided in a Jupyter notebook (`py_prog/main.ipynb`). It uses the standard `zipfile` library to attempt to extract the contents of the password-protected ZIP file using each password from the list.

### Running the Python Code

1. Ensure you have Python and Jupyter installed.
2. Navigate to the `py_prog` directory.
3. Open the `main.ipynb` notebook in Jupyter.
4. Run the cells to execute the password-cracking process.

The Python code takes approximately 28.4 seconds per loop (mean ± std. dev. of 7 runs, 1 loop each).

## Rust Implementation

The Rust implementation is provided in the `rust_prog` directory. It uses the `zip` crate to handle ZIP file operations and attempts to extract the contents using each password from the list.

### Running the Rust Code

1. Ensure you have Rust installed. If not, install it using `rustup`.
2. Navigate to the `rust_prog` directory.
3. Build and run the Rust program:
   ```sh
   cargo build --release
   cargo run --release
   ```

The Rust code takes approximately 15 seconds in release build.

## Performance Comparison

| Language | Time       |
|----------|------------|
| Python   | 28.4 s     |
| Rust     | 15 s       |



## Creating the Password-Protected ZIP File

The `make_zip.py` script creates a password-protected ZIP file with an example payload. You can run this script to generate a new `protected.zip` file if needed.

```sh
python make_zip.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
