# -*- coding: utf-8 -*-
name        = "x265"
version     = "3.5"
authors     = ["M83"]
description = "x265 HEVC encoder library – for FFmpeg"

build_requires = [
    "gcc-11.5.0",      # 플랫폼 표준 GCC
    "cmake-3.26.5",    # CMake 기반 빌드
    "ninja-1.11.1",    # 빠른 빌드 백엔드
    "python-3.13.2",   # rezbuild.py 실행용
]

# install 단계에서 rezbuild.py를 호출
build_command = "python {root}/rezbuild.py install"

def commands():
    # 빌드/런타임에 x264 바이너리·라이브러리가 올라가도록
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

