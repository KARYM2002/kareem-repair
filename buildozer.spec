[app]

# (str) Title of your application
title = Kareem Repair

# (str) Package name
package.name = kareemrepair

# (str) Package domain (needed for android packaging)
package.domain = com.kareem.repair

# (str) Source files where the include files are located
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Note: Removed heavy libraries like pillow temporarily to ensure smooth compilation
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) List of target architectures
android.archs = arm64-v8a

# (int) Android API to use
android.api = 31

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK build tools version
android.build_tools_version = 33.0.0

# (bool) Automatically accept Android SDK licenses
android.accept_sdk_license = True
