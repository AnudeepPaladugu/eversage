# EverSage
### A quiet, offline guide to stories and wisdom across traditions

EverSage is a native Android prototype designed to help people explore short episodes of traditional stories and reflections. The current preview keeps its content bundled with the app and uses rule-based matching to suggest a relevant episode, without requiring a live AI service.

> **Project status:** Work in progress. The Android preview is available in the repository, while content coverage, runtime validation, and parts of the intended interface are still being refined.

## At a Glance

- **Platform:** Native Android
- **Language:** Java
- **Interface:** Android Views
- **Content model:** Bundled episode data and rule-based offline matching
- **Preview version:** 0.3.0
- **Minimum Android version:** Android 8.0 (API 26)
- **Build target:** Android SDK 35

## Current Preview

The bundled preview contains **57 episodes across 23 tradition groups**. It is intended as an early exploration experience, not an exhaustive reference library.

The matching logic works offline and relies on the included knowledge data. It is not a generative model, and some traditions or situations may not yet have a close match.

## Repository Guide

| Path | Purpose |
|---|---|
| `app/` | Active native Android Java source, manifest, resources, artwork, and bundled episode data |
| `apk/` | Existing signed preview APK and its supporting reports |
| `artwork/` and `branding/` | Artwork masters and approved brand assets |
| `design-reference/` | UI concept references; these do not guarantee every pictured screen is implemented |
| `knowledge/episodes/` | Readable episode text grouped by tradition |
| `legacy/` | Earlier web implementation and text retained for reference, not included in the native Android build |
| `tools/` | Content-generation scripts used during preparation of the bundled data |

## Build Locally

### Requirements
- Android Studio
- Android SDK 35
- JDK 17, or a compatible JDK bundled with Android Studio
- Gradle 8.9 installed separately if building from the command line

### Open in Android Studio

1. Clone or download this repository.
2. Open the repository root in Android Studio.
3. Allow Gradle sync to complete.
4. Select **Build APK(s)** from the Build menu.

### Command line

```bash
gradle :app:assembleDebug
```

A Gradle wrapper is not bundled. A locally built APK uses your local debug signing key. The supplied preview may have a different signature, so uninstall it before installing a newly built APK if Android reports a signature conflict.

## Validation Notes

The repository's existing preview passed compilation, signature, archive, and seven classifier checks at the time it was prepared. It has **not yet been runtime-tested on a phone or emulator**, and the checked-in Gradle project has not been independently built with the documented Gradle command in this workspace.

The concept artwork may also show screens or details that are not present in the current implementation. Treat the APK as a development preview.

## Roadmap

- [ ] Run the app on multiple Android devices and emulator configurations.
- [ ] Improve offline matching for traditions, themes, and user situations.
- [ ] Expand and review the episode library with clear source references.
- [ ] Bring the implemented UI closer to the design references.
- [ ] Add tests for content matching, empty results, and invalid or missing data.
- [ ] Review accessibility, text scaling, and navigation behavior.
- [ ] Complete edition-specific source-rights review before public or commercial distribution.

## Content and Usage

Episode texts include source references and retellings. EverSage does not claim exhaustive coverage of any scripture or tradition, and inclusion does not imply blanket commercial rights clearance. Review source editions, translations, and applicable rights before publication.

Signing keys, credentials, SDKs, OCR packages, caches, original PDFs, and conversation exports are intentionally excluded from this repository.

---

Built as an independent Android learning project by **Anudeep Paladugu**.
