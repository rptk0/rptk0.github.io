import os
import subprocess
import gzip

# 已预置所有热门源
SOURCE_LIST = [
    "https://repo.chariz.io/",
    "https://repo.dynastic.co/",
    "https://opa334.github.io/",
    "https://ellekit.space/",
    "https://repo.initnil.com/",
    "https://roothide.github.io/",
    "https://repo.palera.in/",
    "https://34306.github.io/",
    "https://apt.thebigboss.org/repofiles/cydia/",
    "https://zhenpi.github.io/repo/",
    "https://niceios.github.io/repo/",
    "https://filzarepo.github.io/",
    "https://trollstore.github.io/repo/",
    "https://bangongyuan.github.io/repo/"
]

def main():
    # 创建必要目录
    os.makedirs("debs", exist_ok=True)
    os.makedirs("debs/rootless", exist_ok=True)
    os.makedirs("debs/roothide", exist_ok=True)
    os.makedirs("debs/trollstore", exist_ok=True)
    os.makedirs("icons", exist_ok=True)

    # 生成基础 Packages 文件（即使没有插件也能让源被识别）
    packages_path = "debs/Packages"
    with open(packages_path, "w", encoding="utf-8") as f:
        f.write("""Package: com.rptk0.placeholder
Name: Rptk0 私人聚合源
Version: 1.0
Architecture: iphoneos-arm64, iphoneos-arm64e
Section: Utilities
Description: 自动聚合无根/隐根/巨魔热门插件
Author: rptk0
Maintainer: rptk0
""")

    # 压缩 Packages.gz
    with open(packages_path, "rb") as f_in:
        with gzip.open("debs/Packages.gz", "wb") as f_out:
            f_out.writelines(f_in)

if __name__ == "__main__":
    main()
