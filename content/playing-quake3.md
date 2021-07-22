Title: Playing Quake III Arena on a modern system
Date: 2021-03-16 20:00
Summary: If you decided you don't want to give Quake Live a go, which is honestly a better choice for playing online, you can still do some things to run Quake III: Arena more comfortably. 

If you decided you don't want to give [Quake Live](https://store.steampowered.com/app/282440/Quake_Live/) a go, which is honestly a better choice for playing online, you can still do some things to run Quake III: Arena more comfortably.

![Quake III Logo]({static}/images/quake-iii-logo.png)

# First of all, you need to get Quake III
You can get it on [Steam](https://store.steampowered.com/app/2200/Quake_III_Arena/), [GOG](https://www.gog.com/game/quake_iii_gold) or any other platform of choice. Both versions come with the **Team Arena** expansion. All you need is the **baseq3** and **expansionpack** folders from the game's folder.

# Download ioquake3
[ioquake3](https://ioquake3.org/) is a modern source-port based on the original source code with improvements and cross-platform capabilities. At the moment, the website is broken after a migration and the downloads don't work, direct links to the builds can be found below:

* [Linux](https://github.com/ioquake/ioq3/suites/3288039970/artifacts/76728853)
* [Windows](https://github.com/ioquake/ioq3/suites/3288039970/artifacts/76728855)
* [macOS](https://github.com/ioquake/ioq3/suites/3288039970/artifacts/76728854)

*Update: the download page seems to work now, but I will leave these just in case.*

Inside the archive, you will find another archive, contents of which you have to put inside your Quake III installation folder.

# Creating a config
Easiest way to configure the game is creating an **autoexec.cfg** file inside **baseq3** folder. Copy the following contents into the file:
```text
r_mode -2 // automatically selects your native resolution
com_maxfps 125 // explanation: https://www.youtube.com/watch?v=P13KmJBNn1c
com_hunkmegs 128 // even Team Arena crashes if you don't increase this
r_fullscreen 1
```

# Recommended mods
[High Quality Quake](https://www.moddb.com/mods/high-quality-quake) - for HQ icons and fonts.  
[Flexible HUD](https://clover.moe/flexible-hud-for-ioq3/) - widescreen HUD support.

# Finishing up
Now you can run the **ioquake** executable and enjoy the game!