# DLLExportHeaderGen
This tool generate header files that contain #pragma directive using in Visual Studio to generate DLL that contain export function from other DLL.

Using in DLL proxying/Sideloading.

## Installation
1. Install Python3 https://www.python.org/downloads/
2. Get needed dependencies
```
python -m pip install -r requirements.txt
```

3. Usage.
```bash
python DLLExportHeaderGen.py <dll_path>
```
4. Header file will save at current directory

## Example Usage
```sh
python main.py "C:\Windows\SysWOW64\UiAutomationCore.dll"
```



