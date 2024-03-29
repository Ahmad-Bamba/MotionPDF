# MotionPDF
A crossplatform Python tool for converting PDFs to plaintext, built on the Tesseract OCR Open Source Library and 
[pyPDF-OCR](https://github.com/Ahmad-Bamba/pyPDF-OCR). It was designed to make the process of scanning zines and 
pamphlets into readable, accessible formats easier.

# Prerequisites

This application is tested with Tesseract-OCR 4.1. As such, Tesseract-OCR 4.1 or higher should be installed on the 
system and located in the system PATH.

For guidance on how to do this, please see the [Tesseract user manual](https://github.com/tesseract-ocr/tessdoc#readme).
 For installation on Windows machines, see the 
 [following](https://medium.com/quantrium-tech/installing-and-using-tesseract-4-on-windows-10-4f7930313f82) resource.

If you would like to use a language other than English (explained below), you must install it to Tessearct first. 
For Mac OS or Ubuntu, additional Tessearct languages may be available through Homebrew `brew install tesseract-[lang]` 
or apt `apt install tesseract-[lang]` respectively. Tesseract language files can also be 
[downloaded and installed manually]() TODO

# Installation

The entire package will be available to install on pip. TODO

# Behavior

MotionPDF converts PDF files with no available plaintext information into a single .txt file.

# Usage

This program is simply a user-friendly wrapper for Tesseract. The command-line tool can be used as follows:

`motionpdf (path) [-v] [-o path_to_output] [-l languages] [-L line width]`

where square brackets indicate optional arguments and round brackets indicate mandatory, positional arguments.

`motionpdf -h`

will generate the help page for the command line tool and explain each option in detail.

## Flags

- `-v` or `--verbose` enables verbose mode. Verbose mode will save the images created from the provided PDF files, as well
as print more detailed error messages in the event of a failure. By default this option is disabled.

- `-o` or `--output` allows the user to specify the path the resulting .txt file will be generated. By default, files 
will be generated in a new directory called "text" in the current working directory

- `-l` or `--language` passes the given language directly to tesseract. To specify one language, use its 
[language code](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html). To specify that a PDF 
has multiple languages, put both language codes in this flag, separated by a `+` (e.g. `eng+fra`).

- `-L` or `--linewidth` tries to organize the text so that each line has at most the specified number of characters. 
By default, this is set to 0, meaning that the program will let Tesseract try to reproduce the line spacing found in 
the original document.

# Flaws

MotionPDF relies on Tesseract-OCR, a powerful and open source OCR engine. However, Tesseract is not as good as 
commercial OCR engines. For best results, scan zines, pamphlets, and other texts such that the text is flat and 
undistorted.

When the process is complete, the resulting text will most likely still have garbage, incorrect lines, or out of order 
lines. The user can fix these manually to get the clean text, then move that text into whatever format they desire.