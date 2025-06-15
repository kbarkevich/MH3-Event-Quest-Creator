# MH3-Event-Quest-Creator
SpyRo's Monster Hunter Tri Event Quest Creator

This software may be used for the creation and editing of custom quests for Monster Hunter Tri. It is capable of creating new Event Quests and Arena Quests compatible with the [MH3SP](https://discord.gg/E9pbeYRYmd) private server software. This is the tool that is used to keep that server's rotating event and arena quests up-to-date.

## Where can I download it?

The [releases](https://github.com/kbarkevich/MH3-Event-Quest-Creator/releases) page contains download links for each version. Under your selected version, the pre-compiled .exe is available under **Assets**.

If you would like to run this software from source, download the code from this GitHub page and run `quest_creator.py` with a Python 3 installation

## How do I use it?

Much of the software is self-explanatory, with the more complex options having explanation-filled tooltips that you may access by mousing over the field names.

### Importing/Loading Quests

This software comes pre-filled with data for the online Event Quest _Jump Four Jaggi_. You may use this as a template to build off of, if you wish. If you would like to build off of an existing Event Quest, download the relevant .json file(s) from the MH3SP github page (the page with the most up-to-date Event and Arena Quest .jsons [may currently be found here](https://github.com/kbarkevich/MH3SP/tree/event-quest-rotation-full/event)) and load it with the `Load Json` button at the bottom of the software window. If you would like to view/edit/build off of the offline/online quests contained within the game, you may extract a quest file (such as _quest00_eng.bin_ or _quest01_eng.bin_) from your ripped Monster Hunter Tri ISO and load it with the `Load Game Binary` button. Once a binary file is selected this way, a menu will appear that will allow you to load any quest contained within the binary.

As these binary files are proprietary to Capcom, we may not redistribute it.

### Exporting/Saving Quests

If you would like to save your quest data to the .json format recognized by the MH3SP server, press the `Save` button at the bottom of the software window. These quests may be loaded back up for further editing at any time using the `Load Json` option. Save these `.json` files to the `events/` directory of your MH3SP server (and edit the `events/quest_rotation.json` file to include their filenames) to see them in your private server!

You may also use this software to export your quest to an offline/online quest slot contained within one of the quest binaries. This function is highly experimental, and may break your game. Use with caution. It may be accessed via the `Overwrite Game Binary` button at the bottom of the software window.

Additionally, this export-to-binary function will _not_ save over the quest's Small Monster data. Therefore, it is highly recommended that if you choose to overwrite the quest files within your binary, you only overwrite quests with quests that take place on the same map.

## Unknowns

The unknown fields under the **Unknowns** tab are as described -- values in the quest data for which we have no little-to-no knowledge of their purpose. If you would like to experiment and help is figure out what (if anything) these fields do, it would be very helpful! More knowledge of how the quest data works may lead to ever more interesting quests!
