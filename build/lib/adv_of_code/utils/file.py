import sys
import os


def read_file(file_path: str) -> list:
    outfile = open(file_path, "r")
    data = outfile.readlines()
    outfile.close()

    return data
