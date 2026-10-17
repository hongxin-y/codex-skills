---
name: disk-space-diagnosis
description: "Analyze Windows disk usage, explain what large items are used for, classify what can be cleaned and how, and propose lower-risk optimization paths without deleting or changing anything by default. Use for requests to find why a drive is filling up or what can be safely cleaned."
---

# Disk Space Diagnosis

Analyze Windows storage pressure as a read-only investigation. The default deliverable is an evidence-based attribution report, not a cleanup operation.

## Safety and authorization

- Never delete, move, compress, resize, disable, or modify files, services, registry values, storage settings, or application data during diagnosis.
- Treat any automatic or dynamic allocation change as **high risk** and require a fresh, explicit user confirmation immediately before execution. This includes changing pagefile automatic management or size/location, hibernation or fast-startup state, system-restore/shadow-copy limits, storage quotas, virtual disks, and other system-managed allocations.
- A general request such as "clean up space" is not permission to mutate. Before any cleanup, identify exact paths, estimated reclaimable space, what may be lost, and whether an application or reboot is required; ask for confirmation of that exact action.
- Do not recommend direct deletion of system directories or system-managed files such as `Windows\Installer`, `WinSxS`, `pagefile.sys`, `hiberfil.sys`, or `swapfile.sys`. Prefer supported Windows settings, application cleanup, uninstallers, or vendor tools.
- Preserve user data and privacy. Do not open file contents unless needed to identify a file type; report paths, sizes, timestamps, and metadata only.

## Investigation workflow

1. Establish the target volume(s): capacity, used space, free space, and free percentage. If the user did not name a drive, ask or use the drive implicated by the complaint; do not scan unrelated volumes unnecessarily.
2. Measure top-level directories and large files with read-only filesystem queries. Exclude reparse points/junctions where possible to avoid double-counting; note inaccessible paths and scan limitations. Treat a scan as incomplete unless every target top-level directory has either a verified total or an explicitly recorded failure/timeout.
   - Use a two-pass scan for each target volume: first enumerate immediate children, then measure each child independently, recursively splitting unusually large or slow children. Do not rely on one monolithic recursive scan of the whole volume.
   - Maintain a coverage ledger containing every top-level path, measured size/status, elapsed time, and whether the result is complete. If a command times out, returns partial output, or is stopped by an execution limit, mark that path `incomplete` and continue with smaller subtrees until its material contribution is accounted for.
   - Reconcile measured child totals against the volume's used space before ranking findings. A large unexplained residual, or a directory omitted because it was slow, must be reported and investigated; never present a partial ranking as a complete disk diagnosis.
3. Attribute space by category:
   - user data: documents, downloads, media, game saves, project files;
   - application data: caches, logs, browser profiles, package stores, chat attachments;
   - developer/tooling data: package caches, build caches, virtual environments, container/VM images;
   - Windows maintenance: update downloads, temp files, installer caches, component store;
   - system-managed allocations: pagefile, hibernation file, crash dumps, restore points/shadow copies;
   - duplicated or stale installers, archives, backups, and game libraries.
4. For system-managed allocations, query configuration and actual usage separately. On Windows, use CIM/WMI classes such as `Win32_PageFileUsage`, `Win32_PageFileSetting`, and `Win32_ComputerSystem`; distinguish allocated size from current/peak use. Do not infer that a large allocation is currently consuming the same amount of active memory.
5. If the user has a prior scan, compare the same paths and report deltas. Distinguish true growth from measurement differences, junction double-counting, and files that were removed or moved.
6. Identify the purpose of every material finding, not just its size. Use path components, extensions, timestamps, known application ownership, read-only metadata, and (when available) installed-app or service associations. Do not claim a purpose with high confidence from a folder name alone; label it inferred or unknown when evidence is weak.
7. Classify each finding by content type (user data, application data, cache, log, installer/update payload, build/package cache, system file, or unknown), supported handling, reversibility, and risk. System-managed and automatic allocations are always **high risk / confirmation required**.
8. For each large item, explain why it may be large or growing, what functionality depends on it, what happens after cleanup, and the supported cleanup method. Prefer an application's own storage/cache controls, Windows Storage/Disk Cleanup, an uninstaller, or a vendor tool over manual deletion. Never turn "cache" into an unconditional delete recommendation: verify whether it contains downloads, offline data, thumbnails, shader caches, logs, or user-created content.
   - For `C:\Windows\Installer`, do not propose deleting `.msi`/`.msp` files or the directory. Inventory it only for attribution; reclaim space through Windows Settings or the owning application's uninstaller/repair workflow. There is no generic safe delete operation for this cache.
   - For `C:\Windows\WinSxS`, explain that Explorer size may include hard-linked files and that it is the component store. Use an elevated `DISM /Online /Cleanup-Image /AnalyzeComponentStore` for read-only analysis. Only after a fresh, explicit confirmation may a supported cleanup such as `DISM /Online /Cleanup-Image /StartComponentCleanup` or Windows Storage/Disk Cleanup be run; disclose that superseded update rollback options can be reduced. Never use direct deletion or recommend `/ResetBase` as routine cleanup.
   - For every material application-owned item, provide an actionable cleanup route, not just a classification. First identify the owning app and version when practical, then state one of: (a) exact in-app menu path and button/setting, (b) exact Windows Settings/app repair or uninstall path, (c) vendor-supported tool/command, or (d) a clearly labeled manual path when no supported UI control exists. If no in-app control is available, say so explicitly instead of inventing a menu.
   - Make the route operational: list prerequisites (finish/cancel updates, exit the app, elevation, reboot, or backup), the exact target scope, what will be regenerated or lost, and a verification step (before/after size, app launch, or update check). Distinguish “disable future downloads” from “delete already-downloaded data”; changing an auto-update setting does not imply existing payloads are removed.
   - When the UI is version-dependent or uncertain, verify against the installed app metadata and, when needed, current official vendor documentation. Record the observed version and label unverified alternatives as such. For vendor update caches (for example graphics-driver or launcher payloads), preserve state/registry folders and recommend the narrowest payload/cache subdirectory rather than deleting the whole framework.
9. If the largest items are not suitable for deletion, produce an optimization plan from the remaining candidates. Select a combination of actions by expected reclaimable space, risk, reversibility, and user impact; show the estimated total range and which items would need the user's confirmation. Include non-deletion options such as moving user libraries or game libraries using supported app settings, changing download/cache locations, uninstalling unused software, reducing retention, or adjusting system allocations. Moving or changing locations is a mutation and still requires exact-target confirmation.
10. Rank findings by likely reclaimable space, confidence, reversibility, and user impact. State when a folder is a cache that can regenerate, when it may contain user content, and when only an application or Windows-supported workflow should be used.

## Required cleanup guidance

For each candidate large enough to affect the user's decision, include a compact “how to clean” block alongside the diagnosis:

- `In-app`: exact navigation (for example `App → Settings → ...`), the control name, and whether it removes existing data or only changes retention/download behavior.
- `Windows/vendor`: exact supported path such as Windows Storage/Disk Cleanup, `Settings → Apps → Installed apps → ... → Advanced options → Repair/Reset`, an uninstaller, or a vendor utility. Explain the impact of Reset/uninstall before recommending it.
- `Manual fallback`: only when the first two routes are unavailable or insufficient. Give the exact folder/file scope, stop/close prerequisites, elevation requirement, and a post-cleanup verification. Never broaden a user-approved target from a subfolder to its parent.

If a candidate is not safe to clean, still give a useful next step (for example, identify the owning app, reduce retention, move the library through the app, or run a read-only analysis) and explain why direct deletion is unsuitable. Do not perform any mutation merely because these instructions describe it; obtain fresh confirmation for the exact action.

## Commands and collection guidance

Use PowerShell or equivalent read-only commands. Prefer `Get-PSDrive`, `Get-ChildItem`, `Measure-Object`, and CIM queries. Avoid broad recursive scans when a targeted scan is enough, and handle access-denied errors without retry loops. For large-file reports include full path, size in GB/MB, and last-write time. For folder totals, make the counting method clear and warn that protected or linked content may be omitted. Prefer bounded, per-subtree measurements over a single unbounded recursive walk. Record timeouts, access-denied paths, reparse-point exclusions, and any residual between the volume total and attributed folders; a timeout is a scan limitation, not evidence that the path is empty or small.

For purpose attribution, use read-only evidence where practical: file extensions and names, parent/child structure, last-write patterns, installed application metadata, service/process names, and Windows ownership signals. Do not execute unknown binaries, inspect private message contents, or assume that a vendor-named folder is disposable. Read [references/decision-guide.md](references/decision-guide.md) when interpreting common Windows/application paths or when the user asks for an optimization plan.

Useful Windows-specific checks include:

```powershell
Get-PSDrive -PSProvider FileSystem
Get-CimInstance Win32_PageFileUsage
Get-CimInstance Win32_PageFileSetting
Get-CimInstance Win32_ComputerSystem | Select-Object AutomaticManagedPagefile
```

These checks are diagnostic only. Any command that sets CIM properties, edits the registry, invokes cleanup, or removes files is a mutation and must not run until the user confirms the exact proposed change.

### Windows servicing directories

Use [references/decision-guide.md](references/decision-guide.md) for the detailed decision path when `Windows\Installer`, `WinSxS`, or update servicing files are material findings. Keep analysis and mutation separate: `AnalyzeComponentStore` is read-only; `StartComponentCleanup`, Storage/Disk Cleanup, uninstallers, and vendor tools change state and require confirmation immediately before execution.

## Report format

Lead with the result: total capacity, used/free space, and the main causes. Then provide a compact table with:

`Priority | Location | Size | What it is/does | Why it grew | Reclaimable estimate | Supported handling | Risk`

Include a brief `Coverage and limitations` note naming any unmeasured, timed-out, access-denied, or reparse-point paths and the residual space not yet attributed. Do not claim the largest causes or complete coverage until the slowest material top-level directories have been split and measured.

For every high-impact item, include a short explanation covering its dependency and likely consequence of cleanup. Do not merely repeat the path and size.

Separate:

- safe-to-review candidates (reversible caches or stale downloads, still requiring exact-target confirmation before deletion);
- application-owned data that must be cleaned inside the application or backed up first;
- system-managed or automatic allocations, explicitly labeled **high risk / confirmation required**;
- items that should not be touched directly.

If the biggest item is not a viable cleanup target, add a section named `Optimization when the biggest items stay` and list a practical combination of smaller candidates, supported relocation/retention options, estimated total savings, and the confirmation required for each mutation. Make clear which savings are one-time and which prevent future growth.

When proposing action, give an estimated reclaimable range rather than promising an exact result. If no mutation was authorized, explicitly say that nothing was changed. If a requested mutation cannot run because elevation or a reboot is required, report that as a blocker and provide the supported manual path.
