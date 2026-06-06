"""
AI CMS - AI内容管理系统工具
支持内容建模、编辑器、发布流程
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AICMSTools:
    """
    AI CMS工具
    支持：内容建模、编辑器、发布
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_cms(self, content_types: List[str], features: List[str]) -> Dict:
        """设计CMS"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        types_text = ", ".join(content_types)
        features_text = ", ".join(features)

        prompt = f"""请设计CMS系统：

内容类型：{types_text}
功能：{features_text}

请返回JSON格式：
{{
    "architecture": "架构",
    "content_model": "内容模型",
    "workflow": "工作流",
    "tools": ["推荐工具"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"cms": content}

    def generate_content_model(self, content_type: str, fields: List[Dict]) -> str:
        """生成内容模型"""
        if not self.client:
            return "LLM客户端未配置"

        fields_text = json.dumps(fields, ensure_ascii=False)

        prompt = f"""请生成{content_type}内容模型：

字段：{fields_text}

要求：
1. 数据库Schema
2. API端点
3. 验证规则"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_rich_editor(self, features: List[str], framework: str = "react") -> str:
        """生成富文本编辑器"""
        if not self.client:
            return "LLM客户端未配置"

        features_text = ", ".join(features)

        prompt = f"""请生成{framework}富文本编辑器：

功能：{features_text}

要求：
1. 工具栏
2. 快捷键
3. 插件支持
4. Markdown支持"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_media_library(self, features: List[str]) -> str:
        """生成媒体库"""
        if not self.client:
            return "LLM客户端未配置"

        features_text = ", ".join(features)

        prompt = f"""请生成媒体库组件：

功能：{features_text}

要求：
1. 文件上传
2. 预览
3. 分类管理
4. 搜索"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_publish_workflow(self, roles: List[str]) -> Dict:
        """生成发布工作流"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        roles_text = ", ".join(roles)

        prompt = f"""请设计发布工作流：

角色：{roles_text}

请返回JSON格式：
{{
    "states": ["状态"],
    "transitions": ["转换"],
    "permissions": {{"角色": ["权限"]}},
    "notifications": ["通知"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"workflow": content}

    def generate_seo_tools(self, content_type: str) -> str:
        """生成SEO工具"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{content_type}生成SEO优化工具：

要求：
1. 标题优化
2. 描述生成
3. 关键词建议
4. 结构化数据"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AICMSTools:
    """创建CMS工具"""
    return AICMSTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI CMS Tools")
    print()

    # 测试
    cms = tools.design_cms(["文章", "产品", "页面"], ["富文本", "媒体库", "版本控制"])
    print(json.dumps(cms, ensure_ascii=False, indent=2))
