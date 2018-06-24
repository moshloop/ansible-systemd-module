Ansible Role for created systemd services, for managing existing services use the built-in [systemd](https://docs.ansible.com/ansible/latest/modules/systemd_module.html) module.

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
- systemd_service:
          Name: test
          ExecStart: "/usr/bin/nc -l 200"
```


```yaml
- systemd_service:
          Name: test
          ExecStart: "/usr/bin/nc -l 200"
          UnitArgs:
            After: networking.service
```