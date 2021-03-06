#
# PySNMP MIB module IPV6-LOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV6-LOOPBACK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:56:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
InetAddressPrefixLength, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength")
Ipv6AddressPrefix, = mibBuilder.importSymbols("IPV6-TC", "Ipv6AddressPrefix")
agentLoopbackID, = mibBuilder.importSymbols("LOOPBACK-MIB", "agentLoopbackID")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ObjectIdentity, NotificationType, Bits, ModuleIdentity, Integer32, IpAddress, TimeTicks, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Gauge32, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "NotificationType", "Bits", "ModuleIdentity", "Integer32", "IpAddress", "TimeTicks", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Gauge32", "mib-2")
RowStatus, TextualConvention, DisplayString, PhysAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "PhysAddress", "TruthValue")
ipv6Loopback = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 23))
if mibBuilder.loadTexts: ipv6Loopback.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: ipv6Loopback.setOrganization('QCI')
if mibBuilder.loadTexts: ipv6Loopback.setContactInfo(' Customer Support Postal: Quanta Computer Inc. 4, Wen Ming 1 St., Kuei Shan Hsiang, Tao Yuan Shien, Taiwan, R.O.C. Tel: +886 3 328 0050 E-Mail: strong.chen@quantatw.com')
if mibBuilder.loadTexts: ipv6Loopback.setDescription('The Quanta Private MIB for Loopback IPV6 address configuration')
agentLoopbackIpv6Group = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1))
agentLoopbackIpv6PrefixTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1), )
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixTable.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixTable.setDescription('A table of the Ipv6 prefixes associated with loopback instances')
agentLoopbackIpv6PrefixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1), ).setIndexNames((0, "LOOPBACK-MIB", "agentLoopbackID"), (0, "IPV6-LOOPBACK-MIB", "agentLoopbackIpv6PrefixPrefix"), (0, "IPV6-LOOPBACK-MIB", "agentLoopbackIpv6PrefixPrefixLen"))
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixEntry.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixEntry.setDescription('')
agentLoopbackIpv6PrefixPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1, 1), Ipv6AddressPrefix())
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixPrefix.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixPrefix.setDescription('The prefix associated with the loopback interface. The data type is used to model the Ipv6 address. It is a binary string of 16 octects in network byte-order. It specifies the IP address of loopback which will be in Ipv6 Format, generated using internal interface number.')
agentLoopbackIpv6PrefixPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1, 2), InetAddressPrefixLength())
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixPrefixLen.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixPrefixLen.setDescription('The length of the prefix (in bits).')
agentLoopbackIpv6PrefixStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixStatus.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixStatus.setDescription('Status of this instance.Row can be added or deleted by setting the value to createAndGo/destroy active(1) - this Loopback instance is active createAndGo(4) - set to this value to create an instance destroy(6) - set to this value to delete an instance')
mibBuilder.exportSymbols("IPV6-LOOPBACK-MIB", agentLoopbackIpv6PrefixStatus=agentLoopbackIpv6PrefixStatus, PYSNMP_MODULE_ID=ipv6Loopback, agentLoopbackIpv6PrefixEntry=agentLoopbackIpv6PrefixEntry, ipv6Loopback=ipv6Loopback, agentLoopbackIpv6PrefixPrefix=agentLoopbackIpv6PrefixPrefix, agentLoopbackIpv6PrefixTable=agentLoopbackIpv6PrefixTable, agentLoopbackIpv6PrefixPrefixLen=agentLoopbackIpv6PrefixPrefixLen, agentLoopbackIpv6Group=agentLoopbackIpv6Group)
