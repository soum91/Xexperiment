# Xexperiment

Experimental X for iOS repackaging and FlareStore feed.

## Status

- Target app: X 12.44, build 22 (`com.atebits.Tweetie2`), iOS 15+
- Local patched IPA: built and ZIP-verified, **not yet uploaded to GitHub Releases**.
- Native authenticated login, ad filtering, and device compatibility have **not** been verified on an iPhone.
- GitHub Releases is the intended binary distribution channel; never put large IPAs in the Git tree.

## FlareStore source

```
https://raw.githubusercontent.com/soum91/Xexperiment/main/repo.json
```

The feed is intentionally empty until an actual `.ipa` release asset exists. This avoids broken installation links.

## Publish the existing patched IPA

1. From a computer, obtain the full patched IPA (`X_12.44_AdFiltered_WebLogin_NFB731.ipa`) from the ChatGPT file Library.
2. Open **GitHub → Xexperiment → Releases → Draft a new release**.
3. Create tag `v12.44-b22` and title `X 12.44 experimental web login`. Keep **Set as a pre-release** checked.
4. Attach the complete **IPA file**, not the 5 MB repair ZIP. Wait for the 304 MB file to finish uploading.
5. Click **Publish release**. The FlareStore-feed workflow reads the real released IPA asset and updates `repo.json`.
6. If you attach assets *after* publishing, manually run **Actions → Refresh FlareStore feed → Run workflow**.

Do not put authentication cookies, passwords, bearer tokens, or other credentials in any release files or bug reports.

## Integrity

The IPA that was built locally is 304,332,783 bytes (291 MiB). Installation requires re-signing with your existing iOS sideloading solution. Structural ZIP verification is **not** a substitute for live sign-in testing.

## Release rules

All future versions must include changelog notes, a unique tag, the updated on-device version/build when the executable version changes, and an actual downloadable GitHub Release IPA asset before being indexed in FlareStore.
