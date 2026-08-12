# IOC-Hunter

IOC-Hunter is a Python command-line tool for extracting and validating Indicators of Compromise (IOCs) from text files and security logs.

The project is being developed as a practical exercise in Python, cybersecurity automation, log analysis, and software engineering practices.

## Current Features

IOC-Hunter currently supports:

* IPv4 address extraction
* IPv4 validation
* SHA-256 hash extraction
* CVE identifier extraction
* CVE normalization
* Detection of invalid IPv4 candidates
* Command-line file input

## Usage

Run the tool by providing the path to a text or log file:

```bash
python iochunter.py samples/suspicious.log
```

Example output:

```text
Resultados encontrados:

Endereço IPv4 válido: 192.168.1.45
Endereço IPv4 válido: 10.0.0.12

Quantidade de endereços IPv4 válidos: 2

Hash SHA-256 encontrado: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Quantidade de hashes SHA-256 encontrados: 1

CVE encontrado: CVE-2024-3094

Quantidade de CVEs encontrados: 1
Quantidade de CVEs únicos encontrados: 1
```

Command-line help is also available:

```bash
python iochunter.py --help
```

## Requirements

* Python 3

The current version uses only modules from the Python standard library.

## Project Structure

```text
ioc-hunter/
├── iochunter.py
├── samples/
│   └── suspicious.log
├── README.md
├── requirements.txt
└── .gitignore
```

The sample log contains valid indicators, malformed values, and unrelated data for testing extraction and validation behavior.

## Development Status

The project is under active development. Planned improvements include:

* IPv6 extraction
* MD5 and SHA-1 hashes
* URLs, domains, and e-mail addresses
* Automated tests
* Deduplication options
* JSON and CSV output
* Whitelisting
* Improved command-line options
* Optional threat intelligence integrations

The project will remain intentionally small and incremental, prioritizing readable code, validation, testing, and clear separation of responsibilities.
