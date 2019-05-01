#
# PySNMP MIB module A3COM-HUAWEI-LI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-LI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:05:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressPrefixLength, InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetPortNumber", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, IpAddress, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Gauge32, iso, Bits, Integer32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "IpAddress", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Gauge32", "iso", "Bits", "Integer32", "NotificationType", "TimeTicks")
DisplayString, TruthValue, RowStatus, TextualConvention, MacAddress, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention", "MacAddress", "DateAndTime")
h3cLI = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111))
h3cLI.setRevisions(('2009-08-25 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cLI.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: h3cLI.setLastUpdated('200908251000Z')
if mibBuilder.loadTexts: h3cLI.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: h3cLI.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cLI.setDescription('Lawful Interception MIB')
h3cLICommon = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1))
h3cLITrapBindObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 1))
h3cLIBoardInformation = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cLIBoardInformation.setStatus('current')
if mibBuilder.loadTexts: h3cLIBoardInformation.setDescription('It is a slot number.')
h3cLINotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 2))
h3cLINotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 2, 0))
h3cLIActive = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 2, 0, 1)).setObjects(("A3COM-HUAWEI-LI-MIB", "h3cLIStreamtype"))
if mibBuilder.loadTexts: h3cLIActive.setStatus('current')
if mibBuilder.loadTexts: h3cLIActive.setDescription('This Notification is sent when a type of intercepting configuration is changed from inactive to active. The value of the h3cLIStreamtype which identify the actual intercept stream is included in this notification.')
h3cLITimeOut = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 2, 0, 2)).setObjects(("A3COM-HUAWEI-LI-MIB", "h3cLIMediationRowStatus"))
if mibBuilder.loadTexts: h3cLITimeOut.setStatus('current')
if mibBuilder.loadTexts: h3cLITimeOut.setDescription('When the time specified in h3cLIMediationTimeout arrives, the device notifies the manager corresponding intercept is removed.')
h3cLIFailureInformation = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 2, 0, 3)).setObjects(("A3COM-HUAWEI-LI-MIB", "h3cLIStreamtype"), ("A3COM-HUAWEI-LI-MIB", "h3cLIBoardInformation"))
if mibBuilder.loadTexts: h3cLIFailureInformation.setStatus('current')
if mibBuilder.loadTexts: h3cLIFailureInformation.setDescription('When interception is configured on distributed device, the configuration perhaps failed on some board. If this happened, this notification will occur.')
h3cLIObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3))
h3cLINewIndex = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLINewIndex.setStatus('current')
if mibBuilder.loadTexts: h3cLINewIndex.setDescription('This object will be used as an index value for a new h3cLIMediationEntry. Whenever read, the agent will give a non-used value. This is to reduce the probability of conflict during creation of new h3cLIMediationTable entries.')
h3cLIMediationTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2), )
if mibBuilder.loadTexts: h3cLIMediationTable.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationTable.setDescription('This table describes interception gateway information with which interception device communicates.')
h3cLIMediationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-LI-MIB", "h3cLIMediationIndex"))
if mibBuilder.loadTexts: h3cLIMediationEntry.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationEntry.setDescription('An entry of configuring mediation device.')
h3cLIMediationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cLIMediationIndex.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationIndex.setDescription('h3cLIMediationIndex is a entry identifier. The Mediation Device should be responsible for making sure these are unique. Before creating a new entry, a value for this variable may be obtained by reading h3cLINewIndex to reduce the probability of a value collision.')
h3cLIMediationDestAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 2), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMediationDestAddrType.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationDestAddrType.setDescription('The type of h3cLIMediationDestAddr.')
h3cLIMediationDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMediationDestAddr.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationDestAddr.setDescription('The IP Address of the Mediation Device to receive intercepted traffic.')
h3cLIMediationDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 4), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMediationDestPort.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationDestPort.setDescription('The L4-port number on the Mediation Device to receive intercepted traffic.')
h3cLIMediationSrcInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMediationSrcInterface.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationSrcInterface.setDescription('The interface on the intercepting device from which to transmit intercepted data. If zero, intercepting device will select an outbound interface according to h3cLIMediationDestAddr.')
h3cLIMediationDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 6), Integer32().clone(34)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMediationDscp.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationDscp.setDescription('The Differentiated Services Code Point the intercepting device applies to the IP packets encapsulating the intercepted traffic.')
h3cLIMediationTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 7), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMediationTimeOut.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationTimeOut.setDescription('The time at which this row and all related Stream Table rows should be automatically removed, and the intercept function expire.')
h3cLIMediationTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("udp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMediationTransport.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationTransport.setDescription('The protocol used in transferring intercepted data to the Mediation Device.')
h3cLIMediationNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 9), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMediationNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationNotificationEnable.setDescription('This variable controls the generation of any notifications or informs by the MIB agent for this table entry.')
h3cLIMediationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLIMediationRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cLIMediationRowStatus.setDescription('Operation status of this table entry.')
h3cLIStreamTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3), )
if mibBuilder.loadTexts: h3cLIStreamTable.setStatus('current')
if mibBuilder.loadTexts: h3cLIStreamTable.setDescription("This table lists the traffic stream's type to be intercepted. The specified filter is defined in h3cLIIPStreamTable, h3cLIMACStreamTable or h3cLIUserStreamTable, according to h3cLIStreamtype. Also it contains counters for packets to be intercepted and dropped by attached type of filter.")
h3cLIStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-LI-MIB", "h3cLIMediationIndex"), (0, "A3COM-HUAWEI-LI-MIB", "h3cLIStreamIndex"))
if mibBuilder.loadTexts: h3cLIStreamEntry.setStatus('current')
if mibBuilder.loadTexts: h3cLIStreamEntry.setDescription('A single type of data stream to be intercepted.')
h3cLIStreamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cLIStreamIndex.setStatus('current')
if mibBuilder.loadTexts: h3cLIStreamIndex.setDescription('The index of the stream entry.')
h3cLIStreamtype = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ip", 1), ("mac", 2), ("userConnection", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIStreamtype.setStatus('current')
if mibBuilder.loadTexts: h3cLIStreamtype.setDescription('Identifies the type of stream, and according to it uses filter table. It can not be changed after a filter table is attached to it. The following types of streams are supported: ip: IP filter. The exact definition is a row in h3cLIIPStreamTable. mac: MAC filter. The exact definition is a row in h3cLIMACStreamTable. userConnecton: User connection filter. The exact definition is a row in h3cLIUserStreamTable.')
h3cLIStreamEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIStreamEnable.setStatus('current')
if mibBuilder.loadTexts: h3cLIStreamEnable.setDescription("If 'true', the interception is active. And it is set to 'true' only after an additional filter specification has been attached to this stream.")
h3cLIStreamPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLIStreamPackets.setStatus('current')
if mibBuilder.loadTexts: h3cLIStreamPackets.setDescription('The numbers of packets that have been intercepted.')
h3cLIStreamDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLIStreamDrops.setStatus('current')
if mibBuilder.loadTexts: h3cLIStreamDrops.setDescription('The numbers of packets were dropped in the lawful intercept process.')
h3cLIStreamHPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLIStreamHPackets.setStatus('current')
if mibBuilder.loadTexts: h3cLIStreamHPackets.setDescription('The numbers of packets have been intercepted. This object is a 64-bit version of h3cLIStreamPackets.')
h3cLIStreamHDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLIStreamHDrops.setStatus('current')
if mibBuilder.loadTexts: h3cLIStreamHDrops.setDescription('The numbers of packets were dropped in the lawful intercept process. This object is a 64-bit version of h3cLIStreamDrops.')
h3cLIStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLIStreamRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cLIStreamRowStatus.setDescription('Operation status of this table entry.')
h3cLIIPStream = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2))
h3cLIIPStreamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1))
h3cLIIPStreamTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1), )
if mibBuilder.loadTexts: h3cLIIPStreamTable.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamTable.setDescription('This table lists the IPv4 and IPv6 streams to be intercepted. It is associated with h3cLIMediationTable and h3cLIStreamTable.')
h3cLIIPStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LI-MIB", "h3cLIMediationIndex"), (0, "A3COM-HUAWEI-LI-MIB", "h3cLIStreamIndex"))
if mibBuilder.loadTexts: h3cLIIPStreamEntry.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamEntry.setDescription("A single stream to be intercepted. The first index indicates the Mediation Device. The second index is that of the stream's counter entry in the h3cLIStreamTable. The second index permits multiple classifiers to be used together, such as having an IP address as source or destination.")
h3cLIIPStreamInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamInterface.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamInterface.setDescription('Traffic received or transmitted over this interface will be intercepted. This value must be set when creating a stream entry, either zero, or a valid interface index. If the value is zero, interception accepts any interface. Then at least one additional parameter must be selected, and not be default value.')
h3cLIIPStreamAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamAddrType.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamAddrType.setDescription('The type of address, used in packet selection.')
h3cLIIPStreamDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 3), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamDestAddr.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamDestAddr.setDescription('The Destination address used in packet selection. This address will be consistent with the type specified in h3cLIIPStreamAddrType.')
h3cLIIPStreamDestAddrLength = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 4), InetAddressPrefixLength()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamDestAddrLength.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamDestAddrLength.setDescription('The length of the Destination Prefix. A value of zero means all addresses to match. This prefix length will be consistent with the type specified in h3cLIIPStreamAddrType.')
h3cLIIPStreamSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 5), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamSrcAddr.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamSrcAddr.setDescription('The Source Address used in packet selection. This address will be consistent with the type specified in h3cLIIPStreamAddrType.')
h3cLIIPStreamSrcAddrLength = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 6), InetAddressPrefixLength()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamSrcAddrLength.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamSrcAddrLength.setDescription('The length of the Source Prefix. A value of zero means all addresses to match. This prefix length will be consistent with the type specified in h3cLIIPStreamAddrType.')
h3cLIIPStreamTosByte = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamTosByte.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamTosByte.setDescription('The value of the TOS byte. If h3cLIIPStreamTosByte&(~h3cLIIPStreamTosByteMask)!=0, configuration is rejected.')
h3cLIIPStreamTosByteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamTosByteMask.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamTosByteMask.setDescription('This value is ANDed with the value of the TOS byte in a packet and compared with h3cLIIPStreamTosByte. If the values are equal, the comparison is equal. If both the mask and the TosByte value are zero, the result is to always accept.')
h3cLIIPStreamFlowId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1048575), )).clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamFlowId.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamFlowId.setDescription('The flow identifier in an IPv6 header. -1 indicates that the Flow Id is unused.')
h3cLIIPStreamProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )).clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamProtocol.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamProtocol.setDescription('The IP protocol to match against the IPv4 protocol number or the IPv6 Next- Header number in the packet.')
h3cLIIPStreamDestL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 11), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamDestL4PortMin.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamDestL4PortMin.setDescription('The minimum value that the layer-4 destination port number in the packet must have in order to match. This value must be equal to or less than the value specified for this entry in h3cLIIPStreamDestL4PortMax. If both h3cLIIPStreamDestL4PortMin and h3cLIIPStreamDestL4PortMax are at their default values, the port number is effectively unused. If h3cLIIPStreamDestL4PortMin is equal to h3cLIIPStreamDestL4PortMax, only one port number to be intercepted.')
h3cLIIPStreamDestL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 12), InetPortNumber().clone(65535)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamDestL4PortMax.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamDestL4PortMax.setDescription('The maximum value that the layer-4 destination port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in h3cLIIPStreamDestL4PortMin. If both h3cLIIPStreamDestL4PortMin and h3cLIIPStreamDestL4PortMax are at their default values, the port number is effectively unused. If h3cLIIPStreamDestL4PortMin is equal to h3cLIIPStreamDestL4PortMax, only one port number to be intercepted.')
h3cLIIPStreamSrcL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 13), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamSrcL4PortMin.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamSrcL4PortMin.setDescription('The minimum value that the layer-4 destination port number in the packet must have in order to match. This value must be equal to or less than the value specified for this entry in h3cLIIPStreamSrcL4PortMax. If both h3cLIIPStreamSrcL4PortMin and h3cLIIPStreamSrcL4PortMax are at their default values, the port number is effectively unused. If h3cLIIPStreamSrcL4PortMin is equal to h3cLIIPStreamSrcL4PortMax, only one port number to be intercepted.')
h3cLIIPStreamSrcL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 14), InetPortNumber().clone(65535)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamSrcL4PortMax.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamSrcL4PortMax.setDescription('The maximum value that the layer-4 destination port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in h3cLIIPStreamSrcL4PortMin. If both h3cLIIPStreamSrcL4PortMin and h3cLIIPStreamSrcL4PortMax are at their default values, the port number is effectively unused. If h3cLIIPStreamSrcL4PortMin is equal to h3cLIIPStreamSrcL4PortMax, only one port number to be intercepted.')
h3cLIIPStreamVRF = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 15), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIIPStreamVRF.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamVRF.setDescription('It is the name of a Virtual Routing and Forwarding (VRF) of a VPN.')
h3cLIIPStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLIIPStreamRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cLIIPStreamRowStatus.setDescription('Operation status of this table entry.')
h3cLIMACStream = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3))
h3cLIMACStreamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1))
h3cLIMACStreamTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1), )
if mibBuilder.loadTexts: h3cLIMACStreamTable.setStatus('current')
if mibBuilder.loadTexts: h3cLIMACStreamTable.setDescription('This table lists the IEEE 802 streams to be intercepted. It is associated with h3cLIMediationTable and h3cLIStreamTable.')
h3cLIMACStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LI-MIB", "h3cLIMediationIndex"), (0, "A3COM-HUAWEI-LI-MIB", "h3cLIStreamIndex"))
if mibBuilder.loadTexts: h3cLIMACStreamEntry.setStatus('current')
if mibBuilder.loadTexts: h3cLIMACStreamEntry.setDescription("A single stream to be intercepted. The first index indicates the Mediation Device. The second index is that of the stream's counter entry in the h3cLIStreamTable. The second index permits multiple classifiers to be used together, such as having an MAC address as source or destination.")
h3cLIMACStreamFields = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("interface", 0), ("dstMacAddress", 1), ("srcMacAddress", 2), ("ethernetPid", 3), ("dSap", 4), ("sSap", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMACStreamFields.setStatus('current')
if mibBuilder.loadTexts: h3cLIMACStreamFields.setDescription('This object displays what attributes will be compared to identify traffic. interface: indicates that traffic on the stated interface is to be intercepted dstMacAddress: indicates that traffic destined to a given address should be intercepted srcMacAddress: indicates that traffic sourced from a given address should be intercepted ethernetPid: indicates that traffic with a stated Ethernet Protocol Identifier should be intercepted dSap: indicates that traffic with an certain 802.2 LLC Destination SAP should be intercepted sSap: indicates that traffic with an certain 802.2 LLC Source SAP should be intercepted At least one of the bits has to be set in order to activate an entry. If multiple bits are set, traffic to be intercepted must be satisfied with all set attributes.')
h3cLIMACStreamInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMACStreamInterface.setStatus('current')
if mibBuilder.loadTexts: h3cLIMACStreamInterface.setDescription('Traffic received or transmitted over this interface will be intercepted. This value must be set when creating a stream entry, either zero, or a valid interface index. If the value is zero, interception accepts any interface. Additional parameter must be selected together.')
h3cLIMACStreamDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMACStreamDestAddr.setStatus('current')
if mibBuilder.loadTexts: h3cLIMACStreamDestAddr.setDescription('The Destination address used in packet selection.')
h3cLIMACStreamSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMACStreamSrcAddr.setStatus('current')
if mibBuilder.loadTexts: h3cLIMACStreamSrcAddr.setDescription('The Source Address used in packet selection.')
h3cLIMACStreamEthPid = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMACStreamEthPid.setStatus('current')
if mibBuilder.loadTexts: h3cLIMACStreamEthPid.setDescription('The value of the Ethernet Protocol Identifier in the Ethernet traffic or IEEE 802.2 SNAP traffic.')
h3cLIMACStreamDSap = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMACStreamDSap.setStatus('current')
if mibBuilder.loadTexts: h3cLIMACStreamDSap.setDescription('The value of the IEEE 802.2 Destination SAP.')
h3cLIMACStreamSSap = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIMACStreamSSap.setStatus('current')
if mibBuilder.loadTexts: h3cLIMACStreamSSap.setDescription('The value of the IEEE 802.2 Source SAP.')
h3cLIMACStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLIMACStreamRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cLIMACStreamRowStatus.setDescription('Operation status of this table entry.')
h3cLIUserStream = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4))
h3cLIUserStreamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4, 1))
h3cLIUserStreamTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4, 1, 1), )
if mibBuilder.loadTexts: h3cLIUserStreamTable.setStatus('current')
if mibBuilder.loadTexts: h3cLIUserStreamTable.setDescription('This table lists the user connection streams to be intercepted. It is associated with h3cLIMediationTable and h3cLIStreamTable.')
h3cLIUserStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LI-MIB", "h3cLIMediationIndex"), (0, "A3COM-HUAWEI-LI-MIB", "h3cLIStreamIndex"))
if mibBuilder.loadTexts: h3cLIUserStreamEntry.setStatus('current')
if mibBuilder.loadTexts: h3cLIUserStreamEntry.setDescription("A single stream to be intercepted. The first index indicates the Mediation Device. The second index is that of the stream's counter entry in the h3cLIStreamTable. This permits multiple classifiers to be used together.")
h3cLIUserStreamAcctSessID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLIUserStreamAcctSessID.setStatus('current')
if mibBuilder.loadTexts: h3cLIUserStreamAcctSessID.setDescription('This is the RADIUS attribute 44 acct-session-ID. The string must be set, and the length not be zero.')
h3cLIUserStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLIUserStreamRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cLIUserStreamRowStatus.setDescription('Operation status of this table entry.')
mibBuilder.exportSymbols("A3COM-HUAWEI-LI-MIB", h3cLIStreamEntry=h3cLIStreamEntry, h3cLIMACStreamSSap=h3cLIMACStreamSSap, h3cLIIPStreamVRF=h3cLIIPStreamVRF, h3cLIFailureInformation=h3cLIFailureInformation, h3cLIStreamHDrops=h3cLIStreamHDrops, h3cLIMACStreamEthPid=h3cLIMACStreamEthPid, h3cLICommon=h3cLICommon, h3cLIMediationDestAddr=h3cLIMediationDestAddr, h3cLIMediationDestPort=h3cLIMediationDestPort, h3cLIStreamRowStatus=h3cLIStreamRowStatus, h3cLIIPStreamDestAddrLength=h3cLIIPStreamDestAddrLength, h3cLIMACStreamInterface=h3cLIMACStreamInterface, h3cLIIPStreamDestL4PortMin=h3cLIIPStreamDestL4PortMin, h3cLIUserStreamObjects=h3cLIUserStreamObjects, h3cLIUserStreamRowStatus=h3cLIUserStreamRowStatus, h3cLIIPStreamInterface=h3cLIIPStreamInterface, h3cLIMACStreamTable=h3cLIMACStreamTable, h3cLIMediationSrcInterface=h3cLIMediationSrcInterface, h3cLIBoardInformation=h3cLIBoardInformation, h3cLIMACStreamEntry=h3cLIMACStreamEntry, h3cLIMACStreamRowStatus=h3cLIMACStreamRowStatus, h3cLIMediationTransport=h3cLIMediationTransport, h3cLIStreamIndex=h3cLIStreamIndex, h3cLIStreamPackets=h3cLIStreamPackets, h3cLIIPStreamDestAddr=h3cLIIPStreamDestAddr, h3cLIUserStream=h3cLIUserStream, h3cLIMACStreamFields=h3cLIMACStreamFields, h3cLIMediationRowStatus=h3cLIMediationRowStatus, h3cLIStreamEnable=h3cLIStreamEnable, h3cLITrapBindObjects=h3cLITrapBindObjects, h3cLINotifications=h3cLINotifications, h3cLIMediationEntry=h3cLIMediationEntry, h3cLIMediationDscp=h3cLIMediationDscp, h3cLIStreamTable=h3cLIStreamTable, h3cLIStreamHPackets=h3cLIStreamHPackets, h3cLI=h3cLI, h3cLIIPStreamSrcL4PortMin=h3cLIIPStreamSrcL4PortMin, h3cLIMACStreamDSap=h3cLIMACStreamDSap, h3cLIUserStreamTable=h3cLIUserStreamTable, h3cLIUserStreamEntry=h3cLIUserStreamEntry, h3cLIMediationNotificationEnable=h3cLIMediationNotificationEnable, h3cLIIPStreamFlowId=h3cLIIPStreamFlowId, h3cLIIPStreamObjects=h3cLIIPStreamObjects, h3cLINewIndex=h3cLINewIndex, h3cLIIPStreamDestL4PortMax=h3cLIIPStreamDestL4PortMax, h3cLIMediationTable=h3cLIMediationTable, h3cLIMediationIndex=h3cLIMediationIndex, h3cLIIPStreamTosByteMask=h3cLIIPStreamTosByteMask, h3cLIObjects=h3cLIObjects, h3cLIStreamDrops=h3cLIStreamDrops, h3cLIMACStream=h3cLIMACStream, h3cLIIPStreamEntry=h3cLIIPStreamEntry, h3cLIIPStreamProtocol=h3cLIIPStreamProtocol, h3cLIMACStreamObjects=h3cLIMACStreamObjects, h3cLIMACStreamDestAddr=h3cLIMACStreamDestAddr, h3cLIMACStreamSrcAddr=h3cLIMACStreamSrcAddr, PYSNMP_MODULE_ID=h3cLI, h3cLIIPStreamAddrType=h3cLIIPStreamAddrType, h3cLIIPStreamSrcAddr=h3cLIIPStreamSrcAddr, h3cLINotificationsPrefix=h3cLINotificationsPrefix, h3cLIIPStreamSrcAddrLength=h3cLIIPStreamSrcAddrLength, h3cLIIPStream=h3cLIIPStream, h3cLIIPStreamTable=h3cLIIPStreamTable, h3cLIIPStreamSrcL4PortMax=h3cLIIPStreamSrcL4PortMax, h3cLIMediationDestAddrType=h3cLIMediationDestAddrType, h3cLIActive=h3cLIActive, h3cLITimeOut=h3cLITimeOut, h3cLIIPStreamTosByte=h3cLIIPStreamTosByte, h3cLIMediationTimeOut=h3cLIMediationTimeOut, h3cLIStreamtype=h3cLIStreamtype, h3cLIIPStreamRowStatus=h3cLIIPStreamRowStatus, h3cLIUserStreamAcctSessID=h3cLIUserStreamAcctSessID)
