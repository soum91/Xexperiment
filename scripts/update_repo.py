#!/usr/bin/env python3
"""Generate FlareStore repo.json exclusively from published, actual GitHub IPA release assets."""
import datetime
import json
import os
import re
import urllib.request
from pathlib import Path

REPO = os.environ.get("GITHUB_REPOSITORY", "soum91/Xexperiment")
SOURCE_URL = "https://raw.githubusercontent.com/soum91/Xexperiment/main/repo.json"
API_URL = f"https://api.github.com/repos/{REPO}/releases?per_page=100"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def fetch_json(url):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "Xexperiment-feed-updater"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=40) as response:
        return json.load(response)

def main():
    releases = fetch_json(API_URL)
    items = []
    for release in releases:
        if release.get("draft"):
            continue
        tag = release.get("tag_name", "")
        match = re.fullmatch(r"v?(\d+\.\d+)-b(\d+)", tag)
        if not match:
            continue
        version, build = match.groups()
        for asset in release.get("assets", []):
            name = asset.get("name", "")
            url = asset.get("browser_download_url", "")
            size = asset.get("size", 0)
            if not name.lower().endswith(".ipa") or not url.startswith(
                f"https://github.com/{REPO}/releases/download/"
            ) or size <= 0:
                continue
            items.append({
                "version": version,
                "buildVersion": build,
                "date": release.get("published_at") or datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "localizedDescription": "Experimental X 12.44 login and ad-filtering build; on-device compatibility unverified.",
                "changelog": release.get("body") or "Experimental IPA package.",
                "downloadURL": url,
                "size": size,
                "minOSVersion": "15.0"
            })
    items.sort(key=lambda item: item.get("date", ""), reverse=True)
    source = {
        "name": "Xexperiment",
        "identifier": "com.soum91.xexperiment.source",
        "subtitle": "Experimental X IPA releases",
        "description": "Only verified, published IPA assets are indexed. Builds may be incompatible with your device.",
        "sourceURL": SOURCE_URL,
        "apps": ([{
            "name": "Xexperiment",
            "bundleIdentifier": "com.atebits.Tweetie2",
            "developerName": "Xexperiment",
            "subtitle": "Experimental modified X iOS app",
            "localizedDescription": "Sideloaded X build with experimental web-login bridge. Not officially supported.",
            "category": "social-networking",
            "versions": items
        }] if items else [])
    }
    Path("repo.json").write_text(json.dumps(source, indent=2, ensure_ascii=False) + "\n")
    print(f"Indexed {len(items)} published IPA release asset(s)")
if __name__ == "__main__":
    main()
