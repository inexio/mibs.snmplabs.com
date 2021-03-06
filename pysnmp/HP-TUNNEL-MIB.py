#
# PySNMP MIB module HP-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:24:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, TimeTicks, iso, Gauge32, Unsigned32, Counter32, Counter64, ModuleIdentity, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "TimeTicks", "iso", "Gauge32", "Unsigned32", "Counter32", "Counter64", "ModuleIdentity", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
tunnelIfRemoteInetAddress, tunnelIfEntry, tunnelIfLocalInetAddress, tunnelIfAddressType, tunnelInetConfigEntry = mibBuilder.importSymbols("TUNNEL-MIB", "tunnelIfRemoteInetAddress", "tunnelIfEntry", "tunnelIfLocalInetAddress", "tunnelIfAddressType", "tunnelInetConfigEntry")
hpTunnelMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77))
hpTunnelMIB.setRevisions(('2015-02-02 00:00', '2014-08-15 00:00', '2014-08-13 00:00', '2010-07-22 00:00',))
if mibBuilder.loadTexts: hpTunnelMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: hpTunnelMIB.setOrganization('HP Networking')
hpTunnelNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 0))
hpTunnelObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1))
hpTunnelConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2))
class HpTunnelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unspecified", 1), ("direct4in4", 2), ("direct6in4", 3), ("direct6in4Ipsec", 4), ("direct6in6", 5), ("ipsecIpv4", 6), ("ipsecIpv6", 7), ("macinudp", 8))

hpTunnelConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1), )
if mibBuilder.loadTexts: hpTunnelConfigTable.setStatus('current')
hpTunnelConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1, 1), ).setIndexNames((0, "HP-TUNNEL-MIB", "hpTunnelID"))
if mibBuilder.loadTexts: hpTunnelConfigEntry.setStatus('current')
hpTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpTunnelID.setStatus('current')
hpTunnelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpTunnelIfIndex.setStatus('deprecated')
hpTunnelRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpTunnelRowStatus.setStatus('current')
hpTunnelInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpTunnelInterfaceIndex.setStatus('current')
hpTunnelIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2), )
if mibBuilder.loadTexts: hpTunnelIfTable.setStatus('current')
hpTunnelIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1), )
tunnelIfEntry.registerAugmentions(("HP-TUNNEL-MIB", "hpTunnelIfEntry"))
hpTunnelIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())
if mibBuilder.loadTexts: hpTunnelIfEntry.setStatus('current')
hpTunnelIfPMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpTunnelIfPMTU.setStatus('current')
hpTunnelIfNUD = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpTunnelIfNUD.setStatus('current')
hpTunnelIfMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1, 3), Unsigned32().clone(1280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpTunnelIfMTU.setStatus('current')
hpTunnelEncapsMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1, 4), HpTunnelType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpTunnelEncapsMethod.setStatus('current')
hpTunnelIpsecName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpTunnelIpsecName.setStatus('current')
hpTunnelInetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 3), )
if mibBuilder.loadTexts: hpTunnelInetConfigTable.setStatus('current')
hpTunnelInetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 3, 1), )
tunnelInetConfigEntry.registerAugmentions(("HP-TUNNEL-MIB", "hpTunnelInetConfigEntry"))
hpTunnelInetConfigEntry.setIndexNames(*tunnelInetConfigEntry.getIndexNames())
if mibBuilder.loadTexts: hpTunnelInetConfigEntry.setStatus('current')
hpTunnelInetConfigEncapsMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 3, 1, 1), HpTunnelType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpTunnelInetConfigEncapsMethod.setStatus('current')
hpTunnelNotifyScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6))
hpTunnelMTUDropRouterAddrType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpTunnelMTUDropRouterAddrType.setStatus('current')
hpTunnelMTUDropRouterAddr = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpTunnelMTUDropRouterAddr.setStatus('current')
hpTunnelMTUDropRouterMTU = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpTunnelMTUDropRouterMTU.setStatus('current')
hpTunnelMTUDropTunnelSrcAddrType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 4), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpTunnelMTUDropTunnelSrcAddrType.setStatus('current')
hpTunnelMTUDropTunnelSource = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 5), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpTunnelMTUDropTunnelSource.setStatus('current')
hpTunnelMTUDropTunnelDstAddrType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 6), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpTunnelMTUDropTunnelDstAddrType.setStatus('current')
hpTunnelMTUDropTunnelDest = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 7), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpTunnelMTUDropTunnelDest.setStatus('current')
hpTunnelMTUDropInIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 8), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpTunnelMTUDropInIfIndex.setStatus('current')
hpTunnelMTUDropNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpTunnelMTUDropNotifyEnable.setStatus('current')
hpTunnelIcmpErrorRcvd = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 0, 1)).setObjects(("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterAddrType"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterAddr"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterMTU"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelSrcAddrType"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelSource"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelDstAddrType"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelDest"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropInIfIndex"), ("TUNNEL-MIB", "tunnelIfAddressType"), ("TUNNEL-MIB", "tunnelIfLocalInetAddress"), ("TUNNEL-MIB", "tunnelIfRemoteInetAddress"))
if mibBuilder.loadTexts: hpTunnelIcmpErrorRcvd.setStatus('current')
hpicfVlanTunnelMappingTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 4), )
if mibBuilder.loadTexts: hpicfVlanTunnelMappingTable.setStatus('current')
hpicfVlanTunnelMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 4, 1), ).setIndexNames((0, "HP-TUNNEL-MIB", "hpicfVLANIndex"), (0, "HP-TUNNEL-MIB", "hpicfTunnelIfIndex"))
if mibBuilder.loadTexts: hpicfVlanTunnelMappingEntry.setStatus('current')
hpicfVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 4, 1, 1), VlanIndex())
if mibBuilder.loadTexts: hpicfVLANIndex.setStatus('current')
hpicfTunnelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 4, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: hpicfTunnelIfIndex.setStatus('current')
hpicfVlanTunnelMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVlanTunnelMappingRowStatus.setStatus('current')
hpicfUDPTunnelTypeTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 5), )
if mibBuilder.loadTexts: hpicfUDPTunnelTypeTable.setStatus('current')
hpicfUDPTunnelTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 5, 1), )
tunnelInetConfigEntry.registerAugmentions(("HP-TUNNEL-MIB", "hpicfUDPTunnelTypeEntry"))
hpicfUDPTunnelTypeEntry.setIndexNames(*tunnelInetConfigEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfUDPTunnelTypeEntry.setStatus('current')
hpicfUDPTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("remotemirror", 1), ("vxlan", 2))).clone('remotemirror')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfUDPTunnelType.setStatus('current')
hpTunnelMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 1))
hpTunnelMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2))
hpTunnelMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 1, 1)).setObjects(("HP-TUNNEL-MIB", "hpTunnelProvisionGroup"), ("HP-TUNNEL-MIB", "hpTunnelInetConfigGroup"), ("HP-TUNNEL-MIB", "hpVlanTunnelMappingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTunnelMIBCompliance = hpTunnelMIBCompliance.setStatus('deprecated')
hpTunnelMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 1, 2)).setObjects(("HP-TUNNEL-MIB", "hpTunnelProvisionGroup2"), ("HP-TUNNEL-MIB", "hpTunnelInetConfigGroup"), ("HP-TUNNEL-MIB", "hpTunnelNotifyScalarsGroup"), ("HP-TUNNEL-MIB", "hpTunnelNotificationsGroup"), ("HP-TUNNEL-MIB", "hpVlanTunnelMappingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTunnelMIBCompliance2 = hpTunnelMIBCompliance2.setStatus('current')
hpTunnelProvisionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 1)).setObjects(("HP-TUNNEL-MIB", "hpTunnelIfIndex"), ("HP-TUNNEL-MIB", "hpTunnelEncapsMethod"), ("HP-TUNNEL-MIB", "hpTunnelIfPMTU"), ("HP-TUNNEL-MIB", "hpTunnelIfMTU"), ("HP-TUNNEL-MIB", "hpTunnelIfNUD"), ("HP-TUNNEL-MIB", "hpTunnelRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTunnelProvisionGroup = hpTunnelProvisionGroup.setStatus('deprecated')
hpTunnelInetConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 2)).setObjects(("HP-TUNNEL-MIB", "hpTunnelInetConfigEncapsMethod"), ("HP-TUNNEL-MIB", "hpTunnelIpsecName"), ("HP-TUNNEL-MIB", "hpicfUDPTunnelType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTunnelInetConfigGroup = hpTunnelInetConfigGroup.setStatus('current')
hpVlanTunnelMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 3)).setObjects(("HP-TUNNEL-MIB", "hpicfVlanTunnelMappingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpVlanTunnelMappingGroup = hpVlanTunnelMappingGroup.setStatus('current')
hpTunnelProvisionGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 4)).setObjects(("HP-TUNNEL-MIB", "hpTunnelInterfaceIndex"), ("HP-TUNNEL-MIB", "hpTunnelEncapsMethod"), ("HP-TUNNEL-MIB", "hpTunnelIfPMTU"), ("HP-TUNNEL-MIB", "hpTunnelIfMTU"), ("HP-TUNNEL-MIB", "hpTunnelIfNUD"), ("HP-TUNNEL-MIB", "hpTunnelRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTunnelProvisionGroup2 = hpTunnelProvisionGroup2.setStatus('current')
hpTunnelNotifyScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 5)).setObjects(("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterAddrType"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterAddr"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterMTU"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelSrcAddrType"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelSource"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelDstAddrType"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelDest"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropInIfIndex"), ("HP-TUNNEL-MIB", "hpTunnelMTUDropNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTunnelNotifyScalarsGroup = hpTunnelNotifyScalarsGroup.setStatus('current')
hpTunnelNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 6)).setObjects(("HP-TUNNEL-MIB", "hpTunnelIcmpErrorRcvd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTunnelNotificationsGroup = hpTunnelNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("HP-TUNNEL-MIB", hpTunnelProvisionGroup2=hpTunnelProvisionGroup2, hpicfVLANIndex=hpicfVLANIndex, hpTunnelMTUDropRouterAddrType=hpTunnelMTUDropRouterAddrType, PYSNMP_MODULE_ID=hpTunnelMIB, hpTunnelInetConfigGroup=hpTunnelInetConfigGroup, hpicfVlanTunnelMappingTable=hpicfVlanTunnelMappingTable, hpicfVlanTunnelMappingRowStatus=hpicfVlanTunnelMappingRowStatus, hpicfUDPTunnelTypeEntry=hpicfUDPTunnelTypeEntry, hpTunnelMTUDropRouterAddr=hpTunnelMTUDropRouterAddr, hpicfVlanTunnelMappingEntry=hpicfVlanTunnelMappingEntry, hpTunnelNotifyScalars=hpTunnelNotifyScalars, hpTunnelConfigTable=hpTunnelConfigTable, hpTunnelObjects=hpTunnelObjects, hpTunnelInetConfigEntry=hpTunnelInetConfigEntry, hpTunnelMTUDropTunnelDstAddrType=hpTunnelMTUDropTunnelDstAddrType, hpTunnelIpsecName=hpTunnelIpsecName, hpTunnelMTUDropTunnelSource=hpTunnelMTUDropTunnelSource, hpTunnelIcmpErrorRcvd=hpTunnelIcmpErrorRcvd, hpVlanTunnelMappingGroup=hpVlanTunnelMappingGroup, hpTunnelInetConfigEncapsMethod=hpTunnelInetConfigEncapsMethod, hpTunnelNotifyScalarsGroup=hpTunnelNotifyScalarsGroup, hpTunnelIfNUD=hpTunnelIfNUD, hpicfUDPTunnelTypeTable=hpicfUDPTunnelTypeTable, hpTunnelMTUDropNotifyEnable=hpTunnelMTUDropNotifyEnable, hpTunnelInetConfigTable=hpTunnelInetConfigTable, hpTunnelIfIndex=hpTunnelIfIndex, hpTunnelID=hpTunnelID, hpTunnelConformance=hpTunnelConformance, hpTunnelInterfaceIndex=hpTunnelInterfaceIndex, hpTunnelMTUDropRouterMTU=hpTunnelMTUDropRouterMTU, hpTunnelProvisionGroup=hpTunnelProvisionGroup, hpTunnelNotificationsGroup=hpTunnelNotificationsGroup, hpTunnelMIBCompliance2=hpTunnelMIBCompliance2, hpTunnelIfPMTU=hpTunnelIfPMTU, HpTunnelType=HpTunnelType, hpTunnelNotifications=hpTunnelNotifications, hpicfUDPTunnelType=hpicfUDPTunnelType, hpTunnelConfigEntry=hpTunnelConfigEntry, hpTunnelMTUDropTunnelDest=hpTunnelMTUDropTunnelDest, hpicfTunnelIfIndex=hpicfTunnelIfIndex, hpTunnelMIBGroups=hpTunnelMIBGroups, hpTunnelMIBCompliance=hpTunnelMIBCompliance, hpTunnelMTUDropInIfIndex=hpTunnelMTUDropInIfIndex, hpTunnelMIB=hpTunnelMIB, hpTunnelRowStatus=hpTunnelRowStatus, hpTunnelIfTable=hpTunnelIfTable, hpTunnelIfMTU=hpTunnelIfMTU, hpTunnelMIBCompliances=hpTunnelMIBCompliances, hpTunnelMTUDropTunnelSrcAddrType=hpTunnelMTUDropTunnelSrcAddrType, hpTunnelIfEntry=hpTunnelIfEntry, hpTunnelEncapsMethod=hpTunnelEncapsMethod)
