from typing import List
from pathlib import Path

def convertPDF(files: List[Path], outdir: Path, verbose: bool) -> int:
    """Convert the list of PDF files to corresponding .txt files"""
    if len(files) == 0:
        if verbose:
            print("No PDF files found. Quitting.")
        return 0
    return 1