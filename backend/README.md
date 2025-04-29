# Development Setup

## Installation

### 1. Create Virtual Environment
First time setup:
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt
```

# Usage

### Local Development
```bash
  # Activate existing virtual environment
  source venv/bin/activate

  # Run FastAPI server
  uvicorn app:app --reload

  # Access API at:
  # - http://localhost:8000
  # - http://localhost:8000/docs (Swagger UI)
```

# Docker Development
```bash
  # Start services
  docker-compose up backend

  # Access API at:
  # - http://localhost:5002
  # - http://localhost:5002/docs (Swagger UI)
```

# Enviroment Management

### Daily Use
```bash
  # Activate virtual environment
  source venv/bin/activate

  # Deactivate when done
  deactivate
```

### Adding New Dependencies
```bash
# With venv activated
pip3 install some-package
pip3 freeze > requirements.txt
```

# Clean Up
### Temporary
```bash
# Just deactivate the environment
deactivate
```

### Complete Removal
```bash
# Deactivate first
deactivate

# Delete virtual environment
rm -rf venv
```
