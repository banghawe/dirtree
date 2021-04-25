# dirtree

CLI-based app to generate directory tree

# Getting Started
1. Setting up your virtual environment or you can use ```pipenv```.
2. Run program from console
    ```console
    python3 tree.py [ROOT_DIR]
    ```
   
   ```console
   python3 tree.py ../test_dirtree
   
   ../test_dirtree/
   │
   ├── test_1/
   │
   ├── test_3/
   │
   ├── test_2/
   │   ├── test_2_file_2
   │   └── test_2_file
   │
   ├── oke
   └── test_1_file
   ```
   
# Features
1. Generate directory tree and display it on your terminal
    ```console
    python3 tree.py [ROOT_DIR]
    ```
2. Generate directory tree and create output file markdown
    ```console
    python3 tree.py [ROOT_DIR] -o [OUTPUT_FILE]
    ```
   
### What's next?
- [x] create output file
- [ ] add sort feature
- [ ] give tree more color
