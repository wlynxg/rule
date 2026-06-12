# Clash Rule Manager

Private Repo + GitHub Action + GitHub Release 管理 Clash 规则。

## 工作原理

```
sources/*.txt (域名列表)
    ↓ GitHub Action
release 分支 + GitHub Release (rule.yaml)
    ↓
raw.githubusercontent.com (公开链接)
```

## 添加规则

编辑 `sources/` 下的文件，push 即生效：

```bash
# sources/proxy.txt - 需要走代理的域名
echo "google.com" >> sources/proxy.txt

# sources/direct.txt - 直连域名
echo "baidu.com" >> sources/direct.txt

# sources/reject.txt - 拦截域名
echo "ads.example.com" >> sources/reject.txt

git add . && git commit -m "update rules" && git push
```

## 订阅链接

```
https://raw.githubusercontent.com/wlynxg/rule/release/rule.yaml
```

## Clash 配置

```yaml
rule-providers:
  my-rules:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/wlynxg/rule/release/rule.yaml"
    path: ./ruleset/my-rules.yaml
    interval: 86400

rules:
  - RULE-SET,my-rules,PROXY
  - MATCH,DIRECT
```
