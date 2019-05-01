#
# PySNMP MIB module AcPerfMediaGateway (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AcPerfMediaGateway
# Produced by pysmi-0.3.4 at Wed May  1 11:33:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Counter32, ObjectIdentity, IpAddress, MibIdentifier, ModuleIdentity, Gauge32, Unsigned32, iso, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Counter32", "ObjectIdentity", "IpAddress", "MibIdentifier", "ModuleIdentity", "Gauge32", "Unsigned32", "iso", "enterprises", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
audioCodes = MibIdentifier((1, 3, 6, 1, 4, 1, 5003))
acRegistrations = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 7))
acGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 8))
acProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9))
acPerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10))
acPerfMediaGateway = ModuleIdentity((1, 3, 6, 1, 4, 1, 5003, 10, 1))
acPerfMediaGateway.setRevisions(('2003-11-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acPerfMediaGateway.setRevisionsDescriptions(('Version 4.4. November 20, 2003. Made these changes: o Initial revision',))
if mibBuilder.loadTexts: acPerfMediaGateway.setLastUpdated('200407121502Z')
if mibBuilder.loadTexts: acPerfMediaGateway.setOrganization('AudioCodes Ltd')
if mibBuilder.loadTexts: acPerfMediaGateway.setContactInfo('Postal: Support AudioCodes LTD 1 Hayarden Street Airport City Lod, ISRAEL 70151 Tel: 972-3-9764000 Fax: 972-3-9764040 Email: support@audiocodes.com Web: www.audiocodes.com')
if mibBuilder.loadTexts: acPerfMediaGateway.setDescription('This MIB defines the enterprise-specific objects needed to support performance management of the AudioCodes product. Performance measurements are grouped into the following MIB trees: acPerfCp - performance measurements related to the control protocol acPerfRtp - performance measurements related to RTP streams acPerfSystem - performance measurements related to network element as a whole')
acPerfCp = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 1, 1))
acPerfCpNumDupsForCompletedTransactions = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfCpNumDupsForCompletedTransactions.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfCpNumDupsForCompletedTransactions.setDescription('The number of times a duplicate transaction request was received after the initial transaction had already been completed. In this case, the gateway resends the response for this transaction. Products: All Capabilities: All')
acPerfCpNumDupsForOutstandingTransactions = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfCpNumDupsForOutstandingTransactions.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfCpNumDupsForOutstandingTransactions.setDescription('The number of times a duplicate transaction request was received while the initial transaction was outstanding, that is, still in progress. In this case, the gateway ignores the duplicate request. Products: All Capabilities: All')
acPerfCpMessageSendSuccesses = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfCpMessageSendSuccesses.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfCpMessageSendSuccesses.setDescription("Number of times there was a success in sending a call control (H.248) message. Call control messages are sent using the system's socket library. This counter tracks successes in using the local socket services. It does not track successes in end-to-end message transfer between the gateway and the call agent. Products: All Capabilities: All")
acPerfCpMessageSendErrors = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfCpMessageSendErrors.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfCpMessageSendErrors.setDescription("Number of times there was a failure in sending a call control (H.248) message. The message is sent via a datagram using the system's socket library. Normally a failure on a socket send operation would be attributed to an internal system problem. Products: All Capabilities: All")
acPerfCpMessageReceiveSuccesses = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfCpMessageReceiveSuccesses.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfCpMessageReceiveSuccesses.setDescription("Number of times there was a success in receiving a call control (H.248) message. Call control messages are received using the system's socket library. This counter tracks successes in using the local socket services. It does not track successes in end-to-end message transfer between the gateway and the call agent. Products: All Capabilities: All")
acPerfCpMessageReceiveErrors = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfCpMessageReceiveErrors.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfCpMessageReceiveErrors.setDescription("Number of times there was a failure in receiving a call control ( H.248) message. Call control messages are received using the system's socket library. A failure on the socket receive operation can be attributed to an internal system problem or with the call agent sending a message larger than what is supported by the gateway. Products: All Capabilities: All")
acPerfCpProtocolSyntaxErrors = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfCpProtocolSyntaxErrors.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfCpProtocolSyntaxErrors.setDescription('Number of syntax errors detected in incoming call control (H.248) messages. Products: All Capabilities: All')
acPerfCpMessageRetransmissions = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfCpMessageRetransmissions.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfCpMessageRetransmissions.setDescription('Each time the call engine times out waiting for an acknowledgement it retransmits the control protocol message, unless the number of max retransmissions is exceeded. This counter is incremented each time a message is retransmitted due to a timeout. Products: All Capabilities: All')
acPerfCpMessageMaxRetransmissionsExceeded = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfCpMessageMaxRetransmissionsExceeded.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfCpMessageMaxRetransmissionsExceeded.setDescription('Number of times the call control message maximum retransmission count was exceeded. The gateway attempted several times to send a message to the call agent, but each time, an ack was not received. A failure of this type results in a failed call and is usually an indication that subsequent calls will fail. This problem is typically a result of the call agent being down or a result of a network problem. Products: All Capabilities: All')
acPerfCpMessagesFromUntrustedSources = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfCpMessagesFromUntrustedSources.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfCpMessagesFromUntrustedSources.setDescription('Number of messages received from untrusted sources, that is from network nodes other than the node on which the call agent is running. Products: All Capabilities: All')
acPerfRtp = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2))
acPerfRtpSenderPackets = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpSenderPackets.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpSenderPackets.setDescription('Total number of RTP packets sent by the system for this card. Products: All IP-based products Capabilities: IVR, BCT, Conferencing, Test Trunks')
acPerfRtpSenderOctets = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpSenderOctets.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpSenderOctets.setDescription('Total number of non-header RTP octets sent by this card. Products: All IP-based products Capabilities: IVR, BCT, Conferencing, Test Trunks')
acPerfRtpReceiverPackets = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpReceiverPackets.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpReceiverPackets.setDescription('Total number of RTP packets received by the system for this card. Products: All IP-based products Capabilities: IVR, BCT, Conferencing, Test Trunks')
acPerfRtpReceiverOctets = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpReceiverOctets.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpReceiverOctets.setDescription('Total number of non-header RTP octets received by this card. Products: All IP-based products Capabilities: IVR, BCT, Conferencing, Test Trunks')
acPerfRtpRcvrLostPackets = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpRcvrLostPackets.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpRcvrLostPackets.setDescription('Total number of RTP packets lost as observed by this card. Products: All IP-based products Capabilities: IVR, BCT, Conferencing, Test Trunks')
acPerfRtpFailedDueToLackOfResources = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpFailedDueToLackOfResources.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpFailedDueToLackOfResources.setDescription('The number of times a rtp request was rejected due to lack of resources since the last application restart. Products: IPmedia 2000')
acPerfRtpSimplexInSessionsTotal = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpSimplexInSessionsTotal.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpSimplexInSessionsTotal.setDescription('Total number of simplex input RTP sessions. A simplex (one-way) session would be used to play an announcement. Products: All IP-based products Capabilities: IVR, BCT, Conferencing, Test Trunks')
acPerfRtpSimplexInSessionsCurrent = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpSimplexInSessionsCurrent.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpSimplexInSessionsCurrent.setDescription('Current number of simplex input RTP sessions. Products: All IP-based products Capabilities: IVR, BCT, Conferencing, Test Trunks')
acPerfRtpSimplexOutSessionsTotal = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpSimplexOutSessionsTotal.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpSimplexOutSessionsTotal.setDescription('Total number of simplex output RTP sessions. Products: All IP-based products Capabilities: IVR, BCT, Conferencing, Test Trunks')
acPerfRtpSimplexOutSessionsCurrent = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpSimplexOutSessionsCurrent.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpSimplexOutSessionsCurrent.setDescription('Current number of simplex output RTP sessions. Products: All IP-based products Capabilities: IVR, BCT, Conferencing, Test Trunks')
acPerfRtpDuplexSessionsTotal = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpDuplexSessionsTotal.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpDuplexSessionsTotal.setDescription('Total number of duplex RTP sessions. A duplex (two-way) session would be used for conferencing. Products: All IP-based products Capabilities: IVR, BCT, Conferencing, Test Trunks')
acPerfRtpDuplexSessionsCurrent = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfRtpDuplexSessionsCurrent.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfRtpDuplexSessionsCurrent.setDescription('Current number of duplex RTP sessions. Products: All IP-based products Capabilities: IVR, BCT, Conferencing, Test Trunks')
acPerfSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 1, 3))
acPerfSystemPacketEndpoints = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfSystemPacketEndpoints.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfSystemPacketEndpoints.setDescription("Number of endpoints reserved for all packet network-related functions (conferencing, plays, etc.). This is an attribute that is derived from the type of hardware and the values of certain config parameters. Currently, its value is fixed after init-time. In the future, it's value might be impacted by configuration of online parameters. That is, its value might increase or decrease over time. For example, in a multi-card system, addition of a board would cause it to increase. Products: All Capabilities: All ")
acPerfSystemPacketEndpointsInUse = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 1, 3, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPerfSystemPacketEndpointsInUse.setStatus('deprecated')
if mibBuilder.loadTexts: acPerfSystemPacketEndpointsInUse.setDescription('Number of endpoints that the call engine is currently using for all packet network-related functions (conferencing, plays, etc.). Products: All Capabilities: All')
mibBuilder.exportSymbols("AcPerfMediaGateway", acPerfCpMessageReceiveSuccesses=acPerfCpMessageReceiveSuccesses, acProducts=acProducts, acPerfRtpDuplexSessionsTotal=acPerfRtpDuplexSessionsTotal, acPerfCpMessageSendErrors=acPerfCpMessageSendErrors, acPerformance=acPerformance, acGeneric=acGeneric, acPerfMediaGateway=acPerfMediaGateway, acPerfRtpRcvrLostPackets=acPerfRtpRcvrLostPackets, acPerfRtpSenderPackets=acPerfRtpSenderPackets, acPerfRtpReceiverOctets=acPerfRtpReceiverOctets, acRegistrations=acRegistrations, acPerfCpNumDupsForCompletedTransactions=acPerfCpNumDupsForCompletedTransactions, acPerfCpMessagesFromUntrustedSources=acPerfCpMessagesFromUntrustedSources, acPerfRtpSimplexOutSessionsTotal=acPerfRtpSimplexOutSessionsTotal, acPerfCpProtocolSyntaxErrors=acPerfCpProtocolSyntaxErrors, acPerfRtpReceiverPackets=acPerfRtpReceiverPackets, acPerfCpMessageSendSuccesses=acPerfCpMessageSendSuccesses, acPerfRtpFailedDueToLackOfResources=acPerfRtpFailedDueToLackOfResources, acPerfCpNumDupsForOutstandingTransactions=acPerfCpNumDupsForOutstandingTransactions, acPerfCpMessageReceiveErrors=acPerfCpMessageReceiveErrors, acPerfRtpDuplexSessionsCurrent=acPerfRtpDuplexSessionsCurrent, acPerfRtpSimplexOutSessionsCurrent=acPerfRtpSimplexOutSessionsCurrent, acPerfRtpSimplexInSessionsTotal=acPerfRtpSimplexInSessionsTotal, PYSNMP_MODULE_ID=acPerfMediaGateway, acPerfCpMessageRetransmissions=acPerfCpMessageRetransmissions, acPerfCpMessageMaxRetransmissionsExceeded=acPerfCpMessageMaxRetransmissionsExceeded, acPerfCp=acPerfCp, acPerfSystem=acPerfSystem, acPerfRtpSenderOctets=acPerfRtpSenderOctets, acPerfRtpSimplexInSessionsCurrent=acPerfRtpSimplexInSessionsCurrent, acPerfRtp=acPerfRtp, acPerfSystemPacketEndpointsInUse=acPerfSystemPacketEndpointsInUse, audioCodes=audioCodes, acPerfSystemPacketEndpoints=acPerfSystemPacketEndpoints)
