import argparse
from license_identifier import LicenseAndCopyrightIdentifier


def main():
    parser = argparse.ArgumentParser(description='Identify open source license and copyright statements in a text file')
    parser.add_argument('file_path', help='Path to the file to analyze')
    args = parser.parse_args()
    file_path = args.file_path

    with open(args.file_path, 'r') as f:
        text = f.read()

    identifier = LicenseAndCopyrightIdentifier()
    license_spdx_code, license_proba = identifier.identify_license(text)
    print(f'License: {license_spdx_code} ({license_proba:.2f} probability)')
    year_range, statement = identifier.identify_copyright(text)
    if statement:
        print(f'Copyright: {statement}')


if __name__ == '__main__':
    main()
