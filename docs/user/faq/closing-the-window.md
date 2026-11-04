---
title: Does closing the window quit LightKub?
description: On a Mac, closing the LightKub window with the red button or ⌘W quits the app, after it checks for running tasks and unsaved changes.
order: 30
verified: 0.14.0
---

On a Mac, yes. Closing LightKub's main window quits the app, the same as **LightKub** > **Quit LightKub** (⌘Q). Many Mac apps keep running with no window open; LightKub doesn't.

These all do the same thing when the main window is the one in front:

- the red close button in the top-left corner of the window
- **File** > **Close Window** (⌘W)
- **LightKub** > **Quit LightKub** (⌘Q)

## Does it ask first?

Only when something would be lost:

- A task that can be stopped is still running, such as an import or an export. LightKub asks **Quit while tasks are running?** Choose **Cancel** to keep working, or **Quit Anyway** to stop the task and quit.
- Some changes couldn't be written to disk, for example because a drive was unplugged. LightKub tries to save them again, and if that still fails it asks **Quit with unsaved changes?** Choose **Cancel** to stay, **Try Saving Again** once the drive is back, or **Quit Anyway** to give up those changes.

With nothing running and everything saved, the window closes and LightKub quits at once. As the app quits, LightKub saves your settings and closes your library. If either save fails, the error goes to the log file and the app quits anyway.

The second window (**Window** > **Second Window**) is different: its red button, or ⌘W while it is in front, closes only that window, and LightKub keeps running.

## Can I keep LightKub open without a window?

No. To get the window out of the way, minimize it with the yellow button or **Window** > **Minimize** (⌘M), or hide the app with **LightKub** > **Hide LightKub** (⌘H). Both keep your place and any running task going.
