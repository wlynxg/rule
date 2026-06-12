# Clash Rule Manager

Private Repo + GitHub Action + GitHub Pages 自动部署 Clash 规则。

## 订阅链接

- **代理规则**: `https://wlynxg.github.io/rule/proxy.yaml`
- **直连规则**: `https://wlynxg.github.io/rule/direct.yaml`

## Clash 配置示例

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

编辑 `sources/proxy.txt`，每行一个域名，push 即可自动生效。
