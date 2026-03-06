import requests
import hashlib
from pathlib import Path
class Mc_mod_migration:
    def __init__(self,source_path):
        self.modname = [str(file) for file in source_path.glob("**/*.jar")]
        self.modhash = [self.calculate_hashes(x) for x in self.modname]
        self.filter_list = ["Fabric", "fabric", "forge", "Forge"]
        self.DOWMLOAD_URL_MODRINTH = "https://api.modrinth.com/v2"
        self.HEADERS = {"User-Agent": "mcLauncher/1.0 (contact@example.com)"}

    def parse_name_readable(self,name: str):
        name = name.replace("_", "-")
        c = name.split("-")
        cc = []
        for x in range(0, len(c)):
            if x != 0 and c[x] in self.filter_list:
                continue
            else:
                f = c[x].split(".")
                if [(F in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) for F in f] and len(f) != 1:
                    continue
            cc.append(f" {c[x]}")
        for xx in range(0, len(cc)):
            try:
                int(cc[xx])
                cc[xx] = ""
            except:
                pass
        return "".join((str(item)) for item in cc)[1:]

    def find_mod_files_search(self,directory: str):  # read mods from a folder
        path = Path(directory)
        p = [file.name for file in path.glob("**/*.jar")]
        l = [self.parse_name_readable(name).lower() for name in p]
        return l

    def calculate_hashes(self,file_path):
        sha1 = hashlib.sha1()
        # sha512 = hashlib.sha512()

        with open(file_path, 'rb') as f:
            while True:

                data = f.read(65536)
                if not data:
                    break
                sha1.update(data)
        #       sha512.update(data)

        return sha1.hexdigest()

    def get_mod_download_url(self,tag, loader, mc_version, algorithm="sha1"):
        project_id = ""
        try:
            response = requests.get(f"{self.DOWMLOAD_URL_MODRINTH}/version_file/{self.modhash[tag]}",
                                    params={"algorithm": algorithm}, headers=self.HEADERS)
            if response.status_code == 200:
                data = response.json()
                project_id = data['project_id']
                print(f"Matched mod ID: {self.modname[tag].split("/")[-1]} ------> {project_id} ", end=" ------> ")
            elif response.status_code == 404:
                print(f"Modrinth didnt Recognize this Hash code {self.modhash[tag]} from mod :{self.modname[tag].split("/")[-1]}")
                return ",,,"
            else:
                print(f"Failed Requesting: {response.status_code}")
                return ",,,"

        except Exception as e:

            print("unexpected error: ", e)
            return ",,,"

        try:
            version_params = {
                "loaders": f'["{loader}"]',
                "game_versions": f'["{mc_version}"]'
            }
            version_res = requests.get(f"{self.DOWMLOAD_URL_MODRINTH}/project/{project_id}/version", params=version_params,
                                       headers=self.HEADERS)
            if version_res.status_code != 200:
                print("Failed to Request from server")
                return ",,,"
            versions = version_res.json()
            if not versions:
                print(f"Not in game version {mc_version}/{loader}")
                return f",,,"
            latest_version = versions[0]
            latest_file = latest_version['files'][0]
            print(f"{latest_file['filename']} ", end="")
            return (f"{latest_version['version_number']},"
                    f"{latest_file['filename']},"
                    f"{latest_file['url']},"
                    f"{project_id}")
        except Exception as e:
            print("unexpected error: ", e)

            return ",,,"

    def download_mod(self,mod_url, name, path):

        if mod_url == "":
            return False
        try:
            response = requests.get(mod_url, stream=True)
            response.raise_for_status()

            save_dir = Path(path)
            save_dir.mkdir(parents=True, exist_ok=True)
            save_file = save_dir / name
            with open(save_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("-----> downloaded ")

            return True
        except Exception as e:
            print(f"Failed Downloading: {e}")
            return False




