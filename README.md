Upgrade Distribution packages
=============================

[![Actions Status](https://github.com/ome/ansible-role-upgrade-distpackages/workflows/Molecule/badge.svg)](https://github.com/ome/ansible-role-upgrade-distpackages/actions)
[![Ansible Role](https://img.shields.io/ansible/role/41406.svg)](https://galaxy.ansible.com/ome/upgrade_distpackages/)

Upgrades all packages installed with the distribution's package manager.
Optionally reboots the system if a kernel update was found.


Role Variables
--------------

Optional variables:

- `upgrade_distpackages`: List of packages to upgrade (default: all)
- `upgrade_distpackages_excludes`: List of package specifications to exclude from upgrade (default empty)
- `upgrade_distpackages_reboot_kernel`: Automatically reboot if a new kernel is installed (default `False`)
- `upgrade_distpackages_reboot_timeout`: Maximum time to wait for a reboot (default `600` seconds)


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
