"""普通 NoneBot 配置；不依赖真寻配置系统。"""

from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseModel, Field, conint


class Config(BaseModel):
    """农场启动配置。"""

    farm_data_dir: Optional[Path] = Field(
        None, description="数据目录；默认兼容旧版 localstore 农场目录",
    )
    farm_font: Optional[Path] = Field(
        None, description="中文字体路径；不可用时退回文字响应",
    )
    farm_deployment: str = Field(
        "nonebot", min_length=1, description="农场存档部署标识",
    )
    farm_image_format: Literal["AUTO", "JPEG", "PNG"] = Field(
        "AUTO", description="图片格式，AUTO 优先使用压缩 JPEG",
    )
    farm_image_quality: conint(strict=True, ge=1, le=95) = Field(
        75,
        description="全部农场图片编码质量；仅我的农场高清时至少85",
    )
    farm_resource_source: Literal['Github', 'Gitea', 'farm_service'] = Field(
        'Github', description='资源获取地址，修改后重载插件',
    )
    farm_service_url: str = Field(
        '', description='farm_service 地址，独立供资源及活动服务使用',
    )
