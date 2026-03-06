#一个简单的模组迁移工具

# minecraft-mod-migrate-tool_V0.1
a python tool with Capability of migrating All MC game mods from Versions to versions Within only one command as long as the mods support version/loader you specified.
Thanks to Modrinth for providing api with Comprehensive functions! 
This Script Relies on Python Completely, so download python in advance or choose the Packed up Program in release
    
## 使用方法
0. 快速使用: 在打包的程序所在的目录下新建文件夹'from'，然后将你想要迁移的模组放在这，然后运行程序并填入提示的参数即可,之后在自动创建的'to'文件夹下找到迁移成功的模组
1. 安装依赖：`pip install requests`
2. 运行脚本：`python mod_migrater.py -s <源mod文件夹> -v <目标Minecraft版本> -l <加载器> -o <输出文件夹>`

## Usage
0. Quick Tutorial: create new folder 'from' in the same folder where the Executable(.exe file) is in , then place all the mods you Desired to migrate to other version/loader, then run the program and type in prompted papameters(new version and Mod loader) , all Succeed mods would be in auto-created folder 'to'.
1. Install dependencies: `pip install requests`
2. Run script: `python mod_migrater.py -s <source_mod_folder> -v <target_mc_version> -l <loader> -o <output_folder>`


