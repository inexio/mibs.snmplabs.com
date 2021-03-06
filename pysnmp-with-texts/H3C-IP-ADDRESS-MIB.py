#
# PySNMP MIB module H3C-IP-ADDRESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-IP-ADDRESS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:22:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, IpAddress, Bits, NotificationType, Unsigned32, ModuleIdentity, Counter32, Counter64, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "IpAddress", "Bits", "NotificationType", "Unsigned32", "ModuleIdentity", "Counter32", "Counter64", "ObjectIdentity", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
h3cIpAddrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67))
h3cIpAddrMIB.setRevisions(('2005-11-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cIpAddrMIB.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: h3cIpAddrMIB.setLastUpdated('200511220000Z')
if mibBuilder.loadTexts: h3cIpAddrMIB.setOrganization('H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cIpAddrMIB.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: h3cIpAddrMIB.setDescription('The MIB module for managing IPv4 address.')
h3cIpAddressObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1))
h3cIpAddressConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1))
h3cIpAddrSetTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 1), )
if mibBuilder.loadTexts: h3cIpAddrSetTable.setReference('RFC 2011')
if mibBuilder.loadTexts: h3cIpAddrSetTable.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrSetTable.setDescription("The table of address information is relevant to this entity's IPv4 addresses for setting. The address information that can be read and set in this table is a subset of the address information that can be read in h3cIpAddrReadTable and ipAddrTable in IP-MIB. This table is used to configure IPv4 addresses of an interface identified by h3cIpAddrSetIfIndex. When users create or delete an entry in this table, the agent also increases or reduces a corresponding entry in the h3cIpAddrReadTable and ipAddrTable in IP-MIB. When an interface which has been assigned IPv6 address is deleted, the agent also deletes the entry corresponding to the interface in this table and h3cIpAddrReadTable. All IPv4 addresses in this table will also show in ipAddrTable in IP-MIB. ")
h3cIpAddrSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 1, 1), ).setIndexNames((0, "H3C-IP-ADDRESS-MIB", "h3cIpAddrSetIfIndex"), (0, "H3C-IP-ADDRESS-MIB", "h3cIpAddrSetAddrType"), (0, "H3C-IP-ADDRESS-MIB", "h3cIpAddrSetAddr"))
if mibBuilder.loadTexts: h3cIpAddrSetEntry.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrSetEntry.setDescription('Define the IPv4 address information. ')
h3cIpAddrSetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cIpAddrSetIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrSetIfIndex.setDescription("The index value which uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of RFC 1573's ifIndex. ")
h3cIpAddrSetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 1, 1, 2), InetAddressType())
if mibBuilder.loadTexts: h3cIpAddrSetAddrType.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrSetAddrType.setDescription("The IP address type to which this entry's address information pertains. The value must be ipv4. ")
h3cIpAddrSetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 1, 1, 3), InetAddress())
if mibBuilder.loadTexts: h3cIpAddrSetAddr.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrSetAddr.setDescription("The IPv4 address to which this entry's address information pertains. ")
h3cIpAddrSetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cIpAddrSetMask.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrSetMask.setDescription('The subnet mask associated with the IPv4 address of this entry. The value of the mask is an IPv4 address with all the network bits set to 1 and all the hosts bits set to 0. ')
h3cIpAddrSetSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("assignedIp", 1))).clone('assignedIp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cIpAddrSetSourceType.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrSetSourceType.setDescription('Indicate the type of source of the IPv4 address.')
h3cIpAddrSetCatalog = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("sub", 2))).clone('primary')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cIpAddrSetCatalog.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrSetCatalog.setDescription('Indicate the category of the IPv4 address.')
h3cIpAddrSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cIpAddrSetRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrSetRowStatus.setDescription('This object is used to create a new row or delete an existing row in this table, only support active, createAndGo and destroy. ')
h3cIpAddrReadTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 2), )
if mibBuilder.loadTexts: h3cIpAddrReadTable.setReference('RFC 2011')
if mibBuilder.loadTexts: h3cIpAddrReadTable.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrReadTable.setDescription("The table of address information is relevant to this entity's IP addresses for reading. This is the extension of the ipAddrTable in IP-MIB. All IPv4 addresses in this table will also show in ipAddrTable in IP-MIB. ")
h3cIpAddrReadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 2, 1), ).setIndexNames((0, "H3C-IP-ADDRESS-MIB", "h3cIpAddrReadIfIndex"), (0, "H3C-IP-ADDRESS-MIB", "h3cIpAddrReadAddrType"), (0, "H3C-IP-ADDRESS-MIB", "h3cIpAddrReadAddr"))
if mibBuilder.loadTexts: h3cIpAddrReadEntry.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrReadEntry.setDescription('Define the IPv4 address information. ')
h3cIpAddrReadIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cIpAddrReadIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrReadIfIndex.setDescription("The index value which uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of RFC 1573's ifIndex. ")
h3cIpAddrReadAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: h3cIpAddrReadAddrType.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrReadAddrType.setDescription("The IP address type to which this entry's address information pertains. The value must be ipv4. ")
h3cIpAddrReadAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 2, 1, 3), InetAddress())
if mibBuilder.loadTexts: h3cIpAddrReadAddr.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrReadAddr.setDescription("The IPv4 address to which this entry's address information pertains. ")
h3cIpAddrReadMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpAddrReadMask.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrReadMask.setDescription('The subnet mask associated with the IPv4 address of this entry. The value of the mask is an IPv4 address with all the network bits set to 1 and all the hosts bits set to 0. ')
h3cIpAddrReadSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("assignedIp", 1), ("cluster", 2), ("dhcp", 3), ("bootp", 4), ("negotiate", 5), ("unnumbered", 6), ("vrrp", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpAddrReadSourceType.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrReadSourceType.setDescription('Indicate the type of source of the IPv4 address.')
h3cIpAddrReadCatalog = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primary", 1), ("sub", 2), ("cluster", 3), ("vrrp", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpAddrReadCatalog.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrReadCatalog.setDescription('Indicate the category of the IPv4 address.')
h3cIpv4AddrTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 3), )
if mibBuilder.loadTexts: h3cIpv4AddrTable.setStatus('current')
if mibBuilder.loadTexts: h3cIpv4AddrTable.setDescription('This table is used to configure primary IPv4 address of an interface identified by ifIndex.')
h3cIpv4AddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cIpv4AddrEntry.setStatus('current')
if mibBuilder.loadTexts: h3cIpv4AddrEntry.setDescription('Define the IPv4 address information. ')
h3cIpv4AddrAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 3, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cIpv4AddrAddr.setStatus('current')
if mibBuilder.loadTexts: h3cIpv4AddrAddr.setDescription("The IPv4 address to which this entry's address information pertains. ")
h3cIpv4AddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cIpv4AddrMask.setStatus('current')
if mibBuilder.loadTexts: h3cIpv4AddrMask.setDescription('The subnet mask associated with the IPv4 address of this entry. The value of the mask is an IPv4 address with all the network bits set to 1 and all the hosts bits set to 0. ')
h3cIpv4AddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 1, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cIpv4AddrRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cIpv4AddrRowStatus.setDescription('This object is used to create a new row or delete an existing row in this table, only support active, notInService, createAndGo and destroy. ')
h3cIpAddrNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 2))
h3cIpAddrNotifyScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 2, 1))
h3cIpAddrNotifyIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIpAddrNotifyIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrNotifyIfIndex.setDescription('The IP address IfIndex of specified interface on the device.')
h3cIpAddrOldIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 2, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIpAddrOldIpAddress.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrOldIpAddress.setDescription('The Old IP address of specified interface on the device.')
h3cIpAddrNewIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 2, 1, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIpAddrNewIpAddress.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrNewIpAddress.setDescription('The New IP address of specified interface on the device.')
h3cIpAddrNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 2, 2))
h3cIpAddrNotifyObjectsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 2, 2, 0))
h3cIpAddressChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 67, 2, 2, 0, 1)).setObjects(("H3C-IP-ADDRESS-MIB", "h3cIpAddrNotifyIfIndex"), ("H3C-IP-ADDRESS-MIB", "h3cIpAddrOldIpAddress"), ("H3C-IP-ADDRESS-MIB", "h3cIpAddrNewIpAddress"))
if mibBuilder.loadTexts: h3cIpAddressChangeNotify.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddressChangeNotify.setDescription('This notification will be generated when the IP address of interface is changed. The change maybe originate from NMS, DHCP server or administrator. This notification announces useful IP address change. So it is triggered by significative IP address change.')
mibBuilder.exportSymbols("H3C-IP-ADDRESS-MIB", h3cIpAddrNotifyObjectsPrefix=h3cIpAddrNotifyObjectsPrefix, h3cIpAddrSetIfIndex=h3cIpAddrSetIfIndex, h3cIpAddrNotifyIfIndex=h3cIpAddrNotifyIfIndex, h3cIpAddrReadTable=h3cIpAddrReadTable, h3cIpAddressConfig=h3cIpAddressConfig, h3cIpAddressChangeNotify=h3cIpAddressChangeNotify, h3cIpAddrReadIfIndex=h3cIpAddrReadIfIndex, h3cIpAddrOldIpAddress=h3cIpAddrOldIpAddress, h3cIpAddrSetEntry=h3cIpAddrSetEntry, h3cIpAddrNotify=h3cIpAddrNotify, h3cIpAddrNewIpAddress=h3cIpAddrNewIpAddress, h3cIpAddrSetRowStatus=h3cIpAddrSetRowStatus, h3cIpAddrReadMask=h3cIpAddrReadMask, h3cIpAddrSetAddrType=h3cIpAddrSetAddrType, h3cIpv4AddrEntry=h3cIpv4AddrEntry, h3cIpAddrNotifyObjects=h3cIpAddrNotifyObjects, h3cIpAddrSetAddr=h3cIpAddrSetAddr, h3cIpAddrReadAddrType=h3cIpAddrReadAddrType, h3cIpAddrMIB=h3cIpAddrMIB, PYSNMP_MODULE_ID=h3cIpAddrMIB, h3cIpAddrReadSourceType=h3cIpAddrReadSourceType, h3cIpv4AddrRowStatus=h3cIpv4AddrRowStatus, h3cIpAddressObjects=h3cIpAddressObjects, h3cIpAddrSetMask=h3cIpAddrSetMask, h3cIpAddrReadEntry=h3cIpAddrReadEntry, h3cIpv4AddrTable=h3cIpv4AddrTable, h3cIpAddrSetCatalog=h3cIpAddrSetCatalog, h3cIpAddrNotifyScalarObjects=h3cIpAddrNotifyScalarObjects, h3cIpAddrReadCatalog=h3cIpAddrReadCatalog, h3cIpAddrSetTable=h3cIpAddrSetTable, h3cIpAddrReadAddr=h3cIpAddrReadAddr, h3cIpv4AddrMask=h3cIpv4AddrMask, h3cIpAddrSetSourceType=h3cIpAddrSetSourceType, h3cIpv4AddrAddr=h3cIpv4AddrAddr)
