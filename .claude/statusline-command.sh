#!/bin/bash
# Claude Code statusline for NCT project
# Shows: model name + context window usage percentage

input=$(cat)

model=$(echo "$input" | jq -r '.model.display_name // "Claude"')
used=$(echo "$input" | jq -r '.context_window.used_percentage // empty')

RESET="\033[0m"
DIM="\033[2m"
GREEN="\033[2;32m"
YELLOW="\033[2;33m"
RED="\033[2;31m"

if [ -n "$used" ]; then
  used_int=$(printf '%.0f' "$used")

  if [ "$used_int" -ge 80 ]; then
    color="$RED"
  elif [ "$used_int" -ge 50 ]; then
    color="$YELLOW"
  else
    color="$GREEN"
  fi

  printf "${DIM}🤖 %s${RESET} ${DIM}·${RESET} ${color}📊 %s%%${RESET}\n" "$model" "$used_int"
else
  printf "${DIM}🤖 %s${RESET} ${DIM}·${RESET} ${DIM}📊 —${RESET}\n" "$model"
fi
