# Linux Container Security

Containers provide application isolation through operating system features such as namespaces, cgroups, capabilities and filesystem controls.

Container security assessments examine whether these isolation boundaries are correctly configured and whether container workloads expose the host or other workloads to unnecessary risk.

## 1. Container Runtime Identification

Identify common container runtimes:

```bash
docker version
podman version
containerd --version
runc --version
```

Check whether the current environment is itself containerised:

```bash
systemd-detect-virt --container
cat /proc/1/cgroup
ls -la /.dockerenv
```

These indicators are useful but not definitive.

## 2. Docker Enumeration

List running containers:

```bash
docker ps
```

List all containers:

```bash
docker ps -a
```

Review images:

```bash
docker images
```

Inspect a container:

```bash
docker inspect CONTAINER
```

Review container resource usage:

```bash
docker stats
```

Assess:

- Container privileges.
- User identity.
- Mounted host directories.
- Network configuration.
- Exposed ports.
- Environment variables.
- Restart policies.
- Runtime security options.

Treat inspection output as potentially sensitive because it may contain environment variables or credentials.

## 3. Privileged Containers

A privileged container receives significantly broader access to host resources than a standard container.

Review container configuration:

```bash
docker inspect CONTAINER
```

Look for:

```text
"Privileged": true
```

Assess whether privileged mode is genuinely required.

Potential consequences include:

- Expanded device access.
- Weakened isolation.
- Greater access to host kernel interfaces.
- Increased impact if the container is compromised.

Avoid attempting host escape unless specifically authorised.

## 4. Linux Capabilities

Inspect container capability configuration:

```bash
docker inspect --format '{{.HostConfig.CapAdd}}' CONTAINER
docker inspect --format '{{.HostConfig.CapDrop}}' CONTAINER
```

Review dangerous or unnecessary capabilities, including:

- `CAP_SYS_ADMIN`
- `CAP_SYS_PTRACE`
- `CAP_NET_ADMIN`
- `CAP_NET_RAW`
- `CAP_DAC_OVERRIDE`
- `CAP_SYS_MODULE`

Use the principle of least privilege and drop capabilities that the workload does not require.

## 5. Host Filesystem Mounts

Inspect mounts:

```bash
docker inspect --format '{{json .Mounts}}' CONTAINER
```

Review:

- Host paths mounted into containers.
- Read-write versus read-only access.
- Sensitive host directories.
- Docker socket exposure.
- Shared application data.
- Unexpected filesystem mounts.

A read-write mount of a sensitive host directory can undermine container isolation.

## 6. Docker Socket Exposure

The Docker socket commonly exists at:

```text
/var/run/docker.sock
```

Inspect it:

```bash
ls -l /var/run/docker.sock
```

Review:

- Socket ownership.
- Group membership.
- Which workloads can access it.
- Whether containers mount it.
- Whether access is required.

Access to the Docker daemon is highly privileged and may effectively provide control over the host.

Do not interact with an exposed production socket beyond the approved scope.

## 7. Container User Context

Inspect configured container users:

```bash
docker inspect --format '{{.Config.User}}' CONTAINER
```

Where authorised, inspect the running container:

```bash
docker exec CONTAINER id
```

Assess whether applications run as root unnecessarily.

Recommended practices:

- Use dedicated non-root users.
- Avoid unnecessary privilege escalation.
- Use read-only filesystems where possible.
- Restrict writable directories.
- Avoid sharing host user namespaces unless required.

## 8. Network Configuration

Review Docker networks:

```bash
docker network ls
```

Inspect a network:

```bash
docker network inspect NETWORK
```

Review published ports:

```bash
docker port CONTAINER
```

Assess:

- Unnecessary published ports.
- Exposure on all host interfaces.
- Unrestricted inter-container communication.
- Access to internal services.
- Segmentation between workloads.
- Host network mode usage.

## 9. Podman

List containers:

```bash
podman ps -a
```

Review images:

```bash
podman images
```

Inspect a container:

```bash
podman inspect CONTAINER
```

Review configuration:

```bash
podman info
```

Podman commonly supports rootless operation, which can reduce the impact of container compromise. Rootless operation still requires appropriate configuration and does not eliminate all security risks.

## 10. LXC and LXD

Where installed:

```bash
lxc list
lxc info
```

Review:

- Privileged versus unprivileged containers.
- Device access.
- Host filesystem mounts.
- Namespace configuration.
- Container profiles.
- Network interfaces.
- Management socket permissions.

Container management access can be highly privileged. Assess group memberships and API access carefully.

## 11. Container Image Security

Review:

- Base image provenance.
- Image age.
- Installed packages.
- Known vulnerabilities.
- Unnecessary software.
- Embedded credentials.
- Default users.
- Startup configuration.

Useful tools:

| Tool | Purpose |
|---|---|
| Trivy | Image and filesystem vulnerability scanning |
| Grype | Vulnerability scanning |
| Syft | Software bill of materials generation |
| Dockle | Container image configuration checks |
| Docker Scout | Image vulnerability and supply-chain insights |

References:

- https://trivy.dev/
- https://github.com/anchore/grype
- https://github.com/anchore/syft
- https://github.com/goodwithtech/dockle

## 12. Container Escape Risk Assessment

Container escape risk increases when isolation controls are weakened.

Investigate:

- Privileged containers.
- Dangerous capabilities.
- Host namespace sharing.
- Writable host mounts.
- Runtime socket exposure.
- Kernel vulnerabilities.
- Insecure runtime configuration.
- Excessive device access.

A misconfiguration is not automatically proof of a successful escape.

Validate configuration weaknesses using safe evidence and avoid executing destructive host-level actions.

## 13. Defensive Recommendations

- Prefer rootless containers where practical.
- Avoid privileged mode.
- Drop unnecessary capabilities.
- Restrict container socket access.
- Use read-only filesystems.
- Restrict host mounts.
- Apply seccomp profiles.
- Use AppArmor or SELinux.
- Segment container networks.
- Scan images regularly.
- Keep runtimes and host kernels patched.
- Establish image provenance and signing controls.

## 14. Assessment Checklist

- [ ] Container runtime identified.
- [ ] Running containers enumerated.
- [ ] Container privileges reviewed.
- [ ] Capability configuration assessed.
- [ ] Host mounts reviewed.
- [ ] Docker socket exposure assessed.
- [ ] Container user context reviewed.
- [ ] Network exposure assessed.
- [ ] Image security evaluated.
- [ ] LXC/LXD configuration reviewed where applicable.
- [ ] Escape risks documented.
- [ ] Remediation recommendations provided.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
