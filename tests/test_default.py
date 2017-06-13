import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_check_upgrade(Command):
    # If upgrades are available this should fail
    Command.check_output('yum check-upgrade')
