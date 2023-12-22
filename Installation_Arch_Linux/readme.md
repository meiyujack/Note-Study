# 第一章 基本安装 Arch Linux
##  0 连接网络（WLAN）

1. ip link 获取所有网络设备信息，记住无线网卡设备标识A。
2. iwctl 进入交互式提示符模式验证网络。
3. station A scan 扫描无线网络。（device list 同1，取得A）
4. station A get-networks 获得可用无线网络列表，取得欲联接无线网络名称（SSID）B。
5. station A connect B
6. 输入密码，确定。
7. station A show 显示 WiFi 设备详细情况，如连接状态，ip地址、Mac地址等等。
8. exit 退出该交互模式。
## 1 确认系统时间

1. timedatectl 查看时间
2. timedatectl list-timezones 查看所有时区
3. timedatectl set-timezone Asia/Chongqing 设置东八时区。

## 2 硬盘分区
1. fdisk -l 列出所有磁盘及分区情况
2. fdisk 磁盘路径 进入该磁盘下进行分区
3. p 列出该磁盘分区情况， d 删除分区， n 新增分区， l 列出分区类型，如EFI、SWAP等
4. w 写入退出。q 放弃保存退出

## 3 格式化（可选）
1. mkfs.ext4 /dev/root_partition（根分区）
2. mkswap /dev/swap_partition（交换空间分区）
3. mkfs.fat -F 32 /dev/efi_system_partition（EFI 系统分区）

## 4 挂载
1. “/”的挂载，“/”的磁盘分区P0。mount P0 /mnt
2. "boot"的挂载，“/boot”的引导分区P1。 mount --mkdir P1 /mnt/boot
3. "home"的挂载，“/home”的磁盘分区P2。mount --mkdir P2 /mnt/home
4. 启用交换空间。swapon 交换空间的磁盘分区P3。 swapon P3

## 5 安装
0. 更新软件库引擎，确保当下网络是最快最优解。pacman -Sy pacman-mirrorlist会生成/etc/pacman.d/mirrorlist.pacnew，由此更新/etc/pacman.d/mirrorlist。会直接影响未来Arch Linux的软件更新速率。
1. 需安装archlinux-keylinux。pacman -Sy archlinux-keyring
2. pacstrap -K /mnt base linux linux-firmware 使用 pacstrap脚本，安装 base包、软件包和 Linux 内核以及常规硬件的固件。

## 6  配置系统
1. genfstab -U /mnt >> /mnt/etc/fstab 生成fstab文件。（fstab文件可用于定义磁盘分区，各种其他块设备或远程文件系统应如何装入文件系统。每个文件系统在一个单独的行中描述。这些定义将在引导时动态地转换为系统挂载单元，并在系统管理器的配置重新加载时转换。）
2. arch-chroot /mnt 到新安装的系统。
3. 设置时区。如：ln -sf /usr/share/zoneinfo/Asia/Chongqing /etc/localtime 然后再运行hwclock --systohc以生成/etc/adjtime
4. 软件再安装。进入新系统路径后，常规操作，安装vim等等。

## 7 本地化
1. vim /etc/locale.gen 取消en_US.UTF-8 UTF-8 和zh_CN.UTF-8 UTF-8前的#注释。locale-gen 生成locale信息。
2. vim /etc/locale.conf 新建文件，写入LANG=en_US.UTF-8 保存退出。

## 8 安装引导程序
1. pacman -Sy grub efibootmgr
2. 挂载EFI系统分区。 mount P1 /boot
3. grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
4. 安装微码。pacman -Sy intel-ucode （pacman -Sy amd-ucode）
5. grub-mkconfig -o /boot/grub/grub.cfg

## 9 设置root密码
1. passwd
2. 输入密码

## 10 设置主机名及配置网络管理软件
1. vim /etc/hostname 新建文件，写入主机名，如XXComputer，保存退出。
2. pacman -Sy networkmanager
3. systemctl enable --now NetworkManager(一定注意大小写，这个服务，跟安装不一样，若live环境进入启用不行就后面直接进去开启，待试。本管理工具可忽略第二章,若无视本小节，如果没有有线网络后面无法联网。)

## 11 重启
1. exit 退出至live环境
2. umount -R /mnt 取消挂载
3. reboot

# 第二章 基本配置 Arch Linux
## 0. 网络配置(可选，无NetworkManager,不推荐)
1. pacman -Sy iwd
2. systemctl enable iwd && systemctl start iwd
3. vim /etc/iwd/main.conf

    [General]
    EnableNetworkConfiguration=true
4. systemctl enable --now systemd-resolved.service
## 1. 配置账户
1. pacman -Sy sudo
2. useradd -m -G wheel -s /bin/bash 你的账户名
3. vim /etc/sudoers 取消%wheel ALL=(ALL:ALL) All 这一行的注释(#)，保存退出（wq!）

## 2. 配置桌面（xfce4）
1. pacman -Sy xfce4 xfce4-goodies lxdm gvfs
2. vim /etc/lxdm/lxdm.conf 取消这一行注释并修改为session=/usr/bin/startxfce4
3. sudo systemctl enable lxdm
4. reboot

## 3. 设置中文界面
1. vim ~/.profile 键入export LANG=zh_CN.UTF-8，保存退出
2. pacman -S wqy-microhei
3. reboot

## 4. 设置中文输入法
1. sudo pacman -S fcitx5 fcitx5-chinese-addons fcitx5-qt fcitx5-gtk
2. vim /etc/environment 键入以下内容
```
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
SDL_IM_MODULE=fcitx
GLFW_IM_MODULE=ibus
```
3. reboot
