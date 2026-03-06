from pathlib import Path
import json
from time import sleep
import argparse
from lib__1 import Mc_mod_migration

def loop__(cache,version,loader,classer,i):
    count = 0
    f: dict = {}
    try:
        with open(f'{cache}/cache.json', "r", encoding="UTF-8") as F:
            f = json.load(F)
            F.close()
        if f[version] == None:
            f[version] = {
                "fabric": {
                    "done_mods_name": [], "failed_mods_name": []
                },
                "forge": {
                    "done_mods_name": [], "failed_mods_name": []
                }
            }
    except:
        f[version] = {
            "fabric": {
                "done_mods_name": [], "failed_mods_name": []
            },
            "forge": {
                "done_mods_name": [], "failed_mods_name": []
            }
        }
    for x in range(0, len(classer.modname)):
        if classer.modname[x].split("/")[-1] in f[version][loader]["done_mods_name"]:
            print(classer.modname[x].split("/")[-1], "is Completed Already,Skipped......")
            continue
        mod_version, name, url, mod_id = classer.get_mod_download_url(x, loader, version).split(",")
        done_downloading = classer.download_mod(url, name.replace(" ", "-"), f"{cache}/{version}/{loader}")
        if done_downloading:
            f[version][loader]["done_mods_name"].append(classer.modname[x].split("/")[-1])
        else:
            f[version][loader]["failed_mods_name"].append(classer.modname[x].split("/")[-1])
        count += 1
        if count == 4:
            with open(f'{cache}/cache.json', "w", encoding="UTF-8") as F:
                json.dump(f, F, indent=4, ensure_ascii=False)
                F.close()
            count = 0
        sleep(i)
    print("job accomplished,Browser {}/cache.json for more Detail....".format(cache))

def init__():
    parser = argparse.ArgumentParser(description="This is a pyinstaller Program doing Favor for Minecraft gamers who want to Migrant their game version Smoothly and Automatically by any chance ")
    parser.add_argument("-s", help="To The Folder of Source mods")
    parser.add_argument("-o", help="To where New mods will be cached")
    parser.add_argument("-v", help="New game version")
    parser.add_argument("-l", help="fabric or forge loader")
    parser.add_argument("-p",default=4, help="Determining the Interval(3s as default) each matching Process will pause for")
    args = parser.parse_args()
    source = args.s if args.s is not None else "./from"
    version = args.v
    loader = args.l
    cache = args.o if args.o is not None else "./to"

    if args.v is None:
        version=input("Missing -v\n--The New Version for your mods(e.g. 1.20.1): ")
    if args.l is None:
        loader=input("Missing -l\n--the New Loader for your mods('fabric' or 'forge' or others): ")
    p = args.p if args.p is not None else 3

    if "" in [loader,version]:
        print("Error: mandatory Parameter of loader/cache isnt been added. aborting...")
        return 0
    path = Path(source)
    path_1=Path(cache)
    path_2 = Path(f"{cache}/{version}/{loader}")
    path_1.mkdir(parents=True, exist_ok=True)
    path_2.mkdir(parents=True, exist_ok=True)

    process=Mc_mod_migration(path)

    loop__(cache=cache,version=version,loader=loader,classer=process,i=p)

if __name__ =="__main__":
    init__()
