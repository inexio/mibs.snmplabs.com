#
# PySNMP MIB module STN-EXTIF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-EXTIF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:03:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, Counter64, IpAddress, Unsigned32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, ModuleIdentity, Gauge32, MibIdentifier, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "IpAddress", "Unsigned32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Gauge32", "MibIdentifier", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stnExtensions, stnNotification = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnExtensions", "stnNotification")
stnExtIf = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 3, 1))
if mibBuilder.loadTexts: stnExtIf.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnExtIf.setOrganization('Spring Tide Networks, Inc.')
stnExtIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1))
stnExtIfMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 3, 1, 2))
stnExtIfMibTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 3, 1, 3))
stnExtIfL2Table = MibTable((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 1), )
if mibBuilder.loadTexts: stnExtIfL2Table.setStatus('current')
stnExtIfL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 1, 1), ).setIndexNames((0, "STN-EXTIF-MIB", "stnExtIfL2IfName"))
if mibBuilder.loadTexts: stnExtIfL2Entry.setStatus('current')
stnExtIfL2IfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIfL2IfName.setStatus('current')
stnExtIfL2IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIfL2IfIndex.setStatus('current')
stnExtIfL3Table = MibTable((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2), )
if mibBuilder.loadTexts: stnExtIfL3Table.setStatus('current')
stnExtIfL3Entry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1), ).setIndexNames((0, "STN-EXTIF-MIB", "stnExtIfL3IfName"))
if mibBuilder.loadTexts: stnExtIfL3Entry.setStatus('current')
stnExtIfL3IfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIfL3IfName.setStatus('current')
stnExtIfL3IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIfL3IfIndex.setStatus('current')
stnExtIfL3SubnetIfInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIfL3SubnetIfInstance.setStatus('current')
stnExtIfL3IpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIfL3IpAddress.setStatus('current')
stnExtIfL3IpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIfL3IpMask.setStatus('current')
stnExtIpAddrL3Table = MibTable((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3), )
if mibBuilder.loadTexts: stnExtIpAddrL3Table.setStatus('current')
stnExtIpAddrL3Entry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1), ).setIndexNames((0, "STN-EXTIF-MIB", "stnExtIpAddrL3IpAddress"))
if mibBuilder.loadTexts: stnExtIpAddrL3Entry.setStatus('current')
stnExtIpAddrL3IpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIpAddrL3IpAddress.setStatus('current')
stnExtIpAddrL3IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIpAddrL3IfIndex.setStatus('current')
stnExtIpAddrL3SubnetIfInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIpAddrL3SubnetIfInstance.setStatus('current')
stnExtIpAddrL3IfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIpAddrL3IfName.setStatus('current')
stnExtIpAddrL3IpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtIpAddrL3IpMask.setStatus('current')
stnExtSubnetL3Table = MibTable((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4), )
if mibBuilder.loadTexts: stnExtSubnetL3Table.setStatus('current')
stnExtSubnetL3Entry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1), ).setIndexNames((0, "STN-EXTIF-MIB", "stnExtSubnetL3SubnetIfInstance"))
if mibBuilder.loadTexts: stnExtSubnetL3Entry.setStatus('current')
stnExtSubnetL3SubnetIfInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtSubnetL3SubnetIfInstance.setStatus('current')
stnExtSubnetL3IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtSubnetL3IfIndex.setStatus('current')
stnExtSubnetL3IfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtSubnetL3IfName.setStatus('current')
stnExtSubnetL3IpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtSubnetL3IpAddress.setStatus('current')
stnExtSubnetL3IpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnExtSubnetL3IpMask.setStatus('current')
mibBuilder.exportSymbols("STN-EXTIF-MIB", stnExtSubnetL3IfName=stnExtSubnetL3IfName, stnExtIfL3SubnetIfInstance=stnExtIfL3SubnetIfInstance, stnExtIfL3IfIndex=stnExtIfL3IfIndex, stnExtIfMibConformance=stnExtIfMibConformance, stnExtIf=stnExtIf, stnExtSubnetL3IpMask=stnExtSubnetL3IpMask, stnExtIpAddrL3IfIndex=stnExtIpAddrL3IfIndex, stnExtSubnetL3IpAddress=stnExtSubnetL3IpAddress, stnExtIpAddrL3Entry=stnExtIpAddrL3Entry, stnExtIfL3Entry=stnExtIfL3Entry, stnExtIfL2Entry=stnExtIfL2Entry, stnExtIpAddrL3IfName=stnExtIpAddrL3IfName, stnExtIfL3IpAddress=stnExtIfL3IpAddress, stnExtSubnetL3Table=stnExtSubnetL3Table, stnExtIfL3IpMask=stnExtIfL3IpMask, stnExtIfL2Table=stnExtIfL2Table, stnExtSubnetL3Entry=stnExtSubnetL3Entry, stnExtSubnetL3SubnetIfInstance=stnExtSubnetL3SubnetIfInstance, stnExtSubnetL3IfIndex=stnExtSubnetL3IfIndex, stnExtIfL2IfIndex=stnExtIfL2IfIndex, stnExtIfL2IfName=stnExtIfL2IfName, stnExtIfL3Table=stnExtIfL3Table, stnExtIpAddrL3IpAddress=stnExtIpAddrL3IpAddress, PYSNMP_MODULE_ID=stnExtIf, stnExtIfL3IfName=stnExtIfL3IfName, stnExtIfMibTraps=stnExtIfMibTraps, stnExtIpAddrL3Table=stnExtIpAddrL3Table, stnExtIpAddrL3SubnetIfInstance=stnExtIpAddrL3SubnetIfInstance, stnExtIfObjects=stnExtIfObjects, stnExtIpAddrL3IpMask=stnExtIpAddrL3IpMask)
