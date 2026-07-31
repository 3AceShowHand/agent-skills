#!/usr/bin/env bash
# Human-in-the-loop reproduction template. Copy it, replace the sample steps,
# and run the copy when a deterministic repro still requires human actions.

set -euo pipefail

step() {
  printf '\n>>> %s\n' "$1"
  read -r -p "    [Enter when done] " _
}

capture() {
  local var="$1" question="$2" answer
  printf '\n>>> %s\n' "$question"
  read -r -p "    > " answer
  printf -v "$var" '%s' "$answer"
}

# Replace these sample steps with the smallest interaction that reproduces the bug.
step "Perform the action that triggers the failure."
capture REPRODUCED "Did the exact reported failure occur? (y/n)"
capture SYMPTOM "Paste the error or describe the observed symptom:"

printf '\n--- Captured ---\n'
printf 'REPRODUCED=%s\n' "$REPRODUCED"
printf 'SYMPTOM=%s\n' "$SYMPTOM"
