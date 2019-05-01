#
# PySNMP MIB module A3COM0503-PORTINFO (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0503-PORTINFO
# Produced by pysmi-0.3.4 at Wed May  1 11:09:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
a3ComVlanGroup, = mibBuilder.importSymbols("GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanGroup")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, iso, IpAddress, Counter32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, ModuleIdentity, Gauge32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "iso", "IpAddress", "Counter32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "ModuleIdentity", "Gauge32", "TimeTicks", "Integer32")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
class VlanList(OctetString):
    pass

portInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3), )
if mibBuilder.loadTexts: portInfoTable.setStatus('current')
if mibBuilder.loadTexts: portInfoTable.setDescription('A table indexed by ifIndex of a port. This can be a font-panel/module port e.g. 101 or an aggregator 15512.')
portInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: portInfoEntry.setStatus('current')
if mibBuilder.loadTexts: portInfoEntry.setDescription('Bridge information for a port')
portInfoEgressVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 1), VlanList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoEgressVlans.setReference('3fc...')
if mibBuilder.loadTexts: portInfoEgressVlans.setStatus('current')
if mibBuilder.loadTexts: portInfoEgressVlans.setDescription('The set of vlans on which this port is allowed to transmit traffic.')
portInfoForbiddenEgressVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 2), VlanList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoForbiddenEgressVlans.setReference('3fc...')
if mibBuilder.loadTexts: portInfoForbiddenEgressVlans.setStatus('current')
if mibBuilder.loadTexts: portInfoForbiddenEgressVlans.setDescription('The set of vlans on which this port is forbidden to transmit.')
portInfoUntaggedVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 3), VlanList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoUntaggedVlans.setReference('3fc...')
if mibBuilder.loadTexts: portInfoUntaggedVlans.setStatus('current')
if mibBuilder.loadTexts: portInfoUntaggedVlans.setDescription('The set of vlans on which this port transmits untagged frames.')
portInfoStpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoStpPortPriority.setReference('IEEE 802.1D-1990: Section 4.5.5.1')
if mibBuilder.loadTexts: portInfoStpPortPriority.setStatus('current')
if mibBuilder.loadTexts: portInfoStpPortPriority.setDescription('The value of the priority field which is contained in the first (in network byte order) octet of the (2 octet long) Port ID. The other octet of the Port ID is given by the value of dot1dStpPort..')
portInfoStpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoStpPortEnable.setReference('IEEE 802.1D-1990: Section 4.5.5.2')
if mibBuilder.loadTexts: portInfoStpPortEnable.setStatus('current')
if mibBuilder.loadTexts: portInfoStpPortEnable.setDescription('The enabled/disabled status of the port.')
portInfoPvid = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 6), VlanIndex().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoPvid.setReference('IEEE 802.1Q/D11 Section 12.10.1.1')
if mibBuilder.loadTexts: portInfoPvid.setStatus('current')
if mibBuilder.loadTexts: portInfoPvid.setDescription('The PVID, the VLAN ID assigned to untagged frames or Prority-Tagged frames received on this port.')
portInfoAcceptableFrameTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("admitAll", 1), ("admitOnlyVlanTagged", 2))).clone('admitAll')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoAcceptableFrameTypes.setReference('IEEE 802.1Q/D11 Section 12.10.1.3')
if mibBuilder.loadTexts: portInfoAcceptableFrameTypes.setStatus('current')
if mibBuilder.loadTexts: portInfoAcceptableFrameTypes.setDescription('When this is admitOnlyVlanTagged(2) the device will discard untagged frames or Prority-Tagged frames received on this port. When admitAll(1), untagged frames or Prority-Tagged frames received on this port will be accepted and assigned to the PVID for this port. This control does not affect VLAN independent BPDU frames, such as GVRP and STP. It does affect VLAN dependent BPDU frames, such as GMRP.')
portInfoIngressFiltering = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoIngressFiltering.setReference('IEEE 802.1Q/D11 Section 12.10.1.4')
if mibBuilder.loadTexts: portInfoIngressFiltering.setStatus('current')
if mibBuilder.loadTexts: portInfoIngressFiltering.setDescription('When this is true(1) the device will discard incoming frames for VLANs which do not include this Port in its Member set. When false(2), the port will accept all incoming frames. This control does not affect VLAN independent BPDU frames, such as GVRP and STP. It does affect VLAN dependent BPDU frames, such as GMRP.')
portInfoFdbTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4), )
if mibBuilder.loadTexts: portInfoFdbTable.setStatus('mandatory')
if mibBuilder.loadTexts: portInfoFdbTable.setDescription('This table contains the static unicast addresses for each port in the bridge.')
portInfoFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1), ).setIndexNames((0, "A3COM0503-PORTINFO", "portInfoFdbIndex"), (0, "A3COM0503-PORTINFO", "portInfoFdbVlan"), (0, "A3COM0503-PORTINFO", "portInfoFdbAddress"))
if mibBuilder.loadTexts: portInfoFdbEntry.setStatus('mandatory')
if mibBuilder.loadTexts: portInfoFdbEntry.setDescription('Information about a specific unicast MAC address.')
portInfoFdbIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: portInfoFdbIndex.setStatus('mandatory')
if mibBuilder.loadTexts: portInfoFdbIndex.setDescription('This contains the ifIndex of the port that this address has been seen on.')
portInfoFdbVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 2), VlanIndex())
if mibBuilder.loadTexts: portInfoFdbVlan.setStatus('mandatory')
if mibBuilder.loadTexts: portInfoFdbVlan.setDescription('The Vlan index of the port.')
portInfoFdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 3), MacAddress())
if mibBuilder.loadTexts: portInfoFdbAddress.setStatus('mandatory')
if mibBuilder.loadTexts: portInfoFdbAddress.setDescription('This object contains the unicast MAC address of the entry.')
portInfoFdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portInfoFdbStatus.setStatus('mandatory')
if mibBuilder.loadTexts: portInfoFdbStatus.setDescription('This has useful states of active, destroy, and createAndGo. An fdb entry can be created with a state of createAndGo or active. The fdb entry can be deleted by setting the state to destroy.')
mibBuilder.exportSymbols("A3COM0503-PORTINFO", portInfoFdbAddress=portInfoFdbAddress, VlanList=VlanList, portInfoStpPortPriority=portInfoStpPortPriority, portInfoEgressVlans=portInfoEgressVlans, portInfoUntaggedVlans=portInfoUntaggedVlans, portInfoStpPortEnable=portInfoStpPortEnable, portInfoTable=portInfoTable, portInfoIngressFiltering=portInfoIngressFiltering, portInfoFdbEntry=portInfoFdbEntry, portInfoForbiddenEgressVlans=portInfoForbiddenEgressVlans, portInfoFdbStatus=portInfoFdbStatus, portInfoFdbVlan=portInfoFdbVlan, portInfoEntry=portInfoEntry, portInfoFdbIndex=portInfoFdbIndex, portInfoPvid=portInfoPvid, portInfoFdbTable=portInfoFdbTable, portInfoAcceptableFrameTypes=portInfoAcceptableFrameTypes)
