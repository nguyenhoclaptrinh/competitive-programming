#!/bin/bash
# TTS tiếng Việt bằng Edge TTS (giọng vi-VN-HoaiMyNeural).
# Cách dùng: ./tts.sh <narration.txt> <audio.mp3> [voice]
# Yêu cầu: edge-tts trong PATH, .venv hoặc /tmp/opencode/tts-env.
set -e
IN="${1:?Thiếu file narration.txt}"; OUT="${2:?Thiếu file audio.mp3}"
VOICE="${3:-vi-VN-HoaiMyNeural}"

VENV_PY=""
if command -v edge-tts >/dev/null 2>&1; then
    VENV_PY="$(command -v edge-tts)"
elif [ -x ".venv/bin/edge-tts" ]; then
    VENV_PY=".venv/bin/edge-tts"
elif [ -x "/tmp/opencode/tts-env/bin/edge-tts" ]; then
    VENV_PY="/tmp/opencode/tts-env/bin/edge-tts"
else
    echo "ERR: Chưa tìm thấy edge-tts. Cài đặt nhanh: python3 -m venv /tmp/opencode/tts-env && /tmp/opencode/tts-env/bin/pip install edge-tts" >&2
    exit 1
fi

"$VENV_PY" --voice "$VOICE" --file "$IN" --write-media "$OUT"
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$OUT"
