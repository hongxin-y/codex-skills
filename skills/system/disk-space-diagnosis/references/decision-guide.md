# Windows Disk Decision Guide

Use this reference only when a scan needs purpose attribution or a fallback optimization plan. It is a heuristic guide, not proof of ownership or permission to delete.

## Common categories

| Signal | Likely purpose | Default handling | Important caveat |
|---|---|---|---|
| `AppData\\Local\\Temp`, browser cache, shader cache, thumbnail cache | Regenerable temporary data | Review; clean with owning app or Windows tool | Some files may be in use; cleanup can cause re-download or slower first launch |
| `AppData\\Local\\Packages` | Microsoft Store app data | Use app reset/storage controls | May include user settings or offline content |
| `AppData\\Roaming` chat/profile folders | Per-user settings, chat databases, attachments, app data | Use in-app storage/export/backup controls | Do not delete the whole vendor folder; local chat/media can be user data |
| `Downloads`, Desktop, Documents, media, archives | User-created or downloaded data | User review, archive, or move using supported settings | Potentially irreversible and often not reproducible |
| `.cache`, package-manager caches, `go-build`, compiler/build caches | Developer tool cache/artifacts | Use the tool's cache-clean command or review contents | Active environments may need packages rebuilt or re-downloaded |
| game cache folders and launcher downloads | Game assets, shader/cache files, patches, saves | Use launcher/game storage controls; verify saves separately | A folder can mix disposable cache with saves or installed content |
| `ProgramData` vendor update/download/cache folders | Shared updater payloads or application data | Vendor cleanup/uninstaller; review update records | May be recreated; do not infer that every executable is stale |
| `Windows\\SoftwareDistribution\\Download` | Windows Update download cache | Windows Update/Disk Cleanup/Storage settings | Do not manually delete while updates are active |
| `Windows\\Installer`, `WinSxS`, `System32` | Windows/component/software servicing | Supported Windows servicing or uninstall workflow only | Direct deletion can break repair, update, boot, or uninstall |
| `pagefile.sys`, `hiberfil.sys`, `swapfile.sys` | Virtual memory, hibernation/fast startup, swap | Windows system settings only | Automatic sizing/location/state changes are high risk and confirmation-required |
| crash dumps, restore points, shadow copies | Diagnostics and rollback | Windows cleanup/system protection controls | Deleting reduces recovery/debugging capability |
| VM/container images, WSL distributions, emulator data | Virtualized operating systems or disks | Tool-specific export/remove/relocate workflow | Can contain an entire environment; treat as user data |

## Decision order

1. If it is clearly user data or an application-owned database, recommend review/backup and an app-supported workflow, not direct deletion.
2. If it is a regenerable cache or stale download with clear ownership and no active process, it can be a cleanup candidate, but state what will be regenerated or re-downloaded and still ask for exact-target confirmation before mutation.
3. If it is system-managed, automatically sized, shared by multiple accounts, or required for servicing/recovery, label it high risk and require explicit confirmation plus the supported settings path.
4. If ownership or purpose is uncertain, do not recommend deletion. Gather more metadata or present it as unknown.

## Fallback optimization logic

When the largest item is protected or required, do not stop at that finding. Build a ranked set of alternatives: low-risk regenerable caches and stale update/download payloads first; application-supported retention reduction, archive, or relocation next; uninstall unused software/games and orphaned SDKs or environments next; system allocation changes last, always marked high risk and confirmation-required.

For each alternative report one-time reclaimable range, expected recurring growth reduction, what may be lost or re-downloaded, required app closure/elevation/reboot, and whether the action is reversible. Never add estimates across overlapping parent and child paths.
