# Clash Rule Manager

Private repo + GitHub Action + Public Gist 方式管理 Clash 规则。

## 工作原理

```
sources/*.txt (域名列表)
    ↓ scripts/generate.py
dist/*.yaml (Clash rule-provider 格式)
    ↓ GitHub Action
Public Gist (可订阅的规则链接)
```

## 目录结构

```
├── sources/
│   ├── proxy.txt      # 需要走代理的域名
│   ├── direct.txt     # 直连域名
│   └── reject.txt     # 拦截域名
├── scripts/
│   └── generate.py    # 生成 Clash rule-provider YAML
├── dist/              # 生成的规则文件 (gitignored)
└── .github/workflows/
    └── update-rules.yml
```

## 使用方法

### 添加规则

编辑 `sources/` 下的对应文件，每行一个域名：

```
# sources/proxy.txt
example.com
*.google.com
```

### 在 Clash 中订阅

在 `rule-providers` 中配置：

```yaml
rule-providers:
  my-proxy:
    type: http
    behavior: classical
    url: "https://gist.githubusercontent.com/<user>/<gist_id>/raw/proxy.yaml"
    interval: 86400
    path: ./ruleset/my-proxy.yaml
```

然后在 `rules` 中引用：

```yaml
rules:
  - RULE-SET,my-proxy,Proxy
  - MATCH,DIRECT
```

## 首次设置

1. 创建一个 Public Gist（内容随意）
2. 在仓库 Settings → Secrets 中添加：
   - `GIST_TOKEN`: GitHub PAT (需要 `gist` 权限)
   - `GIST_ID`: Gist 的 ID（URL 中那串哈希）
