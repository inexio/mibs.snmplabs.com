#
# PySNMP MIB module H225-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H225-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:21:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mmH323Root, MmCallType, MmAliasTag, MmH225Crv, MmH323EndpointType, MmAliasAddress, MmTAddressTag, MmGlobalIdentifier = mibBuilder.importSymbols("MULTI-MEDIA-MIB-TC", "mmH323Root", "MmCallType", "MmAliasTag", "MmH225Crv", "MmH323EndpointType", "MmAliasAddress", "MmTAddressTag", "MmGlobalIdentifier")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, MibIdentifier, TimeTicks, ObjectIdentity, NotificationType, Counter64, IpAddress, iso, Unsigned32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "MibIdentifier", "TimeTicks", "ObjectIdentity", "NotificationType", "Counter64", "IpAddress", "iso", "Unsigned32", "Integer32", "ModuleIdentity")
DateAndTime, TAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TAddress", "DisplayString", "TextualConvention")
h225CallSignaling = ModuleIdentity((0, 0, 8, 341, 1, 1, 1))
h225CallSignaling.setRevisions(('1998-12-14 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h225CallSignaling.setRevisionsDescriptions(('The initial version of the mib.',))
if mibBuilder.loadTexts: h225CallSignaling.setLastUpdated('9812221200Z')
if mibBuilder.loadTexts: h225CallSignaling.setOrganization(' ITU-T SG 16 ')
if mibBuilder.loadTexts: h225CallSignaling.setContactInfo(' ITU-T SG 16 ')
if mibBuilder.loadTexts: h225CallSignaling.setDescription('The MIB Module supports the functions of a H.225 call signaling .')
callSignalConfig = MibIdentifier((0, 0, 8, 341, 1, 1, 1, 1))
callSignalStats = MibIdentifier((0, 0, 8, 341, 1, 1, 1, 2))
connections = MibIdentifier((0, 0, 8, 341, 1, 1, 1, 3))
callSignalEvents = MibIdentifier((0, 0, 8, 341, 1, 1, 1, 4, 0))
callSignalingMIBConformance = MibIdentifier((0, 0, 8, 341, 1, 1, 1, 5))
callSignalConfigTable = MibTable((0, 0, 8, 341, 1, 1, 1, 1, 1), )
if mibBuilder.loadTexts: callSignalConfigTable.setStatus('current')
if mibBuilder.loadTexts: callSignalConfigTable.setDescription('This table contains configuration information for instances of a call signaling protocol.')
callSignalConfigEntry = MibTableRow((0, 0, 8, 341, 1, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: callSignalConfigEntry.setStatus('current')
if mibBuilder.loadTexts: callSignalConfigEntry.setDescription('It contains objects that describe the configuration.')
callSignalConfigMaxConnections = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalConfigMaxConnections.setStatus('current')
if mibBuilder.loadTexts: callSignalConfigMaxConnections.setDescription('The maximum number of connections the H.225 entity can possibly have.')
callSignalConfigAvailableConnections = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalConfigAvailableConnections.setStatus('current')
if mibBuilder.loadTexts: callSignalConfigAvailableConnections.setDescription(' The number of available connections, out of callSignalConfigMaxConnections.')
callSignalConfigT303 = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callSignalConfigT303.setStatus('current')
if mibBuilder.loadTexts: callSignalConfigT303.setDescription('The amount of time the calling endpoint waits for an ALERTING, CALL PROCEEDING, CONNECT, RELEASE COMPLETE or other message the called endpoint after it has sent a SETUP message. The time value is in seconds. ')
callSignalConfigT301 = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callSignalConfigT301.setStatus('current')
if mibBuilder.loadTexts: callSignalConfigT301.setDescription('The amount of time after which the calling endpoint should stop waiting for the called endpoint to respond. The time value is in seconds. ')
callSignalConfigEnableNotifications = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callSignalConfigEnableNotifications.setStatus('current')
if mibBuilder.loadTexts: callSignalConfigEnableNotifications.setDescription('Indicates whether notifications should be generated from this MIB. The default is disabled.')
callSignalStatsTable = MibTable((0, 0, 8, 341, 1, 1, 1, 2, 1), )
if mibBuilder.loadTexts: callSignalStatsTable.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsTable.setDescription('This table contains statistics information for instances of a call signaling protocol.')
callSignalStatsEntry = MibTableRow((0, 0, 8, 341, 1, 1, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: callSignalStatsEntry.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsEntry.setDescription('It contains objects that describe statistics.')
callSignalStatsCallConnectionsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsCallConnectionsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsCallConnectionsIn.setDescription('The number of successful connections in which this entity has been a callee.')
callSignalStatsCallConnectionsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsCallConnectionsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsCallConnectionsOut.setDescription('The number of successful connections in which this entity has been a caller.')
callSignalStatsAlertingMsgsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsAlertingMsgsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsAlertingMsgsIn.setDescription('The number of alerting messages received by this entity.')
callSignalStatsAlertingMsgsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsAlertingMsgsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsAlertingMsgsOut.setDescription('The number of alerting messages sent by this entity.')
callSignalStatsCallProceedingsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsCallProceedingsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsCallProceedingsIn.setDescription('The number of call proceeding messages received by this entity.')
callSignalStatsCallProceedingsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsCallProceedingsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsCallProceedingsOut.setDescription('The number of call proceeding messages sent by this entity.')
callSignalStatsSetupMsgsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsSetupMsgsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsSetupMsgsIn.setDescription('The number of setup messages received by this entity.')
callSignalStatsSetupMsgsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsSetupMsgsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsSetupMsgsOut.setDescription('The number of setup messages sent by this entity.')
callSignalStatsSetupAckMsgsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsSetupAckMsgsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsSetupAckMsgsIn.setDescription('The number of setupAck messages received by this entity.')
callSignalStatsSetupAckMsgsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsSetupAckMsgsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsSetupAckMsgsOut.setDescription('The number of setupAck messages sent by this entity.')
callSignalStatsProgressMsgsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsProgressMsgsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsProgressMsgsIn.setDescription('The number of progress messages received by this entity.')
callSignalStatsProgressMsgsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsProgressMsgsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsProgressMsgsOut.setDescription('The number of progress messages sent by this entity.')
callSignalStatsReleaseCompleteMsgsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsReleaseCompleteMsgsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsReleaseCompleteMsgsIn.setDescription('The number of release complete messages received by this entity.')
callSignalStatsReleaseCompleteMsgsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsReleaseCompleteMsgsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsReleaseCompleteMsgsOut.setDescription('The number of release complete messages sent by this entity.')
callSignalStatsStatusMsgsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsStatusMsgsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsStatusMsgsIn.setDescription('The number of status messages received by this entity.')
callSignalStatsStatusMsgsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsStatusMsgsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsStatusMsgsOut.setDescription('The number of status messages sent by this entity.')
callSignalStatsStatusInquiryMsgsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsStatusInquiryMsgsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsStatusInquiryMsgsIn.setDescription('The number of status inquiry messages received by this entity.')
callSignalStatsStatusInquiryMsgsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsStatusInquiryMsgsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsStatusInquiryMsgsOut.setDescription('The number of status inquiry messages sent by this entity.')
callSignalStatsFacilityMsgsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsFacilityMsgsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsFacilityMsgsIn.setDescription('The number of connect messages received by this entity.')
callSignalStatsFacilityMsgsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsFacilityMsgsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsFacilityMsgsOut.setDescription('The number of connect messages sent by this entity.')
callSignalStatsInfoMsgsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsInfoMsgsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsInfoMsgsIn.setDescription('The number of info messages received by this entity.')
callSignalStatsInfoMsgsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsInfoMsgsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsInfoMsgsOut.setDescription('The number of info messages sent by this entity.')
callSignalStatsNotifyMsgsIn = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsNotifyMsgsIn.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsNotifyMsgsIn.setDescription('The number of notify messages received by this entity.')
callSignalStatsNotifyMsgsOut = MibScalar((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsNotifyMsgsOut.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsNotifyMsgsOut.setDescription('The number of notify messages sent by this entity.')
callSignalStatsAverageCallDuration = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 2, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callSignalStatsAverageCallDuration.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsAverageCallDuration.setDescription('The average duration of the call in minutes since system boot time. ')
connectionsActiveConnections = MibScalar((0, 0, 8, 341, 1, 1, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsActiveConnections.setStatus('current')
if mibBuilder.loadTexts: connectionsActiveConnections.setDescription('The number of active connections.')
connectionsTable = MibTable((0, 0, 8, 341, 1, 1, 1, 3, 2), )
if mibBuilder.loadTexts: connectionsTable.setStatus('current')
if mibBuilder.loadTexts: connectionsTable.setDescription('This table contains information about entities that are connected to this entity. It is a list of connection entries. The number of entries equals to the number of active connections.')
connectionsTableEntry = MibTableRow((0, 0, 8, 341, 1, 1, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "H225-MIB", "connectionsSrcTransporTAddressTag"), (0, "H225-MIB", "connectionsSrcTransporTAddress"), (0, "H225-MIB", "connectionsCallIdentifier"))
if mibBuilder.loadTexts: connectionsTableEntry.setStatus('current')
if mibBuilder.loadTexts: connectionsTableEntry.setDescription('It contains objects that describe connections that are remotely connected to this callable H.323 entity for a conference.')
connectionsSrcTransporTAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 1), MmTAddressTag())
if mibBuilder.loadTexts: connectionsSrcTransporTAddressTag.setStatus('current')
if mibBuilder.loadTexts: connectionsSrcTransporTAddressTag.setDescription('The transport address tag of the endpoint.')
connectionsSrcTransporTAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 2), TAddress())
if mibBuilder.loadTexts: connectionsSrcTransporTAddress.setStatus('current')
if mibBuilder.loadTexts: connectionsSrcTransporTAddress.setDescription('The transport address of the source endpoint that initiated the connection.')
connectionsCallIdentifier = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 3), MmGlobalIdentifier())
if mibBuilder.loadTexts: connectionsCallIdentifier.setStatus('current')
if mibBuilder.loadTexts: connectionsCallIdentifier.setDescription('The call identifier.')
connectionsRole = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("caller", 1), ("callee", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsRole.setStatus('current')
if mibBuilder.loadTexts: connectionsRole.setDescription('This value reflects the role this entity plays in this connection being either a caller or a callee. ')
connectionsState = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("callInitiated", 1), ("callDelivered", 2), ("callPresent", 3), ("callReceived", 4), ("connectRequest", 5), ("callProceeding", 6), ("active", 7), ("disconnectRequest", 8), ("disconnectIndication", 9), ("releaseRequest", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsState.setStatus('current')
if mibBuilder.loadTexts: connectionsState.setDescription('The state of the H.225 state machine as per Q.931. Outgoing calls: callInitiated - when the user requests call establishment from the network callDelivered - when the calling user has received an indication that remote user alerting has been initiated. Incoming calls: callPresent - when the user has received a call establishment but not yet responded. callReceived - when the user has indicated alerting but not yet answered. connectRequest - when the user has answered the call and is waiting to be awarded the call. Incoming/Outgoing: callProceeding - when the user has received/sent acknowledgement that the network has received all call information necessary to effect call establishment. active - when the user has received/sent an acknoledgement from/to the network that the user has been awarded the call. disconnectRequest - when the user has requested the network to clear the end-to-end connection. disconnectIndication - when the user has received an invitation to disconnect to disconnect because the network has disconnected the end-to-end connection. releaseRequest - when the user has requested the network to release and is waiting for a responce.')
connectionsDestTransporTAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 6), MmTAddressTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsDestTransporTAddressTag.setStatus('current')
if mibBuilder.loadTexts: connectionsDestTransporTAddressTag.setDescription('The transport address tag of the endpoint.')
connectionsDestTransporTAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 7), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsDestTransporTAddress.setStatus('current')
if mibBuilder.loadTexts: connectionsDestTransporTAddress.setDescription('The transport address of the destination endpoint.')
connectionsDestAliasTag = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 8), MmAliasTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsDestAliasTag.setStatus('current')
if mibBuilder.loadTexts: connectionsDestAliasTag.setDescription('The alias tag of the registred endpoint.')
connectionsDestAlias = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 9), MmAliasAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsDestAlias.setStatus('current')
if mibBuilder.loadTexts: connectionsDestAlias.setDescription('The transport port of the destination endpoint. ')
connectionsSrcH245SigTransporTAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 10), MmTAddressTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsSrcH245SigTransporTAddressTag.setStatus('current')
if mibBuilder.loadTexts: connectionsSrcH245SigTransporTAddressTag.setDescription('The transport address tag of the endpoint.')
connectionsSrcH245SigTransporTAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 11), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsSrcH245SigTransporTAddress.setStatus('current')
if mibBuilder.loadTexts: connectionsSrcH245SigTransporTAddress.setDescription('The H245 IP address of the source endpoint. ')
connectionsDestH245SigTransporTAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 12), MmTAddressTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsDestH245SigTransporTAddressTag.setStatus('current')
if mibBuilder.loadTexts: connectionsDestH245SigTransporTAddressTag.setDescription('The transport address tag of the endpoint.')
connectionsDestH245SigTransporTAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 13), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsDestH245SigTransporTAddress.setStatus('current')
if mibBuilder.loadTexts: connectionsDestH245SigTransporTAddress.setDescription('The transport address of the destination endpoint. ')
connectionsConfId = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 14), MmGlobalIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsConfId.setStatus('current')
if mibBuilder.loadTexts: connectionsConfId.setDescription('The conference id for this connection. ')
connectionsCalledPartyNumber = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsCalledPartyNumber.setStatus('current')
if mibBuilder.loadTexts: connectionsCalledPartyNumber.setDescription('The primary e164 address of the destination endpoint. ')
connectionsDestXtraCallingNumber1 = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsDestXtraCallingNumber1.setStatus('current')
if mibBuilder.loadTexts: connectionsDestXtraCallingNumber1.setDescription('The secondary info e164 address of the destination endpoint. ')
connectionsDestXtraCallingNumber2 = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsDestXtraCallingNumber2.setStatus('current')
if mibBuilder.loadTexts: connectionsDestXtraCallingNumber2.setDescription('The third info e164 address of the destination endpoint. ')
connectionsDestXtraCallingNumber3 = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsDestXtraCallingNumber3.setStatus('current')
if mibBuilder.loadTexts: connectionsDestXtraCallingNumber3.setDescription('The fourth info e164 address of the destination endpoint.')
connectionsDestXtraCallingNumber4 = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsDestXtraCallingNumber4.setStatus('current')
if mibBuilder.loadTexts: connectionsDestXtraCallingNumber4.setDescription('The fifth info e164 address of the destination endpoint.')
connectionsDestXtraCallingNumber5 = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsDestXtraCallingNumber5.setStatus('current')
if mibBuilder.loadTexts: connectionsDestXtraCallingNumber5.setDescription('The sixth info e164 address of the destination endpoint. ')
connectionsFastCall = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsFastCall.setStatus('current')
if mibBuilder.loadTexts: connectionsFastCall.setDescription('Indicator of fast call usage for this connection.')
connectionsSecurity = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsSecurity.setStatus('current')
if mibBuilder.loadTexts: connectionsSecurity.setDescription('Indicator of encryption usage for this connection. ')
connectionsH245Tunneling = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notSupported", 1), ("available", 2), ("active", 3), ("closing", 4), ("closed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsH245Tunneling.setStatus('current')
if mibBuilder.loadTexts: connectionsH245Tunneling.setDescription('Indicator of H245 tunneling usage for this connection. ')
connectionsCanOverlapSend = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsCanOverlapSend.setStatus('current')
if mibBuilder.loadTexts: connectionsCanOverlapSend.setDescription('Indicator of canOverLap usage for this connection. ')
connectionsCRV = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 25), MmH225Crv()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsCRV.setStatus('current')
if mibBuilder.loadTexts: connectionsCRV.setDescription('The call reference value.')
connectionsCallType = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 26), MmCallType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsCallType.setStatus('current')
if mibBuilder.loadTexts: connectionsCallType.setDescription('The type of the call for this connection. ')
connectionsRemoteExtensionAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 27), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsRemoteExtensionAddress.setStatus('current')
if mibBuilder.loadTexts: connectionsRemoteExtensionAddress.setDescription('The additional address for GW-GW calls ')
connectionsExtraCRV1 = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 28), MmH225Crv()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsExtraCRV1.setStatus('current')
if mibBuilder.loadTexts: connectionsExtraCRV1.setDescription('The additional call reference value.')
connectionsExtraCRV2 = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 29), MmH225Crv()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsExtraCRV2.setStatus('current')
if mibBuilder.loadTexts: connectionsExtraCRV2.setDescription('The additional call reference value. ')
connectionsConnectionStartTime = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 30), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsConnectionStartTime.setStatus('current')
if mibBuilder.loadTexts: connectionsConnectionStartTime.setDescription('The date and time of the start of this call. ')
connectionsEndpointType = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 31), MmH323EndpointType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsEndpointType.setStatus('current')
if mibBuilder.loadTexts: connectionsEndpointType.setDescription('Terminal type represents the type of H.323 terminal: 50 - terminal without MC 60 - gateway without MC 70 - terminal with MC but without MP 80 - gateway with MC but without MP 120 - gatekeeper with MC but without MP 160 - MCU with MC but without MP 90 - gateway with MC and Data MP 130 - gatekeeper with MC and Data MP 170 - MCU with MC and Data MP 100 - gateway containing MC with Data and audio MP 140 - gatekeeper containing MC with Data and audio MP 180 - MCU containing MC with Data and audio MP 110 - gateway containing MC with Data, Audio and Video MP 150 - gatekeeper containing MC with Data, Audio and Video MP 190 - MCU containing MC with Data, Audio and Video MP 240 - entity with active MC . ')
connectionsReleaseCompleteReason = MibTableColumn((0, 0, 8, 341, 1, 1, 1, 3, 2, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(34, 47, 3, 16, 88, 111, 38, 42, 28, 41, 17, 31))).clone(namedValues=NamedValues(("noBandwidth", 34), ("gatekeeperResourcesUnavailable", 47), ("unreachableDestination", 3), ("destinationReject", 16), ("invalidRevision", 88), ("noPermission", 111), ("unreachableGatekeeper", 38), ("gatewayResources", 42), ("badFormaTAddress", 28), ("adaptiveBusy", 41), ("inConference", 17), ("undefined", 31)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsReleaseCompleteReason.setStatus('current')
if mibBuilder.loadTexts: connectionsReleaseCompleteReason.setDescription('The date and time of the start of this call. ')
callReleaseComplete = NotificationType((0, 0, 8, 341, 1, 1, 1, 4, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("H225-MIB", "connectionsReleaseCompleteReason"))
if mibBuilder.loadTexts: callReleaseComplete.setStatus('current')
if mibBuilder.loadTexts: callReleaseComplete.setDescription('This message will be sent in the case of on generation and reception of releaseComplete for the following reasons: 34 - noBandwidth; no circuit/channel available 47 - gatekeeperResources; resource unavailable 3 - unreachableDestination; no route to destination 16 - destinationReject; destination did not accept this call 88 - invalidRevision; incompatible destination 111- noPermission; Interworking unspecified 38 - unreachableGatekeeper; network out of order 42 - gatewayResources; switching equipment congestion 28 - badFormaTAddress; invalid number format 41 - adaptiveBusy; Temporary Failure 17 - inConference; user busy 31 - undefined. ')
callSignalingMIBGroups = MibIdentifier((0, 0, 8, 341, 1, 1, 1, 5, 1))
callSignalConfigGroup = ObjectGroup((0, 0, 8, 341, 1, 1, 1, 5, 1, 1)).setObjects(("H225-MIB", "callSignalConfigMaxConnections"), ("H225-MIB", "callSignalConfigAvailableConnections"), ("H225-MIB", "callSignalConfigT303"), ("H225-MIB", "callSignalConfigT301"), ("H225-MIB", "callSignalConfigEnableNotifications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    callSignalConfigGroup = callSignalConfigGroup.setStatus('current')
if mibBuilder.loadTexts: callSignalConfigGroup.setDescription('.')
callSignalStatsGroup = ObjectGroup((0, 0, 8, 341, 1, 1, 1, 5, 1, 2)).setObjects(("H225-MIB", "callSignalStatsCallConnectionsIn"), ("H225-MIB", "callSignalStatsCallConnectionsOut"), ("H225-MIB", "callSignalStatsAlertingMsgsIn"), ("H225-MIB", "callSignalStatsAlertingMsgsOut"), ("H225-MIB", "callSignalStatsCallProceedingsIn"), ("H225-MIB", "callSignalStatsCallProceedingsOut"), ("H225-MIB", "callSignalStatsSetupMsgsIn"), ("H225-MIB", "callSignalStatsSetupMsgsOut"), ("H225-MIB", "callSignalStatsSetupAckMsgsIn"), ("H225-MIB", "callSignalStatsSetupAckMsgsOut"), ("H225-MIB", "callSignalStatsProgressMsgsIn"), ("H225-MIB", "callSignalStatsProgressMsgsOut"), ("H225-MIB", "callSignalStatsReleaseCompleteMsgsIn"), ("H225-MIB", "callSignalStatsReleaseCompleteMsgsOut"), ("H225-MIB", "callSignalStatsStatusMsgsIn"), ("H225-MIB", "callSignalStatsStatusMsgsOut"), ("H225-MIB", "callSignalStatsStatusInquiryMsgsIn"), ("H225-MIB", "callSignalStatsStatusInquiryMsgsOut"), ("H225-MIB", "callSignalStatsFacilityMsgsIn"), ("H225-MIB", "callSignalStatsFacilityMsgsOut"), ("H225-MIB", "callSignalStatsInfoMsgsIn"), ("H225-MIB", "callSignalStatsInfoMsgsOut"), ("H225-MIB", "callSignalStatsNotifyMsgsIn"), ("H225-MIB", "callSignalStatsNotifyMsgsOut"), ("H225-MIB", "callSignalStatsAverageCallDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    callSignalStatsGroup = callSignalStatsGroup.setStatus('current')
if mibBuilder.loadTexts: callSignalStatsGroup.setDescription('.')
connectionsGroup = ObjectGroup((0, 0, 8, 341, 1, 1, 1, 5, 1, 3)).setObjects(("H225-MIB", "connectionsActiveConnections"), ("H225-MIB", "connectionsRole"), ("H225-MIB", "connectionsState"), ("H225-MIB", "connectionsDestTransporTAddressTag"), ("H225-MIB", "connectionsDestTransporTAddress"), ("H225-MIB", "connectionsDestAliasTag"), ("H225-MIB", "connectionsDestAlias"), ("H225-MIB", "connectionsSrcH245SigTransporTAddressTag"), ("H225-MIB", "connectionsSrcH245SigTransporTAddress"), ("H225-MIB", "connectionsDestH245SigTransporTAddressTag"), ("H225-MIB", "connectionsDestH245SigTransporTAddress"), ("H225-MIB", "connectionsConfId"), ("H225-MIB", "connectionsCalledPartyNumber"), ("H225-MIB", "connectionsDestXtraCallingNumber1"), ("H225-MIB", "connectionsDestXtraCallingNumber2"), ("H225-MIB", "connectionsDestXtraCallingNumber3"), ("H225-MIB", "connectionsDestXtraCallingNumber4"), ("H225-MIB", "connectionsDestXtraCallingNumber5"), ("H225-MIB", "connectionsFastCall"), ("H225-MIB", "connectionsSecurity"), ("H225-MIB", "connectionsH245Tunneling"), ("H225-MIB", "connectionsCanOverlapSend"), ("H225-MIB", "connectionsCRV"), ("H225-MIB", "connectionsCallType"), ("H225-MIB", "connectionsRemoteExtensionAddress"), ("H225-MIB", "connectionsExtraCRV1"), ("H225-MIB", "connectionsExtraCRV2"), ("H225-MIB", "connectionsConnectionStartTime"), ("H225-MIB", "connectionsReleaseCompleteReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    connectionsGroup = connectionsGroup.setStatus('current')
if mibBuilder.loadTexts: connectionsGroup.setDescription('.')
callSignalEventsGroup = ObjectGroup((0, 0, 8, 341, 1, 1, 1, 5, 1, 4)).setObjects(("H225-MIB", "connectionsReleaseCompleteReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    callSignalEventsGroup = callSignalEventsGroup.setStatus('current')
if mibBuilder.loadTexts: callSignalEventsGroup.setDescription('.')
callSignalingMIBCompliance = ModuleCompliance((0, 0, 8, 341, 1, 1, 1, 5, 2)).setObjects(("H225-MIB", "callSignalConfigGroup"), ("H225-MIB", "callSignalStatsGroup"), ("H225-MIB", "connectionsGroup"), ("H225-MIB", "callSignalEventsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    callSignalingMIBCompliance = callSignalingMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: callSignalingMIBCompliance.setDescription('The set of objects required for compliance.')
mibBuilder.exportSymbols("H225-MIB", callSignalStatsGroup=callSignalStatsGroup, callSignalStatsSetupMsgsIn=callSignalStatsSetupMsgsIn, connectionsState=connectionsState, callSignalConfigT301=callSignalConfigT301, connectionsDestXtraCallingNumber1=connectionsDestXtraCallingNumber1, callSignalStatsSetupAckMsgsIn=callSignalStatsSetupAckMsgsIn, callSignalStatsInfoMsgsIn=callSignalStatsInfoMsgsIn, connectionsDestXtraCallingNumber3=connectionsDestXtraCallingNumber3, connectionsDestXtraCallingNumber4=connectionsDestXtraCallingNumber4, connectionsExtraCRV2=connectionsExtraCRV2, connectionsReleaseCompleteReason=connectionsReleaseCompleteReason, callSignalStatsCallConnectionsIn=callSignalStatsCallConnectionsIn, connectionsDestAliasTag=connectionsDestAliasTag, connectionsSrcTransporTAddress=connectionsSrcTransporTAddress, callSignalConfigGroup=callSignalConfigGroup, connectionsRemoteExtensionAddress=connectionsRemoteExtensionAddress, callSignalStatsAlertingMsgsIn=callSignalStatsAlertingMsgsIn, connectionsCalledPartyNumber=connectionsCalledPartyNumber, connectionsCanOverlapSend=connectionsCanOverlapSend, connectionsCallType=connectionsCallType, callSignalStatsStatusInquiryMsgsIn=callSignalStatsStatusInquiryMsgsIn, connectionsDestH245SigTransporTAddressTag=connectionsDestH245SigTransporTAddressTag, connectionsDestXtraCallingNumber2=connectionsDestXtraCallingNumber2, callSignalStatsEntry=callSignalStatsEntry, callSignalStatsCallProceedingsIn=callSignalStatsCallProceedingsIn, connectionsConfId=connectionsConfId, connectionsSrcTransporTAddressTag=connectionsSrcTransporTAddressTag, connectionsFastCall=connectionsFastCall, callSignalStatsAlertingMsgsOut=callSignalStatsAlertingMsgsOut, connectionsDestH245SigTransporTAddress=connectionsDestH245SigTransporTAddress, callSignalConfigTable=callSignalConfigTable, connectionsGroup=connectionsGroup, callSignalStatsCallConnectionsOut=callSignalStatsCallConnectionsOut, connectionsExtraCRV1=connectionsExtraCRV1, callSignalStatsFacilityMsgsOut=callSignalStatsFacilityMsgsOut, PYSNMP_MODULE_ID=h225CallSignaling, callSignalStatsTable=callSignalStatsTable, callSignalStatsProgressMsgsOut=callSignalStatsProgressMsgsOut, connectionsTableEntry=connectionsTableEntry, connectionsEndpointType=connectionsEndpointType, callSignalStatsReleaseCompleteMsgsIn=callSignalStatsReleaseCompleteMsgsIn, callSignalEvents=callSignalEvents, callSignalConfigT303=callSignalConfigT303, callSignalStatsSetupMsgsOut=callSignalStatsSetupMsgsOut, connectionsDestTransporTAddress=connectionsDestTransporTAddress, callSignalingMIBCompliance=callSignalingMIBCompliance, callSignalConfigEntry=callSignalConfigEntry, callSignalStatsSetupAckMsgsOut=callSignalStatsSetupAckMsgsOut, callSignalStatsStatusInquiryMsgsOut=callSignalStatsStatusInquiryMsgsOut, connectionsCallIdentifier=connectionsCallIdentifier, callSignalConfigAvailableConnections=callSignalConfigAvailableConnections, callSignalEventsGroup=callSignalEventsGroup, callSignalStatsNotifyMsgsOut=callSignalStatsNotifyMsgsOut, callSignalStatsAverageCallDuration=callSignalStatsAverageCallDuration, connectionsH245Tunneling=connectionsH245Tunneling, callSignalStatsStatusMsgsOut=callSignalStatsStatusMsgsOut, callSignalStatsProgressMsgsIn=callSignalStatsProgressMsgsIn, connectionsSrcH245SigTransporTAddressTag=connectionsSrcH245SigTransporTAddressTag, callSignalStatsCallProceedingsOut=callSignalStatsCallProceedingsOut, connections=connections, callSignalConfigMaxConnections=callSignalConfigMaxConnections, callSignalStatsNotifyMsgsIn=callSignalStatsNotifyMsgsIn, callReleaseComplete=callReleaseComplete, connectionsDestAlias=connectionsDestAlias, callSignalingMIBConformance=callSignalingMIBConformance, connectionsSrcH245SigTransporTAddress=connectionsSrcH245SigTransporTAddress, callSignalStatsReleaseCompleteMsgsOut=callSignalStatsReleaseCompleteMsgsOut, callSignalingMIBGroups=callSignalingMIBGroups, callSignalConfig=callSignalConfig, connectionsConnectionStartTime=connectionsConnectionStartTime, callSignalStats=callSignalStats, callSignalStatsStatusMsgsIn=callSignalStatsStatusMsgsIn, connectionsDestTransporTAddressTag=connectionsDestTransporTAddressTag, callSignalConfigEnableNotifications=callSignalConfigEnableNotifications, connectionsSecurity=connectionsSecurity, connectionsCRV=connectionsCRV, connectionsTable=connectionsTable, connectionsDestXtraCallingNumber5=connectionsDestXtraCallingNumber5, connectionsActiveConnections=connectionsActiveConnections, h225CallSignaling=h225CallSignaling, callSignalStatsFacilityMsgsIn=callSignalStatsFacilityMsgsIn, connectionsRole=connectionsRole, callSignalStatsInfoMsgsOut=callSignalStatsInfoMsgsOut)