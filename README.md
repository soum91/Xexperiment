# Xexperiment

Experimental X 12.44 IPA packaging and FlareStore distribution.

## Download status
- The source `repo.json` is live, but contains **no app until an IPA has been published to GitHub Releases**.
- The native X 12.44 login bridge remains **unverified on-device**.
- Files in ChatGPT Library are not GitHub Releases assets, and ChatGPT's large download links may fail on iPhone.

## Direct GitHub delivery using the original IPA on your iPhone

You can create the complete patched IPA on GitHub without downloading the 304 MB file from ChatGPT.

1. On your iPhone, locate your original `X_12.44_AdFiltered(1).ipa` in the Files app.
2. Open `https://github.com/soum91/Xexperiment/releases/new` in Safari and, if necessary, choose **Request Desktop Website**.
3. Enter the tag **`source-12.44`**, and use **Source IPA - build input** as the release title.
4. Under **Attach binaries**, select your original 12.44 IPA in Files, and allow it to finish uploading.
5. Publish the release. The `Build and publish patched X 12.44 IPA` GitHub Actions workflow downloads that release asset, applies the compiled web-login components, validates the complete IPA, and uploads it to another release.
6. After successful completion, download the **single full IPA** from `https://github.com/soum91/Xexperiment/releases/tag/v12.44-b22`. The workflow also refreshes FlareStore automatically.

**Do not upload the 5 MB repair ZIP as source.** The workflow expects exactly one full X 12.44 IPA attached to the `source-12.44` release.

## FlareStore source URL

`https://raw.githubusercontent.com/soum91/Xexperiment/main/repo.json`

The feed only advertises real published IPA assets. It never invents links to files that are not yet uploaded.

## Caveats

The generated IPA preserves the source app executable, bundle identifier, version 12.44/build 22, and original keychain fix. It replaces three embedded tweak components. The package is **not signed**; use FlareStore to sign and install. A passing ZIP integrity test does not prove that the iPhone's login flow will work.

Publishing a full proprietary application IPA publicly may implicate the app copyright holder's rights. Only upload binaries you have authorization to redistribute. For personal testing without public distribution, use a private repository or local re-signing workflow.

## Project rules
- Maintain `CHANGELOG.md` and `AGENTS.md`.
- Publish only real IPA release assets, not placeholder release links.
- Never commit account cookies, auth headers, personal access tokens, or passwords.
