#
# PySNMP MIB module HH3C-LswVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LswVLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:26:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hh3cifVLANTrunkStatusEntry, PortList = mibBuilder.importSymbols("HH3C-LswINF-MIB", "hh3cifVLANTrunkStatusEntry", "PortList")
hh3clswCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3clswCommon")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Counter32, ObjectIdentity, Bits, TimeTicks, ModuleIdentity, Gauge32, iso, NotificationType, Unsigned32, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Counter32", "ObjectIdentity", "Bits", "TimeTicks", "ModuleIdentity", "Gauge32", "iso", "NotificationType", "Unsigned32", "MibIdentifier", "Integer32")
TimeInterval, TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
hh3cLswVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2))
if mibBuilder.loadTexts: hh3cLswVlan.setLastUpdated('200112261452Z')
if mibBuilder.loadTexts: hh3cLswVlan.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cLswVlan.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cLswVlan.setDescription('')
class Hh3cVlanIndex(TextualConvention, Integer32):
    description = 'A value used to index per-VLAN tables: values of 0 and 4095 are not permitted; if the value is between 1 and 4094 inclusive, it represents an IEEE 802.1Q VLAN-ID with global scope within a given bridged domain (see VlanId textual convention). If the value is greater than 4095 then it represents a VLAN with scope local to the particular agent, i.e. one without a global VLAN-ID assigned to it. Such VLANs are outside the scope of IEEE 802.1Q but it is convenient to be able to manage them in the same way using this MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

hh3cLswVlanMngObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1))
if mibBuilder.loadTexts: hh3cLswVlanMngObject.setStatus('current')
if mibBuilder.loadTexts: hh3cLswVlanMngObject.setDescription('Description.')
hh3cdot1qVlanMIBTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1), )
if mibBuilder.loadTexts: hh3cdot1qVlanMIBTable.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanMIBTable.setDescription('VLAN MIB table')
hh3cdot1qVlanMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1), ).setIndexNames((0, "HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex"))
if mibBuilder.loadTexts: hh3cdot1qVlanMIBEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanMIBEntry.setDescription('Entries of VLAN MIB table')
hh3cdot1qVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 1), Hh3cVlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanIndex.setDescription('The VLAN-ID.')
hh3cdot1qVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanName.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanName.setDescription('Name of the VLAN.')
hh3cdot1qVlanPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanPorts.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanPorts.setDescription('Port list of the VLAN.')
hh3cdot1qVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("superVlan", 1), ("common-vlan", 2), ("sub-vlan", 3), ("isolate-user-vlan", 4), ("secondary-vlan", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanType.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanType.setDescription('Vlan types: SuperVlan(1), Common vlan(2), and Sub-vlan(3).')
hh3cdot1qVlanMacFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanMacFilter.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanMacFilter.setDescription('Whether to filter MAC addresses.')
hh3cdot1qVlanMcastUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanMcastUnknownProtos.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanMcastUnknownProtos.setDescription('Whether to broadcast the unknown packets.')
hh3cExistInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cExistInterface.setStatus('current')
if mibBuilder.loadTexts: hh3cExistInterface.setDescription('Whether there is virtual interface.')
hh3cVlanInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVlanInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceIndex.setDescription('Whether vlan interface is configured on vlan. If vlan interface is configured, the value of the node is vlan id, else the value is 0.')
hh3cdot1qVlanMacLearn = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanMacLearn.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanMacLearn.setDescription('MAC address learning identity. (common vlan/Sub-vlan)')
hh3cdot1qVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("static", 2), ("dynamic", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanStatus.setDescription('Status of the VLAN.')
hh3cdot1qVlanCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanCreationTime.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanCreationTime.setDescription('The sysUPTime when the VLAN is created.')
hh3cdot1qVlanPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanPriority.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanPriority.setDescription('Priority of the VLAN.')
hh3cdot1qVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cdot1qVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanRowStatus.setDescription('Operation status.')
hh3cdot1qVlanBroadcastSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanBroadcastSuppression.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanBroadcastSuppression.setDescription('Whether broadcast suppression of vlan be supported pro rata. The vlaue of 100 indicates no broadcast suppression. If the function is not supported, this object cannot be written, and 100 will be returned when reading')
hh3cdot1qVlanBcastSuppressionPPS = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 148800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanBcastSuppressionPPS.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanBcastSuppressionPPS.setDescription('If the broadcast can be controlled with pps(packet per second)type, the value of 0 indicates no suppression. This node is conflicted with hh3cdot1qVlanBroadcastSuppression. If the mode is set, hh3cdot1qVlanBroadcastSuppression is unavailable. And vice versa.')
hh3cdot1qVlanMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanMulticast.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanMulticast.setDescription('Multicast vlan. The default value is disable(0).')
hh3cdot1qVlanTaggedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 17), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanTaggedPorts.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanTaggedPorts.setDescription('Tagged port list of the VLAN.')
hh3cdot1qVlanUntaggedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 18), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanUntaggedPorts.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanUntaggedPorts.setDescription('Untagged port list of the VLAN.')
hh3cdot1qVlanPortIndexs = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 19), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanPortIndexs.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanPortIndexs.setDescription('PortIndex list of the VLAN, that delimited by comma, such as 1,3,4,7.')
hh3cVlanInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2), )
if mibBuilder.loadTexts: hh3cVlanInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceTable.setDescription('Virtual interface configuration table')
hh3cVlanInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1), ).setIndexNames((0, "HH3C-LswVLAN-MIB", "hh3cVlanInterfaceID"))
if mibBuilder.loadTexts: hh3cVlanInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceEntry.setDescription('Entries of virtual interface configuration table')
hh3cVlanInterfaceID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVlanInterfaceID.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceID.setDescription('Index of the vlan interface table.')
hh3cdot1qVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 2), Hh3cVlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanID.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanID.setDescription('VLAN-ID')
hh3cdot1qVlanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanIpAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanIpAddress.setDescription('IP address of interface.')
hh3cdot1qVlanIpAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanIpAddressMask.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanIpAddressMask.setDescription('IP address mask of interface.')
hh3cVlanInterfaceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cVlanInterfaceAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceAdminStatus.setDescription('Status of VLAN virtual interfaces.')
hh3cVlanInterfaceFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernet-ii", 1), ("ethernet-snap", 2), ("ethernet-8022", 3), ("ethernet-8023", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVlanInterfaceFrameType.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceFrameType.setDescription('Frame type accepted by VLAN virtual interfaces.')
hh3cInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cInterfaceRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cInterfaceRowStatus.setDescription('Operation status.')
hh3cVlanInterfaceIpMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("assigned-ip", 1), ("dhcp-ip", 2), ("bootp-ip", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cVlanInterfaceIpMethod.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceIpMethod.setDescription('Vlan interface ip address acquiring method which is manual, dhcp or bootp.')
hh3cVlanInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVlanInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceIfIndex.setDescription('IfIndex of VLAN interface.')
hh3cifIsolateMappingTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 4), )
if mibBuilder.loadTexts: hh3cifIsolateMappingTable.setStatus('current')
if mibBuilder.loadTexts: hh3cifIsolateMappingTable.setDescription('Secondary vlan lists of Isolate-VLANs.')
hh3cifIsolateMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 4, 1), ).setIndexNames((0, "HH3C-LswVLAN-MIB", "hh3cifIsolatePrimaryVlanID"))
if mibBuilder.loadTexts: hh3cifIsolateMappingEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cifIsolateMappingEntry.setDescription('Secondary vlan lists of Isolate-VLANs.')
hh3cifIsolatePrimaryVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 4, 1, 1), Hh3cVlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifIsolatePrimaryVlanID.setStatus('current')
if mibBuilder.loadTexts: hh3cifIsolatePrimaryVlanID.setDescription('Primary VLAN-ID.')
hh3cifIsolateSecondaryVlanlistLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifIsolateSecondaryVlanlistLow.setStatus('current')
if mibBuilder.loadTexts: hh3cifIsolateSecondaryVlanlistLow.setDescription("Each octet within this value specifies a set of eight VLANs, with the first octet specifying VLANs 1 through 8, the second octet specifying VLANs 9 through 16, etc. Within each octet, the most significant bit represents the highest numbered VLAN, and the least significant bit represents the lowest numbered VLAN. Thus, each secondary VLAN of the primary VLAN is represented by a single bit within the value of this object. If that bit has a value of '1' then that VLAN is secondary VLAN in the set of VLANs; the VLAN is not secondary VLAN if its bit has a value of '0'.")
hh3cifIsolateSecondaryVlanlistHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifIsolateSecondaryVlanlistHigh.setStatus('current')
if mibBuilder.loadTexts: hh3cifIsolateSecondaryVlanlistHigh.setDescription("Each octet within this value specifies a set of eight VLANs, with the first octet specifying VLANs 2049 through 2056, the second octet specifying VLANs 2057 through 2064, etc. Within each octet, the most significant bit represents the highest numbered VLAN, and the least significant bit represents the lowest numbered VLAN. Thus, each secondary VLAN of the primary VLAN is represented by a single bit within the value of this object. If that bit has a value of '1' then that VLAN is secondary VLAN in the set of VLANs; the VLAN is not secondary VLAN if its bit has a value of '0'.")
hh3cVlanInterfaceAddrTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5), )
if mibBuilder.loadTexts: hh3cVlanInterfaceAddrTable.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceAddrTable.setDescription('VLAN interface IP address configuration table')
hh3cVlanInterfaceAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1), ).setIndexNames((0, "HH3C-LswVLAN-MIB", "hh3cVlanInterfaceIpIfIndex"), (0, "HH3C-LswVLAN-MIB", "hh3cVlanInterfaceIpAddr"))
if mibBuilder.loadTexts: hh3cVlanInterfaceAddrEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceAddrEntry.setDescription('Entries of VLAN interface IP address configuration table')
hh3cVlanInterfaceIpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVlanInterfaceIpIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceIpIfIndex.setDescription('Index of VLAN interfaces.')
hh3cVlanInterfaceIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cVlanInterfaceIpAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceIpAddr.setDescription('IP address of VLAN interface. When taking destory operation, you could set it zero to destory all IP addresses(but cluster IP address) in this VLAN interface.')
hh3cVlanInterfaceIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cVlanInterfaceIpMask.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceIpMask.setDescription('IP address mask of VLAN interface. When destory single IP address, you must set it correct to relative IP address.')
hh3cVlanInterfaceIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primary", 1), ("sub", 2), ("cluster", 3), ("vrrp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cVlanInterfaceIpType.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceIpType.setDescription('IP address type. cluster(3) will only be set when taking GET or GET NEXT operation. primary(1) is optional when taking SET primary IP address operation.')
hh3cVlanInterfaceIpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVlanInterfaceIpRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cVlanInterfaceIpRowStatus.setDescription('Operation status. active(1) will only be set when taking GET or GET NEXT operation. createAndGo(4) and destory(6) is valid when taking SET operation.')
hh3cDot1qVlanBatchMIBTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6), )
if mibBuilder.loadTexts: hh3cDot1qVlanBatchMIBTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDot1qVlanBatchMIBTable.setDescription("VLAN batch configuration table. In the case of VLAN batch creation, hh3cdot1qVlanBatchSetOperate should be set to 1. For example, if creating a row is for creating VLANs 2 to 4, the value of the objects should be set as follows: hh3cdot1qVlanBatchStartIndex 2, hh3cdot1qVlanBatchEndIndex 4, hh3cdot1qVlanBatchSetOperate create(1), hh3cdot1qVlanBatchRowStatus createAndGo(4). In the case of VLAN batch deletion, hh3cdot1qVlanBatchSetOperate should be set to 2. For example, if creating a row is for deleting VLANs 10 to 20, the value of the objects should be set as follows: hh3cdot1qVlanBatchStartIndex 10, hh3cdot1qVlanBatchEndIndex 20, hh3cdot1qVlanBatchSetOperate delete(2), hh3cdot1qVlanBatchRowStatus createAndGo(4). When the action of batch VLANs deleting or creating is done, one row will be existent until it is deleted manually or ages out, but the VLANs of it won't disappear with the deletion of the row.")
hh3cDot1qVlanBatchMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1), ).setIndexNames((0, "HH3C-LswVLAN-MIB", "hh3cdot1qVlanBatchOperIndex"))
if mibBuilder.loadTexts: hh3cDot1qVlanBatchMIBEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDot1qVlanBatchMIBEntry.setDescription('VLAN batch configuration entry.')
hh3cdot1qVlanBatchOperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanBatchOperIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanBatchOperIndex.setDescription('The consequence of operation.')
hh3cdot1qVlanBatchStartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 2), Hh3cVlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanBatchStartIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanBatchStartIndex.setDescription('The value of start VLAN-ID.')
hh3cdot1qVlanBatchEndIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 3), Hh3cVlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanBatchEndIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanBatchEndIndex.setDescription('The value of end VLAN-ID.')
hh3cdot1qVlanBatchOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("opInprogress", 1), ("opfailure", 2), ("opsuccess", 3), ("opsuccesspartial", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanBatchOperStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanBatchOperStatus.setDescription('The status of operation.')
hh3cdot1qVlanBatchRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cdot1qVlanBatchRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanBatchRowStatus.setDescription('The row status of Hh3cDot1qVlanBatchMIBEntry.')
hh3cdot1qVlanBatchSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cdot1qVlanBatchSetOperate.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1qVlanBatchSetOperate.setDescription('VLAN batch creation or deletion.')
hh3cifSuperVlanMappingTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 7), )
if mibBuilder.loadTexts: hh3cifSuperVlanMappingTable.setStatus('current')
if mibBuilder.loadTexts: hh3cifSuperVlanMappingTable.setDescription('Sub VLAN lists of super-VLANs.')
hh3cifSuperVlanMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 7, 1), ).setIndexNames((0, "HH3C-LswVLAN-MIB", "hh3cifSuperVlanID"))
if mibBuilder.loadTexts: hh3cifSuperVlanMappingEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cifSuperVlanMappingEntry.setDescription('Sub VLAN lists of super-VLANs.')
hh3cifSuperVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 7, 1, 1), Hh3cVlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cifSuperVlanID.setStatus('current')
if mibBuilder.loadTexts: hh3cifSuperVlanID.setDescription('Super VLAN ID.')
hh3cifSubVlanlistLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifSubVlanlistLow.setStatus('current')
if mibBuilder.loadTexts: hh3cifSubVlanlistLow.setDescription("Each octet within this value specifies a set of eight VLANs, with the first octet specifying VLANs 1 through 8, the second octet specifying VLANs 9 through 16, etc. Within each octet, the most significant bit represents the highest numbered VLAN, and the least significant bit represents the lowest numbered VLAN. Thus, each sub VLAN of the super VLAN is represented by a single bit within the value of this object. If that bit has a value of '1' then that VLAN is a sub VLAN of the super VLAN; the VLAN is not a sub VLAN of the super VLAN if its bit has a value of '0'.")
hh3cifSubVlanlistHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cifSubVlanlistHigh.setStatus('current')
if mibBuilder.loadTexts: hh3cifSubVlanlistHigh.setDescription("Each octet within this value specifies a set of eight VLANs, with the first octet specifying VLANs 2049 through 2056, the second octet specifying VLANs 2057 through 2064, etc. Within each octet, the most significant bit represents the highest numbered VLAN, and the least significant bit represents the lowest numbered VLAN. Thus, each sub VLAN of the super VLAN is represented by a single bit within the value of this object. If that bit has a value of '1' then that VLAN is a sub VLAN of the super VLAN; the VLAN is not a sub VLAN of the super VLAN if its bit has a value of '0'.")
hh3cLswVlanProtoObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2))
if mibBuilder.loadTexts: hh3cLswVlanProtoObject.setStatus('current')
if mibBuilder.loadTexts: hh3cLswVlanProtoObject.setDescription('Description.')
hh3cVLANMibGarpLeaveAllTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 14), TimeInterval().clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cVLANMibGarpLeaveAllTime.setStatus('current')
if mibBuilder.loadTexts: hh3cVLANMibGarpLeaveAllTime.setDescription('The GARP LeaveAll time, in centiseconds.')
hh3cvLANMibSwitchCountTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15), )
if mibBuilder.loadTexts: hh3cvLANMibSwitchCountTable.setStatus('current')
if mibBuilder.loadTexts: hh3cvLANMibSwitchCountTable.setDescription('A table containing the information various statistics of switch.')
hh3cvLANMibSwitchCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1), )
hh3cifVLANTrunkStatusEntry.registerAugmentions(("HH3C-LswVLAN-MIB", "hh3cvLANMibSwitchCountEntry"))
hh3cvLANMibSwitchCountEntry.setIndexNames(*hh3cifVLANTrunkStatusEntry.getIndexNames())
if mibBuilder.loadTexts: hh3cvLANMibSwitchCountEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cvLANMibSwitchCountEntry.setDescription('A table containing the information various statistics of switch.')
hh3cVLANMibSwitchGMRPRXPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVLANMibSwitchGMRPRXPkt.setStatus('current')
if mibBuilder.loadTexts: hh3cVLANMibSwitchGMRPRXPkt.setDescription('Number of GMRP frames received.')
hh3cVLANMibSwitchGVRPRXPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVLANMibSwitchGVRPRXPkt.setStatus('current')
if mibBuilder.loadTexts: hh3cVLANMibSwitchGVRPRXPkt.setDescription('Number of GVRP frames received.')
hh3cVLANMibSwitchGMRPTXPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVLANMibSwitchGMRPTXPkt.setStatus('current')
if mibBuilder.loadTexts: hh3cVLANMibSwitchGMRPTXPkt.setDescription('Number of GMRP frames transmitted.')
hh3cVLANMibSwitchGVRPTXPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVLANMibSwitchGVRPTXPkt.setStatus('current')
if mibBuilder.loadTexts: hh3cVLANMibSwitchGVRPTXPkt.setDescription('Number of GVRP frames transmitted.')
hh3cVLANMibSwitchDiscardedPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVLANMibSwitchDiscardedPkt.setStatus('current')
if mibBuilder.loadTexts: hh3cVLANMibSwitchDiscardedPkt.setDescription('Number of discarded frames.')
hh3cVLANMibSwitchGarpStatClear = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cVLANMibSwitchGarpStatClear.setStatus('current')
if mibBuilder.loadTexts: hh3cVLANMibSwitchGarpStatClear.setDescription('Clear various Statistics viz. read operation not supported.')
hh3cvLANMibHoldTimeTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 16), )
if mibBuilder.loadTexts: hh3cvLANMibHoldTimeTable.setStatus('current')
if mibBuilder.loadTexts: hh3cvLANMibHoldTimeTable.setDescription('A table for setting/getting the Hold Time for a particular port.')
hh3cvLANMibHoldTimeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 16, 1), )
ifEntry.registerAugmentions(("HH3C-LswVLAN-MIB", "hh3cvLANMibHoldTimeEntry"))
hh3cvLANMibHoldTimeEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: hh3cvLANMibHoldTimeEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cvLANMibHoldTimeEntry.setDescription('A table for setting/getting the HoldTime of the port.')
hh3cVLANMibHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 16, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 32765)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cVLANMibHoldTime.setStatus('current')
if mibBuilder.loadTexts: hh3cVLANMibHoldTime.setDescription('HoldTime of the port.')
mibBuilder.exportSymbols("HH3C-LswVLAN-MIB", hh3cVlanInterfaceIndex=hh3cVlanInterfaceIndex, hh3cdot1qVlanBatchOperStatus=hh3cdot1qVlanBatchOperStatus, PYSNMP_MODULE_ID=hh3cLswVlan, hh3cifIsolateSecondaryVlanlistHigh=hh3cifIsolateSecondaryVlanlistHigh, hh3cVlanInterfaceIpMethod=hh3cVlanInterfaceIpMethod, hh3cdot1qVlanUntaggedPorts=hh3cdot1qVlanUntaggedPorts, hh3cifIsolatePrimaryVlanID=hh3cifIsolatePrimaryVlanID, hh3cdot1qVlanMacFilter=hh3cdot1qVlanMacFilter, hh3cVlanInterfaceIpRowStatus=hh3cVlanInterfaceIpRowStatus, hh3cifIsolateMappingTable=hh3cifIsolateMappingTable, hh3cdot1qVlanBatchOperIndex=hh3cdot1qVlanBatchOperIndex, hh3cdot1qVlanRowStatus=hh3cdot1qVlanRowStatus, hh3cdot1qVlanCreationTime=hh3cdot1qVlanCreationTime, hh3cdot1qVlanBatchSetOperate=hh3cdot1qVlanBatchSetOperate, hh3cifSuperVlanID=hh3cifSuperVlanID, hh3cvLANMibSwitchCountTable=hh3cvLANMibSwitchCountTable, hh3cdot1qVlanTaggedPorts=hh3cdot1qVlanTaggedPorts, hh3cVlanInterfaceEntry=hh3cVlanInterfaceEntry, hh3cdot1qVlanMIBTable=hh3cdot1qVlanMIBTable, hh3cVLANMibSwitchGMRPTXPkt=hh3cVLANMibSwitchGMRPTXPkt, hh3cdot1qVlanPriority=hh3cdot1qVlanPriority, hh3cLswVlanMngObject=hh3cLswVlanMngObject, Hh3cVlanIndex=Hh3cVlanIndex, hh3cdot1qVlanType=hh3cdot1qVlanType, hh3cdot1qVlanStatus=hh3cdot1qVlanStatus, hh3cdot1qVlanPortIndexs=hh3cdot1qVlanPortIndexs, hh3cVlanInterfaceID=hh3cVlanInterfaceID, hh3cDot1qVlanBatchMIBEntry=hh3cDot1qVlanBatchMIBEntry, hh3cvLANMibHoldTimeTable=hh3cvLANMibHoldTimeTable, hh3cVLANMibHoldTime=hh3cVLANMibHoldTime, hh3cExistInterface=hh3cExistInterface, hh3cVlanInterfaceIpType=hh3cVlanInterfaceIpType, hh3cdot1qVlanIpAddressMask=hh3cdot1qVlanIpAddressMask, hh3cVLANMibSwitchGVRPTXPkt=hh3cVLANMibSwitchGVRPTXPkt, hh3cLswVlanProtoObject=hh3cLswVlanProtoObject, hh3cVlanInterfaceIpMask=hh3cVlanInterfaceIpMask, hh3cVLANMibSwitchDiscardedPkt=hh3cVLANMibSwitchDiscardedPkt, hh3cdot1qVlanPorts=hh3cdot1qVlanPorts, hh3cdot1qVlanBroadcastSuppression=hh3cdot1qVlanBroadcastSuppression, hh3cVlanInterfaceFrameType=hh3cVlanInterfaceFrameType, hh3cVLANMibSwitchGMRPRXPkt=hh3cVLANMibSwitchGMRPRXPkt, hh3cdot1qVlanBcastSuppressionPPS=hh3cdot1qVlanBcastSuppressionPPS, hh3cVlanInterfaceIfIndex=hh3cVlanInterfaceIfIndex, hh3cVlanInterfaceAdminStatus=hh3cVlanInterfaceAdminStatus, hh3cVlanInterfaceAddrTable=hh3cVlanInterfaceAddrTable, hh3cdot1qVlanMulticast=hh3cdot1qVlanMulticast, hh3cifSuperVlanMappingEntry=hh3cifSuperVlanMappingEntry, hh3cVLANMibGarpLeaveAllTime=hh3cVLANMibGarpLeaveAllTime, hh3cVLANMibSwitchGarpStatClear=hh3cVLANMibSwitchGarpStatClear, hh3cVlanInterfaceAddrEntry=hh3cVlanInterfaceAddrEntry, hh3cvLANMibHoldTimeEntry=hh3cvLANMibHoldTimeEntry, hh3cdot1qVlanName=hh3cdot1qVlanName, hh3cifIsolateMappingEntry=hh3cifIsolateMappingEntry, hh3cVlanInterfaceIpIfIndex=hh3cVlanInterfaceIpIfIndex, hh3cdot1qVlanID=hh3cdot1qVlanID, hh3cdot1qVlanBatchStartIndex=hh3cdot1qVlanBatchStartIndex, hh3cdot1qVlanIndex=hh3cdot1qVlanIndex, hh3cdot1qVlanMIBEntry=hh3cdot1qVlanMIBEntry, hh3cifSuperVlanMappingTable=hh3cifSuperVlanMappingTable, hh3cVLANMibSwitchGVRPRXPkt=hh3cVLANMibSwitchGVRPRXPkt, hh3cdot1qVlanIpAddress=hh3cdot1qVlanIpAddress, hh3cifSubVlanlistHigh=hh3cifSubVlanlistHigh, hh3cifIsolateSecondaryVlanlistLow=hh3cifIsolateSecondaryVlanlistLow, hh3cvLANMibSwitchCountEntry=hh3cvLANMibSwitchCountEntry, hh3cifSubVlanlistLow=hh3cifSubVlanlistLow, hh3cDot1qVlanBatchMIBTable=hh3cDot1qVlanBatchMIBTable, hh3cdot1qVlanBatchRowStatus=hh3cdot1qVlanBatchRowStatus, hh3cVlanInterfaceIpAddr=hh3cVlanInterfaceIpAddr, hh3cVlanInterfaceTable=hh3cVlanInterfaceTable, hh3cdot1qVlanMacLearn=hh3cdot1qVlanMacLearn, hh3cLswVlan=hh3cLswVlan, hh3cdot1qVlanBatchEndIndex=hh3cdot1qVlanBatchEndIndex, hh3cInterfaceRowStatus=hh3cInterfaceRowStatus, hh3cdot1qVlanMcastUnknownProtos=hh3cdot1qVlanMcastUnknownProtos)
