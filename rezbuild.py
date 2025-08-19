# -*- coding: utf-8 -*-

import os
import sys
import shutil
import subprocess
import importlib.util

def run(cmd, cwd=None):
    print(f"[RUN] {cmd}")
    subprocess.run(cmd, shell=True, cwd=cwd, check=True)

def clean(path):
    if os.path.exists(path):
        print(f"[CLEAN] Removing {path}")
        shutil.rmtree(path, ignore_errors=True)

def get_pkg_info():
    # rezbuild.py 가 있는 디렉터리 기준으로 package.py 를 로드
    here = os.path.dirname(__file__)
    pkg_path = os.path.join(here, "package.py")
    spec = importlib.util.spec_from_file_location("pkg", pkg_path)
    pkg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pkg)
    return getattr(pkg, "name", "unknown"), getattr(pkg, "version", "unknown")

def build(source_path, build_path, targets):
    name, version = get_pkg_info()
    install_root = f"/core/Linux/APPZ/packages/{name}/{version}"

    # tarball/소스 디렉터리
    src_archive = f"x265_{version}.tar.gz"
    src_root    = os.path.join(source_path, "source", f"x265_{version}")
    cmake_dir   = os.path.join(src_root, "source", "build")

    # 소스 압축 파일 위치
    tarball = os.path.join(source_path, "source", src_archive)
    if not os.path.isfile(tarball):
        print(f"❌ 소스 tarball 없음: {tarball}")
        sys.exit(1)

    # install 단계라면 기존 설치 제거
    if "install" in targets:
        clean(install_root)

    # 기존 풀린 소스 제거 후 다시 추출
    clean(src_root)
    run(f"tar -xvf {src_archive}", cwd=os.path.join(source_path, "source"))

    # out-of-source CMake 빌드 디렉터리 준비
    os.makedirs(cmake_dir, exist_ok=True)

    # CMake Configure & Build
    cmake_cmd = (
        f"cmake .. "
        f"-DCMAKE_INSTALL_PREFIX={install_root} "
        "-DENABLE_SHARED=ON "
        "-DENABLE_CLI=OFF "
        "-DENABLE_PIC=ON"
    )
    run(cmake_cmd, cwd=cmake_dir)
    run("make -j$(nproc)", cwd=cmake_dir)

    # install & package.py 복사
    if "install" in targets:
        run("make install", cwd=cmake_dir)
        pkg_src = os.path.join(os.path.dirname(__file__), "package.py")
        pkg_dst = os.path.join(install_root, "package.py")
        print(f"📄 Copying package.py → {pkg_dst}")
        shutil.copy(pkg_src, pkg_dst)

    print(f"✅ {name} {version} build & install completed: {install_root}")

if __name__ == "__main__":
    build(
        source_path=os.environ["REZ_BUILD_SOURCE_PATH"],
        build_path =os.environ["REZ_BUILD_PATH"],
        targets    =sys.argv[1:]
    )

