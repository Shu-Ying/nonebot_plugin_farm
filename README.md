# 真寻农场(nonebot_plugin_farm)

你是说可以种地对吧🤔?

---

## 如何安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-farm

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-farm

</details>
打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot-plugin-farm"]

</details>

---

## 使用指令

| 指令 | 描述 | Tip |
| --- | --- | --- |
| @小真寻 开通农场 | 首次开通农场 |  |
| 我的农场币 | 查询农场币 |  |
| 种子商店 [页数] | 查看种子商店 | 数量不填默认为1 |
| 购买种子 [种子名称] [数量] | 购买种子 | 数量不填默认为1 |
| 我的种子 | 查询仓库种子 |  |
| 播种 [种子名称] [数量] | 播种种子 | 数量不填默认将最大可能播种 |
| 收获 | 收获成熟作物 |  |
| 铲除 | 铲除荒废作物 |  |
| 我的作物 |  |  |
| 出售作物 [作物名称] [数量] | 从仓库里向系统售卖作物 | 不填写作物名将售卖仓库种全部作物 填作物名不填数量将指定作物全部出售 |
| @美波理 偷菜 | 偷别人的菜 | 每人每天只能偷5次 |
| 购买农场币 | 将真寻金币兑换成农场币 | 兑换比例默认为1:2 手续费默认20% |
| 更改农场名 [新的农场名] | 改名 |

---

## 配置
在 nonebot2 项目的 .env 文件中添加下表中的必填配置

| 配置项 | 是否必填 | 默认值 | 说明 |
| --- | --- | --- | --- |
| farm_draw_quality | 否 | "low" | 绘制农场清晰度 分为："low", "medium", "hight", "original" |
| farm_server_url | 否 | "http://diuse.work" | 后续签到、交易行、活动等服务器地址 |

---

## 更新日志[(详细)](./log/log.md)：
用户方面
---
- 修复重大BUG，该BUG会导致用户经验等级计算异常
- 修正种子价格，现在不会以单价的形式购买种子了，而是新增的种子价格

代码方面
---
- 彻底重构数据库，但是不会像V1.1一样导致用户数据丢失
- 迁移部分代码结构，使文件名和代码功能更加匹配
- 加入事件机制，采用类似Qt信号槽机制
---

## 待办事宜 `Todo` 列表

- [x] 完善我的农场图片，例如左上角显示用户数据
- [ ] 完善升级数据、作物数据、作物图片
- [ ] 签到功能
- [ ] 添加渔场功能
- [ ] 增加活动、交易行功能
- [ ] 增加交易行总行功能
- [ ] 添加其他游戏种子素材
- [ ] 想不到了，想到再说

---

## 关于

本人毫无任何Python经验，也从未正式的、系统的、完整的去学习Python。如有看到写的不对的地方，欢迎指出，也欢迎任何人一起来开发、完善农场。

素材来均源于互联网，侵权请联系我删除

---

## 致谢

最后感谢以下框架/作者的提供的技术支持(排名不分先后):

- [Nonebot2](https://github.com/nonebot/nonebot2) *✨ 跨平台 Python 异步机器人框架 ✨*
- [zhenxun_bot](https://github.com/zhenxun-org/zhenxun_bot) *最爱真寻的一集*
- [HibiKier](https://github.com/HibiKier) *阿咪为什么是神*
- [ATTomato](https://github.com/ATTomatoo) *流泪偷码头.jpg*

## 许可证

`真寻农场(nonebot_plugin_farm)`将采用的是`GPLv3`许可证进行开源
