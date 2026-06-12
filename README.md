# Clash Rule Manager

Private Repo + GitHub Action + GitHub Pages 方式管理 Clash 规则。

## 工作原理

```
sources/*.txt (域名列表)
    ↓ scripts/generate.py
dist/*.yaml (Clash rule-provider 格式)
    ↓ GitHub Action
GitHub Pages (公开可订阅的规则链接)
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
    └── deploy-rules.yml
```

## 订阅链接

推送代码后自动部署到 GitHub Pages：

- **代理规则**: `https://wlynxg.github.io/rule/proxy.yaml`
- **直连规则**: `https://wlynxg.github.io/rule/direct.yaml`
- **拦截规则**: `https://wlynxg.github.io/rule/reject.yaml`

## 在 Clash 中使用

在 `rule-providers` 中配置：

```yaml
rule-providers:
  my-proxy:
    type: http
    behavior: classical
    url: "https://wlynxg.github.io/rule/proxy.yaml"
    interval: 86400
    path: ./ruleset/my-proxy.yaml

rules:
  - RULE-SET,my-proxy,Proxy
  - MATCH,DIRECT
```

## 添加规则

编辑 `sources/` 下的对应文件，每行一个域名，然后 push：

```bash
echo "example.com" >> sources/proxy.txt
git add . && git commit -m "add example.com" && git push
```
