#
# PySNMP MIB module FASTPATH-IPV6-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-IPV6-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:12:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
fastPath, = mibBuilder.importSymbols("BROADCOM-REF-MIB", "fastPath")
InetAddressIPv4, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressPrefixLength")
Ipv6IfIndex, Ipv6AddressPrefix, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6IfIndex", "Ipv6AddressPrefix", "Ipv6Address")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, MibIdentifier, ObjectIdentity, Unsigned32, Counter64, IpAddress, Counter32, Gauge32, Bits, NotificationType, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Counter64", "IpAddress", "Counter32", "Gauge32", "Bits", "NotificationType", "Integer32", "TimeTicks")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
fastPathIpv6Tunnel = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27))
fastPathIpv6Tunnel.setRevisions(('2007-05-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathIpv6Tunnel.setRevisionsDescriptions(('Broadcom branding related changes.',))
if mibBuilder.loadTexts: fastPathIpv6Tunnel.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: fastPathIpv6Tunnel.setOrganization('Broadcom Corporation')
if mibBuilder.loadTexts: fastPathIpv6Tunnel.setContactInfo(' Customer Support Postal: Broadcom Corporation 100, Perimeter Park Drive Morrisville, NC 27560 Tel: +1 919 865 2700')
if mibBuilder.loadTexts: fastPathIpv6Tunnel.setDescription('The Broadcom Private MIB for FastPath IPV6 Tunnel')
agentTunnelIPV6Group = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1))
agentTunnelIPV6Table = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 1), )
if mibBuilder.loadTexts: agentTunnelIPV6Table.setStatus('current')
if mibBuilder.loadTexts: agentTunnelIPV6Table.setDescription('A summary table of the IPV6 tunnel instances')
agentTunnelIPV6Entry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 1, 1), ).setIndexNames((0, "FASTPATH-IPV6-TUNNEL-MIB", "agentTunnelID"))
if mibBuilder.loadTexts: agentTunnelIPV6Entry.setStatus('current')
if mibBuilder.loadTexts: agentTunnelIPV6Entry.setDescription('')
agentTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: agentTunnelID.setStatus('current')
if mibBuilder.loadTexts: agentTunnelID.setDescription('The tunnel ID is associated with Internal Interface number which is generated when we create a tunnel, and is used to configure the tunnel.')
agentTunnelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentTunnelIfIndex.setStatus('current')
if mibBuilder.loadTexts: agentTunnelIfIndex.setDescription('The external interface of the tunnel is associted with internal interface. The tunnel ID associated with Internal Interface number is generated when we create a tunnel, which is used to configure the tunnel.')
agentTunnelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("undefined", 1), ("ip6over4", 2), ("ip6to4", 3))).clone('undefined')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentTunnelMode.setStatus('current')
if mibBuilder.loadTexts: agentTunnelMode.setDescription('Specifies the type of Tunnel either undefined, 6over4 or 6to4. The default value is undefined. It supports 6over4 which supports an assigned IPV6 address, an IPV4 address is not allowed. For this mode, the tunnel source and tunnel destination must be IPV4 address. For 6to4 tunnel, the tunnel source must be IPv4 address. Tunnel destination should not be set. The first 48-bits of the IPv4 address assigned to the 6to4 tunnel should be of the format 2002:sourceIpv4address.')
agentTunnelLocalIP4Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 1, 1, 4), InetAddressIPv4()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentTunnelLocalIP4Addr.setStatus('current')
if mibBuilder.loadTexts: agentTunnelLocalIP4Addr.setDescription('The address of the Local endpoint of the tunnel i.e. the source address used in the outer IP header. It is 0.0.0.0 if unknown or the tunnel is over IPv6.')
agentTunnelRemoteIP4Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 1, 1, 5), InetAddressIPv4()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentTunnelRemoteIP4Addr.setStatus('current')
if mibBuilder.loadTexts: agentTunnelRemoteIP4Addr.setDescription('The address of the Remote endpoint of the tunnel i.e. the destination address used in the outer IP header. It is 0.0.0.0 if the tunnel is unknown or IPv6 address, or not a point to point link')
agentTunnelLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentTunnelLocalIfIndex.setStatus('current')
if mibBuilder.loadTexts: agentTunnelLocalIfIndex.setDescription('Specifies the interface for IPv6 Tunnel Source')
agentTunnelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentTunnelStatus.setStatus('current')
if mibBuilder.loadTexts: agentTunnelStatus.setDescription('Status of this instance.Row can be added or deleted by setting the value to createAndGo/destroy active(1) - this Tunnel instance is active createAndGo(4) - set to this value to create an instance destroy(6) - set to this value to delete an instance')
agentTunnelIcmpUnreachableMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentTunnelIcmpUnreachableMode.setStatus('current')
if mibBuilder.loadTexts: agentTunnelIcmpUnreachableMode.setDescription('Specifies the Mode of Sending ICMPv6 Unreachable messages on this tunnel interface.')
agentTunnelIPV6PrefixTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 2), )
if mibBuilder.loadTexts: agentTunnelIPV6PrefixTable.setStatus('current')
if mibBuilder.loadTexts: agentTunnelIPV6PrefixTable.setDescription('A table of the IPV6 prefixes associated with tunnel instances')
agentTunnelIPV6PrefixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 2, 1), ).setIndexNames((0, "FASTPATH-IPV6-TUNNEL-MIB", "agentTunnelID"), (0, "FASTPATH-IPV6-TUNNEL-MIB", "agentTunnelIPV6PrefixPrefix"), (0, "FASTPATH-IPV6-TUNNEL-MIB", "agentTunnelIPV6PrefixPrefixLen"))
if mibBuilder.loadTexts: agentTunnelIPV6PrefixEntry.setStatus('current')
if mibBuilder.loadTexts: agentTunnelIPV6PrefixEntry.setDescription('')
agentTunnelIPV6PrefixPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 2, 1, 1), Ipv6AddressPrefix())
if mibBuilder.loadTexts: agentTunnelIPV6PrefixPrefix.setStatus('current')
if mibBuilder.loadTexts: agentTunnelIPV6PrefixPrefix.setDescription('The prefix associated with the tunnel interface. The data type is used to model the IPV6 address. It is a binary string of 16 octects in network byte-order. It specifies the IP address of tunnel which will be in IPV6 Format, generated using internal interface number.')
agentTunnelIPV6PrefixPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 2, 1, 2), InetAddressPrefixLength())
if mibBuilder.loadTexts: agentTunnelIPV6PrefixPrefixLen.setStatus('current')
if mibBuilder.loadTexts: agentTunnelIPV6PrefixPrefixLen.setDescription('The length of the prefix (in bits).')
agentTunnelIPV6PrefixStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 27, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentTunnelIPV6PrefixStatus.setStatus('current')
if mibBuilder.loadTexts: agentTunnelIPV6PrefixStatus.setDescription('Status of this instance.Row can be added or deleted by setting the value to createAndGo/destroy active(1) - this Tunnel instance is active createAndGo(4) - set to this value to create an instance destroy(6) - set to this value to delete an instance')
mibBuilder.exportSymbols("FASTPATH-IPV6-TUNNEL-MIB", agentTunnelIPV6Table=agentTunnelIPV6Table, agentTunnelIcmpUnreachableMode=agentTunnelIcmpUnreachableMode, agentTunnelRemoteIP4Addr=agentTunnelRemoteIP4Addr, fastPathIpv6Tunnel=fastPathIpv6Tunnel, agentTunnelID=agentTunnelID, agentTunnelLocalIP4Addr=agentTunnelLocalIP4Addr, agentTunnelStatus=agentTunnelStatus, agentTunnelIPV6PrefixTable=agentTunnelIPV6PrefixTable, agentTunnelLocalIfIndex=agentTunnelLocalIfIndex, agentTunnelIPV6Entry=agentTunnelIPV6Entry, agentTunnelIPV6PrefixPrefix=agentTunnelIPV6PrefixPrefix, agentTunnelIPV6PrefixStatus=agentTunnelIPV6PrefixStatus, PYSNMP_MODULE_ID=fastPathIpv6Tunnel, agentTunnelIfIndex=agentTunnelIfIndex, agentTunnelIPV6PrefixEntry=agentTunnelIPV6PrefixEntry, agentTunnelIPV6PrefixPrefixLen=agentTunnelIPV6PrefixPrefixLen, agentTunnelIPV6Group=agentTunnelIPV6Group, agentTunnelMode=agentTunnelMode)
