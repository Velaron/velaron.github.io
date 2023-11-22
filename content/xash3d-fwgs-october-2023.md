Title: Xash3D FWGS - November 2023
Date: 2023-11-22 12:00
Category: Xash3D FWGS
Summary: Catching up on what was going on with the engine until now (again).

While we want to do a stable release as soon as possible, there is still lots of stuff to do before we switch all our users to the new codebase.

### Consider Donating
[**a1batross**](https://github.com/a1batross)

Initial Xash3D SDL2/Linux port author, Xash3D FWGS engine maintainer, creator of non-commercial Flying With Gauss organization.

* Boosty page: <https://boosty.to/a1ba>

[**nekonomicon**](https://github.com/nekonomicon)

[hlsdk-portable](https://github.com/FWGS/hlsdk-portable), [mdldec](https://github.com/FWGS/xash3d-fwgs/tree/master/utils/mdldec), [opensource-mods.md](https://github.com/FWGS/xash3d-fwgs/blob/master/Documentation/opensource-mods.md) maintainer and Xash3D FWGS [contributor](https://github.com/FWGS/xash3d-fwgs/commits?author=nekonomicon) (*BSD/clang port, PNG support, etc).

* Boosty page: <https://boosty.to/nekonomicon>

[**Velaron**](https://github.com/Velaron)

[cs16-client](https://github.com/Velaron/cs16-client) & [tf15-client](<https://github.com/Velaron/tf15-client>) maintainer and Xash3D FWGS [contributor](<https://github.com/FWGS/xash3d-fwgs/commits?author=Velaron>) (Android port, voice chat, etc).

* Buy Me A Coffee page: <https://www.buymeacoffee.com/velaron>

[**SNMetamorph**](https://github.com/SNMetamorph)

[PrimeXT](https://github.com/SNMetamorph/PrimeXT) & [GoldSrc Monitor](https://github.com/SNMetamorph/goldsrc-monitor) maintainer and Xash3D FWGS [contributor](https://github.com/FWGS/xash3d-fwgs/commits?author=SNMetamorph) (Windows port, voice chat, etc).

* BTC: `16GAzK3qei5AwBW7sggXp3yNcFHBtdpxXj`
* ETH (ERC20): `0xb580eeca9756e3881f9d6d026e28db28eb72a383`
* USDT (ERC20): `0xb580eeca9756e3881f9d6d026e28db28eb72a383`
* USDC (ERC20): `0xb580eeca9756e3881f9d6d026e28db28eb72a383`

# Tasty New Stuff
##### by [**Flying With Gauss**](https://github.com/FWGS)
* Fix for streaming and other overlays (OBS, Discord, etc.)
* IPv6 support
* ID3v2 tags for .mp3 files
* Anti-speedhack protection
* Minidumps support for Windows
* Demo RCE exploits fixed
* Improved and faster filesystem for Linux
* Borderless fullscreen support
* VBO is back with bugfixes
* New GLES3Compat renderer
* PlayStation Vita port by [**fgsfds**](https://github.com/fgsfdsfgs)
* Cross-platform port of [**The Wastes**](https://git.mentality.rip/a1batross/halflife-thewastes-sdk) by [**a1batross**](https://github.com/a1batross)
* Nintendo Switch port by [**fgsfds**](https://github.com/fgsfdsfgs)
* MacOS port by [**sofakng**](https://github.com/sofakng)
* PlayStation Portable port by [**Crow_bar**](https://github.com/Crow_bar)

# .pk3dir support
##### by [**a1batross**](https://github.com/a1batross)
Xash3D FWGS now supports pk3dir convention. It first appeared in ioquake3, which then got supported in FTE and DarkPlaces.

What does it do? Well, if you're using PK3 and PAK archives, you may not waste your time on repacking the archive during development. Instead, you create a folder ".pk3dir" extension. Keeping the same directory hierarchy, as with PK3 and PAK, you can think of it as an archive. And engine will work with it, like it's an archive as well. Of course, it also gives you possibility to not spill over temporary assets and files onto game directory.

# Cross-platform video playback (WIP)
##### by [**a1batross**](https://github.com/a1batross)
Xash3D engine supported movie playback for a long time, but it utilizes Video for Windows API, which has downsides from obviously being closed source and Windows exclusive and requiring the user to install third-party software. It also sometimes just outright doesn't work for an unknown reason.

This time I have implemented video player using ffmpeg to the Xash3D FWGS engine, which actually was in the plan for a whopping eight years already.

The obvious improvement of using ffmpeg is a wide variety of codecs. It successfully worked with movie intros from Half-Life, Opposing Force and Paranoia mod.

But very VFW specific internal engine logic, bites me. Instead of normal playback, the engine tracks frames by itself and tries to seek over the movie stream. Seeking itself is harmless, but it makes playback very suboptimal, and some frames may be lost, which doesn't make the decoder happy. A random Bink file my friend found for me works, but it absolutely fails on VP9 streams, from refusing playing them at all or just showing random artifacts.

<div class="embed-responsive embed-responsive-16by9">
	<video class="embed-responsive-item" allowfullscreen controls>
		<source src="{static}/videos/valve.mp4" type="video/mp4" />
	</video>
</div>

# GoldSrc protocol / VGUI2 support (WIP)
Experimental support of GoldSrc protocol on [**goldsrc-proto**](https://github.com/FWGS/xash3d-fwgs/tree/goldsrc-proto) branch. Also progress being made on supporting VGUI2 on the [**new_vgui_support_api**](https://github.com/FWGS/xash3d-fwgs/tree/new_vgui_support_api) branch.

![Screenshot]({static}/images/goldsrc-proto-1.png)
![Screenshot]({static}/images/goldsrc-proto-2.png)

# FreeVGUI
##### by [**Flying With Gauss**](https://github.com/FWGS)
Announcing clean-er re-implementation of original Valve's GUI library from Half-Life 1 under the work title freevgui. I'm working on it since last year in my free time of free time of free time.

This implementation is intended to be used within Xash3D FWGS as a drop-in FOSS and cross-platform alternative to the proprietary vgui.dll library, but potentially can be used as a replacement in Half-Life mods as well, as it's both API and ABI compatible.

Unlike Nagist's implementation, this library specifically hasn't been derived from HLSDK code, and every line of code has been carefully restored from DWARF debug information and decompilation using Ghidra.

Source code will be published as soon as I finish implementing the controls library and when I decide on licensing. For now, it has dependency on 3-clause BSD licensed C++ templates library, and C utilities library from Xash3D FWGS which is GPLv2 licensed. I'll probably drop GPL dependency to allow it included in Half-Life mods as a bug fixed replacement of original vgui code, when it will have bug fixes in the first place.

# Half-Life 25th Anniversary
With Half-Life turning whole 25 years, Valve released an update to the game which we now support too (make sure to update your engine to the latest version). I would like to personally thank everyone who has been supporting the developers and Xash3D FWGS all these years, stay tuned for more updates and have fun!