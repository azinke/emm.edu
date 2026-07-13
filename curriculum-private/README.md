# Restricted curriculum store boundary

This tracked directory is a public policy marker only. It is **not** the
restricted store, and no restricted payload, private URL, identity, key, answer,
or partner detail may be placed below it.

Create the real separately permissioned repository outside this public checkout:

```sh
python3 curriculum/scripts/initialize_restricted_store.py \
  /approved/private/path/emm-edu-restricted \
  --remote ssh://private-host/controlled/emm-edu-restricted.git
```

Classification, roles, access review, backup, incident response, and opaque
public-reference rules are controlled by
`curriculum/governance/restricted-material.md`. The empty markers below make
accidental writes visible to the leak scan; `.gitignore` is not access control.
