ofabric
=======

A thin object oriented wrapper on Fabric. This enables changing hosts dynamically without fiddling with env or decorators.
Can be used as

z2 = Host('abhishek', '/home/abhishek/id_rsa', 'server.hosting.com')
z2.run('uname -a')
