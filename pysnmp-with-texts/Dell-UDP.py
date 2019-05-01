#
# PySNMP MIB module Dell-UDP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-UDP
# Produced by pysmi-0.3.4 at Wed May  1 12:57:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ipCidrRouteEntry, ipCidrRouteDest, ipCidrRouteTos, ipCidrRouteMask, ipCidrRouteNextHop = mibBuilder.importSymbols("IP-FORWARD-MIB", "ipCidrRouteEntry", "ipCidrRouteDest", "ipCidrRouteTos", "ipCidrRouteMask", "ipCidrRouteNextHop")
ipAddrEntry, = mibBuilder.importSymbols("IP-MIB", "ipAddrEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, ObjectIdentity, MibIdentifier, Gauge32, Integer32, Counter64, IpAddress, iso, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Gauge32", "Integer32", "Counter64", "IpAddress", "iso", "Counter32", "ModuleIdentity")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
rsUDP = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 42))
rsUDP.setRevisions(('2004-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsUDP.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rsUDP.setLastUpdated('200406010000Z')
if mibBuilder.loadTexts: rsUDP.setOrganization('Dell')
if mibBuilder.loadTexts: rsUDP.setContactInfo('www.dell.com')
if mibBuilder.loadTexts: rsUDP.setDescription('The private MIB module definition for RND UDP MIB.')
rsUdpRelayTable = MibTable((1, 3, 6, 1, 4, 1, 89, 42, 1), )
if mibBuilder.loadTexts: rsUdpRelayTable.setStatus('current')
if mibBuilder.loadTexts: rsUdpRelayTable.setDescription('This table contains the udp relay configuration per port.')
rsUdpRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 42, 1, 1), ).setIndexNames((0, "Dell-UDP", "rsUdpRelayDstPort"), (0, "Dell-UDP", "rsUdpRelaySrcIpInf"), (0, "Dell-UDP", "rsUdpRelayDstIpAddr"))
if mibBuilder.loadTexts: rsUdpRelayEntry.setStatus('current')
if mibBuilder.loadTexts: rsUdpRelayEntry.setDescription(' The row definition for this table.')
rsUdpRelayDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 42, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsUdpRelayDstPort.setStatus('current')
if mibBuilder.loadTexts: rsUdpRelayDstPort.setDescription('The UDP port number in the UDP message header.')
rsUdpRelaySrcIpInf = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 42, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsUdpRelaySrcIpInf.setStatus('current')
if mibBuilder.loadTexts: rsUdpRelaySrcIpInf.setDescription('The source interface IP that receives UDP message. 255.255.255.255 from all IP interface. 0.0.0.0 - 0.255.255.255 and 127.0.0.0 - 127.255.255.255 not relevant addresses.')
rsUdpRelayDstIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 42, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsUdpRelayDstIpAddr.setStatus('current')
if mibBuilder.loadTexts: rsUdpRelayDstIpAddr.setDescription('The destination IP address the UDP message will be forward. 0.0.0.0 does not forward, 255.255.255.255 broadcasts to all addresses.')
rsUdpRelayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 42, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsUdpRelayStatus.setStatus('current')
if mibBuilder.loadTexts: rsUdpRelayStatus.setDescription('The status of a table entry. It is used to delete an entry from this table.')
rsUdpRelayUserInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 42, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsUdpRelayUserInfo.setStatus('current')
if mibBuilder.loadTexts: rsUdpRelayUserInfo.setDescription('The information used for implementation purposes')
rsUdpRelayMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 42, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsUdpRelayMibVersion.setStatus('current')
if mibBuilder.loadTexts: rsUdpRelayMibVersion.setDescription('Mib version. The current version is 1.')
rlUdpSessionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 42, 3), )
if mibBuilder.loadTexts: rlUdpSessionTable.setStatus('current')
if mibBuilder.loadTexts: rlUdpSessionTable.setDescription('This table contains the udp sessions information')
rlUdpSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 42, 3, 1), ).setIndexNames((0, "Dell-UDP", "rlUdpSessionLocalAddrType"), (0, "Dell-UDP", "rlUdpSessionLocalAddr"), (0, "Dell-UDP", "rlUdpSessionLocalPort"), (0, "Dell-UDP", "rlUdpSessionAppInst"))
if mibBuilder.loadTexts: rlUdpSessionEntry.setStatus('current')
if mibBuilder.loadTexts: rlUdpSessionEntry.setDescription(' The row definition for this table.')
rlUdpSessionLocalAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 42, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: rlUdpSessionLocalAddrType.setStatus('current')
if mibBuilder.loadTexts: rlUdpSessionLocalAddrType.setDescription('The type of the rlUdpSessionLocalAddress address')
rlUdpSessionLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 42, 3, 1, 2), InetAddress())
if mibBuilder.loadTexts: rlUdpSessionLocalAddr.setStatus('current')
if mibBuilder.loadTexts: rlUdpSessionLocalAddr.setDescription('The UDP port session number.')
rlUdpSessionLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 42, 3, 1, 3), Integer32())
if mibBuilder.loadTexts: rlUdpSessionLocalPort.setStatus('current')
if mibBuilder.loadTexts: rlUdpSessionLocalPort.setDescription('The UDP port local IP address.')
rlUdpSessionAppInst = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 42, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: rlUdpSessionAppInst.setStatus('current')
if mibBuilder.loadTexts: rlUdpSessionAppInst.setDescription('The instance ID for the application on the port (for future use).')
rlUdpSessionAppName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 42, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdpSessionAppName.setStatus('current')
if mibBuilder.loadTexts: rlUdpSessionAppName.setDescription('The name of the application that created the session.')
mibBuilder.exportSymbols("Dell-UDP", rsUdpRelayUserInfo=rsUdpRelayUserInfo, rsUDP=rsUDP, rlUdpSessionEntry=rlUdpSessionEntry, rsUdpRelayDstPort=rsUdpRelayDstPort, rsUdpRelayTable=rsUdpRelayTable, rsUdpRelaySrcIpInf=rsUdpRelaySrcIpInf, rsUdpRelayStatus=rsUdpRelayStatus, rlUdpSessionLocalPort=rlUdpSessionLocalPort, rlUdpSessionLocalAddrType=rlUdpSessionLocalAddrType, rsUdpRelayMibVersion=rsUdpRelayMibVersion, rlUdpSessionAppName=rlUdpSessionAppName, rsUdpRelayEntry=rsUdpRelayEntry, PYSNMP_MODULE_ID=rsUDP, rlUdpSessionLocalAddr=rlUdpSessionLocalAddr, rlUdpSessionTable=rlUdpSessionTable, rlUdpSessionAppInst=rlUdpSessionAppInst, rsUdpRelayDstIpAddr=rsUdpRelayDstIpAddr)
