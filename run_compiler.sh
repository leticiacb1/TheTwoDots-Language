#!/bin/bash

test_function="./scripts/test_function.td"
test_if="./scripts/test_if.td"
test_loop="./scripts/test_loop.td"
test_in_out="./scripts/test_stdout_stdin.td"

compiler="./compiler/main.py"

run_test() {
  local test_name="$1"
  local test_file="$2"

  echo "------------------------------------------"
  echo "[INFO] Run $test_name test file ..."
  echo "------------------------------------------"

  if python3 "$compiler" < "$test_file"; then
    echo "------------------------------------------"
    echo "[INFO] TEST $test_name PASS ..."
    echo "------------------------------------------"
  else
    echo "------------------------------------------"
    echo "[ERROR] TEST $test_name FAILED ..."
    echo "------------------------------------------"
    exit 1
  fi
}

if [ "$1" = "test_function" ]; then
  run_test "function" "$test_function"

elif [ "$1" = "test_if" ]; then
  run_test "if" "$test_if"

elif [ "$1" = "test_loop" ]; then
  run_test "loop" "$test_loop"

elif [ "$1" = "test_in_out" ]; then
  run_test "stdout/stdin" "$test_in_out"

else
  echo "------------------------------------------"
  echo "[INFO] Run all tests file ..."
  echo "------------------------------------------"

  run_test "function" "$test_function"
  run_test "if" "$test_if"
  run_test "loop" "$test_loop"
  run_test "stdout/stdin" "$test_in_out"

fi