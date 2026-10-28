# EverSage

Native Android offline preview, version 0.3.0. Open this repository folder in Android Studio and let Gradle sync. Install Android SDK 35 and use JDK 17 or a compatible Android Studio bundled JDK. Android 8.0 or newer is required.

## Contents

- `app/`: active native Android Java source, manifest, resources, compressed artwork, and bundled episode data.
- `apk/`: the existing signed preview APK, hash, signature report, and build report.
- `artwork/` and `branding/`: PNG master artwork and approved logo.
- `design-reference/`: existing UI concept images; these are reference designs, not a claim that every pictured screen is implemented.
- `knowledge/episodes/`: readable per-tradition episode text.
- `legacy/`: earlier web implementation and text content for reference only; excluded from the native Android build.
- `tools/`: original content-generation scripts. These retain their original workspace output assumptions; use the bundled data directly for normal app builds.

## Build

Open the root folder in Android Studio, sync, and choose Build APK(s). Alternatively, with Gradle 8.9 installed, run `gradle :app:assembleDebug`. No Gradle wrapper binary is bundled. A new build uses your local debug key; uninstall the supplied preview before installing a differently signed build. Signing keys and credentials are deliberately excluded. The Gradle project layout is newly prepared for portability; it has not been Gradle-built here. The included APK was built using the Android command-line compiler tools.

## Current scope and limitations

The included APK uses native Android Views, not a WebView. It bundles 57 episodes across 23 tradition groups and uses rule-based offline matching, not a generative model. Some selected traditions and situations have no close match. This preview does not yet meet the intended comprehensive knowledge coverage. The native APK passed compilation, signature, archive, and seven classifier checks, but has not been runtime-tested on a phone or emulator. The artwork and design references may exceed the currently implemented UI.

Source references and retellings are included in the data. No claim of exhaustive scripture coverage or blanket commercial rights clearance is made. Review edition-specific source rights before publishing. No new license grant is implied by this archive.

No chat conversations, chat exports, signing keys, credentials, SDKs, OCR packages, caches, or original PDFs are included.
