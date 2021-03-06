#
# PySNMP MIB module PEPVPN-SPEEDFUSION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PEPVPN-SPEEDFUSION
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, TimeTicks, Gauge32, enterprises, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, MibIdentifier, Unsigned32, IpAddress, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "TimeTicks", "Gauge32", "enterprises", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "MibIdentifier", "Unsigned32", "IpAddress", "Counter64", "iso")
MacAddress, RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
pepwave = MibIdentifier((1, 3, 6, 1, 4, 1, 27662))
productMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200))
generalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1))
pepvpnMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10))
pepvpn = ModuleIdentity((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1))
if mibBuilder.loadTexts: pepvpn.setLastUpdated('201305140000Z')
if mibBuilder.loadTexts: pepvpn.setOrganization('PEPWAVE')
pepVpnInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1))
pepVpnStatusTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2), )
if mibBuilder.loadTexts: pepVpnStatusTable.setStatus('current')
pepVpnStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1), ).setIndexNames((0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"))
if mibBuilder.loadTexts: pepVpnStatusEntry.setStatus('current')
pepVpnStatusId = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusId.setStatus('current')
pepVpnStatusProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusProfileName.setStatus('current')
pepVpnStatusConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("start", 0), ("authen", 1), ("tunnel", 2), ("route", 3), ("connected", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusConnectionState.setStatus('current')
pepVpnStatusEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("off", 1), ("aes256", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusEncryption.setStatus('current')
pepVpnStatusL2Bridging = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusL2Bridging.setStatus('current')
pepVpnStatusL2Vlan = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusL2Vlan.setStatus('current')
pepVpnRemotePeerId = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnRemotePeerId.setStatus('current')
pepVpnRemotePeer = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnRemotePeer.setStatus('current')
pepVpnStatusWanTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3), )
if mibBuilder.loadTexts: pepVpnStatusWanTable.setStatus('current')
pepVpnStatusWanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1), ).setIndexNames((0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnStatusWanId"))
if mibBuilder.loadTexts: pepVpnStatusWanEntry.setStatus('current')
pepVpnStatusWanId = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanId.setStatus('current')
pepVpnStatusWanName = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanName.setStatus('current')
pepVpnStatusWanTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanTxBytes.setStatus('current')
pepVpnStatusWanRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanRxBytes.setStatus('current')
pepVpnStatusWanDropPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanDropPackets.setStatus('current')
pepVpnStatusWanLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanLatency.setStatus('current')
pepVpnStatusRemoteNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4), )
if mibBuilder.loadTexts: pepVpnStatusRemoteNetworkTable.setStatus('current')
pepVpnStatusRemoteNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1), ).setIndexNames((0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnStatusRemoteNetowrkId"))
if mibBuilder.loadTexts: pepVpnStatusRemoteNetworkEntry.setStatus('current')
pepVpnStatusRemoteNetowrkId = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusRemoteNetowrkId.setStatus('current')
pepVpnStatusRemoteNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusRemoteNetwork.setStatus('current')
pepVpnStatusRemoteSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusRemoteSubnet.setStatus('current')
mibBuilder.exportSymbols("PEPVPN-SPEEDFUSION", pepVpnStatusEncryption=pepVpnStatusEncryption, PYSNMP_MODULE_ID=pepvpn, pepwave=pepwave, pepVpnRemotePeerId=pepVpnRemotePeerId, pepVpnStatusL2Bridging=pepVpnStatusL2Bridging, pepVpnStatusWanRxBytes=pepVpnStatusWanRxBytes, pepVpnStatusL2Vlan=pepVpnStatusL2Vlan, pepVpnStatusWanDropPackets=pepVpnStatusWanDropPackets, pepVpnStatusWanEntry=pepVpnStatusWanEntry, pepVpnStatusWanLatency=pepVpnStatusWanLatency, pepVpnInfo=pepVpnInfo, pepVpnStatusEntry=pepVpnStatusEntry, pepVpnRemotePeer=pepVpnRemotePeer, pepVpnStatusRemoteNetworkEntry=pepVpnStatusRemoteNetworkEntry, pepVpnStatusWanTable=pepVpnStatusWanTable, pepVpnStatusId=pepVpnStatusId, pepVpnStatusWanName=pepVpnStatusWanName, pepVpnStatusRemoteSubnet=pepVpnStatusRemoteSubnet, pepVpnStatusRemoteNetowrkId=pepVpnStatusRemoteNetowrkId, pepVpnStatusWanTxBytes=pepVpnStatusWanTxBytes, generalMib=generalMib, pepvpnMib=pepvpnMib, pepVpnStatusRemoteNetworkTable=pepVpnStatusRemoteNetworkTable, pepvpn=pepvpn, pepVpnStatusTable=pepVpnStatusTable, pepVpnStatusProfileName=pepVpnStatusProfileName, pepVpnStatusConnectionState=pepVpnStatusConnectionState, pepVpnStatusRemoteNetwork=pepVpnStatusRemoteNetwork, productMib=productMib, pepVpnStatusWanId=pepVpnStatusWanId)
