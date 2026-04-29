import os
import requests
import subprocess
import gzip

# 你要同步的所有热门源（已帮你填好：真皮、Nice、Filza、搬运工、巨魔、无根/隐根源）
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
    # 创建分类目录
    os.makedirs("debs/rootless", exist_ok=True)
    os.makedirs("debs/roothide", exist_ok=True)
    os.makedirs("debs/trollstore", exist_ok=True)
    os.makedirs("icons", exist_ok=True)

    # 生成源索引
    subprocess.run(["apt-ftparchive", "packages", "debs"], capture_output=True)
    subprocess.run(["mv", "Packages", "debs/"])
    with open("debs/Packages", "rb") as f_in:
        with gzip.open("debs/Packages.gz", "wb") as f_out:
            f_out.writelines(f_in)

if __name__ == "__main__":
    main()
