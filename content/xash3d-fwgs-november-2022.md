Title: Xash3D FWGS - November 2022
Date: 2022-12-01 20:00
Category: Xash3D FWGS
Summary: Catching up on what was going on with the engine until now.

As you may have noticed, we often refer to the engine as "old engine", that's because for a while now we have been moving onto a new codebase, refactoring and adding features along, such as much requested **voice chat**.

# What Is Coming?
##### by [**Flying With Gauss**](https://github.com/FWGS)
**Better network prediction and overall multiplayer improvements.**  
I mean it, much better, playing multiplayer now sometimes feels like better than on GoldSrc, but it still needs some work.

**Enhanced compatibility with GoldSrc.**  
Support for original Half-Life game saves and compatibility fixes.

**The "small" stuff:**  

* Implementation of an extended map format made on top of original Half-Life's BSP30 (per-vertex lighting, extended clipnodes, etc.), BSP31 is now obsolete.
* Implementation of Unkle Mike's extended studiomodel format: bone weights, inverse kinematics, procedural bones and other stuff for mod developers.
* RefAPI for multiple rendering APIs support: OpenGL renderer split from engine and a basic Software renderer implementation.
* Improved platform backend system that allows better portability across different systems.
* Extension on library naming, that allows mod developers to distribute libraries for different operating systems and architectures in the same archive.
* New library for common code: libpublic, that holds custom Xash3D's CRT, math and hashing functions.
* New touch control: *_wheel*, works like a mouse wheel.
* Temporary support for legacy 48 protocol.
* Restored On-Screen Keyboard implementation for ports that don't have normal HW or SW keyboards.
* Support of AArch64, MIPS, Elbrus and Risc-V CPU architectures.
* SerenityOS support.
<div class="embed-responsive embed-responsive-16by9">
	<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/_sRkKZQPpO4" title="Half-Life running on SerenityOS" allowfullscreen />
</div>
* Support of MotoMAGX platform.
* Support for systems with limited system memory. Allows to run complete engine on 32 megabytes of RAM.
* Support for embedded Linux, i.e. using evdev, fbdev and alsa directly instead of SDL2.
* Support for legacy SDL1.2.
* Support for compressed ZIP/PK3 archives.
* Non-dedicated Linux builds are now distributed as AppImages for i686 and x86_64 platforms.
* Ongoing work on documentation of FWGS extensions, engine porting guide and ports maintainers list.

# Voice Chat
##### by [**a1batross**](https://github.com/a1batross), [**SNMetamorph**](https://github.com/SNMetamorph) and [**Velaron**](https://github.com/Velaron)
Voice chat support is finally coming to all platforms, as requested by many for years.

# Customization support
##### by **Uncle Mike**
Finally you can change your spray and more, with in-game downloads support!
<div class="embed-responsive embed-responsive-16by9">
	<video class="embed-responsive-item" allowfullscreen controls>
		<source src="{static}/videos/waltuh.mp4" type="video/mp4" />
	</video>
</div>

# New Android Port
##### by [**Velaron**](https://github.com/Velaron)
We moved to SDL2 as our backend, it used to suck back then, but right now our implementation seems to suck more. You know what also sucks? Google with their OS. They keep being so paranoid about user's "security", we need to do a lot of work just to make this thing running. Right now we need to write a new frontend and finish up on fixing bugs before releasing a stable build, but it's coming better than ever.

* Android builds have GLES1 and GLES2 renderers enabled, choose from game menu or by passing `-ref gles1` or `-ref gles2` to the command line.
* Android builds also have special mod hacks, allowing you to play some mods without any additional launchers.

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

# filesystem_stdio Implementation
##### by [**a1batross**](https://github.com/a1batross)
Engine's filesystem was moved into a separate module, which also implements support for Valve's interface allowing to run more mods and clean up the codebase.

# Drop of OSX/iOS support
##### by [**Flying With Gauss**](https://github.com/FWGS)
Sadly we had to drop Apple devices support, simply because we don't and probably not going to own any of them and they keep removing essential features from the OS (see [issue #61](https://github.com/FWGS/xash3d-fwgs/issues/61)). If you own any of these devices and are willing to maintain the engine for them, you are welcome!


# PNG support
##### by [**nekonomicon**](https://github.com/nekonomicon)
Engine supports reading and writing PNGs now, so you can use an accessible format for your touch buttons and more. Due to conversion of touch button graphics, you may need to reset your touch configuration if you are missing some textures.

# Half-Life SDK (hlsdk-portable) fixes and additions
##### by [**nekonomicon**](https://github.com/nekonomicon)
* FIXED: RPG laser visible when using func_tank.
* ADDED: cl_autowepswitch CVar, allows you to change automatic weapon switch behavior when picking them up.
* FIXED: MP5 spread being switched between singleplayer and multiplayer.
* FIXED: Bullsquid's spit crashing the game.
* Исправлено поведение гонарча при ожидании у ноды.
* FIXED: numerous problems around playing scripted sequences.
* FIXED: most cases of FPS-dependent entity behaviour.
* FIXED: incorrect SF_MONSTER_GAG flag check.
* При застревании монстров в стене светящие желтые точки теперь появляются только при включеном режиме разработчика
* Более плавные анимации удара, стрельбы, перезарядки и смены оружия.
* FIXED: Tau Cannon's beam has invalid color.
* FIXED: reload animations playing twice sometimes.
* Исправлен баг с извлечением патронов из MP5, когда запас подствольных гранат полон.
* Добавлен опущенный прекэш звуков для стационарных автоматических туррелей.
* Испрален возможный вылет во время плевка гонарча если значение квара sv_gravity равно нулю.
* Исправлено отображение локальной модели игрока от третьего лица.
* Исправлен возможный вылет при отправке сообщения о смерти игрока в мультиплеере.
* Ученыe теперь реагируют на запахи.
* Исправлено воспроизведение звуков дыхания под водой, когда игрок не полностью погружен в воду.
* Исправлен цвет луча глюонной пушки.
* Улучшено поведение монстров в стае/отряде.
* Исправлен цвет звуковой волны для хаундаев в стае из 5 хаундаев.
* В мультиплеере теперь форсирован вид от первого лица.
* Изменено положение камеры в режиме вида от третьего лица.
* Добавлен квар explosionfix, отключающий урон взрывной волны за стенами.
* При попадании в левую половину osprey теперь дымится левое крыло, при попадании в правую* правое, а не наоборот.
* Исправлен непрерывающийся в некоторых случаях звук тау-пушки.
* Исправлен непрерывающийся в некоторых случаях звук открытия дверей.
* Добавлен квар corpsephysics, для изменения физики падения трупов.
* Исправлена неверная бодимодель вьюмодели трипмины при первом подборе.
* Исправлен поворот контроллеров лицом к worldspawn во время idle-анимации.
* Исправлены возможные зависания на лестницах, например в моде Half-Life: Sum.
* Исправлена громкость голосов ученых с разными головами.
* FIXED: sleeping Houndeyes now close their eyes.
* Исправлено застревание и возможный вылет если запрыгнуть на башню танка, например на карте c2a5b.