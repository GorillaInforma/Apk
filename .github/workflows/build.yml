name: Build APK

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Instalar dependencias
        run: |
          sudo apt update
          sudo apt install -y openjdk-17-jdk zip unzip git python3-pip
          pip install Cython==0.29.33 buildozer

      - name: Compilar APK
        run: |
          buildozer -v android debug

      - name: Subir APK
        uses: actions/upload-artifact@v4
        with:
          name: mi-apk
          path: bin/*.apk
