### 1. Naming Convention
Konvensi penamaan untuk konsistensi kode, standar python PEP 8:
*   **CamelCase** `MyName` untuk class
*   **snake_case** `my_name` untuk variabel, function, modules and packages
*   **UPPER_CASE** `100` untuk konstanta
---

### 2. White Space
Karakter kosong yang tidak terlihat tetapi tetap dibaca oleh interpreter Python. Fungsi utamanya adalah untuk struktur dan keterbacaan:

*   **Spasi**
    ```python
    x = 1 + 10
    ```

*   **Tab** (`\t`)
    ```python
    print("\thalo")
    # Output:    halo
    ```

*   **Newline** (`\n`)
    ```python
    print("my\nname")
    # Output:
    # my
    # name
    ```

---

### 3. Syntax Separator
Aturan pemisah statement dalam Python:

*   **Newline** (Baris Baru)
    ```python
    print("my")
    print("name")
    ```

*   **Semicolon** (Titik Koma)
    ```python
    print("my"); print("name")
    ```

*   **Backslash** (`\`)
    Digunakan untuk melanjutkan baris di bawahnya agar tetap terbaca sebagai satu statement:
    ```python
    x = 2 + 3 + 4 \
    9 + 4
    ```

*   **Implicit Continuation** `()`, `[]`, `{}`
    Memecah pernyataan panjang menjadi beberapa baris tanpa perlu menggunakan tanda backslash (`\`) untuk meningkatkan keterbacaan kode:
    ```python
    numbers = [
        1, 2, 3,
        4, 5
    ]
    ```
    
