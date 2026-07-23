import argparse
import subprocess
import sys

# Usage
# python main.py "https://example.com/playlist.m3u8" output.mp4


def main():
    parser = argparse.ArgumentParser(
        description="Download an HLS (.m3u8) stream and save it as an MP4 file."
    )
    parser.add_argument("url", help="HLS playlist URL (.m3u8)")
    parser.add_argument("output", help="Output MP4 filename")

    args = parser.parse_args()

    cmd = [
        "ffmpeg",
        "-i", args.url,
        "-c", "copy",
        "-bsf:a", "aac_adtstoasc",
        args.output,
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"Saved to {args.output}")
    except FileNotFoundError:
        print("Error: ffmpeg is not installed or not in PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("Error: ffmpeg failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
