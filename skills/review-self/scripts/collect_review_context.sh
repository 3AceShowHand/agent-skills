#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  collect_review_context.sh [--base <ref>] [--paths p1,p2] [--no-fetch]

Collect read-only git context for reviewing the current branch.

Options:
  --base <ref>   Override base ref. Examples: upstream/master, upstream/main,
                 origin/main, master, main, HEAD.
  --paths <csv>  Print additional path-filtered diff stats for comma-separated paths.
  --no-fetch     Do not fetch remote-tracking refs.
  -h, --help     Show this help.

Default base resolution:
  1. Fetch upstream master, then use upstream/master if available.
  2. Otherwise fetch upstream main, then use upstream/main if available.

The script does not checkout, merge, reset, or edit files.
When fetching is enabled, it stops if no candidate base can be refreshed. Use
--no-fetch only when reviewing against existing local refs is intentional.
EOF
}

BASE_INPUT=""
PATHS_CSV=""
FETCH=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --base)
      if [[ $# -lt 2 ]]; then
        echo "ERROR: --base requires a value" >&2
        exit 2
      fi
      BASE_INPUT="$2"
      shift 2
      ;;
    --paths)
      if [[ $# -lt 2 ]]; then
        echo "ERROR: --paths requires a value" >&2
        exit 2
      fi
      PATHS_CSV="$2"
      shift 2
      ;;
    --no-fetch)
      FETCH=0
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

git rev-parse --show-toplevel >/dev/null
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

remote_exists() {
  git remote get-url "$1" >/dev/null 2>&1
}

ref_exists() {
  git rev-parse --verify --quiet "$1^{commit}" >/dev/null
}

fetch_branch() {
  local remote="$1"
  local branch="$2"
  if [[ "$FETCH" -eq 0 ]]; then
    return 0
  fi
  if ! remote_exists "$remote"; then
    echo "ERROR: remote not found: $remote" >&2
    return 1
  fi
  if git fetch --prune "$remote" "$branch" >/dev/null; then
    return 0
  fi
  echo "ERROR: failed to refresh $remote/$branch. Use --no-fetch only to accept existing local refs." >&2
  return 1
}

resolve_base() {
  if [[ -n "$BASE_INPUT" ]]; then
    if [[ "$BASE_INPUT" == */* ]]; then
      local remote="${BASE_INPUT%%/*}"
      local branch="${BASE_INPUT#*/}"
      if ! fetch_branch "$remote" "$branch"; then
        return 1
      fi
      if ref_exists "$BASE_INPUT"; then
        printf '%s\n' "$BASE_INPUT"
        return 0
      fi
    else
      if [[ "$BASE_INPUT" == "HEAD" || "$BASE_INPUT" == "@" ]]; then
        printf '%s\n' "$BASE_INPUT"
        return 0
      fi
      if remote_exists upstream; then
        if fetch_branch upstream "$BASE_INPUT"; then
          if ref_exists "upstream/$BASE_INPUT"; then
            printf '%s\n' "upstream/$BASE_INPUT"
            return 0
          fi
        elif [[ "$FETCH" -eq 1 ]]; then
          return 1
        fi
      fi
      if ref_exists "$BASE_INPUT"; then
        printf '%s\n' "$BASE_INPUT"
        return 0
      fi
    fi
    echo "ERROR: base ref not found: $BASE_INPUT" >&2
    return 1
  fi

  if ! remote_exists upstream; then
    echo "ERROR: upstream remote not found. Use --base <ref> or add an upstream remote." >&2
    return 1
  fi

  if fetch_branch upstream master && ref_exists upstream/master; then
    printf '%s\n' "upstream/master"
    return 0
  fi

  if fetch_branch upstream main && ref_exists upstream/main; then
    printf '%s\n' "upstream/main"
    return 0
  fi

  echo "ERROR: could not refresh upstream/master or upstream/main. Use --no-fetch only to accept existing local refs." >&2
  return 1
}

BASE_REF="$(resolve_base)"
BASE_SHA="$(git rev-parse "$BASE_REF^{commit}")"
HEAD_SHA="$(git rev-parse HEAD)"
BRANCH="$(git branch --show-current || true)"

IFS=',' read -r -a PATH_FILTERS <<< "$PATHS_CSV"

print_section() {
  printf '\n== %s ==\n' "$1"
}

print_section "repository"
printf 'root: %s\n' "$REPO_ROOT"
printf 'branch: %s\n' "${BRANCH:-detached HEAD}"
printf 'head_sha: %s\n' "$HEAD_SHA"
printf 'base_ref: %s\n' "$BASE_REF"
printf 'base_sha: %s\n' "$BASE_SHA"
printf 'commit_range: %s..HEAD\n' "$BASE_REF"
printf 'diff_range: %s...HEAD\n' "$BASE_REF"
if [[ "$FETCH" -eq 0 ]]; then
  printf 'fetch_status: skipped (--no-fetch)\n'
elif [[ "$BASE_REF" == */* ]]; then
  printf 'fetch_status: succeeded\n'
else
  printf 'fetch_status: not needed for local ref\n'
fi

print_section "remotes"
git remote -v || true

print_section "worktree status"
git status --porcelain

print_section "commits unique to HEAD"
git log --oneline --decorate "$BASE_REF"..HEAD || true

print_section "committed diff stat"
git diff --stat "$BASE_REF"...HEAD

print_section "committed changed files"
git diff --name-status "$BASE_REF"...HEAD

if [[ -n "$PATHS_CSV" ]]; then
  print_section "path-filtered committed diff stat"
  git diff --stat "$BASE_REF"...HEAD -- "${PATH_FILTERS[@]}"
fi

print_section "staged diff stat"
git diff --cached --stat

print_section "unstaged diff stat"
git diff --stat

print_section "next commands"
printf 'git diff %s...HEAD\n' "$BASE_REF"
printf 'git diff --cached\n'
printf 'git diff\n'
