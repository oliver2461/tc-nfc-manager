[app]

# (str) Title of your application
title = TC NFC Manager

# (str) Package name
package.name = tcnfcmanager

# (str) Package domain (unique, usually your reverse domain)
package.domain = org.oliver

# (str) Source code where your main.py is
source.dir = .

# (str) The main .py file to use
source.main = main.py

# (list) Application requirements
requirements = python3,kivy

# (str) Application versioning (shown in Android settings)
version = 0.1

# (int) Application version code (used internally by Android)
version.code = 1

# (str) Supported orientation (portrait, landscape, etc.)
orientation = portrait

# (list) Permissions your app needs (NFC and basic access)
android.permissions = INTERNET,NFC

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (str) Icon path (set your icon here)
icon.filename = %(source.dir)s/icon.png

# (list) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# (str) Android API to use
android.api = 33

# (str) Android NDK API minimum version
android.minapi = 21

# (str) Android SDK Build Tools version
android.build_tools_version = 33.0.2

# (bool) Copy library instead of using linker
android.copy_libs = 1

# (str) Bootstrap to use
bootstrap = sdl2

# (bool) Indicate if you want to use a custom Java class
android.ndk = 23b

# (list) Additional Java .jar files to add (optional)
android.sdk = 33

# (list) .so files to include (optional)
#android.add_libs = 

# (str) Path to Java class files (optional)
#android.java_src = 

# (str) Android entry point, default is org.kivy.android.PythonActivity
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Add Android AAR dependencies (optional)
#android.add_aars = 

# (bool) Enable Android logcat output in the terminal (for debugging)
log_level = 2

# (str) The format used to package the app (default is apk)
android.package_format = apk

# (bool) Rebuild the .apk every time, even if not changed
#android.force_build = 1

# (bool) If True, automatically accept SDK licenses
accept_sdk_license = True

# (str) Additional buildozer commands (optional)
# buildozer postcmd can go here

[buildozer]

# (str) Log file location
log_level = 2

# (str) Path to where .apk files will be placed
bin_dir = bin

# (str) Buildozer download cache (default is ~/.buildozer)
cache_dir = ~/.buildozer

# (bool) Use git if available to download packages
use_git = 1
