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

## Mandatory factual release changelog
Every published release must identify specific genuine changes since the preceding release, cite commits and diff, and keep GitHub release notes and root CHANGELOG.md reconciled. No generic filler, copied notes or invented capabilities. Rebuild-only releases must identify actual toolchain, packaging, signing or artifact differences. Keep the release-event and six-hour fallback checks enabled; do not suppress failed audits. When a release producer is known, monitor its completed workflow by exact name. GITHUB_TOKEN-created releases do not trigger release events.

## Universal diagnostic export contract
All diagnostic and log report screens must provide Copy with actual clipboard read-back verification and visible success/failure feedback; native Share; native Save as plain-text .txt via Files picker (fileExporter or UIDocumentPickerViewController on iOS); and selectable full report text as fallback. Never provide silent clipboard-only controls. Include app and version/build, device and OS, and actionable error/return codes; redact tokens, cookies, passwords and other secrets. Verify cross-app paste, Share and Files export on a signed device; until then explicitly mark the functionality unverified.

## Mandatory file picker / import policy (release-blocking)

Every file picker, browser, import, export, signing or upload workflow in this repository **MUST** comply with [MANDATORY_FILE_PICKER.md](https://github.com/soum91/tweaks/blob/main/MANDATORY_FILE_PICKER.md). This covers future apps and all platforms. Files must be selectable with a real tap, return to the caller, copy safely to app-owned storage, complete the import and give visible success/error. Real-device end-to-end testing is required before claiming success. Merely opening Files or compiling is insufficient. Preserve existing project policies. Codex and Claude must propagate this rule to new app repositories.
