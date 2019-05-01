#
# PySNMP MIB module COLUBRIS-DEVICE-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-DEVICE-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:25:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
coDevDisIndex, = mibBuilder.importSymbols("COLUBRIS-DEVICE-MIB", "coDevDisIndex")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, MibIdentifier, Integer32, Counter64, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, iso, NotificationType, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "MibIdentifier", "Integer32", "Counter64", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "iso", "NotificationType", "TimeTicks", "Counter32")
DisplayString, MacAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention", "TruthValue")
colubrisDeviceIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 24))
if mibBuilder.loadTexts: colubrisDeviceIfMIB.setLastUpdated('200901140000Z')
if mibBuilder.loadTexts: colubrisDeviceIfMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisDeviceIfMIB.setContactInfo('Colubris Networks Postal: 200 West Street Ste 300 Waltham, Massachusetts 02451-1121 UNITED STATES Phone: +1 781 684 0001 Fax: +1 781 684 0009 E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisDeviceIfMIB.setDescription('Colubris Device Interface MIB.')
colubrisDeviceIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1))
coDeviceIfStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1))
coDeviceIfStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2))
coDeviceIfFdbGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3))
coDeviceIfStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1), )
if mibBuilder.loadTexts: coDeviceIfStatusTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceIfStatusTable.setDescription('Device interface status attributes.')
coDeviceIfStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-IF-MIB", "coDevIfStaIfIndex"))
if mibBuilder.loadTexts: coDeviceIfStatusEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceIfStatusEntry.setDescription('An entry in the coDeviceIfStatusTable. coDevDisIndex - Uniquely identifies a device on the controller. coDevIfStaIfIndex - Uniquely identifies an interface on the device.')
coDevIfStaIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevIfStaIfIndex.setStatus('current')
if mibBuilder.loadTexts: coDevIfStaIfIndex.setDescription('Specifies the index of an interface on the device.')
coDevIfStaFriendlyInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaFriendlyInterfaceName.setStatus('current')
if mibBuilder.loadTexts: coDevIfStaFriendlyInterfaceName.setDescription('The friendly name associated with the interface.')
coDevIfStaType = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("ethernet", 2), ("l2vlan", 3), ("bridge", 4), ("ieee80211", 5), ("ieee80211Wds", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaType.setStatus('current')
if mibBuilder.loadTexts: coDevIfStaType.setDescription('The current state of the interface.')
coDevIfStaVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaVLAN.setStatus('current')
if mibBuilder.loadTexts: coDevIfStaVLAN.setDescription('Specifies the VLAN associated with the interface. The value 0 is used when coDevIfStaType is not set to l2vlan.')
coDevIfStaIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaIpAddress.setStatus('current')
if mibBuilder.loadTexts: coDevIfStaIpAddress.setDescription('The IP address assigned to the interface.')
coDevIfStaNetworkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaNetworkMask.setStatus('current')
if mibBuilder.loadTexts: coDevIfStaNetworkMask.setDescription('The network mask assigned to the interface.')
coDevIfStaMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaMACAddress.setStatus('current')
if mibBuilder.loadTexts: coDevIfStaMACAddress.setDescription('The MAC address assigned to the interface.')
coDevIfStaState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaState.setStatus('current')
if mibBuilder.loadTexts: coDevIfStaState.setDescription('The current state of the interface.')
coDevIfStaPowerForwardingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaPowerForwardingStatus.setStatus('current')
if mibBuilder.loadTexts: coDevIfStaPowerForwardingStatus.setDescription('When True indicates that power forwarding is enabled on this Ethernet port.')
coDeviceIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceIfStatsTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceIfStatsTable.setDescription('Device interface statistic attributes.')
coDeviceIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1), )
coDeviceIfStatusEntry.registerAugmentions(("COLUBRIS-DEVICE-IF-MIB", "coDeviceIfStatsEntry"))
coDeviceIfStatsEntry.setIndexNames(*coDeviceIfStatusEntry.getIndexNames())
if mibBuilder.loadTexts: coDeviceIfStatsEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceIfStatsEntry.setDescription('An entry in the coDeviceIfStatsTable. coDevDisIndex - Uniquely identify a device on the controller. coDevIfStaIfIndex - Uniquely identify an interface on the device.')
coDevIfStsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsRxBytes.setStatus('current')
if mibBuilder.loadTexts: coDevIfStsRxBytes.setDescription('The total number of octets received on the interface.')
coDevIfStsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsRxPackets.setStatus('current')
if mibBuilder.loadTexts: coDevIfStsRxPackets.setDescription('The number of packets delivered by this sub-layer to a higher (sub-)layer.')
coDevIfStsRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsRxErrors.setStatus('current')
if mibBuilder.loadTexts: coDevIfStsRxErrors.setDescription('The number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.')
coDevIfStsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsTxBytes.setStatus('current')
if mibBuilder.loadTexts: coDevIfStsTxBytes.setDescription('The total number of octets transmitted by the interface.')
coDevIfStsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsTxPackets.setStatus('current')
if mibBuilder.loadTexts: coDevIfStsTxPackets.setDescription('The total number of packets that higher-level protocols requested to be transmitted.')
coDevIfStsTxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsTxErrors.setStatus('current')
if mibBuilder.loadTexts: coDevIfStsTxErrors.setDescription('The number of outbound packets that could not be transmitted because of errors.')
coDeviceIfFdbTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1), )
if mibBuilder.loadTexts: coDeviceIfFdbTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceIfFdbTable.setDescription('This table contains the network forwarding databases.')
coDeviceIfFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-IF-MIB", "coDevIfStaIfIndex"), (0, "COLUBRIS-DEVICE-IF-MIB", "coDevIfFdbMacIndex"))
if mibBuilder.loadTexts: coDeviceIfFdbEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceIfFdbEntry.setDescription('An entry in the coDeviceIfFdbTable. coDevDisIndex - Uniquely identifies a device ion the controller. coDevIfStaIfIndex - Uniquely identifies an interface on the device. coDevIfFdbMacIndex - Uniquely identifies a remote device connected to an interface on the device.')
coDevIfFdbMacIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevIfFdbMacIndex.setStatus('current')
if mibBuilder.loadTexts: coDevIfFdbMacIndex.setDescription('Specifies the index of a remote device connected to an interface on the device.')
coDevIfFdbMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfFdbMACAddress.setStatus('current')
if mibBuilder.loadTexts: coDevIfFdbMACAddress.setDescription('The MAC address of the remote device.')
coDevIfFdbAuthorized = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfFdbAuthorized.setStatus('current')
if mibBuilder.loadTexts: coDevIfFdbAuthorized.setDescription('When True, indicates that traffic coming from this remote device is allowed.')
coDevIfFdbAgeing = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1, 1, 4), Integer32()).setUnits('msec').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfFdbAgeing.setStatus('current')
if mibBuilder.loadTexts: coDevIfFdbAgeing.setDescription('Indicates the elapsed time when when the last frame was received for the remote device.')
colubrisDeviceIfMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 2))
colubrisDeviceIfMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 2, 0))
colubrisDeviceIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3))
colubrisDeviceIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 1))
colubrisDeviceIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 2))
colubrisDeviceIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 1, 1)).setObjects(("COLUBRIS-DEVICE-IF-MIB", "colubrisDeviceIfStatusMIBGroup"), ("COLUBRIS-DEVICE-IF-MIB", "colubrisDeviceIfStatsMIBGroup"), ("COLUBRIS-DEVICE-IF-MIB", "colubrisDeviceIfFdbMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceIfMIBCompliance = colubrisDeviceIfMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceIfMIBCompliance.setDescription('The compliance statement for the device Interface MIB.')
colubrisDeviceIfStatusMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 2, 1)).setObjects(("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaFriendlyInterfaceName"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaType"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaVLAN"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaIpAddress"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaNetworkMask"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaMACAddress"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaState"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaPowerForwardingStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceIfStatusMIBGroup = colubrisDeviceIfStatusMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceIfStatusMIBGroup.setDescription('A collection of objects for the device Interface Status group.')
colubrisDeviceIfStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 2, 2)).setObjects(("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsRxBytes"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsRxPackets"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsRxErrors"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsTxBytes"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsTxPackets"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsTxErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceIfStatsMIBGroup = colubrisDeviceIfStatsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceIfStatsMIBGroup.setDescription('A collection of objects for the device Interface Stats group.')
colubrisDeviceIfFdbMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 2, 3)).setObjects(("COLUBRIS-DEVICE-IF-MIB", "coDevIfFdbMACAddress"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfFdbAuthorized"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfFdbAgeing"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceIfFdbMIBGroup = colubrisDeviceIfFdbMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceIfFdbMIBGroup.setDescription('A collection of objects for the device Interface FDB group.')
mibBuilder.exportSymbols("COLUBRIS-DEVICE-IF-MIB", colubrisDeviceIfMIBObjects=colubrisDeviceIfMIBObjects, coDeviceIfStatusGroup=coDeviceIfStatusGroup, colubrisDeviceIfFdbMIBGroup=colubrisDeviceIfFdbMIBGroup, coDeviceIfFdbGroup=coDeviceIfFdbGroup, coDeviceIfStatsGroup=coDeviceIfStatsGroup, coDeviceIfFdbEntry=coDeviceIfFdbEntry, colubrisDeviceIfMIBCompliance=colubrisDeviceIfMIBCompliance, coDevIfStaVLAN=coDevIfStaVLAN, coDevIfStsRxBytes=coDevIfStsRxBytes, coDevIfStsRxPackets=coDevIfStsRxPackets, coDevIfStaFriendlyInterfaceName=coDevIfStaFriendlyInterfaceName, coDevIfStsRxErrors=coDevIfStsRxErrors, coDevIfStaMACAddress=coDevIfStaMACAddress, coDevIfStaIpAddress=coDevIfStaIpAddress, coDevIfFdbAuthorized=coDevIfFdbAuthorized, coDevIfStsTxBytes=coDevIfStsTxBytes, colubrisDeviceIfMIBNotificationPrefix=colubrisDeviceIfMIBNotificationPrefix, coDeviceIfFdbTable=coDeviceIfFdbTable, PYSNMP_MODULE_ID=colubrisDeviceIfMIB, colubrisDeviceIfMIBCompliances=colubrisDeviceIfMIBCompliances, colubrisDeviceIfStatsMIBGroup=colubrisDeviceIfStatsMIBGroup, colubrisDeviceIfStatusMIBGroup=colubrisDeviceIfStatusMIBGroup, colubrisDeviceIfMIB=colubrisDeviceIfMIB, colubrisDeviceIfMIBNotifications=colubrisDeviceIfMIBNotifications, coDevIfStaType=coDevIfStaType, coDeviceIfStatsEntry=coDeviceIfStatsEntry, colubrisDeviceIfMIBConformance=colubrisDeviceIfMIBConformance, coDeviceIfStatusEntry=coDeviceIfStatusEntry, coDeviceIfStatsTable=coDeviceIfStatsTable, coDevIfStaIfIndex=coDevIfStaIfIndex, colubrisDeviceIfMIBGroups=colubrisDeviceIfMIBGroups, coDevIfFdbMACAddress=coDevIfFdbMACAddress, coDevIfFdbAgeing=coDevIfFdbAgeing, coDeviceIfStatusTable=coDeviceIfStatusTable, coDevIfStsTxPackets=coDevIfStsTxPackets, coDevIfStaState=coDevIfStaState, coDevIfStaNetworkMask=coDevIfStaNetworkMask, coDevIfStsTxErrors=coDevIfStsTxErrors, coDevIfFdbMacIndex=coDevIfFdbMacIndex, coDevIfStaPowerForwardingStatus=coDevIfStaPowerForwardingStatus)
