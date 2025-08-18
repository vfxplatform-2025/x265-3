#!/bin/bash
set -e

DIRNAME=$(basename "$(pwd)")
VER=$(echo "$DIRNAME" | sed -E 's/.*-([0-9]+\.[0-9]+)/\1/')
SRC_DIR=$(dirname "$0")/source
ARCHIVE="x265_${VER}.tar.gz"
DIR="x265_${VER}"
URL="https://bitbucket.org/multicoreware/x265_git/downloads/${ARCHIVE}"

mkdir -p "$SRC_DIR"
cd "$SRC_DIR"

if [ ! -f "$ARCHIVE" ]; then
    echo "📦 Downloading $ARCHIVE"
    wget "$URL"
else
    echo "✅ Archive already exists: $ARCHIVE"
fi

if [ ! -d "$DIR" ]; then
    echo "📂 Extracting $ARCHIVE"
    tar -xzf "$ARCHIVE"
else
    echo "✅ Source directory already exists: $DIR"
fi

