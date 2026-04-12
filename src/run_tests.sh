#!/usr/bin/env bash

# Activate virtual environment
source ../venv/bin/activate

# Run tests
pytest --headless
test_status=$?

# If 0 then pass, if 1 fail
if [ $test_status -eq 0 ]; then
  echo "Tests Passed!"
  exit 0
else
  echo "Tests Failed!"
  exit 1
fi

