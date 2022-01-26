import argparse
from pathlib import Path
import errno
import os
import glob
from motion import convertPDF


def curate_pdfs(path: Path, o: str, directory: bool, verbose: bool) -> None:
    """Find the PDF files the user specified and send them to be converted"""
    o_path = None
    if o != os.getcwd():
        o_path = Path(o)
    else:
        o_path = Path(o + '/text')
    o_path.mkdir(parents=True, exist_ok=True)
        
    n = 0

    if directory:
        n = convertPDF(list(glob.glob("*.pdf")) + list(glob.glob("*.PDF")))
    else:
        if path.suffix.lower() == '.pdf':
            n = convertPDF([path], o_path, verbose)
        else:
            n = convertPDF([], o_path, verbose)
    
    if verbose:
        print("Converted {} PDF files.".format(n))


def is_path(path_str: str) -> Path:
    """Type function to make sure a string is an existing path"""
    path = Path(path_str)
    if path.exists():
        return path
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path_str)


def main():
    """Commmand line entry point."""
    parser = argparse.ArgumentParser(description="A script built on "
                                    "Tesseract-OCR for converting .pdf to .txt")
    parser.add_argument('path', help="Path to PDF file(s).", type=is_path)
    parser.add_argument('--directory', '-d', action='store_true',
                    help="Use if supplied path is directory of PDF files")
    parser.add_argument('--verbose', '-v', action='store_true', 
                    help="Print debug information")
    parser.add_argument('--out', '-o', help="Directory to put the resulting "
                    ".txt file(s). Default: [currect directory]/text", 
                    type=str, default=os.getcwd(), required=False)
    parser.parse_args()

    curate_pdfs(parser.path, parser.out, parser.directory, parser.verbose)
