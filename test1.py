from __future__ import print_function
ip1 = '220.1..1.17'
ip2 = '242.234.22.2'
ip3 = '234.1.2.2'
try:
   ip4 = raw_input("Enter from ip4")
except NameError:
   ip4 = input("Enter ip4")
print("-",50)
print("\n{:30}{:20}{:30}\n".format('ip1','ip2','ip3','ip4'))
print("\n{:30}{:20}{:30}{:20}\n".format(ip1,ip2,ip3,ip4))

