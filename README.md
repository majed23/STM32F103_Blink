# STM32F103_Blink

## Installation and tools
Download embedded toolchain: https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads
Used version: 9-2020-q2

For STM headers:
1. Start a CubeMx file, STMCube (eol) file, and generate code
2. Use the generated code as a starting point
3. Check the build script or make file to find out about files used by the compiler

Used device: stm32f411re, stm32F103

## Compilation using SCons
Use SCons to call the GCC compiler.
### Installation
```Python
pip install scons  
```
SCons configuration from: https://elektronotes.wordpress.com/2015/02/05/using-scons-with-gnu-toolchain-for-arm-on-windows-part-3-the-scons-script/  
Used version: 4.0.0  

SCons is configured using Python language.

### Usage
Call scons by opening a command prompt and command "scons". The SConstruct.py file will be called automatically.

## Debugging

### STM32 GDB debugger
1. Install OpenOCD as GDB server and ST-Link interface: 
links:  
http://openocd.org/getting-openocd/  
https://github.com/xpack-dev-tools/openocd-xpack  

2. Install the Cortex-Debug vs code extension
3. Install the Native Debug extension. For cortex-debug get the a board svd file from: https://www.keil.com/dd2/Pack/

