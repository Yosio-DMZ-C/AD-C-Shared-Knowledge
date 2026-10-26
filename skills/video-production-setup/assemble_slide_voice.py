#!/usr/bin/env python3
"""Match slide-NN.png with human-recorded slide-NN.wav/mp3/m4a; assemble MP4.

Missing recordings stop the output (exit 2). Requires ffmpeg and ffprobe.
Inputs stay local: no TTS, no upload, no generated replacement narration.
"""
import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


def call(args):
    return subprocess.run(args, check=True, text=True, capture_output=True).stdout


def numbered(folder, pattern):
    result = {}
    if not folder.is_dir():
        raise ValueError("input folder unavailable")
    for item in folder.iterdir():
        m = re.fullmatch(pattern, item.name, re.I)
        if m:
            number = int(m.group(1))
            if number in result or not item.is_file() or item.is_symlink():
                raise ValueError("duplicate or unsafe slide file")
            result[number] = item
    return result


def probe_audio(path):
    info = json.loads(call(["ffprobe", "-v", "error", "-select_streams", "a:0",
                            "-show_entries", "stream=codec_type:format=duration",
                            "-of", "json", str(path)]))
    if not info.get("streams") or info["streams"][0].get("codec_type") != "audio":
        raise ValueError("recording has no audio track")
    length = float(info.get("format", {}).get("duration", 0))
    if not math.isfinite(length) or not 0.1 <= length <= 3600:
        raise ValueError("invalid recording duration")
    return length


def make_video(images, sounds, output):
    with tempfile.TemporaryDirectory(prefix="adnc-voice-") as tmp:
        temp = Path(tmp)
        segments = []
        for index in sorted(images):
            length = probe_audio(sounds[index])
            part = temp / ("part-%02d.mp4" % index)
            call(["ffmpeg", "-nostdin", "-v", "error", "-y", "-loop", "1",
                  "-framerate", "24", "-i", str(images[index]), "-i", str(sounds[index]),
                  "-filter:v", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
                  "-af", "apad=pad_dur=0.3", "-map", "0:v", "-map", "1:a:0",
                  "-c:v", "libx264", "-preset", "ultrafast", "-r", "24",
                  "-c:a", "aac", "-ar", "48000", "-ac", "2",
                  "-t", "%.3f" % (length + 0.3), str(part)])
            segments.append(part)
        listing = temp / "list.ffconcat"
        listing.write_text("ffconcat version 1.0\n" +
                           "".join("file '%s'\n" % x.name for x in segments))
        joined = temp / "joined.mp4"
        call(["ffmpeg", "-nostdin", "-v", "error", "-y", "-safe", "0",
              "-f", "concat", "-i", str(listing), "-c", "copy",
              "-movflags", "+faststart", str(joined)])
        kinds = json.loads(call(["ffprobe", "-v", "error", "-show_entries",
                                 "stream=codec_type", "-of", "json", str(joined)]))
        tracks = {x.get("codec_type") for x in kinds.get("streams", [])}
        if not {"video", "audio"} <= tracks:
            raise ValueError("output stream missing")
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(joined, output)
        return {"size_bytes": output.stat().st_size,
                "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--images", type=Path, required=True)
    p.add_argument("--audio", type=Path, required=True)
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    report = {"status": "NOT_RUN"}
    try:
        if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
            raise FileNotFoundError("ffmpeg/ffprobe unavailable")
        images = numbered(args.images, r"slide-(\d{2})\.png")
        sounds = numbered(args.audio, r"slide-(\d{2})\.(?:wav|mp3|m4a)")
        ids = sorted(images)
        if not ids or ids != list(range(1, len(ids) + 1)):
            raise ValueError("images must be sequential from slide-01.png")
        manifest = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
        texts = manifest.get("slides")
        if not isinstance(texts, list) or [t.get("id") for t in texts] != [
                "slide-%02d" % i for i in ids] or any(not isinstance(t.get("text"), str)
                or not t["text"].strip() for t in texts):
            raise ValueError("manifest IDs or text do not match slides")
        missing = ["slide-%02d" % i for i in ids if i not in sounds]
        extra = ["slide-%02d" % i for i in sounds if i not in images]
        if extra:
            raise ValueError("recording without matching slide")
        report = {"status": "NOT_RUN", "slide_count": len(ids),
                  "missing_recordings": missing}
        if not missing:
            report["output"] = make_video(images, sounds, args.output)
            report["status"] = "PASS_TECHNICAL_ONLY"
    except FileNotFoundError:
        report = {"status": "NOT_RUN", "reason": "required input/tool unavailable"}
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError,
            json.JSONDecodeError):
        report = {"status": "FAIL", "reason": "invalid input or encode failure"}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["status"].startswith("PASS") else
                     2 if report["status"] == "NOT_RUN" else 1)


if __name__ == "__main__":
    main()
