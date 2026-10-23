# NoneBot 农场

<p align="center"><img src="./logo.png" width="400" alt="真寻农场 Logo"></p>

从 `main_plugin_farm` 自动生成的普通 NoneBot 插件，与真寻版使用相同的
业务核心、命令和渲染资源，不依赖真寻或 zhenxun-utils。

![农场预览](images/farm-preview.png)

## 安装与配置

需要 Python 3.10 及以上。生成仓库中执行 `pip install .`，或安装经过
标签发布的 `nonebot_plugin_farm` 包，然后在 NoneBot 启动脚本中加入：

```python
nonebot.load_plugin("nonebot_plugin_farm")
```

可在 `.env` 中设置：

```dotenv
FARM_FONT=C:/Windows/Fonts/msyh.ttc
FARM_IMAGE_FORMAT=AUTO
FARM_IMAGE_QUALITY=75
FARM_DEPLOYMENT=nonebot
FARM_RESOURCE_SOURCE=Github
FARM_SERVICE_URL=
```

`FARM_DATA_DIR` 可显式指定数据目录，默认沿用旧版插件 localstore 下的
`nonebot_plugin_farm/farm_db` 子目录。旧 `farm.db` 保留，首次使用按当前
机器人和平台迁入 `farm.sqlite3`；遇到账号或平台冲突会拒绝覆盖。
日志写入该目录的 `farm-preview.log`。字体不可用时提供文字响应。

`FARM_RESOURCE_SOURCE`（资源获取地址）支持`Github`、`Gitea`、`farm_service`，
默认`Github`。`FARM_SERVICE_URL`（farm_service 地址）始终独立存在，
供资源及后续活动功能共用；选择farm_service下载时须填写HTTPS基础地址。
两项修改后重载。插件不包含素材ZIP：每次启动校验本地SHA256，缺失或不匹配
才从`farm_service`仓库根目录`assets/assets.zip`下载，校验成功后原子替换。
失败时保留文字功能，不自动跨源切换，重载后重试。活动功能尚未实施。

`FARM_IMAGE_QUALITY` 为整数1～95，默认75，统一控制全部农场图片
的编码质量；越高通常越清晰、文件越大，PNG无损格式不受此值影响。
启动时校验配置。只有“我的农场 高清”允许高清，使用1536宽，质量
取配置值与85的较大值；其他命令不接受高清。种子/作物仓库保留
分页和“文字”选项，例如“我的种子 2 文字”。
部署标识一旦使用，不应随意变更，否则会切换到不同的存档身份。

## 当前命令

开通农场、我的农场、农场详述、地块编号、我的农场币、我的点券、
我的种子、我的作物、种子商店、购买种子、播种、收获、铲除、
作物加锁、作物解锁、出售作物、农场除虫、除虫、偷菜、农场帮助。
发送「农场帮助」查看参数。图片与提及由 Alconna 统一消息适配。
开垦每次增加1块普通空地；开垦 条件查询下一块地的等级与费用。
初始3块的旧账号按可靠注册或旧库迁移记录一次性补3块，保留已开垦成果；
来源不明、编号异常或补后超出30位置则保留原状并明确提示。
范围与当前真寻生成版一致；旧版签到、改名、土地升级等命令
尚未在共享核心中实现，此版本不提供这些命令。

## 生成与发布

主仓库 `version.txt` 是版本的唯一来源，生成 ZIP、包版本和清单。
`nonebot-preview.yml` 在 PR 中测试和构建，在主仓库 `main` 推送后
使用 `FARM_RELEASE_TOKEN` 同步到 `Shu-Ying/nonebot_plugin_farm/main`。
同步任务沿用真寻的 `zhenxun-preview` environment，兼容其中已有密钥。

目标仓库保留 `v*` 标签发布 PyPI 的方式和 `PYPI_TOKEN` 密钥。
普通同步只校验、构建，不发布 PyPI。手动推送标签前应确认版本未在
PyPI 使用，且标签去掉 `v` 后与 `version.txt` 完全一致。
接入时远端旧版为 1.5.7，主仓库为 1.5.4；用户计划后续统一改为
2.0.0，本次未提前修改。统一后发布标签应为 `v2.0.0`。

生成仓库的 `verify_package.py --directory .` 校验文件完整性；
`python -m build` 生成 wheel/sdist。远端 CI 和实际机器人消息行为
需要在部署环境进一步验证。
