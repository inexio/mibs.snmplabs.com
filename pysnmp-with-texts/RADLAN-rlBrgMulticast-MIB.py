#
# PySNMP MIB module RADLAN-rlBrgMulticast-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-rlBrgMulticast-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:50:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
PortList, VlanIndex = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "VlanIndex")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, ObjectIdentity, iso, Bits, NotificationType, Gauge32, IpAddress, Integer32, Unsigned32, MibIdentifier, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "ObjectIdentity", "iso", "Bits", "NotificationType", "Gauge32", "IpAddress", "Integer32", "Unsigned32", "MibIdentifier", "Counter32", "TimeTicks")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
rlBrgMulticast = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 116))
rlBrgMulticast.setRevisions(('2013-04-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlBrgMulticast.setRevisionsDescriptions(('Added MODULE-IDENTITY',))
if mibBuilder.loadTexts: rlBrgMulticast.setLastUpdated('201304010000Z')
if mibBuilder.loadTexts: rlBrgMulticast.setOrganization('Marvell Semiconductor, Inc.')
if mibBuilder.loadTexts: rlBrgMulticast.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlBrgMulticast.setDescription('The MIB module describes the private MIB for Multicast Bridge supported by Marvell MTS software and products.')
rlBrgMulticastMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 116, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgMulticastMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastMibVersion.setDescription("MIB's version, the current version is 4. Snooping supports IGMPv1/v2/v3 and MLDv1/v2.")
rlBrgStaticIpMulticastTable = MibTable((1, 3, 6, 1, 4, 1, 89, 116, 3), )
if mibBuilder.loadTexts: rlBrgStaticIpMulticastTable.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticIpMulticastTable.setDescription('A table containing filtering information for IP Multicast addresses for each VLAN.')
rlBrgStaticIpMulticastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 116, 3, 1), ).setIndexNames((0, "RADLAN-rlBrgMulticast-MIB", "rlBrgStaticIpMulticastVlanTag"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgStaticIpMulticastGroupAddress"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgStaticIpMulticastSourceAddress"))
if mibBuilder.loadTexts: rlBrgStaticIpMulticastEntry.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticIpMulticastEntry.setDescription('Filtering information configured into the device. The set of ports to which frames containing this IP Multicast destination address and IP source address are allowed to be forwarded.')
rlBrgStaticIpMulticastVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 1), VlanIndex())
if mibBuilder.loadTexts: rlBrgStaticIpMulticastVlanTag.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticIpMulticastVlanTag.setDescription('The VLAN tag for which this entry is configured.')
rlBrgStaticIpMulticastGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: rlBrgStaticIpMulticastGroupAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticIpMulticastGroupAddress.setDescription('The multicast group address for which the filtering information applies ')
rlBrgStaticIpMulticastSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 3), IpAddress())
if mibBuilder.loadTexts: rlBrgStaticIpMulticastSourceAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticIpMulticastSourceAddress.setDescription('The unicast group address for which the filtering information applies.')
rlBrgStaticIpMulticastFrwPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgStaticIpMulticastFrwPorts.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticIpMulticastFrwPorts.setDescription('The ports the data should be forwarded to ')
rlBrgStaticIpMulticastForbiddenPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 5), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgStaticIpMulticastForbiddenPorts.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticIpMulticastForbiddenPorts.setDescription('The ports that overrides dynamic configuration and prevents multicast data forwarding for the group or group and source to these ports.')
rlBrgStaticIpMulticastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgStaticIpMulticastStatus.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticIpMulticastStatus.setDescription("The status of the table entry. It's used to add/delete an entry")
rlBrgIpMulticastTable = MibTable((1, 3, 6, 1, 4, 1, 89, 116, 4), )
if mibBuilder.loadTexts: rlBrgIpMulticastTable.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpMulticastTable.setDescription('A table containing all filtering information for IP Multicast addresses for each VLAN ')
rlBrgIpMulticastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 116, 4, 1), ).setIndexNames((0, "RADLAN-rlBrgMulticast-MIB", "rlBrgIpMulticastVlanTag"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgIpMulticastGroupAddress"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgIpMulticastSourceAddress"))
if mibBuilder.loadTexts: rlBrgIpMulticastEntry.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpMulticastEntry.setDescription('An entry (conceptual row) in the rlBrgIpMulticastTable contains IP Multicast FDB data ')
rlBrgIpMulticastVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 4, 1, 1), VlanIndex())
if mibBuilder.loadTexts: rlBrgIpMulticastVlanTag.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpMulticastVlanTag.setDescription('The VLAN tag for which this entry is configured.')
rlBrgIpMulticastGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: rlBrgIpMulticastGroupAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpMulticastGroupAddress.setDescription('Multicast group address (destination address) of data frames ')
rlBrgIpMulticastSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 4, 1, 3), IpAddress())
if mibBuilder.loadTexts: rlBrgIpMulticastSourceAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpMulticastSourceAddress.setDescription('Unicast source address of data frames.')
rlBrgIpMulticastEgressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 4, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgIpMulticastEgressPorts.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpMulticastEgressPorts.setDescription('The complete set of ports, in this VLAN, to which frames destined for this Group IP address or Group and Source address are currently being explicitly forwarded. This does not include ports for which this address is only implicitly forwarded, in the dot1qForwardAllPorts list.')
rlBrgIpMulticastLearntPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 4, 1, 5), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgIpMulticastLearntPorts.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpMulticastLearntPorts.setDescription('The subset of ports in rlBrgIpMulticastEgressPorts which were learnt by IGMP or some other dynamic mechanism, in this Filtering database..')
rlBrgStaticInetMulticastTable = MibTable((1, 3, 6, 1, 4, 1, 89, 116, 5), )
if mibBuilder.loadTexts: rlBrgStaticInetMulticastTable.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticInetMulticastTable.setDescription('A table containing filtering information for INET (Pv4 and IPv6) Multicast addresses for each VLAN.')
rlBrgStaticInetMulticastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 116, 5, 1), ).setIndexNames((0, "RADLAN-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastVlanTag"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastGroupAddressType"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastGroupAddress"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastSourceAddressType"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastSourceAddress"))
if mibBuilder.loadTexts: rlBrgStaticInetMulticastEntry.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticInetMulticastEntry.setDescription('Filtering information configured into the device. The set of ports to which frames containing this IP Multicast destination address and IP source address are allowed to be forwarded.')
rlBrgStaticInetMulticastVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 1), VlanIndex())
if mibBuilder.loadTexts: rlBrgStaticInetMulticastVlanTag.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticInetMulticastVlanTag.setDescription('The VLAN tag for which this entry is configured.')
rlBrgStaticInetMulticastGroupAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgStaticInetMulticastGroupAddressType.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticInetMulticastGroupAddressType.setDescription('Inet type ipv6/ipv4.')
rlBrgStaticInetMulticastGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 3), InetAddress())
if mibBuilder.loadTexts: rlBrgStaticInetMulticastGroupAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticInetMulticastGroupAddress.setDescription('The multicast group address for which the filtering information applies ')
rlBrgStaticInetMulticastSourceAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgStaticInetMulticastSourceAddressType.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticInetMulticastSourceAddressType.setDescription('Inet type ipv6/ipv4.')
rlBrgStaticInetMulticastSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 5), InetAddress())
if mibBuilder.loadTexts: rlBrgStaticInetMulticastSourceAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticInetMulticastSourceAddress.setDescription('The unicast group address for which the filtering information applies.')
rlBrgStaticInetMulticastFrwPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 6), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgStaticInetMulticastFrwPorts.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticInetMulticastFrwPorts.setDescription('The ports the data should be forwarded to ')
rlBrgStaticInetMulticastForbiddenPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 7), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgStaticInetMulticastForbiddenPorts.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticInetMulticastForbiddenPorts.setDescription('The ports that overrides dynamic configuration and prevents multicast data forwarding for the group or group and source to these ports.')
rlBrgStaticInetMulticastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgStaticInetMulticastStatus.setStatus('current')
if mibBuilder.loadTexts: rlBrgStaticInetMulticastStatus.setDescription("The status of the table entry. It's used to add/delete an entry")
rlBrgInetMulticastTable = MibTable((1, 3, 6, 1, 4, 1, 89, 116, 6), )
if mibBuilder.loadTexts: rlBrgInetMulticastTable.setStatus('current')
if mibBuilder.loadTexts: rlBrgInetMulticastTable.setDescription('A table containing all filtering information for IP Multicast addresses for each VLAN ')
rlBrgInetMulticastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 116, 6, 1), ).setIndexNames((0, "RADLAN-rlBrgMulticast-MIB", "rlBrgInetMulticastVlanTag"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgInetMulticastGroupAddressType"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgInetMulticastGroupAddress"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgInetMulticastSourceAddressType"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgInetMulticastSourceAddress"))
if mibBuilder.loadTexts: rlBrgInetMulticastEntry.setStatus('current')
if mibBuilder.loadTexts: rlBrgInetMulticastEntry.setDescription('An entry (conceptual row) in the rlBrgInetMulticastTable contains IP Multicast FDB data ')
rlBrgInetMulticastVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 1), VlanIndex())
if mibBuilder.loadTexts: rlBrgInetMulticastVlanTag.setStatus('current')
if mibBuilder.loadTexts: rlBrgInetMulticastVlanTag.setDescription('The VLAN tag for which this entry is configured.')
rlBrgInetMulticastGroupAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgInetMulticastGroupAddressType.setStatus('current')
if mibBuilder.loadTexts: rlBrgInetMulticastGroupAddressType.setDescription('Inet type IPv4/IPv6.')
rlBrgInetMulticastGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 3), InetAddress())
if mibBuilder.loadTexts: rlBrgInetMulticastGroupAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgInetMulticastGroupAddress.setDescription('Multicast group address (destination address) of data frames ')
rlBrgInetMulticastSourceAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgInetMulticastSourceAddressType.setStatus('current')
if mibBuilder.loadTexts: rlBrgInetMulticastSourceAddressType.setDescription('Inet type IPv4/IPv6.')
rlBrgInetMulticastSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 5), InetAddress())
if mibBuilder.loadTexts: rlBrgInetMulticastSourceAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgInetMulticastSourceAddress.setDescription('Unicast source address of data frames.')
rlBrgInetMulticastEgressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 6), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgInetMulticastEgressPorts.setStatus('current')
if mibBuilder.loadTexts: rlBrgInetMulticastEgressPorts.setDescription('The complete set of ports, in this VLAN, to which frames destined for this Group IP address or Group and Source address are currently being explicitly forwarded. This does not include ports for which this address is only implicitly forwarded, in the dot1qForwardAllPorts list.')
rlBrgInetMulticastLearntPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 7), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgInetMulticastLearntPorts.setStatus('current')
if mibBuilder.loadTexts: rlBrgInetMulticastLearntPorts.setDescription('The subset of ports in rlBrgIpMulticastEgressPorts which were learnt by IGMP or some other dynamic mechanism, in this Filtering database..')
rlBrgIpmFdbRefTable = MibTable((1, 3, 6, 1, 4, 1, 89, 116, 7), )
if mibBuilder.loadTexts: rlBrgIpmFdbRefTable.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpmFdbRefTable.setDescription('A table containing all information stored in IPM FDB overlapping Reference Table ')
rlBrgIpmFdbRefEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 116, 7, 1), ).setIndexNames((0, "RADLAN-rlBrgMulticast-MIB", "rlBrgIpmFdbRefVlanTag"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgIpmFdbRefGroupAddressType"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgIpmFdbRefGroupAddress"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgIpmFdbRefSourceAddressType"), (0, "RADLAN-rlBrgMulticast-MIB", "rlBrgIpmFdbRefSourceAddress"))
if mibBuilder.loadTexts: rlBrgIpmFdbRefEntry.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpmFdbRefEntry.setDescription('An entry (conceptual row) in the rlBrgIpmFdbRefTable contains overlapping Reference Table FDB data ')
rlBrgIpmFdbRefVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 1), VlanIndex())
if mibBuilder.loadTexts: rlBrgIpmFdbRefVlanTag.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpmFdbRefVlanTag.setDescription('The VLAN tag for which this entry is configured.')
rlBrgIpmFdbRefGroupAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 2), InetAddressType())
if mibBuilder.loadTexts: rlBrgIpmFdbRefGroupAddressType.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpmFdbRefGroupAddressType.setDescription('Multicast group address (destination address) of data frames ')
rlBrgIpmFdbRefGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 3), InetAddress())
if mibBuilder.loadTexts: rlBrgIpmFdbRefGroupAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpmFdbRefGroupAddress.setDescription('Multicast group address (destination address) of data frames ')
rlBrgIpmFdbRefSourceAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 4), InetAddressType())
if mibBuilder.loadTexts: rlBrgIpmFdbRefSourceAddressType.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpmFdbRefSourceAddressType.setDescription('Unicast source address of data frames.')
rlBrgIpmFdbRefSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 5), InetAddress())
if mibBuilder.loadTexts: rlBrgIpmFdbRefSourceAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpmFdbRefSourceAddress.setDescription('Unicast source address of data frames.')
rlBrgIpmFdbRefPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 6), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgIpmFdbRefPorts.setStatus('current')
if mibBuilder.loadTexts: rlBrgIpmFdbRefPorts.setDescription('The list of ports represented in IPM FDB overlapping Reference Table')
class DynamicCmdType(TextualConvention, Integer32):
    description = 'Type of Dynamic IPM FDB command: Create Entry, Delete Entry, Set ports Pset.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("createEntry", 0), ("deleteEntry", 1), ("addPorts", 2), ("deletePorts", 3))

rlBrgDynamicCmdTable = MibTable((1, 3, 6, 1, 4, 1, 89, 116, 8), )
if mibBuilder.loadTexts: rlBrgDynamicCmdTable.setStatus('current')
if mibBuilder.loadTexts: rlBrgDynamicCmdTable.setDescription('The (conceptual) table for Dynamic IPM FDB command. For debugging purposes only. This MIB is prohibited to be used with working IGMP/MLD snooping')
rlBrgDynamicCmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 116, 8, 1), ).setIndexNames((0, "RADLAN-rlBrgMulticast-MIB", "rlBrgDynamicCmdKey"))
if mibBuilder.loadTexts: rlBrgDynamicCmdEntry.setStatus('current')
if mibBuilder.loadTexts: rlBrgDynamicCmdEntry.setDescription('An entry (conceptual row) in the rlBrgDynamicCmdTable.')
rlBrgDynamicCmdKey = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: rlBrgDynamicCmdKey.setStatus('current')
if mibBuilder.loadTexts: rlBrgDynamicCmdKey.setDescription('Key of the rlBrgDynamicCmdTable table')
rlBrgDynamicCmdVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 2), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgDynamicCmdVlanTag.setStatus('current')
if mibBuilder.loadTexts: rlBrgDynamicCmdVlanTag.setDescription('The VLAN tag for which this entry is configured.')
rlBrgDynamicCmdGroupAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 3), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgDynamicCmdGroupAddressType.setStatus('current')
if mibBuilder.loadTexts: rlBrgDynamicCmdGroupAddressType.setDescription('Multicast group address (destination address) of data frames ')
rlBrgDynamicCmdGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgDynamicCmdGroupAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgDynamicCmdGroupAddress.setDescription('Multicast group address (destination address) of data frames ')
rlBrgDynamicCmdSourceAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 5), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgDynamicCmdSourceAddressType.setStatus('current')
if mibBuilder.loadTexts: rlBrgDynamicCmdSourceAddressType.setDescription('Unicast source address of data frames.')
rlBrgDynamicCmdSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgDynamicCmdSourceAddress.setStatus('current')
if mibBuilder.loadTexts: rlBrgDynamicCmdSourceAddress.setDescription('Unicast source address of data frames.')
rlBrgDynamicCmdPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 7), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgDynamicCmdPorts.setStatus('current')
if mibBuilder.loadTexts: rlBrgDynamicCmdPorts.setDescription('The list of ports for them the command is issued')
rlBrgDynamicCmdType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 8), DynamicCmdType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBrgDynamicCmdType.setStatus('current')
if mibBuilder.loadTexts: rlBrgDynamicCmdType.setDescription('Current type of command')
rlUserAssignedVidx = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 116, 9))
class VidxIndex(TextualConvention, Unsigned32):
    description = 'Values of Vidx. 0 means no free Vidx.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(4096, 32767), )
rlUserAssignedVidxConfigTable = MibTable((1, 3, 6, 1, 4, 1, 89, 116, 9, 1), )
if mibBuilder.loadTexts: rlUserAssignedVidxConfigTable.setStatus('current')
if mibBuilder.loadTexts: rlUserAssignedVidxConfigTable.setDescription('A table containing entries of User Assigned Vidx configuration information')
rlUserAssignedVidxConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 116, 9, 1, 1), ).setIndexNames((0, "RADLAN-rlBrgMulticast-MIB", "rlUserAssignedVidxConfigIndex"))
if mibBuilder.loadTexts: rlUserAssignedVidxConfigEntry.setStatus('current')
if mibBuilder.loadTexts: rlUserAssignedVidxConfigEntry.setDescription('A table entry of User Assigned Vidx information table')
rlUserAssignedVidxConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 9, 1, 1, 1), VidxIndex())
if mibBuilder.loadTexts: rlUserAssignedVidxConfigIndex.setStatus('current')
if mibBuilder.loadTexts: rlUserAssignedVidxConfigIndex.setDescription('Vidx index. Values from 4K to 32K')
rlUserAssignedVidxConfigPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 9, 1, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUserAssignedVidxConfigPorts.setStatus('current')
if mibBuilder.loadTexts: rlUserAssignedVidxConfigPorts.setDescription('List of ports that belong to the Vidx')
rlUserAssignedVidxConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 116, 9, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlUserAssignedVidxConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlUserAssignedVidxConfigRowStatus.setDescription('This object indicates the status of this entry.')
rlUserAssignedVidxGetNextFreeIndex = MibScalar((1, 3, 6, 1, 4, 1, 89, 116, 9, 2), VidxIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUserAssignedVidxGetNextFreeIndex.setStatus('current')
if mibBuilder.loadTexts: rlUserAssignedVidxGetNextFreeIndex.setDescription('Returns the next free Vidx index. Values from 4K to 32K')
rlBrgMulticastCurrentNumberOfEntries = MibScalar((1, 3, 6, 1, 4, 1, 89, 116, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBrgMulticastCurrentNumberOfEntries.setStatus('current')
if mibBuilder.loadTexts: rlBrgMulticastCurrentNumberOfEntries.setDescription('Current number of multicast entries.')
mibBuilder.exportSymbols("RADLAN-rlBrgMulticast-MIB", rlBrgIpmFdbRefGroupAddressType=rlBrgIpmFdbRefGroupAddressType, rlUserAssignedVidxConfigEntry=rlUserAssignedVidxConfigEntry, rlBrgStaticInetMulticastGroupAddressType=rlBrgStaticInetMulticastGroupAddressType, rlBrgIpMulticastEgressPorts=rlBrgIpMulticastEgressPorts, rlBrgInetMulticastVlanTag=rlBrgInetMulticastVlanTag, rlBrgInetMulticastGroupAddress=rlBrgInetMulticastGroupAddress, rlBrgStaticIpMulticastGroupAddress=rlBrgStaticIpMulticastGroupAddress, rlBrgStaticInetMulticastSourceAddressType=rlBrgStaticInetMulticastSourceAddressType, rlBrgIpMulticastSourceAddress=rlBrgIpMulticastSourceAddress, rlBrgStaticIpMulticastSourceAddress=rlBrgStaticIpMulticastSourceAddress, PYSNMP_MODULE_ID=rlBrgMulticast, rlBrgStaticInetMulticastVlanTag=rlBrgStaticInetMulticastVlanTag, rlBrgInetMulticastSourceAddress=rlBrgInetMulticastSourceAddress, rlBrgDynamicCmdSourceAddressType=rlBrgDynamicCmdSourceAddressType, rlBrgStaticIpMulticastTable=rlBrgStaticIpMulticastTable, rlBrgStaticIpMulticastEntry=rlBrgStaticIpMulticastEntry, rlUserAssignedVidxConfigTable=rlUserAssignedVidxConfigTable, rlBrgStaticIpMulticastStatus=rlBrgStaticIpMulticastStatus, VidxIndex=VidxIndex, rlBrgIpmFdbRefGroupAddress=rlBrgIpmFdbRefGroupAddress, rlBrgStaticIpMulticastVlanTag=rlBrgStaticIpMulticastVlanTag, rlBrgInetMulticastGroupAddressType=rlBrgInetMulticastGroupAddressType, rlBrgStaticInetMulticastStatus=rlBrgStaticInetMulticastStatus, rlBrgInetMulticastLearntPorts=rlBrgInetMulticastLearntPorts, rlBrgStaticIpMulticastForbiddenPorts=rlBrgStaticIpMulticastForbiddenPorts, rlBrgDynamicCmdGroupAddressType=rlBrgDynamicCmdGroupAddressType, rlBrgStaticInetMulticastGroupAddress=rlBrgStaticInetMulticastGroupAddress, rlBrgStaticInetMulticastSourceAddress=rlBrgStaticInetMulticastSourceAddress, rlBrgDynamicCmdPorts=rlBrgDynamicCmdPorts, rlUserAssignedVidxConfigRowStatus=rlUserAssignedVidxConfigRowStatus, rlBrgDynamicCmdGroupAddress=rlBrgDynamicCmdGroupAddress, rlUserAssignedVidxGetNextFreeIndex=rlUserAssignedVidxGetNextFreeIndex, rlBrgStaticInetMulticastForbiddenPorts=rlBrgStaticInetMulticastForbiddenPorts, rlBrgIpmFdbRefPorts=rlBrgIpmFdbRefPorts, rlBrgIpMulticastVlanTag=rlBrgIpMulticastVlanTag, rlUserAssignedVidx=rlUserAssignedVidx, rlBrgStaticInetMulticastEntry=rlBrgStaticInetMulticastEntry, rlUserAssignedVidxConfigPorts=rlUserAssignedVidxConfigPorts, rlBrgIpmFdbRefEntry=rlBrgIpmFdbRefEntry, rlBrgStaticIpMulticastFrwPorts=rlBrgStaticIpMulticastFrwPorts, rlBrgIpMulticastEntry=rlBrgIpMulticastEntry, rlBrgStaticInetMulticastFrwPorts=rlBrgStaticInetMulticastFrwPorts, rlBrgInetMulticastTable=rlBrgInetMulticastTable, rlBrgInetMulticastEntry=rlBrgInetMulticastEntry, rlBrgIpmFdbRefVlanTag=rlBrgIpmFdbRefVlanTag, rlBrgDynamicCmdVlanTag=rlBrgDynamicCmdVlanTag, rlBrgIpMulticastTable=rlBrgIpMulticastTable, rlBrgDynamicCmdTable=rlBrgDynamicCmdTable, rlBrgDynamicCmdType=rlBrgDynamicCmdType, rlBrgIpmFdbRefSourceAddressType=rlBrgIpmFdbRefSourceAddressType, rlBrgDynamicCmdEntry=rlBrgDynamicCmdEntry, rlBrgMulticastMibVersion=rlBrgMulticastMibVersion, rlBrgIpmFdbRefTable=rlBrgIpmFdbRefTable, rlBrgIpMulticastLearntPorts=rlBrgIpMulticastLearntPorts, rlBrgDynamicCmdKey=rlBrgDynamicCmdKey, rlBrgInetMulticastSourceAddressType=rlBrgInetMulticastSourceAddressType, rlBrgDynamicCmdSourceAddress=rlBrgDynamicCmdSourceAddress, rlUserAssignedVidxConfigIndex=rlUserAssignedVidxConfigIndex, rlBrgIpMulticastGroupAddress=rlBrgIpMulticastGroupAddress, rlBrgStaticInetMulticastTable=rlBrgStaticInetMulticastTable, rlBrgMulticast=rlBrgMulticast, rlBrgIpmFdbRefSourceAddress=rlBrgIpmFdbRefSourceAddress, rlBrgMulticastCurrentNumberOfEntries=rlBrgMulticastCurrentNumberOfEntries, rlBrgInetMulticastEgressPorts=rlBrgInetMulticastEgressPorts, DynamicCmdType=DynamicCmdType)
