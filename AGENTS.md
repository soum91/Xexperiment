# AGENTS.md

Repository purpose: distribute an experimental repackaged X iOS IPA only through an actual GitHub Release, and maintain a valid FlareStore-compatible `repo.json`.

Rules:
- Never claim a build is released or downloadable unless a real release asset exists and its URL is verified.
- Never create placeholder FlareStore `downloadURL` values.
- Never publish account cookies, personal access tokens, passwords, authentication headers, or device-specific credentials.
- Keep `CHANGELOG.md` up to date for every change and include release notes.
- FlareStore version/build fields should correspond to the app's actual Info.plist rather than an arbitrary workflow revision. For the initial experimental IPA the values are 12.44 / 22.
- Keep release binary assets outside git history; IPA files are distributed through GitHub Releases.
- This is an app packaging repository. Any new standalone jailbreak tweaks belong in the separate tweaks repository.
- Any edits to app signing, entitlements, or login behavior need on-device validation. ZIP integrity alone does not prove functionality.
