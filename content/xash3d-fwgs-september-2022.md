Title: Xash3D FWGS - September 2022
Date: 2022-09-23 20:00
Category: Xash3D FWGS
Summary: Catching up on what was going on with the engine until now.

As you may have noticed, we often refer to the engine as "old engine", that's because for a while now we have been moving onto a new codebase, refactoring and adding features along, such as much requested **voice chat**.

# The "Small" Stuff
##### by [**Flying With Gauss**](https://github.com/FWGS)
**Better network prediction and overall multiplayer improvements.**  
I mean it, much better, playing multiplayer now sometimes feels like better than on GoldSrc, but it still needs some work.

**Implementation of Unkle Mike's extended studiomodel format.**  
Bone weights, inverse kinematics, procedural bones and other stuff for mod developers.

**Enhanced compatibility with GoldSrc.**  
Support for original Half-Life game saves and compatibility fixes.

**New map format.**  
Implementation of an extended map format made on top of original Half-Life's BSP30 (per-vertex lighting, extended clipnodes, etc). BSP31 is now obsolete.

**Customization support.**  
Finally you can change your spray and more, with in-game downloads support!

RefAPI for multiple rendering API support. (#31)
OpenGL renderer split from engine to ref_gl library. (#31)
Software renderer implementation. Incomplete, but playable. repo
Improved platform backend system that allows better portability across different systems.
Extension on library naming, that allows mod developers to distribute libraries for different operating systems and architectures in same archive. (doc)
Changed ABI for Android ports: removed hardfp support, AArch64 is now mandatory. (#90)
New library for common code: libpublic, that holds custom Xash3D's CRT, math and hashing functions.
New touch control: _wheel. Works like a mouse wheel.
Temporary support for legacy 48 protocol.
Restored Half-Life: Blue Shift maps support that were removed by Unkle Mike.
Restored On-Screen Keyboard implementation for ports that don't have normal hw or sw keyboards.
Support of AArch64, MIPS, Elbrus CPU architectures.
Support of MotoMAGX platform.
Support for systems with limited system memory. Allows to run complete engine on 32 megabytes of RAM. (#83)
Support for embedded Linux, i.e. using evdev, fbdev and alsa directly instead of SDL2. (#83)
Support for legacy SDL1.2.
Support for compressed ZIP/PK3 archives. (#41)
Support for reading and writing PNG. (#48)
Some behavior changes to match GoldSrc.
Fixes for different UB and preventing them to be compiled.
Linux client builds are now distributed as AppImages for i686 and x86_64 and dedicated builds as just semi-static binary.
Android builds now has special mod hacks, that allows to play some simple mods so special launchers aren't required. list
Android builds also now has GLES1 and GLES2 renderers enabled. Choose from game menu or by passing -ref gles1 or -ref gles2 to engine command line.
Android version now has new adaptive icon inspired by updated Valve's design. :)
Clean of unused code and macros we got from Old Engine to New Engine transition.
Drop of OSX/iOS support (#61)
CMake, Makefile and Android.mk are removed and replaced by Waf build system.
Started to publish documentation on FWGS extensions, engine porting guide and ports maintainers list.
What's next? We will working on improving stability and compatibility at first but we also have a lot of ideas that may be implemented to the next version. Follow our issue tracker and repository commits to keep up with the latest news. Although we consider this release as first stable and it really is for Linux, BSD and Windows, Android builds may still be a bit unstable. Bugreports are welcome!
Have questions? You can contact FWGS on our Discord server: http://discord.fwgs.ru.

# New Android Port
##### by [**Velaron**](https://github.com/Velaron)
We moved to SDL2 as our backend, it used to suck back then, but right now our implementation seems to suck more. You know what also sucks? Google with their OS. They keep being so paranoid about user's "security", we need to do a lot of work just to make this thing running. Right now we need to write a new frontend and finish up on fixing bugs before releasing a stable build, but it's coming better than ever.

# Voice Chat
##### by [**a1batross**](https://github.com/a1batross), [**SNMetamorph**](https://github.com/SNMetamorph) and [**Velaron**](https://github.com/Velaron)
ass

# filesystem_stdio Implementation
##### by [**a1batross**](https://github.com/a1batross)
Engine's filesystem was moved into a separate module, which also implements support for Valve's interface allowing to run more mods and clean up the codebase.

# mod hacks
```c
MOD_VALVE,		// Half-Life
MOD_AOM,		// Afraid of Monsters
MOD_BIGLOLLY,	// Big Lolly
MOD_BSHIFT,		// Half-Life: Blue Shift
MOD_HALFSECRET,	// Half-Secret
MOD_HEVSUIT,	// Case Closed, Bloody Pizza: Vendetta, Borderlands
MOD_INDUCTION,	// Half-Life: Induction
MOD_REDEMPT,	// Redemption/Absolute Redemption
MOD_SEWER_BETA,	// Sewer Beta
MOD_TOT,		// Times of Troubles
MOD_URBICIDE	// Half-Life: Urbicide
```