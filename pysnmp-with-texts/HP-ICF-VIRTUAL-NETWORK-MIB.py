#
# PySNMP MIB module HP-ICF-VIRTUAL-NETWORK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-VIRTUAL-NETWORK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:35:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Gauge32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Counter64, ObjectIdentity, ModuleIdentity, iso, Integer32, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Counter64", "ObjectIdentity", "ModuleIdentity", "iso", "Integer32", "IpAddress", "Unsigned32")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
tunnelIfAddressType, tunnelIfLocalInetAddress, tunnelIfEntry, tunnelIfRemoteInetAddress = mibBuilder.importSymbols("TUNNEL-MIB", "tunnelIfAddressType", "tunnelIfLocalInetAddress", "tunnelIfEntry", "tunnelIfRemoteInetAddress")
hpicfVirtualNetwork = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107))
hpicfVirtualNetwork.setRevisions(('2014-03-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfVirtualNetwork.setRevisionsDescriptions(('Initial Revision.',))
if mibBuilder.loadTexts: hpicfVirtualNetwork.setLastUpdated('201403190000Z')
if mibBuilder.loadTexts: hpicfVirtualNetwork.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfVirtualNetwork.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfVirtualNetwork.setDescription('This MIB module contains HP proprietary objects for managing Virtual Networks.')
hpicfVirtualNetworkNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 0))
hpicfVirtualNetworkObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1))
hpicfVirtualNetworkScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 1))
hpicfVirtualNetworkNotifyScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3))
hpicfTunnelObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2))
hpicfVXLANTunnelObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1))
hpicfVXLANTunnelConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1))
hpicfVXLANTunnelScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2))
hpicfVirtualNetworkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3))
hpicfMaxVirtualNetworks = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMaxVirtualNetworks.setStatus('current')
if mibBuilder.loadTexts: hpicfMaxVirtualNetworks.setDescription('Maximum number of Virtual Networks supported on the device.')
hpicfTotalVirtualNetworks = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTotalVirtualNetworks.setStatus('current')
if mibBuilder.loadTexts: hpicfTotalVirtualNetworks.setDescription('Total number of Virtual Networks configured on the device.')
hpicfVirtualNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2), )
if mibBuilder.loadTexts: hpicfVirtualNetworkTable.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkTable.setDescription('Table containing information about virtual networks.')
hpicfVirtualNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2, 1), ).setIndexNames((0, "HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkID"))
if mibBuilder.loadTexts: hpicfVirtualNetworkEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkEntry.setDescription('An entry containing the information about a virtual network and the associated VLAN.')
hpicfVirtualNetworkID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16777215)))
if mibBuilder.loadTexts: hpicfVirtualNetworkID.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkID.setDescription('This is a unique 24-bit segment ID referred to as a VXLAN Network Identifier (VNI). It is included as a part of the VXLAN encapsulation.')
hpicfVirtualNetworkName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVirtualNetworkName.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkName.setDescription('This object refers to the virtual network name. If the name is not configured for a virtual network, the system will generate a default name for the virtual network.')
hpicfVirtualNetworkVLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2, 1, 3), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVirtualNetworkVLANID.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkVLANID.setDescription('This object refers to the VLAN ID mapped to this virtual network. A VLAN associated with a virtual network is known as an overlay VLAN. Only one VLAN can be associated with a virtual network and that VLAN should be an existing VLAN.')
hpicfVirtualNetworkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVirtualNetworkRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkRowStatus.setDescription('The status of a row for a virtual network entry.')
hpicfVXLANTunnelIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfVXLANTunnelIfTable.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelIfTable.setDescription('Table containing additional information about VXLAN tunnels')
hpicfVXLANTunnelIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1), )
tunnelIfEntry.registerAugmentions(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelIfEntry"))
hpicfVXLANTunnelIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfVXLANTunnelIfEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelIfEntry.setDescription('An entry containing additional information about a VXLAN tunnel.')
hpicfVXLANTunnelIfDownReason = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("ifAdminDown", 1), ("tepNotReachable", 2), ("resourceUnavailable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVXLANTunnelIfDownReason.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelIfDownReason.setDescription('This object provides the information about the operational status of a tunnel. A value of none (0) indicates that the operational status is up. A value of ifAdminDown(1) indicates that the interface is administratively down. A value of tepNotReachable(2) indicates that the tunnel endpoint is not reachable. A value of resourceUnavailable (3) indicates that the hardware resource is not available.')
hpicfVXLANTunnelIfNextHopIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVXLANTunnelIfNextHopIpType.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelIfNextHopIpType.setDescription('This object provides the address type for resolved next hop IP address to reach the tunnel end point.')
hpicfVXLANTunnelIfNextHopIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVXLANTunnelIfNextHopIp.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelIfNextHopIp.setDescription('This object provides the resolved next hop IPv4 address to reach the tunnel end point. A NULL address indicates that the next hop IPv4 address is not resolved.')
hpicfVXLANTunnelIfNextHopInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVXLANTunnelIfNextHopInterface.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelIfNextHopInterface.setDescription('This object provides next hop interface to reach the tunnel end point. An empty string indicates that the next hop interface is not resolved')
hpicfVXLANTunnelIfNextHopPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVXLANTunnelIfNextHopPortName.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelIfNextHopPortName.setDescription('This object provides the resolved port name to reach the tunnel end point. An empty string indicates that the next hop port name is not resolved.')
hpicfVXLANTunnelStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVXLANTunnelStatsRxPackets.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelStatsRxPackets.setDescription('This object provides the number of packets received on a tunnel interface.')
hpicfVXLANTunnelStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVXLANTunnelStatsTxPackets.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelStatsTxPackets.setDescription('This object provides the number of packets transmitted on a tunnel interface.')
hpicfVXLANTunnelStatsClear = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVXLANTunnelStatsClear.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelStatsClear.setDescription('This object clears tunnel interface statistics when set to TRUE. A GET request for this object always returns FALSE.')
hpicfMaxVXLANTunnels = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMaxVXLANTunnels.setStatus('current')
if mibBuilder.loadTexts: hpicfMaxVXLANTunnels.setDescription('Maximum number of VXLAN tunnels supported on the device.')
hpicfTotalVXLANTunnels = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTotalVXLANTunnels.setStatus('current')
if mibBuilder.loadTexts: hpicfTotalVXLANTunnels.setDescription('Total number of VXLAN tunnels configured on the device.')
hpicfVXLANTunnelStatsTxMTUViolation = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVXLANTunnelStatsTxMTUViolation.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelStatsTxMTUViolation.setDescription('This object provides the number of packets which were not transmitted from the tunnel interface because of MTU violations. This counter is global for all VXLAN tunnels')
hpicfVXLANTunnelGlobalStatsDropCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVXLANTunnelGlobalStatsDropCount.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelGlobalStatsDropCount.setDescription('This object provides the number of packets dropped for the following reasons: 1. When a VXLAN packet is received from unknown sources. 2. When a VXLAN packet received has IP options.')
hpicfVXLANTunnelGlobalStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVXLANTunnelGlobalStatsClear.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelGlobalStatsClear.setDescription('This object clears global tunnel interface statistics when set to TRUE. A GET request for this object always returns FALSE.')
hpicfVXLANTunnelEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVXLANTunnelEnable.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelEnable.setDescription('This object, when set to TRUE, allows VXLAN tunnels to be created.')
hpicfVXLANTunnelUDPPort = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(4789)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVXLANTunnelUDPPort.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelUDPPort.setDescription('This object sets the UDP destination port of teh VXLAN tunnel.')
hpicfMTUDropRouterAddrType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMTUDropRouterAddrType.setStatus('current')
if mibBuilder.loadTexts: hpicfMTUDropRouterAddrType.setDescription('Address type of the router that sent the ICMP destination unreachable message.')
hpicfMTUDropRouterAddr = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMTUDropRouterAddr.setStatus('current')
if mibBuilder.loadTexts: hpicfMTUDropRouterAddr.setDescription('IP address of the router that sent the ICMP destination unreachable message.')
hpicfMTUDropRouterMTU = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMTUDropRouterMTU.setStatus('current')
if mibBuilder.loadTexts: hpicfMTUDropRouterMTU.setDescription('The MTU of the router interface that sent the ICMP destination unreachable message.')
hpicfMTUDropVTEPSrcAddrType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 4), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMTUDropVTEPSrcAddrType.setStatus('current')
if mibBuilder.loadTexts: hpicfMTUDropVTEPSrcAddrType.setDescription('Address type of the source IP address of the inner packet that was sent through the VXLAN tunnel interface.')
hpicfMTUDropVTEPSource = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 5), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMTUDropVTEPSource.setStatus('current')
if mibBuilder.loadTexts: hpicfMTUDropVTEPSource.setDescription('Source IP address of the inner packet that was sent through the VXLAN tunnel.')
hpicfMTUDropVTEPDstAddrType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 6), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMTUDropVTEPDstAddrType.setStatus('current')
if mibBuilder.loadTexts: hpicfMTUDropVTEPDstAddrType.setDescription('Address type of the destination IP address of the inner packet that was sent through the VXLAN tunnel.')
hpicfMTUDropVTEPDest = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 7), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMTUDropVTEPDest.setStatus('current')
if mibBuilder.loadTexts: hpicfMTUDropVTEPDest.setDescription('Destination IP address of the inner packet that was sent through the VXLAN tunnel.')
hpicfMTUDropInIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 8), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMTUDropInIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfMTUDropInIfIndex.setDescription('Interface index of the inbound VLAN of the ICMP destination unreachable packet.')
hpicfMTUDropNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMTUDropNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: hpicfMTUDropNotifyEnable.setDescription(' This enables or disables the virtual network notifications.')
hpicfVirtualNetworkIcmpErrorRcvd = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 0, 1)).setObjects(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterAddrType"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterAddr"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterMTU"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPSrcAddrType"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPSource"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPDstAddrType"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPDest"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropInIfIndex"), ("TUNNEL-MIB", "tunnelIfAddressType"), ("TUNNEL-MIB", "tunnelIfLocalInetAddress"), ("TUNNEL-MIB", "tunnelIfRemoteInetAddress"))
if mibBuilder.loadTexts: hpicfVirtualNetworkIcmpErrorRcvd.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkIcmpErrorRcvd.setDescription('This notification is generated when the tunnel source recevied an ICMP destination unreachable error message from one of teh underlay networks due to MTU violation.')
hpicfVirtualNetworkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 1))
hpicfVirtualNetworkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2))
hpicfVirtualNetworkCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 1, 1)).setObjects(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkGroup"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkScalarGroup"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelStatsGroup"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelScalarGroup"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkNotifyScalarsGroup"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVirtualNetworkCompliance = hpicfVirtualNetworkCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkCompliance.setDescription('The compliance statement for the Virtual Network MIB.')
hpicfVirtualNetworkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 1)).setObjects(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkName"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkVLANID"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVirtualNetworkGroup = hpicfVirtualNetworkGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkGroup.setDescription('The collection of objects providing information about the Virtual Network.')
hpicfVirtualNetworkScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 2)).setObjects(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMaxVirtualNetworks"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfTotalVirtualNetworks"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVirtualNetworkScalarGroup = hpicfVirtualNetworkScalarGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkScalarGroup.setDescription('The collection of objects providing information about the Virtual Network scalar objects.')
hpicfVXLANTunnelStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 3)).setObjects(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelIfDownReason"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelIfNextHopIpType"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelIfNextHopIp"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelIfNextHopInterface"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelIfNextHopPortName"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelStatsRxPackets"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelStatsTxPackets"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelStatsClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVXLANTunnelStatsGroup = hpicfVXLANTunnelStatsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelStatsGroup.setDescription('The collection of objects providing information about the VXLAN tunnel statistics.')
hpicfVXLANTunnelScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 4)).setObjects(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMaxVXLANTunnels"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfTotalVXLANTunnels"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelStatsTxMTUViolation"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelGlobalStatsDropCount"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelGlobalStatsClear"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelEnable"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelUDPPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVXLANTunnelScalarGroup = hpicfVXLANTunnelScalarGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfVXLANTunnelScalarGroup.setDescription('The collection of objects providing information about the Virtual Network scalar objects.')
hpicfVirtualNetworkNotifyScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 5)).setObjects(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterAddrType"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterAddr"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterMTU"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPSrcAddrType"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPSource"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPDstAddrType"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPDest"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropInIfIndex"), ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVirtualNetworkNotifyScalarsGroup = hpicfVirtualNetworkNotifyScalarsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkNotifyScalarsGroup.setDescription('Group of objects required for notifications.')
hpicfVirtualNetworkNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 6)).setObjects(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkIcmpErrorRcvd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVirtualNetworkNotificationsGroup = hpicfVirtualNetworkNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfVirtualNetworkNotificationsGroup.setDescription('Notifications for the VXLAN tunnels.')
mibBuilder.exportSymbols("HP-ICF-VIRTUAL-NETWORK-MIB", hpicfVirtualNetworkIcmpErrorRcvd=hpicfVirtualNetworkIcmpErrorRcvd, hpicfMTUDropVTEPDest=hpicfMTUDropVTEPDest, hpicfVirtualNetworkScalars=hpicfVirtualNetworkScalars, hpicfVXLANTunnelStatsTxPackets=hpicfVXLANTunnelStatsTxPackets, hpicfVXLANTunnelIfNextHopInterface=hpicfVXLANTunnelIfNextHopInterface, hpicfVXLANTunnelIfNextHopPortName=hpicfVXLANTunnelIfNextHopPortName, PYSNMP_MODULE_ID=hpicfVirtualNetwork, hpicfVXLANTunnelIfNextHopIpType=hpicfVXLANTunnelIfNextHopIpType, hpicfVirtualNetworkGroups=hpicfVirtualNetworkGroups, hpicfVXLANTunnelGlobalStatsClear=hpicfVXLANTunnelGlobalStatsClear, hpicfVXLANTunnelUDPPort=hpicfVXLANTunnelUDPPort, hpicfMaxVXLANTunnels=hpicfMaxVXLANTunnels, hpicfMTUDropVTEPSource=hpicfMTUDropVTEPSource, hpicfVirtualNetworkNotifyScalarsGroup=hpicfVirtualNetworkNotifyScalarsGroup, hpicfVirtualNetworkNotifyScalars=hpicfVirtualNetworkNotifyScalars, hpicfVXLANTunnelIfEntry=hpicfVXLANTunnelIfEntry, hpicfVXLANTunnelStatsRxPackets=hpicfVXLANTunnelStatsRxPackets, hpicfVirtualNetworkGroup=hpicfVirtualNetworkGroup, hpicfVirtualNetworkObjects=hpicfVirtualNetworkObjects, hpicfMTUDropRouterAddrType=hpicfMTUDropRouterAddrType, hpicfVirtualNetworkEntry=hpicfVirtualNetworkEntry, hpicfVirtualNetwork=hpicfVirtualNetwork, hpicfVirtualNetworkTable=hpicfVirtualNetworkTable, hpicfMTUDropVTEPSrcAddrType=hpicfMTUDropVTEPSrcAddrType, hpicfVirtualNetworkCompliance=hpicfVirtualNetworkCompliance, hpicfVirtualNetworkConformance=hpicfVirtualNetworkConformance, hpicfVirtualNetworkNotificationsGroup=hpicfVirtualNetworkNotificationsGroup, hpicfVirtualNetworkID=hpicfVirtualNetworkID, hpicfVirtualNetworkVLANID=hpicfVirtualNetworkVLANID, hpicfVXLANTunnelStatsTxMTUViolation=hpicfVXLANTunnelStatsTxMTUViolation, hpicfMaxVirtualNetworks=hpicfMaxVirtualNetworks, hpicfVXLANTunnelStatsClear=hpicfVXLANTunnelStatsClear, hpicfVXLANTunnelIfTable=hpicfVXLANTunnelIfTable, hpicfVirtualNetworkCompliances=hpicfVirtualNetworkCompliances, hpicfVXLANTunnelEnable=hpicfVXLANTunnelEnable, hpicfMTUDropRouterMTU=hpicfMTUDropRouterMTU, hpicfVXLANTunnelScalars=hpicfVXLANTunnelScalars, hpicfVXLANTunnelConfigObjects=hpicfVXLANTunnelConfigObjects, hpicfTotalVirtualNetworks=hpicfTotalVirtualNetworks, hpicfVXLANTunnelIfNextHopIp=hpicfVXLANTunnelIfNextHopIp, hpicfMTUDropRouterAddr=hpicfMTUDropRouterAddr, hpicfVXLANTunnelIfDownReason=hpicfVXLANTunnelIfDownReason, hpicfVXLANTunnelObjects=hpicfVXLANTunnelObjects, hpicfMTUDropNotifyEnable=hpicfMTUDropNotifyEnable, hpicfTunnelObjects=hpicfTunnelObjects, hpicfTotalVXLANTunnels=hpicfTotalVXLANTunnels, hpicfVXLANTunnelStatsGroup=hpicfVXLANTunnelStatsGroup, hpicfVirtualNetworkName=hpicfVirtualNetworkName, hpicfVXLANTunnelGlobalStatsDropCount=hpicfVXLANTunnelGlobalStatsDropCount, hpicfMTUDropVTEPDstAddrType=hpicfMTUDropVTEPDstAddrType, hpicfVirtualNetworkNotifications=hpicfVirtualNetworkNotifications, hpicfVirtualNetworkRowStatus=hpicfVirtualNetworkRowStatus, hpicfVirtualNetworkScalarGroup=hpicfVirtualNetworkScalarGroup, hpicfVXLANTunnelScalarGroup=hpicfVXLANTunnelScalarGroup, hpicfMTUDropInIfIndex=hpicfMTUDropInIfIndex)
