#!/usr/bin/env python3
"""Patch a user-uploaded X 12.44 IPA with the tested web-login components.

Requires the system 'zip' executable. Output is unsigned; re-sign for iOS.
Usage: python3 scripts/rebuild_from_upload.py ORIGINAL.ipa COMPONENTS.ipa OUTPUT.ipa
"""
import argparse
import hashlib
import plistlib
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

COMPONENTS = (
    "Frameworks/BHTwitter.dylib",
    "BHTwitter.bundle/",
    "Frameworks/CydiaSubstrate.framework/",
)

def get_root(z):
    paths = [n for n in z.namelist() if n.startswith("Payload/") and n.count("/") == 2 and n.endswith(".app/Info.plist")]
    if len(paths) != 1:
        raise RuntimeError(f"Expected one app Info.plist; found {len(paths)}")
    return paths[0].removesuffix("Info.plist")

def included(relative):
    return any(relative == p or relative.startswith(p) for p in COMPONENTS)

def main(source, donor, output):
    if not shutil.which("zip"):
        raise RuntimeError("The system zip executable is required")
    with zipfile.ZipFile(source) as orig, zipfile.ZipFile(donor) as patched:
        root = get_root(orig)
        donor_root = get_root(patched)
        info = plistlib.loads(orig.read(root + "Info.plist"))
        if info.get("CFBundleIdentifier") != "com.atebits.Tweetie2" or info.get("CFBundleShortVersionString") != "12.44":
            raise RuntimeError("The uploaded IPA is not X 12.44")
        extracted = []
        with tempfile.TemporaryDirectory(prefix="xexperiment-") as t:
            staging = Path(t)
            for name in patched.namelist():
                if name.startswith(donor_root):
                    rel = name[len(donor_root):]
                    if included(rel):
                        target = staging / root / rel
                        if name.endswith("/"):
                            target.mkdir(parents=True, exist_ok=True)
                        else:
                            target.parent.mkdir(parents=True, exist_ok=True)
                            with patched.open(name) as src, target.open("wb") as dest:
                                shutil.copyfileobj(src, dest, 1024*1024)
                            extracted.append(rel)
            if "Frameworks/BHTwitter.dylib" not in extracted:
                raise RuntimeError("No replacement library in components IPA")
            if not any(p.startswith("BHTwitter.bundle/") for p in extracted):
                raise RuntimeError("Replacement resources missing")
            if not any(p.startswith("Frameworks/CydiaSubstrate.framework/") for p in extracted):
                raise RuntimeError("Replacement substrate framework missing")

            shutil.copy2(source, output)
            subprocess.run([
                "zip", "-q", "-d", str(output.resolve()),
                root + "Frameworks/BHTwitter.dylib",
                root + "BHTwitter.bundle/*",
                root + "Frameworks/CydiaSubstrate.framework/*"
            ], check=True)
            subprocess.run(["zip","-q","-r",str(output.resolve()),"Payload"],cwd=staging,check=True)

    with zipfile.ZipFile(output) as z:
        bad = z.testzip()
        if bad:
            raise RuntimeError(f"ZIP integrity failed: {bad}")
        assert plistlib.loads(z.read(root+"Info.plist")) == info
        assert root+"Frameworks/TwitterLoginFix.dylib" in z.namelist()
        assert root+"Frameworks/BHTwitter.dylib" in z.namelist()
        assert root+"Twitter" in z.namelist()
        print(f"Verified {len(z.namelist())} archive entries")
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    print(f"Built {output}: {output.stat().st_size} bytes, SHA256 {digest}")
    (output.parent/"SHA256SUMS.txt").write_text(f"{digest}  {output.name}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source",type=Path)
    parser.add_argument("components",type=Path)
    parser.add_argument("output",type=Path)
    args = parser.parse_args()
    if args.output.resolve() in (args.source.resolve(),args.components.resolve()):
        parser.error("Output must not overwrite either input")
    main(args.source, args.components, args.output)
