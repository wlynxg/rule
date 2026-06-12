# Clash Rule Manager

Private Repo + GitHub Action 方式管理 Clash 规则。

## 工作原理

```
sources/*.txt (域名列表)
    ↓ GitHub Action
单个 rules.yaml (Clash rule-provider 格式)
    ↓ 提交到 release 分支 + 创建 GitHub Release
公开可订阅的规则链接
```

## 目录结构

```
├── sources/
│   ├── proxy.txt      # 需要走代理的域名
│   ├── direct.txt     # 直连域名
│   └── reject.txt     # 拦截域名
└── .github/workflows/
    └── update-rules.yml
```

## 订阅链接

```yaml
rule-providers:
  rules:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/wlynxg/rule/release/rules.yaml"
    path: ./ruleset/rules.yaml
    interval: 86400

rules:
  - RULE-SET,rules,PROXY
  - MATCH,DIRECT
```

## 添加规则

编辑 `sources/` 下的对应文件，每行一个域名，然后 push：

```bash
echo "example.com" >> sources/proxy.txt
git add . && git commit -m "add example.com" && git push
```
