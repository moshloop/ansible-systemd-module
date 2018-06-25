Ansible Role for creating systemd services, for managing existing services use the built-in [systemd](https://docs.ansible.com/ansible/latest/modules/systemd_module.html) module.

### Install

```bash
ansible-galaxy ansible-galaxy install moshloop.systemd
```

### Options
```
OPTIONS (= is mandatory):
= ExecStart
= Name
- Description
- InstallArgs
- RestartOn [Default: on-failure]
- RunAs [Default: root]
- ServiceArgs
- UnitArgs
- WantedBy [Default: multi-user.target]
- state (Choices: present, absent)[Default: present]
```

### EXAMPLES:
```yaml
  - hosts: all
    roles:
      - moshloop.systemd
    tasks:
        - systemd_service:
            Name: test
            ExecStart: "/usr/bin/nc -l 200"
        - systemd_service:
            Name: test
            ExecStart: "/usr/bin/nc -l 200"
            UnitArgs:
            After: networking.service
```