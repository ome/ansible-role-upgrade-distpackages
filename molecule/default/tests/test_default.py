import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_check_upgrade(host):
    # If upgrades are available this should fail
    host.check_output('yum check-upgrade')
