import argparse
import os
from scanner.sast import scan_directory as scan_sast
from scanner.dep_scan import scan_directory as scan_dep
from scanner.utils import load_json_file

def main():
    parser = argparse.ArgumentParser(description="Security Scanner CLI")
    parser.add_argument("directory", help="Directory to scan")
    parser.add_argument("--sast", action="store_true", help="Perform static code analysis")
    parser.add_argument("--dep-scan", action="store_true", help="Perform dependency scan")
    args = parser.parse_args()

    if args.sast:
        print("Performing static code analysis...")
        issues = scan_sast(args.directory)
        for issue in issues:
            print(issue)

    if args.dep_scan:
        print("Performing dependency scan...")
        issues = scan_dep(args.directory)
        for issue in issues:
            print(issue)

if __name__ == "__main__":
    main()
