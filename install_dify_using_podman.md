1. 安装podman、docker-buildx、docker-cli、docker-compose
2. 启用systemctl --user enable --now podman.socket
3. 配置/etc/containers/registries.conf,令unqualified-search-registries = ["docker.io"]
4. 代理~/.config/systemd/user/podman.service.d/override.conf
```
[Service]
Environment=HTTP_PROXY=http://localhost:10808
Environment=HTTPS_PROXY=http://localhost:10808
Environment=NO_PROXY=localhost,127.0.0.1,::1
 ```
 5. git clone https://github.com/langgenius/dify.git
 6. cd dify/docker
 7. cp .env.example .env
 8. 修改docker-compose.yaml及.env的nginx端口80为8080,443为8443
 9. podman compose up -d
