"""普通 NoneBot 配置；不依赖真寻配置系统。"""

from typing import Literal
from pathlib import Path

from pydantic import BaseModel, Field, conint, validator


class Config(BaseModel):
    """农场启动配置。"""

    farm_deployment: str = Field(
        "nonebot", min_length=1, description="农场存档部署标识",
    )
    farm_data_dir: Path | None = Field(
        None, description='兼容旧部署的数据目录；未设置时使用平台默认目录',
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

    @validator('farm_data_dir', pre=True)
    def empty_data_directory(cls, value):
        return None if value == '' else value
