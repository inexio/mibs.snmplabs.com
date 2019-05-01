#
# PySNMP MIB module MCAST-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MCAST-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Bits, Integer32, NotificationType, Gauge32, ObjectIdentity, iso, Counter64, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "Integer32", "NotificationType", "Gauge32", "ObjectIdentity", "iso", "Counter64", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "TimeTicks")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
swMcastVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 64))
if mibBuilder.loadTexts: swMcastVlanMIB.setLastUpdated('1001110000Z')
if mibBuilder.loadTexts: swMcastVlanMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swMcastVlanMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swMcastVlanMIB.setDescription('The structure of IGMP&MLD snooping multicast VLAN for the proprietary enterprise.')
class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swMcastVlanCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 64, 1))
swMcastVlanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 64, 2))
swMcastVlanMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 64, 3))
swISMVlanGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 64, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swISMVlanGlobalState.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGlobalState.setDescription('This indicates the global state of the IGMP snooping multicast VLAN.')
swMSMVlanGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 64, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSMVlanGlobalState.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGlobalState.setDescription('This indicates the global state of the MLD snooping multicast VLAN.')
swISMVlanForwardUnmatchedState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 64, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swISMVlanForwardUnmatchedState.setStatus('current')
if mibBuilder.loadTexts: swISMVlanForwardUnmatchedState.setDescription("This indicates the IGMP snooping multicast VLAN's forwarding state for Multicast VLAN unmatched packet.")
swMSMVlanForwardUnmatchedState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 64, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSMVlanForwardUnmatchedState.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanForwardUnmatchedState.setDescription("This indicates the MLD snooping multicast VLAN's forwarding state for Multicast VLAN unmatched packet.")
swISMVlanTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1), )
if mibBuilder.loadTexts: swISMVlanTable.setStatus('current')
if mibBuilder.loadTexts: swISMVlanTable.setDescription('This contains information about the IGMP snooping multicast VLAN table.')
swISMVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1), ).setIndexNames((0, "MCAST-VLAN-MIB", "swISMVlanID"))
if mibBuilder.loadTexts: swISMVlanEntry.setStatus('current')
if mibBuilder.loadTexts: swISMVlanEntry.setDescription('This is an entry of the swISMVlanTable.')
swISMVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swISMVlanID.setStatus('current')
if mibBuilder.loadTexts: swISMVlanID.setDescription('This indicates the VLAN ID of the IGMP snooping multicast VLAN entry.')
swISMVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swISMVlanName.setStatus('current')
if mibBuilder.loadTexts: swISMVlanName.setDescription('This indicates the VLAN name of the IGMP snooping multicast VLAN entry.')
swISMVlanSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swISMVlanSourcePort.setStatus('current')
if mibBuilder.loadTexts: swISMVlanSourcePort.setDescription('This indicates the port list of the source ports of the IGMP snooping multicast VLAN. The source ports will be set as tag ports of the VLAN entry and the IGMP control messages received from the member ports will be forwarded to the source ports.')
swISMVlanMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swISMVlanMemberPort.setStatus('current')
if mibBuilder.loadTexts: swISMVlanMemberPort.setDescription('This indicates the port list of the member ports of the IGMP snooping multicast VLAN. The source ports will be set as untagged ports of the VLAN entry and the IGMP control messages received from the member ports will be forwarded to the source ports.')
swISMVlanTagMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 5), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swISMVlanTagMemberPort.setStatus('current')
if mibBuilder.loadTexts: swISMVlanTagMemberPort.setDescription('This indicates the port list of the tag member ports of the IGMP snooping multicast VLAN.')
swISMVlanUntagSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 6), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swISMVlanUntagSourcePort.setStatus('current')
if mibBuilder.loadTexts: swISMVlanUntagSourcePort.setDescription('This indicates the untagged member ports to add to the multicast VLAN.')
swISMVlanState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swISMVlanState.setStatus('current')
if mibBuilder.loadTexts: swISMVlanState.setDescription('This can be used to enable or disable the IGMP snooping multicast VLAN.')
swISMVlanRepSourceAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 8), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swISMVlanRepSourceAddrType.setStatus('current')
if mibBuilder.loadTexts: swISMVlanRepSourceAddrType.setDescription("This is the type of multicast VLAN replacement address as specified by object 'swISMVlanRepSourceAddr'.")
swISMVlanRepSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 9), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swISMVlanRepSourceAddr.setStatus('current')
if mibBuilder.loadTexts: swISMVlanRepSourceAddr.setDescription('This is the replacement address of this multicast VLAN.')
swISMVlanRemapPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swISMVlanRemapPriority.setStatus('current')
if mibBuilder.loadTexts: swISMVlanRemapPriority.setDescription("This is the priority value (0 to 7) to be associated with the data traffic to be forwarded on the multicast VLAN. When set to -1, the packet's original priority will be used.")
swISMVlanReplacePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swISMVlanReplacePriority.setStatus('current')
if mibBuilder.loadTexts: swISMVlanReplacePriority.setDescription("This specifies that a packet's priority will be changed by the switch based on the remap priority. This flag will only take effect when remap priority is set.")
swISMVlanProfileIDList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 12), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swISMVlanProfileIDList.setStatus('current')
if mibBuilder.loadTexts: swISMVlanProfileIDList.setDescription('This specifies a profile ID list for each VLAN ID of the IGMP snooping multicast VLAN entry.')
swISMVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swISMVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: swISMVlanRowStatus.setDescription('This indicates the status of this entry.')
swISMVlanGroupProfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 2), )
if mibBuilder.loadTexts: swISMVlanGroupProfTable.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGroupProfTable.setDescription('This table contains the IGMP snooping multicast VLAN group profile name.')
swISMVlanGroupProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 2, 1), ).setIndexNames((0, "MCAST-VLAN-MIB", "swISMVlanGroupProfName"))
if mibBuilder.loadTexts: swISMVlanGroupProfEntry.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGroupProfEntry.setDescription('This is an entry of the swISMVlanGroupProfTable.')
swISMVlanGroupProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swISMVlanGroupProfName.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGroupProfName.setDescription('This indicates the name of the IGMP snooping multicast VLAN group profile.')
swISMVlanGroupProfID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swISMVlanGroupProfID.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGroupProfID.setDescription('This indicates the index of the IGMP snooping multicast VLAN group profile.')
swISMVlanGroupProfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swISMVlanGroupProfStatus.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGroupProfStatus.setDescription('This indicates the status of this entry.')
swISMVlanGroupProfAddrTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3), )
if mibBuilder.loadTexts: swISMVlanGroupProfAddrTable.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGroupProfAddrTable.setDescription('This table contains the multicast address of each IGMP snooping multicast VLAN group profile.')
swISMVlanGroupProfAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3, 1), ).setIndexNames((0, "MCAST-VLAN-MIB", "swISMVlanGroupProfName"), (0, "MCAST-VLAN-MIB", "swISMVlanGroupProfAddrType"), (0, "MCAST-VLAN-MIB", "swISMVlanGroupProfAddrStart"), (0, "MCAST-VLAN-MIB", "swISMVlanGroupProfAddrEnd"))
if mibBuilder.loadTexts: swISMVlanGroupProfAddrEntry.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGroupProfAddrEntry.setDescription('This is an entry of the swISMVlanGroupProfAddrTable.')
swISMVlanGroupProfAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swISMVlanGroupProfAddrType.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGroupProfAddrType.setDescription("This is the type of multicast address as specified by object 'swISMVlanGroupProfAddrToIp'.")
swISMVlanGroupProfAddrStart = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swISMVlanGroupProfAddrStart.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGroupProfAddrStart.setDescription('This specifies the multicast address list for this profile.')
swISMVlanGroupProfAddrEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swISMVlanGroupProfAddrEnd.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGroupProfAddrEnd.setDescription('The specifies the multicast address list for this profile.')
swISMVlanGroupProfAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swISMVlanGroupProfAddrStatus.setStatus('current')
if mibBuilder.loadTexts: swISMVlanGroupProfAddrStatus.setDescription('This indicates the status of this entry.')
swMSMVlanTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4), )
if mibBuilder.loadTexts: swMSMVlanTable.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanTable.setDescription('This contains information about the MLD snooping multicast VLAN table.')
swMSMVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1), ).setIndexNames((0, "MCAST-VLAN-MIB", "swMSMVlanID"))
if mibBuilder.loadTexts: swMSMVlanEntry.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanEntry.setDescription('This is an entry of the swMSMVlanTable.')
swMSMVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSMVlanID.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanID.setDescription('This indicates the VLAN ID of the MLD snooping multicast VLAN entry.')
swMSMVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSMVlanName.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanName.setDescription('This indicates the VLAN name of the MLD snooping multicast VLAN entry.')
swMSMVlanSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSMVlanSourcePort.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanSourcePort.setDescription('This indicates the port list of the source ports of the MLD snooping multicast VLAN. The source ports will be set as tag ports of the VLAN entry and the MLD control messages received from the member ports will be forwarded to the source ports.')
swMSMVlanMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSMVlanMemberPort.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanMemberPort.setDescription('This indicates the port list of the member ports of the MLD snooping multicast VLAN. The source ports will be set as untagged ports of the VLAN entry and the MLD control messages received from the member ports will be forwarded to the source ports.')
swMSMVlanTagMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 5), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSMVlanTagMemberPort.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanTagMemberPort.setDescription('This indicates the port list of the tag member ports of the MLD snooping multicast VLAN.')
swMSMVlanUntagSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 6), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSMVlanUntagSourcePort.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanUntagSourcePort.setDescription('This indicates the untagged member ports to add to the multicast VLAN.')
swMSMVlanState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSMVlanState.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanState.setDescription('This can be used to enable or disable the MLD snooping multicast VLAN.')
swMSMVlanRepSourceAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 8), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSMVlanRepSourceAddrType.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanRepSourceAddrType.setDescription("This is the type of multicast VLAN replacement address as specified by object 'swMSMVlanRepSourceAddr'.")
swMSMVlanRepSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 9), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSMVlanRepSourceAddr.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanRepSourceAddr.setDescription('This is the replacement address of this multicast VLAN.')
swMSMVlanRemapPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSMVlanRemapPriority.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanRemapPriority.setDescription("This is the priority value (0 to 7) to be associated with the data traffic to be forwarded on the multicast VLAN. When set to -1, the packet's original priority will be used.")
swMSMVlanReplacePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSMVlanReplacePriority.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanReplacePriority.setDescription("This specifies that a packet's priority will be changed by the switch based on the remap priority. This flag will only take effect when remap priority is set.")
swMSMVlanProfileIDList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 12), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSMVlanProfileIDList.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanProfileIDList.setDescription('This specifies a profile ID list for each VLAN ID of the MLD snooping multicast VLAN entry.')
swMSMVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSMVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanRowStatus.setDescription('This indicates the status of this entry.')
swMSMVlanGroupProfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 5), )
if mibBuilder.loadTexts: swMSMVlanGroupProfTable.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGroupProfTable.setDescription('This table contains the MLD snooping multicast VLAN group profile name.')
swMSMVlanGroupProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 5, 1), ).setIndexNames((0, "MCAST-VLAN-MIB", "swMSMVlanGroupProfName"))
if mibBuilder.loadTexts: swMSMVlanGroupProfEntry.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGroupProfEntry.setDescription('This is an entry of the swMSMVlanGroupProfTable.')
swMSMVlanGroupProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 5, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSMVlanGroupProfName.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGroupProfName.setDescription('This indicates the name of the MLD snooping multicast VLAN group profile.')
swMSMVlanGroupProfID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSMVlanGroupProfID.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGroupProfID.setDescription('This indicates the index of the MLD snooping multicast VLAN group profile.')
swMSMVlanGroupProfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSMVlanGroupProfStatus.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGroupProfStatus.setDescription('This indicates the status of this entry.')
swMSMVlanGroupProfAddrTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6), )
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrTable.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrTable.setDescription('This table contains the multicast address of each MLD snooping multicast VLAN group profile.')
swMSMVlanGroupProfAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6, 1), ).setIndexNames((0, "MCAST-VLAN-MIB", "swMSMVlanGroupProfName"), (0, "MCAST-VLAN-MIB", "swMSMVlanGroupProfAddrType"), (0, "MCAST-VLAN-MIB", "swMSMVlanGroupProfAddrStart"), (0, "MCAST-VLAN-MIB", "swMSMVlanGroupProfAddrEnd"))
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrEntry.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrEntry.setDescription('This is an entry of the swMSMVlanGroupProfAddrTable.')
swMSMVlanGroupProfAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrType.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrType.setDescription("This is the type of multicast address as specified by object 'swMSMVlanGroupProfAddrToIp'.")
swMSMVlanGroupProfAddrStart = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrStart.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrStart.setDescription('This specifies the multicast address list for this profile.')
swMSMVlanGroupProfAddrEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrEnd.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrEnd.setDescription('The specifies the multicast address list for this profile.')
swMSMVlanGroupProfAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrStatus.setStatus('current')
if mibBuilder.loadTexts: swMSMVlanGroupProfAddrStatus.setDescription('This indicates the status of this entry.')
mibBuilder.exportSymbols("MCAST-VLAN-MIB", swMSMVlanGroupProfEntry=swMSMVlanGroupProfEntry, swISMVlanName=swISMVlanName, swISMVlanReplacePriority=swISMVlanReplacePriority, swISMVlanGroupProfAddrTable=swISMVlanGroupProfAddrTable, swMcastVlanMgmt=swMcastVlanMgmt, swISMVlanGroupProfName=swISMVlanGroupProfName, swISMVlanMemberPort=swISMVlanMemberPort, swMSMVlanID=swMSMVlanID, swISMVlanGroupProfTable=swISMVlanGroupProfTable, swMSMVlanUntagSourcePort=swMSMVlanUntagSourcePort, swMSMVlanGlobalState=swMSMVlanGlobalState, swISMVlanRepSourceAddr=swISMVlanRepSourceAddr, swISMVlanRepSourceAddrType=swISMVlanRepSourceAddrType, swISMVlanUntagSourcePort=swISMVlanUntagSourcePort, swISMVlanGroupProfEntry=swISMVlanGroupProfEntry, swMSMVlanGroupProfAddrStart=swMSMVlanGroupProfAddrStart, PortList=PortList, swISMVlanTable=swISMVlanTable, swMSMVlanSourcePort=swMSMVlanSourcePort, PYSNMP_MODULE_ID=swMcastVlanMIB, swMSMVlanGroupProfAddrStatus=swMSMVlanGroupProfAddrStatus, swMSMVlanGroupProfTable=swMSMVlanGroupProfTable, swISMVlanState=swISMVlanState, swISMVlanSourcePort=swISMVlanSourcePort, swISMVlanGroupProfAddrStart=swISMVlanGroupProfAddrStart, swISMVlanGroupProfAddrEnd=swISMVlanGroupProfAddrEnd, swMSMVlanMemberPort=swMSMVlanMemberPort, swMSMVlanRepSourceAddrType=swMSMVlanRepSourceAddrType, swMSMVlanReplacePriority=swMSMVlanReplacePriority, swMcastVlanInfo=swMcastVlanInfo, swISMVlanRemapPriority=swISMVlanRemapPriority, swMSMVlanTable=swMSMVlanTable, swMSMVlanProfileIDList=swMSMVlanProfileIDList, swMSMVlanState=swMSMVlanState, swMSMVlanRemapPriority=swMSMVlanRemapPriority, swMSMVlanGroupProfAddrEntry=swMSMVlanGroupProfAddrEntry, swISMVlanGlobalState=swISMVlanGlobalState, swMSMVlanTagMemberPort=swMSMVlanTagMemberPort, swMSMVlanGroupProfName=swMSMVlanGroupProfName, swISMVlanGroupProfAddrType=swISMVlanGroupProfAddrType, swMSMVlanForwardUnmatchedState=swMSMVlanForwardUnmatchedState, swISMVlanProfileIDList=swISMVlanProfileIDList, swMSMVlanRowStatus=swMSMVlanRowStatus, swISMVlanEntry=swISMVlanEntry, swISMVlanRowStatus=swISMVlanRowStatus, swMSMVlanName=swMSMVlanName, swISMVlanForwardUnmatchedState=swISMVlanForwardUnmatchedState, swISMVlanTagMemberPort=swISMVlanTagMemberPort, swMSMVlanGroupProfID=swMSMVlanGroupProfID, swMSMVlanRepSourceAddr=swMSMVlanRepSourceAddr, swMSMVlanGroupProfStatus=swMSMVlanGroupProfStatus, swISMVlanGroupProfAddrStatus=swISMVlanGroupProfAddrStatus, swMcastVlanMIB=swMcastVlanMIB, swISMVlanID=swISMVlanID, swISMVlanGroupProfID=swISMVlanGroupProfID, swMcastVlanCtrl=swMcastVlanCtrl, swISMVlanGroupProfAddrEntry=swISMVlanGroupProfAddrEntry, swMSMVlanGroupProfAddrTable=swMSMVlanGroupProfAddrTable, swMSMVlanEntry=swMSMVlanEntry, swMSMVlanGroupProfAddrEnd=swMSMVlanGroupProfAddrEnd, swMSMVlanGroupProfAddrType=swMSMVlanGroupProfAddrType, swISMVlanGroupProfStatus=swISMVlanGroupProfStatus)
