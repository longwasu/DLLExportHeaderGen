import pefile
import os
import sys


def generate_header_file(dll_path):
    pe = pefile.PE(dll_path)
    if not hasattr(pe, "DIRECTORY_ENTRY_EXPORT"):
        print("[!] File has no export table")
        return
    
    file_name = os.path.splitext(os.path.basename(dll_path))[0]
    file_path = os.path.split(dll_path)[0]
    path_without_ext = (file_path + "\\" + file_name).replace("\\", "\\\\")

    output_file = f"{file_name}.h"
    exports = pe.DIRECTORY_ENTRY_EXPORT.symbols

    with open(output_file, "w") as f:
        for function in exports:
            function_name = function.name.decode() if function.name else f"Ordinal{function.ordinal}"
            ordinal = function.ordinal
            link_cmd = f"#pragma comment(linker, \"/export:{function_name}={path_without_ext}.{function_name},@{ordinal}\")\n"
            f.write(link_cmd)

    print(f"[+] Header file save as {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: export.py <dll_path>")
        sys.exit(1)
    
    dll_path = sys.argv[1]
    if not os.path.exists(dll_path):
        print("[!] Invalid dll path")
    else:
        generate_header_file(dll_path)