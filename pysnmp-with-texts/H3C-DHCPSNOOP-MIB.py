#
# PySNMP MIB module H3C-DHCPSNOOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-DHCPSNOOP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:21:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
hwdot1qVlanIndex, = mibBuilder.importSymbols("HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter32, Integer32, Counter64, Gauge32, ObjectIdentity, ModuleIdentity, Bits, Unsigned32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter32", "Integer32", "Counter64", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Bits", "Unsigned32", "MibIdentifier", "iso")
TruthValue, DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
h3cDhcpSnoop = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36))
if mibBuilder.loadTexts: h3cDhcpSnoop.setLastUpdated('200501140000Z')
if mibBuilder.loadTexts: h3cDhcpSnoop.setOrganization('Huawei-3com Technologies Co.,Ltd.')
if mibBuilder.loadTexts: h3cDhcpSnoop.setContactInfo('Platform Team Beijing Institute Huawei-3com Tech, Inc. Http:\\\\www.huawei-3com.com E-mail:support@huawei-3com.com')
if mibBuilder.loadTexts: h3cDhcpSnoop.setDescription('The private mib file includes the DHCP Snooping profile.')
h3cDhcpSnoopMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1))
h3cDhcpSnoopEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDhcpSnoopEnable.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopEnable.setDescription('DHCP Snooping status (enable or disable).')
h3cDhcpSnoopTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2), )
if mibBuilder.loadTexts: h3cDhcpSnoopTable.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopTable.setDescription("The table containing information of DHCP clients listened by DHCP snooping and it's enabled or disabled by setting h3cDhcpSnoopEnable node.")
h3cDhcpSnoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1), ).setIndexNames((0, "H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopClientIpAddressType"), (0, "H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopClientIpAddress"))
if mibBuilder.loadTexts: h3cDhcpSnoopEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopEntry.setDescription('An entry containing information of DHCP clients.')
h3cDhcpSnoopClientIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 1), InetAddressType().clone('ipv4'))
if mibBuilder.loadTexts: h3cDhcpSnoopClientIpAddressType.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopClientIpAddressType.setDescription("DHCP clients' IP addresses type (IPv4 or IPv6).")
h3cDhcpSnoopClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: h3cDhcpSnoopClientIpAddress.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopClientIpAddress.setDescription("DHCP clients' IP addresses collected by DHCP snooping.")
h3cDhcpSnoopClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDhcpSnoopClientMacAddress.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopClientMacAddress.setDescription("DHCP clients' MAC addresses collected by DHCP snooping.")
h3cDhcpSnoopClientProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDhcpSnoopClientProperty.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopClientProperty.setDescription('Method of getting IP addresses collected by DHCP snooping.')
h3cDhcpSnoopClientUnitNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDhcpSnoopClientUnitNum.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopClientUnitNum.setDescription('IRF (Intelligent Resilient Fabric) unit number via whom the clients get their IP addresses. The value 0 means this device does not support IRF.')
h3cDhcpSnoopTrustTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 3), )
if mibBuilder.loadTexts: h3cDhcpSnoopTrustTable.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopTrustTable.setDescription('A table is used to configure and monitor port trusted status.')
h3cDhcpSnoopTrustEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cDhcpSnoopTrustEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopTrustEntry.setDescription('An entry containing information about trusted status of ports.')
h3cDhcpSnoopTrustStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("untrusted", 0), ("trusted", 1))).clone('untrusted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDhcpSnoopTrustStatus.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopTrustStatus.setDescription('Trusted status of current port which supports both get and set operation.')
h3cDhcpSnoopVlanTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4), )
if mibBuilder.loadTexts: h3cDhcpSnoopVlanTable.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopVlanTable.setDescription('A table is used to configure and monitor DHCP Snooping status of VLANs.')
h3cDhcpSnoopVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4, 1), ).setIndexNames((0, "H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopVlanIndex"))
if mibBuilder.loadTexts: h3cDhcpSnoopVlanEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopVlanEntry.setDescription('The entry information about h3cDhcpSnoopVlanTable.')
h3cDhcpSnoopVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: h3cDhcpSnoopVlanIndex.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopVlanIndex.setDescription('Current VLAN index.')
h3cDhcpSnoopVlanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDhcpSnoopVlanEnable.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopVlanEnable.setDescription('DHCP Snooping status of current VLAN.')
h3cDhcpSnoopTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2))
h3cDhcpSnoopTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 0))
h3cDhcpSnoopTrapsObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 1))
h3cDhcpSnoopSpoofServerMac = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDhcpSnoopSpoofServerMac.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopSpoofServerMac.setDescription('MAC address of the spoofing server and it is derived from link-layer header of offer packet. If the offer packet is relayed by dhcp relay entity, it may be the MAC address of relay entity. ')
h3cDhcpSnoopSpoofServerIP = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 1, 2), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDhcpSnoopSpoofServerIP.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopSpoofServerIP.setDescription("IP address of the spoofing server and it is derived from IP header of offer packet. A tricksy host may send offer packet use other host's address, so this address can not always be trust. ")
h3cDhcpSnoopSpoofServerDetected = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"), ("H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopSpoofServerMac"), ("H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopSpoofServerIP"))
if mibBuilder.loadTexts: h3cDhcpSnoopSpoofServerDetected.setStatus('current')
if mibBuilder.loadTexts: h3cDhcpSnoopSpoofServerDetected.setDescription('To detect unauthorized DHCP servers on a network, the DHCP snooping device sends DHCP-DISCOVER messages through its downstream port (which is connected to the DHCP clients). If any response (DHCP-OFFER message) is received from the downstream port, an unauthorized DHCP server is considered present, and then the device sends a trap. With unauthorized DHCP server detection enabled, the interface sends a DHCP-DISCOVER message to detect unauthorized DHCP servers on the network. If this interface receives a DHCP-OFFER message, the DHCP server which sent it is considered unauthorized. ')
mibBuilder.exportSymbols("H3C-DHCPSNOOP-MIB", h3cDhcpSnoopTrapsObject=h3cDhcpSnoopTrapsObject, h3cDhcpSnoopTrustTable=h3cDhcpSnoopTrustTable, h3cDhcpSnoopClientProperty=h3cDhcpSnoopClientProperty, h3cDhcpSnoopClientIpAddress=h3cDhcpSnoopClientIpAddress, h3cDhcpSnoopVlanIndex=h3cDhcpSnoopVlanIndex, h3cDhcpSnoopSpoofServerMac=h3cDhcpSnoopSpoofServerMac, h3cDhcpSnoopSpoofServerIP=h3cDhcpSnoopSpoofServerIP, h3cDhcpSnoopTrapsPrefix=h3cDhcpSnoopTrapsPrefix, h3cDhcpSnoopEntry=h3cDhcpSnoopEntry, h3cDhcpSnoopVlanEntry=h3cDhcpSnoopVlanEntry, h3cDhcpSnoopTraps=h3cDhcpSnoopTraps, h3cDhcpSnoopClientMacAddress=h3cDhcpSnoopClientMacAddress, h3cDhcpSnoopTrustStatus=h3cDhcpSnoopTrustStatus, h3cDhcpSnoopClientUnitNum=h3cDhcpSnoopClientUnitNum, h3cDhcpSnoopTable=h3cDhcpSnoopTable, h3cDhcpSnoopEnable=h3cDhcpSnoopEnable, h3cDhcpSnoop=h3cDhcpSnoop, h3cDhcpSnoopMibObject=h3cDhcpSnoopMibObject, h3cDhcpSnoopTrustEntry=h3cDhcpSnoopTrustEntry, h3cDhcpSnoopVlanEnable=h3cDhcpSnoopVlanEnable, h3cDhcpSnoopSpoofServerDetected=h3cDhcpSnoopSpoofServerDetected, h3cDhcpSnoopVlanTable=h3cDhcpSnoopVlanTable, PYSNMP_MODULE_ID=h3cDhcpSnoop, h3cDhcpSnoopClientIpAddressType=h3cDhcpSnoopClientIpAddressType)
