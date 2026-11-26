# Claude instructions

Follow every rule in [AGENTS.md](AGENTS.md), including the factual release changelog and universal diagnostic export contract. Preserve the existing changelog, FlareStore packaging rules, release history and unrelated application behavior. Never claim device diagnostic export is verified without a signed-device cross-app paste, native Share and Files export test.

## Mandatory cross-project file picker standard

**RELEASE-BLOCKING:** Follow [MANDATORY_FILE_PICKER.md](https://github.com/soum91/tweaks/blob/main/MANDATORY_FILE_PICKER.md) and this repository's AGENTS.md for every existing and future importer, exporter, signer, browser and file picker. A picker that merely opens but ignores a file tap is broken. Require end-to-end real-device selection/import verification before claiming a fix; preserve security scope and asynchronous staged files; report actionable failures. Propagate this requirement to every new app. Do not weaken existing policies.
