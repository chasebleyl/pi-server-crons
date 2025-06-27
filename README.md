# PI Server Crons

A Python-based data hydration system for game data management, supporting multiple game types including Predecessor, NFL, and FFB.

## Features

- **Multi-game Support**: Predecessor, NFL, and FFB data hydration
- **Database Integration**: PostgreSQL support with connection management
- **API Integration**: RESTful API client with Pydantic models
- **Comprehensive Testing**: Unit and integration test support
- **Cross-platform**: Works on Windows and Linux

## Project Structure

```
pi-server-crons/
├── db/                          # Database layer
│   ├── database.py             # PostgreSQL implementation
│   ├── database_interface.py   # Database interface
│   └── database_mock.py        # Mock for testing
├── scripts/                     # Data hydration scripts
│   ├── hydrate_predecessor_data.py
│   ├── hydrate_predecessor_data_test.py
│   ├── utils_requests.py       # HTTP client
│   ├── utils_requests_interface.py
│   └── utils_requests_mock.py  # Mock for testing
├── schemas/                     # Pydantic data models
│   ├── predecessor/
│   ├── nfl/
│   └── ffb/
├── requirements.txt            # Python dependencies
├── packages.config             # Windows system dependencies (Chocolatey)
├── Makefile                   # Build and test automation
├── pytest.ini                # Test configuration
└── README.md                 # This file
```

## SETUP

### Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)
- **Git** (for version control)
- **GNU make** (for script execution/testing)

### Setup

```bash
# Setup linux development environment
make setup-linux
# OR, setup windows  development environment
make setup-windows

# Verify setup
make verify-setup
```

## Usage

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
make test-cov

# Run only unit tests
make test-unit

# Run only integration tests
make test-integration

# Run tests in specific directory
make test-scripts
make test-db
```

### Development

```bash
# Install development dependencies
make install-dev

# Clean up test artifacts
make clean

# Show available commands
make help
```

### Direct Python Usage

```bash
# Run specific test file
python -m pytest scripts/hydrate_predecessor_data_test.py -v

# Run tests with specific pattern
python -m pytest -k "hero" -v

# Run tests with coverage
python -m pytest --cov=. --cov-report=html
```

## Dependencies

### System Dependencies

**Windows (via Chocolatey - packages.config):**
- **GNU Make 4.4.1+**: Build automation and test running

**Linux (via apt/yum):**
- **GNU Make 4.4.1+**: Build automation and test running

### Python Dependencies (via pip - requirements.txt)
- **psycopg2-binary**: PostgreSQL adapter
- **python-dotenv**: Environment variable management
- **pydantic**: Data validation and settings management
- **requests**: HTTP library for API calls
- **pytest**: Testing framework
- **pytest-cov**: Coverage reporting
- **pytest-html**: HTML test reports

## Testing

The project uses pytest for testing with the following features:

- **Test Discovery**: Automatically finds test files matching `*_test.py`
- **Coverage Reporting**: Generates coverage reports in terminal and HTML
- **Test Markers**: Categorize tests as unit, integration, or slow
- **Mock Support**: Comprehensive mocking for database and HTTP operations

### Test Structure

- **Unit Tests**: Fast, isolated tests using mocks
- **Integration Tests**: Tests that interact with real dependencies
- **Slow Tests**: Tests that take longer to run (marked with `@pytest.mark.slow`)

### Running Specific Test Types

```bash
# Run only unit tests
make test-unit

# Run only integration tests
make test-integration

# Run tests excluding slow ones
python -m pytest -m "not slow"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite: `make test`
6. Submit a pull request

## Troubleshooting

### Common Issues

**Make not found on Windows:**
```powershell
# Ensure Chocolatey is installed and make is available
choco install packages.config -y
```

**Python dependencies not found:**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

**Test failures:**
```bash
# Clean and reinstall
make clean
make install-dev
make test
```

### Environment Variables

Create a `.env` file in the root directory for database configuration:

```env
DB_HOST=localhost
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
```

## License

[Add your license information here] 