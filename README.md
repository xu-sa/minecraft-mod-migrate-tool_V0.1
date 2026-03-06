#一个简单的模组迁移工具
这个程序可以用一行指令将多个模组在不同版本之间迁移，如果版本不支持会跳过，所以后期需要自己补齐少量模组（可以添加这个功能但是暂时问题应该不大），用python写的脚本，用pyinstaller打包的程序

# minecraft-mod-migrate-tool_V0.1
a python tool with Capability of migrating All MC game mods from Versions to versions Within only one command.
Thanks to Modrinth for providing api with Comprehensive functions! 
choose the Packed up Program in release According to your system as if you dont use python.
The downloading Result wont be letting you run a new version effortlessly , for some mods may have different Dependency on different Loader or version however the Function of "auto Detecting Dependency & adding to Download Queue" Isnt Available yet (may consider if i got enough spare time)

## 使用方法
0. 快速使用: 在打包的程序所在的目录下新建文件夹'from'，然后将你想要迁移的模组放在这，然后运行程序(最好打开命令行执行)并填入提示的参数即可,之后在自动创建的'to'文件夹下找到迁移成功的模组
1. 安装依赖：`pip install requests`
2. 运行脚本：`python mod_migrater.py -s <源mod文件夹> -v <目标Minecraft版本> -l <加载器> -o <输出文件夹>`

## Usage
0. Quick Tutorial: create new folder 'from' in the same folder where the Executable(.exe file) is in , then place all the mods you Desired to migrate to other version/loader, then run the program(better to run this in a shell) and type in prompted papameters(new version and Mod loader) , all Succeed mods would be in auto-created folder 'to'.
1. Install dependencies: `pip install requests`
2. Run script: `python mod_migrater.py -s <source_mod_folder> -v <target_mc_version> -l <loader> -o <output_folder>`


