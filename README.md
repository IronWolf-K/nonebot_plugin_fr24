# nonebot2 fr24插件
QQ机器人FrightRadar24 航班查询插件v0.2，基于cqhttp+nonebot2开发

## 声明

该插件仅获取FR24提供的免费数据，获取更多数据请前往官网[订阅](https://www.flightradar24.com/premium/)

更多内容请参阅：<https://www.flightradar24.com/terms-and-conditions>

## 安装

该项目需要`brotlipy`用于解码响应内容：

```shell
pip install brotlipy
```

目前暂时仅支持git clone至本地：

```shell
git clone https://github.com/IronWolf-K/nonebot_plugin_fr24.git
```

将插件移动至`plugin`下即可使用

## 功能与使用方法

+ 目前支持功能：实时在线航班统计，筛选航班统计
+ 使用方法：/fr24 help 可获取操作教程
  + /fr24 now 查看当前航空器
  + /fr24 from XXX 出发机场筛选（IATA）
  + /fr24 to XXX 到达机场筛选（IATA）
  + /fr24 airport XXX 机场筛选（IATA）
  + /fr24 type XXXX 机型筛选（例：B738）
  + /fr24 airline XX 航司筛选（例：MF）

+ TODO
  - [ ] 查询某一航班详情
  - [ ] 查询机场详情
  - [ ] 查看关注人数最多的航班
  - [ ] 图片支持













