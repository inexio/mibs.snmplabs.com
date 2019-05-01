#
# PySNMP MIB module SWPROTOCOLVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWPROTOCOLVLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:13:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
dot1vProtocolPortEntry, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1vProtocolPortEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Counter32, Integer32, ObjectIdentity, iso, MibIdentifier, ModuleIdentity, Bits, NotificationType, Counter64, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Counter32", "Integer32", "ObjectIdentity", "iso", "MibIdentifier", "ModuleIdentity", "Bits", "NotificationType", "Counter64", "IpAddress", "Unsigned32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
swProtocolVLANMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 16))
if mibBuilder.loadTexts: swProtocolVLANMIB.setLastUpdated('0710260000Z')
if mibBuilder.loadTexts: swProtocolVLANMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swProtocolVLANMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swProtocolVLANMIB.setDescription('The Protocol (Policy-based) VLAN module MIB for the proprietary enterprise. Other related VLAN parameters will reference to rfc2674q.mib.')
class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swProtocolVLANCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 16, 1))
swProtocolVLANTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1), )
if mibBuilder.loadTexts: swProtocolVLANTable.setStatus('obsolete')
if mibBuilder.loadTexts: swProtocolVLANTable.setDescription('A table that contains information about protocol (policy-based) VLAN method lists.')
swProtocolVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1), ).setIndexNames((0, "SWPROTOCOLVLAN-MIB", "swProtocolVLANIndex"))
if mibBuilder.loadTexts: swProtocolVLANEntry.setStatus('obsolete')
if mibBuilder.loadTexts: swProtocolVLANEntry.setDescription('A list of the protocol (policy-based) VLAN methods.')
swProtocolVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swProtocolVLANIndex.setStatus('obsolete')
if mibBuilder.loadTexts: swProtocolVLANIndex.setDescription('A value that identifies this SwProtocolVLANEntry.')
swProtocolVLANName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swProtocolVLANName.setStatus('obsolete')
if mibBuilder.loadTexts: swProtocolVLANName.setDescription('Specifies the name of the VLAN')
swProtocolVLANProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("dot1q-vlan", 1), ("protocol-ip", 2), ("protocol-ipx803dot3", 3), ("protocol-ipx802dot2", 4), ("protocol-ipxSnap", 5), ("protocol-ipxEthernet2", 6), ("protocol-appleTalk", 7), ("protocol-decLat", 8), ("protocol-dexOther", 9), ("protocol-sna802dot2", 10), ("protocol-snaEthernet2", 11), ("protocol-netBios", 12), ("protocol-xns", 13), ("protocol-vines", 14), ("protocol-ipV6", 15), ("protocol-userDefined", 16), ("protocol-rarp", 17)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swProtocolVLANProtocolType.setStatus('obsolete')
if mibBuilder.loadTexts: swProtocolVLANProtocolType.setDescription('The protocol type of protocol (policy-based) VLAN list. The group protocol types include dot1q-vlan(1), protocol-ip(2), protocol-ipx803dot3(3), protocol-ipx802dot2(4), protocol-ipxSnap(5), protocol-ipxEthernet2(6), protocol-appleTalk(7), protocol-decLat(8), protocol-dexOther(9), protocol-sna802dot2(10), protocol-snaEthernet2(11), protocol-netBios(12), protocol-xns(13), protocol-vines(14), protocol-ipV6(15), protocol-userDefined(16) and protocol-rarp(17)')
swProtocolVLANAdvertisement = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swProtocolVLANAdvertisement.setStatus('obsolete')
if mibBuilder.loadTexts: swProtocolVLANAdvertisement.setDescription('This object indicates whether advertisement is active or not.')
swProtocolVLANUserDefinedProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swProtocolVLANUserDefinedProtocol.setStatus('obsolete')
if mibBuilder.loadTexts: swProtocolVLANUserDefinedProtocol.setDescription('If the protocol type is protocol-userDefined(16), this value will fill with the user defined protocol type. This value will be ignored for other protocol types. The user cannot fill the pre-defined protocol type in this value. These pre-defined protocol types are: 0x0800 PROTO_VLAN_IPETHER2 0x8035 PROTO_VLAN_RARPETHER2 0xFFFF PROTO_VLAN_IPX802_3 0xE0E0 PROTO_VLAN_IPX802_2 0x8137 PROTO_VLAN_IPXSNAP 0x8137 PROTO_VLAN_IPXETHER2 0x809B PROTO_VLAN_APLTKETHER2SNAP 0x6000 PROTO_VLAN_DECETHER2 0x6009 PROTO_VLAN_DECOTHERETHER2 0x0404 PROTO_VLAN_SNA802_2 0x80D5 PROTO_VLAN_SNAETHER2 0xF0F0 PROTO_VLAN_NETBIOS 0x0600 PROTO_VLAN_XNSETHER2 0x0BAD PROTO_VLAN_VINESETHER2 0x86DD PROTO_VLAN_IPV6ETHER2 ')
swProtocolVLANencap = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernet", 1), ("llc", 2), ("snap", 3), ("all", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swProtocolVLANencap.setStatus('obsolete')
if mibBuilder.loadTexts: swProtocolVLANencap.setDescription('If the protocol type is protocol-userDefined(16), this value will fill with the encap type. For other protocol types, this value will be ignored. The group encap type includes ethernet(1), llc(2), snap(3),and all(4).')
swProtocolVLANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swProtocolVLANRowStatus.setStatus('obsolete')
if mibBuilder.loadTexts: swProtocolVLANRowStatus.setDescription('This object indicates the status of this entry.')
swdot1vProtocolPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 2), )
if mibBuilder.loadTexts: swdot1vProtocolPortTable.setReference('IEEE 802.1v clause 8.4.4')
if mibBuilder.loadTexts: swdot1vProtocolPortTable.setStatus('current')
if mibBuilder.loadTexts: swdot1vProtocolPortTable.setDescription('A table that contains VID sets used for Port-and-Protocol-based VLAN Classification.')
swdot1vProtocolPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 2, 1), )
dot1vProtocolPortEntry.registerAugmentions(("SWPROTOCOLVLAN-MIB", "swdot1vProtocolPortEntry"))
swdot1vProtocolPortEntry.setIndexNames(*dot1vProtocolPortEntry.getIndexNames())
if mibBuilder.loadTexts: swdot1vProtocolPortEntry.setStatus('current')
if mibBuilder.loadTexts: swdot1vProtocolPortEntry.setDescription('A VID set for a port.')
swdot1vProtocolPortGroupPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swdot1vProtocolPortGroupPriority.setStatus('current')
if mibBuilder.loadTexts: swdot1vProtocolPortGroupPriority.setDescription('The Priority associated with a group of protocols for each port.')
mibBuilder.exportSymbols("SWPROTOCOLVLAN-MIB", swProtocolVLANMIB=swProtocolVLANMIB, swProtocolVLANName=swProtocolVLANName, swProtocolVLANencap=swProtocolVLANencap, swProtocolVLANUserDefinedProtocol=swProtocolVLANUserDefinedProtocol, PortList=PortList, swProtocolVLANIndex=swProtocolVLANIndex, swProtocolVLANCtrl=swProtocolVLANCtrl, swdot1vProtocolPortTable=swdot1vProtocolPortTable, swProtocolVLANAdvertisement=swProtocolVLANAdvertisement, swdot1vProtocolPortEntry=swdot1vProtocolPortEntry, swdot1vProtocolPortGroupPriority=swdot1vProtocolPortGroupPriority, swProtocolVLANTable=swProtocolVLANTable, swProtocolVLANEntry=swProtocolVLANEntry, swProtocolVLANProtocolType=swProtocolVLANProtocolType, PYSNMP_MODULE_ID=swProtocolVLANMIB, swProtocolVLANRowStatus=swProtocolVLANRowStatus)
