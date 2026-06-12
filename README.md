# Clash Rule Manager

Private source + GitHub Action → Release 发布 Clash 规则。

## 目录结构

```
├── sources/
│   ├── proxy.txt      # 代理域名（每行一个）
│   ├── direct.txt     # 直连域名
│   └── reject.txt     # 拦截域名
└── .github/workflows/
    └── release.yml    # 自动构建并发布 Release
```

## 规则链接

| 规则 | 链接 |
|------|------|
| 代理 | `https://raw.githubusercontent.com/wlynxg/rule/release/proxy.txt` |
| 直连 | `https://raw.githubusercontent.com/wlynxg/rule/release/direct.txt` |
| 拦截 | `https://raw.githubusercontent.com/wlynxg/rule/release/reject.txt` |

## Clash 配置

```yaml
rule-providers:
  proxy:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/wlynxg/rule/release/proxy.txt"
    path: ./ruleset/proxy.yaml
    interval: 86400
  direct:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/wlynxg/rule/release/direct.txt"
    path: ./ruleset/direct.yaml
    interval: 86400
  reject:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/wlynxg/rule/release/reject.txt"
    path: ./ruleset/reject.yaml
    interval: 86400

rules:
  - RULE-SET,reject,REJECT
  - RULE-SET,proxy,PROXY
  - RULE-SET,direct,DIRECT
  - MATCH,PROXY
```

## 添加规则

编辑 `sources/` 下的文件，push 后自动发布：
```bash
echo "example.com" >> sources/proxy.txt
git add . && git commit -m "add example.com" && git push
```
