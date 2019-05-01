#
# PySNMP MIB module ETS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ETS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:06:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Gauge32, MibIdentifier, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, NotificationType, iso, ModuleIdentity, IpAddress, TimeTicks, ObjectIdentity, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "MibIdentifier", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "NotificationType", "iso", "ModuleIdentity", "IpAddress", "TimeTicks", "ObjectIdentity", "Counter32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiEts = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 17))
if mibBuilder.loadTexts: aiEts.setLastUpdated('9703131900Z')
if mibBuilder.loadTexts: aiEts.setOrganization('Applied Innovation Inc.')
if mibBuilder.loadTexts: aiEts.setContactInfo(' Postal: Applied Innovation Inc. 5800 Innovation Drive Dublin, Ohio 43017-3271 Tel: 614-798-2000 Fax: 614-798-1770 E-Mail: snmp@aiinet.com')
if mibBuilder.loadTexts: aiEts.setDescription('This MIB provides configuration and status information for a 196IETS project.')
aiEtsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 17, 1))
aiCardType = MibScalar((1, 3, 6, 1, 4, 1, 539, 17, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("headEndCard", 1), ("remoteEndCard", 2))).clone('remoteEndCard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiCardType.setStatus('current')
if mibBuilder.loadTexts: aiCardType.setDescription('indicates whether this is a head end AI196IETS card, or a remote end AI196IETS card.')
aiPollRetryLimit = MibScalar((1, 3, 6, 1, 4, 1, 539, 17, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiPollRetryLimit.setStatus('current')
if mibBuilder.loadTexts: aiPollRetryLimit.setDescription("the number of retries attempted following an E2A Timeout, before the E2A RTU's communication state is deemed to have failed.")
aiHealthMessageInterval = MibScalar((1, 3, 6, 1, 4, 1, 539, 17, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiHealthMessageInterval.setStatus('current')
if mibBuilder.loadTexts: aiHealthMessageInterval.setDescription('the period of time (in seconds) with-in which the remote end card must send a health message. If the head end card does not receive the message within this period, it closes the connection to the remote end card.')
aiReconnectionTimeOutPeriod = MibScalar((1, 3, 6, 1, 4, 1, 539, 17, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiReconnectionTimeOutPeriod.setStatus('current')
if mibBuilder.loadTexts: aiReconnectionTimeOutPeriod.setDescription('the period of time (in seconds) that the head end card waits before attempting to re-establish a connection with a remote end card.')
aiEtsConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 539, 17, 2), )
if mibBuilder.loadTexts: aiEtsConnectionTable.setStatus('current')
if mibBuilder.loadTexts: aiEtsConnectionTable.setDescription('Entries define the text associated with the head end/remote end connections.')
aiEtsConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 17, 2, 1), ).setIndexNames((0, "ETS-MIB", "aiConnectionIndex"))
if mibBuilder.loadTexts: aiEtsConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: aiEtsConnectionEntry.setDescription('Information about a particular ETS Connection.')
aiConnectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiConnectionIndex.setStatus('current')
if mibBuilder.loadTexts: aiConnectionIndex.setDescription('there can be up to 64 head end/remote end connections.')
aiIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiIpAddress.setStatus('current')
if mibBuilder.loadTexts: aiIpAddress.setDescription('The IP address to which this 196IETS card is connected.')
aiConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noActiveConnection", 1), ("connecting", 2), ("activeConnection", 3), ("suspended", 4))).clone('noActiveConnection')).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiConnectionStatus.setStatus('current')
if mibBuilder.loadTexts: aiConnectionStatus.setDescription('indicates the current status of the head end/remote end connection.')
aiE2aLinkTable = MibTable((1, 3, 6, 1, 4, 1, 539, 17, 3), )
if mibBuilder.loadTexts: aiE2aLinkTable.setStatus('current')
if mibBuilder.loadTexts: aiE2aLinkTable.setDescription('Entries define the text associated with the head end/remote end connections.')
aiE2aLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 17, 3, 1), ).setIndexNames((0, "ETS-MIB", "aiE2aLinkIndex"))
if mibBuilder.loadTexts: aiE2aLinkEntry.setStatus('current')
if mibBuilder.loadTexts: aiE2aLinkEntry.setDescription('Information about a particular E2A Link.')
aiE2aLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiE2aLinkIndex.setStatus('current')
if mibBuilder.loadTexts: aiE2aLinkIndex.setDescription('each 196IETS card can have 16 E2A links. Head end cards connect to NMA, remote end cards connect to E2A RTUs.')
aiProvisioned = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notProvisioned", 1), ("provisioned", 2))).clone('provisioned')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiProvisioned.setStatus('current')
if mibBuilder.loadTexts: aiProvisioned.setDescription('allows each E2A link to be put in and out of service.')
aiLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("linkOnLine", 1), ("linkOffLine", 2))).clone('linkOffLine')).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkStatus.setStatus('current')
if mibBuilder.loadTexts: aiLinkStatus.setDescription('whether there are any communicating E2A RTUs on this link.')
aiBaudRate = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("e2aBaud600", 1), ("e2aBaud1200", 2))).clone('e2aBaud1200')).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiBaudRate.setStatus('current')
if mibBuilder.loadTexts: aiBaudRate.setDescription('baud rate for this E2A link.')
aiProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("protocolE2", 1), ("protocolE2A", 2))).clone('protocolE2A')).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiProtocol.setStatus('current')
if mibBuilder.loadTexts: aiProtocol.setDescription('protocol used on this E2A link.')
aiTxMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTxMessages.setStatus('current')
if mibBuilder.loadTexts: aiTxMessages.setDescription('number of E2A messages transmitted since power up on this E2A link.')
aiTxWords = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTxWords.setStatus('current')
if mibBuilder.loadTexts: aiTxWords.setDescription('number of E2A words transmitted since power up on this E2A link.')
aiTxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTxErrors.setStatus('current')
if mibBuilder.loadTexts: aiTxErrors.setDescription('number of E2A transmit errors since power up on this E2A link.')
aiRxMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiRxMessages.setStatus('current')
if mibBuilder.loadTexts: aiRxMessages.setDescription('number of E2A messages received since power up on this E2A link.')
aiRxWords = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiRxWords.setStatus('current')
if mibBuilder.loadTexts: aiRxWords.setDescription('number of E2A words received since power up on this E2A link.')
aiRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiRxErrors.setStatus('current')
if mibBuilder.loadTexts: aiRxErrors.setDescription('number of E2A receive errors since power up on this E2A link.')
aiRxTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiRxTimeouts.setStatus('current')
if mibBuilder.loadTexts: aiRxTimeouts.setDescription('number of timeouts when expecting receipt of E2A messages since power up on this E2A link.')
aiFlushes = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiFlushes.setStatus('current')
if mibBuilder.loadTexts: aiFlushes.setDescription('number of times the link has been flushed since power up.')
aiE2aRtuTable = MibTable((1, 3, 6, 1, 4, 1, 539, 17, 4), )
if mibBuilder.loadTexts: aiE2aRtuTable.setStatus('current')
if mibBuilder.loadTexts: aiE2aRtuTable.setDescription('Entries define the E2A RTUs connected to the AI196IETS card.')
aiE2aRtuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 17, 4, 1), ).setIndexNames((0, "ETS-MIB", "aiE2aRtuIndex"))
if mibBuilder.loadTexts: aiE2aRtuEntry.setStatus('current')
if mibBuilder.loadTexts: aiE2aRtuEntry.setDescription('Information about a particular E2A RTU on the AI196IETS card.')
aiE2aRtuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiE2aRtuIndex.setStatus('current')
if mibBuilder.loadTexts: aiE2aRtuIndex.setDescription('each of 16 E2A Links can have 256 RTU addresses, 4096 addressable RTUs in total: E2A RTU Indexes 1..256 map to E2A Link 1 E2A RTU Indexes 257..512 map to E2A Link 2 E2A RTU Indexes 513..768 map to E2A Link 3 E2A RTU Indexes 769..1024 map to E2A Link 4 E2A RTU Indexes 1025..1280 map to E2A Link 5 E2A RTU Indexes 1281..1536 map to E2A Link 6 E2A RTU Indexes 1537..1792 map to E2A Link 7 E2A RTU Indexes 1793..2048 map to E2A Link 8 E2A RTU Indexes 2049..2304 map to E2A Link 9 E2A RTU Indexes 2305..2560 map to E2A Link 10 E2A RTU Indexes 2561..2816 map to E2A Link 11 E2A RTU Indexes 2817..3072 map to E2A Link 12 E2A RTU Indexes 3073..3328 map to E2A Link 13 E2A RTU Indexes 3329..3584 map to E2A Link 14 E2A RTU Indexes 3585..3840 map to E2A Link 15 E2A RTU Indexes 3841..4096 map to E2A Link 16')
aiE2aLink = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiE2aLink.setStatus('current')
if mibBuilder.loadTexts: aiE2aLink.setDescription('the E2A Link this E2A RTU resides on.')
aiRtuAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiRtuAddress.setStatus('current')
if mibBuilder.loadTexts: aiRtuAddress.setDescription('the address of the E2A RTU on the e2aLinkIndex.')
aiRtuType = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("e2aSacRtu", 1), ("e2aAprRtu", 2), ("e2aDasRtu", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiRtuType.setStatus('current')
if mibBuilder.loadTexts: aiRtuType.setDescription('The model type of the E2A RTU.')
aiCommunicationState = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rtuOffLine", 1), ("rtuOnLine", 2))).clone('rtuOffLine')).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiCommunicationState.setStatus('current')
if mibBuilder.loadTexts: aiCommunicationState.setDescription('whether communication with the RTU is normal or failed.')
aiInitialPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiInitialPoll.setStatus('current')
if mibBuilder.loadTexts: aiInitialPoll.setDescription('whether or not this RTU is in initial poll mode. An RTU is in initial poll mode when all of its RTU Displays have not yet been polled. This object only has meaning when the AI196IETS card is configured as a remote end card. 0=normal poll mode, 1=initial poll mode.')
aiEtsConnectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiEtsConnectionIndex.setStatus('current')
if mibBuilder.loadTexts: aiEtsConnectionIndex.setDescription('index into the etsConnectionTable of the connection associated with this RTU. A value of 0 indicates that there is no active connection.')
aiE2aRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiE2aRequests.setStatus('current')
if mibBuilder.loadTexts: aiE2aRequests.setDescription('number of E2A requests since power up for this RTU.')
aiE2aResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiE2aResponses.setStatus('current')
if mibBuilder.loadTexts: aiE2aResponses.setDescription('number of E2A responses since power up for this RTU.')
aiPollRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiPollRequests.setStatus('current')
if mibBuilder.loadTexts: aiPollRequests.setDescription('number of E2A poll requests since power up for this RTU.')
aiPollResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiPollResponses.setStatus('current')
if mibBuilder.loadTexts: aiPollResponses.setDescription('number of E2A poll responses since power up for this RTU.')
aiLatchingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLatchingRequests.setStatus('current')
if mibBuilder.loadTexts: aiLatchingRequests.setDescription('number of E2A latching control requests since power up for this RTU.')
aiLatchingResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLatchingResponses.setStatus('current')
if mibBuilder.loadTexts: aiLatchingResponses.setDescription('number of E2A latching control responses since power up for this RTU.')
aiMomentaryRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiMomentaryRequests.setStatus('current')
if mibBuilder.loadTexts: aiMomentaryRequests.setDescription('number of E2A momentary control requests since power up for this RTU.')
aiMomentaryResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiMomentaryResponses.setStatus('current')
if mibBuilder.loadTexts: aiMomentaryResponses.setDescription('number of E2A momentary control responses since power up for this RTU.')
aiTestRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTestRequests.setStatus('current')
if mibBuilder.loadTexts: aiTestRequests.setDescription('number of E2A test requests since power up on this RTU.')
aiTestResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTestResponses.setStatus('current')
if mibBuilder.loadTexts: aiTestResponses.setDescription('number of E2A test responses since power up on this RTU.')
aiUnknownRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiUnknownRequests.setStatus('current')
if mibBuilder.loadTexts: aiUnknownRequests.setDescription('number of unknown E2A requests since power up on this RTU.')
aiUnknownResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiUnknownResponses.setStatus('current')
if mibBuilder.loadTexts: aiUnknownResponses.setDescription('number of unknown E2A responses since power up on this RTU.')
mibBuilder.exportSymbols("ETS-MIB", aiCommunicationState=aiCommunicationState, aiProtocol=aiProtocol, aiCardType=aiCardType, aiLatchingRequests=aiLatchingRequests, aiRtuType=aiRtuType, aiEtsConnectionTable=aiEtsConnectionTable, aiPollRequests=aiPollRequests, aiPollResponses=aiPollResponses, aiInitialPoll=aiInitialPoll, aiTxWords=aiTxWords, aiLinkStatus=aiLinkStatus, aiFlushes=aiFlushes, aiRxWords=aiRxWords, aii=aii, aiE2aLinkEntry=aiE2aLinkEntry, aiE2aLinkIndex=aiE2aLinkIndex, aiEts=aiEts, aiE2aRtuTable=aiE2aRtuTable, aiProvisioned=aiProvisioned, PYSNMP_MODULE_ID=aiEts, aiHealthMessageInterval=aiHealthMessageInterval, aiRxErrors=aiRxErrors, aiEtsConnectionIndex=aiEtsConnectionIndex, aiLatchingResponses=aiLatchingResponses, aiPollRetryLimit=aiPollRetryLimit, aiUnknownResponses=aiUnknownResponses, aiUnknownRequests=aiUnknownRequests, aiTxErrors=aiTxErrors, aiE2aLink=aiE2aLink, aiE2aRtuIndex=aiE2aRtuIndex, aiMomentaryRequests=aiMomentaryRequests, aiConnectionStatus=aiConnectionStatus, aiRtuAddress=aiRtuAddress, aiE2aLinkTable=aiE2aLinkTable, aiE2aResponses=aiE2aResponses, aiE2aRequests=aiE2aRequests, aiReconnectionTimeOutPeriod=aiReconnectionTimeOutPeriod, aiIpAddress=aiIpAddress, aiRxTimeouts=aiRxTimeouts, aiTestRequests=aiTestRequests, aiTestResponses=aiTestResponses, aiMomentaryResponses=aiMomentaryResponses, aiRxMessages=aiRxMessages, aiEtsConnectionEntry=aiEtsConnectionEntry, aiConnectionIndex=aiConnectionIndex, aiE2aRtuEntry=aiE2aRtuEntry, aiTxMessages=aiTxMessages, aiEtsSystem=aiEtsSystem, aiBaudRate=aiBaudRate)
