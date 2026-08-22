[app]
title = Mi Mini App
package.name = minimapp
package.domain = com.miniapp.leon

source.dir =.
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec

version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Configuración Android necesaria para que no falle en la nube
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
