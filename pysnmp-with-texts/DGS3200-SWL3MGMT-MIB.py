#
# PySNMP MIB module DGS3200-SWL3MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS3200-SWL3MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:46:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, ObjectIdentity, ModuleIdentity, iso, Gauge32, Bits, Integer32, Unsigned32, TimeTicks, MibIdentifier, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "ObjectIdentity", "ModuleIdentity", "iso", "Gauge32", "Bits", "Integer32", "Unsigned32", "TimeTicks", "MibIdentifier", "NotificationType", "Counter32")
TruthValue, MacAddress, RowStatus, PhysAddress, DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "RowStatus", "PhysAddress", "DisplayString", "TextualConvention", "TimeStamp")
dgs3200, = mibBuilder.importSymbols("SW3200PRIMGMT-MIB", "dgs3200")
swL3MgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3))
if mibBuilder.loadTexts: swL3MgmtMIB.setLastUpdated('0008240000Z')
if mibBuilder.loadTexts: swL3MgmtMIB.setOrganization(' ')
if mibBuilder.loadTexts: swL3MgmtMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swL3MgmtMIB.setDescription('The Structure of Layer 3 Network Management Information for the proprietary enterprise.')
class NodeAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class NetAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

swL3IpMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2))
swL3IpCtrlMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1))
class Ipv6Address(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 addresses. This is a binary string of 16 octets in network byte-order.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class VrId(TextualConvention, Integer32):
    description = 'A number which, along with an interface index (ifIndex), serves to uniquely identify a virtual router on a given VRRP router. A set of one or more associated addresses is assigned to a VRID.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

swL3IpCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3), )
if mibBuilder.loadTexts: swL3IpCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlTable.setDescription('This table contains IP interface information.')
swL3IpCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1), ).setIndexNames((0, "DGS3200-SWL3MGMT-MIB", "swL3IpCtrlInterfaceName"))
if mibBuilder.loadTexts: swL3IpCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlEntry.setDescription('A list of information about a specific IP interface.')
swL3IpCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlInterfaceName.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlInterfaceName.setDescription('This object indicates the name of the IP interface.')
swL3IpCtrlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIfIndex.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIfIndex.setDescription('This object uniquely identifies the IP interface number in the swL3IpCtrlTable.')
swL3IpCtrlIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpAddr.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpAddr.setDescription('The IP address of the interface. This object only can take the value of the unicast IP address.')
swL3IpCtrlIpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpSubnetMask.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpSubnetMask.setDescription('The IP net mask for this interface.')
swL3IpCtrlVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlVlanName.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlVlanName.setDescription("This object indicates the IP control entry's VLAN name. The VLAN name in each entry must be unique in the IP Control Table.")
swL3IpCtrlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("bootp", 3), ("dhcp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlMode.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlMode.setDescription('This object indicates the IP operation mode. other(1) - This entry is currently in use but the conditions under which it will remain are determined by each of the following values. bootp(3) - The IP address will be set automatically from a BOOTP server. dhcp(4) - The IP address will be set automatically from a DHCP server.')
swL3IpCtrlAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlAdminState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlAdminState.setDescription('The state of the IP interface.')
swL3IpCtrlIpv6LinkLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 14), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAddress.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAddress.setDescription('The IPv6 link local address for this interface.')
swL3IpCtrlIpv6LinkLocalPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalPrefixLen.setDescription('The IPv6 prefix length for this IPv6 link local address.')
swL3IpCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpCtrlState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlState.setDescription('This variable displays the status of the entry. The status is used for creating, modifying, and deleting instances of the objects in this table.')
swL3IpCtrlIpv6LinkLocalAutoState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAutoState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAutoState.setDescription('The state of the IPv6 link local auto.')
swL3IpCtrlDhcpv6ClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlDhcpv6ClientState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlDhcpv6ClientState.setDescription('The object indicates the state of the DHCPv6 client.')
swL3IpCtrlIpDhcpOption12State = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12State.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12State.setDescription('Enable or disable insertion of option 12 in the DHCPDISCOVER and DHCPREQUEST message.')
swL3IpCtrlIpDhcpOption12HostName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 3, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12HostName.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12HostName.setDescription('Specify the host name to be inserted in the DHCPDISCOVER and DHCPREQUEST message. The specified host name must start with a letter, end with a letter or digit, and have only letters, digits, and hyphen as interior characters; the maximal length is 63. By default, the host name is empty. When set an empty host name, means to clear the host name setting and use the default value to encode option 12.')
swL3Ipv6CtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4), )
if mibBuilder.loadTexts: swL3Ipv6CtrlTable.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlTable.setDescription('This table contains IPv6 information of an IP interface.')
swL3Ipv6CtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1), ).setIndexNames((0, "DGS3200-SWL3MGMT-MIB", "swL3Ipv6CtrlInterfaceName"))
if mibBuilder.loadTexts: swL3Ipv6CtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlEntry.setDescription('A list of IPv6 information about a specific IP interface.')
swL3Ipv6CtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6CtrlInterfaceName.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlInterfaceName.setDescription('This object indicates the name of the IP interface.')
swL3Ipv6CtrlMaxReassmblySize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6CtrlMaxReassmblySize.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlMaxReassmblySize.setDescription('Maximum Reassembly Size of the IP interface.')
swL3Ipv6CtrlNsRetransTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlNsRetransTimer.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlNsRetransTimer.setDescription("Neighbor solicitation's retransmit timer. The unit is set in milliseconds.")
swL3Ipv6CtrlRaState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlRaState.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlRaState.setDescription('Neighbor solicited state.')
swL3Ipv6CtrlRaMinRtrAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 1350))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlRaMinRtrAdvInterval.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlRaMinRtrAdvInterval.setDescription('The minimum time allowed between sending unsolicited multicast Router Advertisements from the interface. The unit is set in seconds. It must be no less than 3 seconds and no greater than .75 * MaxRtrAdvInterval. Default value: 0.33 * MaxRtrAdvInterval')
swL3Ipv6CtrlRaMaxRtrAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 1800)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlRaMaxRtrAdvInterval.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlRaMaxRtrAdvInterval.setDescription('The maximum time allowed between sending unsolicited multicast Router Advertisements from the interface. The unit is set in seconds.')
swL3Ipv6CtrlRaLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlRaLifeTime.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlRaLifeTime.setDescription('Indicates the lifetime of the router as the default router.')
swL3Ipv6CtrlRaReachableTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlRaReachableTime.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlRaReachableTime.setDescription('Indicates the amount of time that a node can consider a neighboring node reachable after receiving a reachability confirmation.')
swL3Ipv6CtrlRaRetransTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlRaRetransTime.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlRaRetransTime.setDescription('Indicates the amount of time between retransmissions of neighbor solicited messages. The unit is set in millisecond.')
swL3Ipv6CtrlRaHopLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlRaHopLimit.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlRaHopLimit.setDescription('Indicates the default value of the hop limit field in the IPv6 header for packets sent by hosts that receive this RA message.')
swL3Ipv6CtrlRaManagedFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlRaManagedFlag.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlRaManagedFlag.setDescription('When enabled, it indicates that hosts receiving this RA must use a stateful address configuration protocol to obtain an address in the addition to the addresses derived from the stateless address configuration.')
swL3Ipv6CtrlRaOtherConfigFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlRaOtherConfigFlag.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlRaOtherConfigFlag.setDescription('When enabled, it indicates that hosts receiving this RA must use a stateful address configuration protocol to obtain an on-link address configuration information.')
swL3Ipv6AddressCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 5), )
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlTable.setDescription('This table contains IPv6 address information for each IP interface.')
swL3Ipv6AddressCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 5, 1), ).setIndexNames((0, "DGS3200-SWL3MGMT-MIB", "swL3Ipv6AddressCtrlInterfaceName"), (0, "DGS3200-SWL3MGMT-MIB", "swL3Ipv6Address"), (0, "DGS3200-SWL3MGMT-MIB", "swL3Ipv6AddressCtrlPrefixLen"))
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlEntry.setDescription('A list of information about a specific IPv6 address.')
swL3Ipv6AddressCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlInterfaceName.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlInterfaceName.setDescription('This object indicates the name of the IP interface. ')
swL3Ipv6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 5, 1, 2), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6Address.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6Address.setDescription('Specify the IPv6 address.')
swL3Ipv6AddressCtrlPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlPrefixLen.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlPrefixLen.setDescription('Indicates the prefix length of this IPv6 address.')
swL3Ipv6AddressCtrlPreferredLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967294))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlPreferredLifeTime.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlPreferredLifeTime.setDescription('Indicates the number of seconds that an address, based on the specified prefix, using the stateless address configuration, remains in preferred state. For an infinite valid lifetime, the value can be set to 0xffffffff.')
swL3Ipv6AddressCtrlValidLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967294))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlValidLifeTime.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlValidLifeTime.setDescription('Indicates the number of seconds that an address, based on the specified prefix, using the stateless address configuration, remains valid. For an infinite valid lifetime, the value can be set to 0xffffffff.')
swL3Ipv6AddressCtrlOnLinkFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlOnLinkFlag.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlOnLinkFlag.setDescription('When enabled, the address implied by the specified prefix is available on the link where the RA message is received.')
swL3Ipv6AddressCtrlAutonomousFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlAutonomousFlag.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlAutonomousFlag.setDescription('When enabled, the specified prefix will be used to create an autonomous address configuration.')
swL3Ipv6AddressCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlState.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlState.setDescription('This variable displays the status of the entry. The status is used for creating, modifying, and deleting instances of the objects in this table.')
swL3Ipv6AddressCtrlAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("dhcpv6", 2), ("stateless", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlAddressType.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlAddressType.setDescription('This object indicates the type of the IPv6 address. manual(1): the IPv6 address is configured by user. dhcpv6(2): the IPv6 address is assigned by DHCPv6 server. stateless(3): the IPv6 address is assigned by router advertisement.')
swL3IpCtrlAllIpIfState = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 101, 1, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlAllIpIfState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlAllIpIfState.setDescription('This object indicates all interface function state of the device.')
mibBuilder.exportSymbols("DGS3200-SWL3MGMT-MIB", swL3Ipv6CtrlTable=swL3Ipv6CtrlTable, swL3Ipv6AddressCtrlOnLinkFlag=swL3Ipv6AddressCtrlOnLinkFlag, swL3Ipv6CtrlRaState=swL3Ipv6CtrlRaState, swL3IpCtrlAllIpIfState=swL3IpCtrlAllIpIfState, swL3Ipv6AddressCtrlAutonomousFlag=swL3Ipv6AddressCtrlAutonomousFlag, swL3Ipv6CtrlRaOtherConfigFlag=swL3Ipv6CtrlRaOtherConfigFlag, swL3Ipv6AddressCtrlEntry=swL3Ipv6AddressCtrlEntry, swL3Ipv6Address=swL3Ipv6Address, swL3Ipv6AddressCtrlPreferredLifeTime=swL3Ipv6AddressCtrlPreferredLifeTime, NetAddress=NetAddress, swL3IpCtrlVlanName=swL3IpCtrlVlanName, swL3IpCtrlIpSubnetMask=swL3IpCtrlIpSubnetMask, swL3IpCtrlIpv6LinkLocalAddress=swL3IpCtrlIpv6LinkLocalAddress, swL3Ipv6CtrlRaRetransTime=swL3Ipv6CtrlRaRetransTime, swL3Ipv6AddressCtrlAddressType=swL3Ipv6AddressCtrlAddressType, VrId=VrId, swL3IpCtrlIpDhcpOption12HostName=swL3IpCtrlIpDhcpOption12HostName, swL3IpCtrlIpv6LinkLocalPrefixLen=swL3IpCtrlIpv6LinkLocalPrefixLen, swL3Ipv6CtrlMaxReassmblySize=swL3Ipv6CtrlMaxReassmblySize, swL3Ipv6CtrlRaReachableTime=swL3Ipv6CtrlRaReachableTime, swL3Ipv6CtrlNsRetransTimer=swL3Ipv6CtrlNsRetransTimer, swL3Ipv6AddressCtrlInterfaceName=swL3Ipv6AddressCtrlInterfaceName, swL3Ipv6CtrlInterfaceName=swL3Ipv6CtrlInterfaceName, swL3Ipv6CtrlRaManagedFlag=swL3Ipv6CtrlRaManagedFlag, swL3IpCtrlDhcpv6ClientState=swL3IpCtrlDhcpv6ClientState, swL3Ipv6CtrlRaLifeTime=swL3Ipv6CtrlRaLifeTime, swL3Ipv6CtrlRaHopLimit=swL3Ipv6CtrlRaHopLimit, swL3Ipv6CtrlEntry=swL3Ipv6CtrlEntry, swL3IpCtrlEntry=swL3IpCtrlEntry, Ipv6Address=Ipv6Address, swL3IpCtrlTable=swL3IpCtrlTable, swL3MgmtMIB=swL3MgmtMIB, swL3Ipv6CtrlRaMaxRtrAdvInterval=swL3Ipv6CtrlRaMaxRtrAdvInterval, swL3Ipv6AddressCtrlPrefixLen=swL3Ipv6AddressCtrlPrefixLen, swL3IpCtrlIpDhcpOption12State=swL3IpCtrlIpDhcpOption12State, swL3Ipv6AddressCtrlTable=swL3Ipv6AddressCtrlTable, NodeAddress=NodeAddress, PYSNMP_MODULE_ID=swL3MgmtMIB, swL3IpMgmt=swL3IpMgmt, swL3IpCtrlState=swL3IpCtrlState, swL3IpCtrlIpAddr=swL3IpCtrlIpAddr, swL3IpCtrlInterfaceName=swL3IpCtrlInterfaceName, swL3Ipv6AddressCtrlValidLifeTime=swL3Ipv6AddressCtrlValidLifeTime, swL3IpCtrlAdminState=swL3IpCtrlAdminState, swL3Ipv6CtrlRaMinRtrAdvInterval=swL3Ipv6CtrlRaMinRtrAdvInterval, swL3IpCtrlIpv6LinkLocalAutoState=swL3IpCtrlIpv6LinkLocalAutoState, swL3IpCtrlMode=swL3IpCtrlMode, swL3IpCtrlMgmt=swL3IpCtrlMgmt, swL3Ipv6AddressCtrlState=swL3Ipv6AddressCtrlState, swL3IpCtrlIfIndex=swL3IpCtrlIfIndex)
