#
# PySNMP MIB module MATIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MATIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, NotificationType, ModuleIdentity, TimeTicks, MibIdentifier, Counter32, enterprises, Counter64, iso, Unsigned32, Gauge32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "NotificationType", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Counter32", "enterprises", "Counter64", "iso", "Unsigned32", "Gauge32", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ngcan = MibIdentifier((1, 3, 6, 1, 4, 1, 1978))
tiger = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2))
matipMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7))
matipUser = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2))
matipSession = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3))
matipTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7, 4))
matipUserTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 1))
matipSessionTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 2))
matipNumUsers = MibScalar((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipNumUsers.setStatus('mandatory')
if mibBuilder.loadTexts: matipNumUsers.setDescription('Number of users in the table.')
matipUserTable = MibTable((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2), )
if mibBuilder.loadTexts: matipUserTable.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserTable.setDescription('A list of line table entries. The number of entries is given by the value of matipNumUsers.')
matipUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1), ).setIndexNames((0, "MATIP-MIB", "matipUserIndex"))
if mibBuilder.loadTexts: matipUserEntry.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserEntry.setDescription('An entry containing information applicable to a particular MATIP user.')
matipUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserIndex.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserIndex.setDescription('The user identifier.')
matipUserHLD = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserHLD.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserHLD.setDescription('The HLD associated with this device.')
matipUserA1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserA1.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserA1.setDescription('The A1 associated with this device.')
matipUserA2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserA2.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserA2.setDescription('The A2 associated with this device.')
matipUserSessionRef = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserSessionRef.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserSessionRef.setDescription('The MATIP session identifier (i.e. the interface index of the associated MATIP session). At configuration time, if the value is zero, then session has not been pre-allocated; otherwise, this value signifies the configured session to use.')
matipUserCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("paddedbaudot", 1), ("ipars", 2), ("ascii", 3), ("ebcdic", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserCoding.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserCoding.setDescription('Defines the coding or data that is associated with this entry: paddedbaudot: 5 bits ipars: 6 bits ascii: 7 bits ebcdic: 8 bits')
matipUserPresentationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("p1024b", 1), ("p1024c", 2), ("sna3270", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserPresentationMode.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserPresentationMode.setDescription('The type of presentation: p1024b p1024c sna3270 (not currently supported)')
matipUserQueueThresholdHi = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserQueueThresholdHi.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserQueueThresholdHi.setDescription("Count of messages queued to the MATIP user before flow control is initiated by 'pushing back' on the MATIP session stream.")
matipUserQueueThresholdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserQueueThresholdLow.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserQueueThresholdLow.setDescription('Count of messages queued to the MATIP user before re-enabling on the MATIP session stream.')
matipUserStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserStateTime.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserStateTime.setDescription('The amount of time (in hundredths of a second) since this user entered the current state.')
matipUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("closed", 1), ("activated", 2), ("bound", 3), ("connected", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserStatus.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserStatus.setDescription('Connect State of the MATIP User')
matipUserMsgsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserMsgsIn.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserMsgsIn.setDescription('The total number of messages from the Type A device.')
matipUserMsgsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserMsgsOut.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserMsgsOut.setDescription('The total number of messages sent to the Type A device.')
matipUserCharIn = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserCharIn.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserCharIn.setDescription('The total number of characters from the Type A device.')
matipUserCharOut = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserCharOut.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserCharOut.setDescription('The total number of characters sent to the Type A device.')
matipUserDisconnects = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserDisconnects.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserDisconnects.setDescription('The total number of MATIP User disconnects.')
matipUserTrapReason = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipUserTrapReason.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserTrapReason.setDescription("The reason that the matipUserStateChange trap was generated: up - when the MATIP User enters 'connected' state. down - when the MATIP User enters 'disconnected' state.")
matipUserStateChangeTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("partial", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipUserStateChangeTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: matipUserStateChangeTrapEnable.setDescription("Indicates whether matipUserStateChange traps should be generated for this interface. disabled - do not generate a trap enabled - generate trap when a user enters either the connected or disconnected state. partial - same as 'enabled' except only for those MATIP sessions initiated by this end.")
matipUserStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 1) + (0,1)).setObjects(("MATIP-MIB", "matipUserIndex"), ("MATIP-MIB", "matipUserTrapReason"))
if mibBuilder.loadTexts: matipUserStateChange.setDescription('This trap signifies that one of the users has changed state to/from connected/disconnected as given by matipUserTrapReason.')
matipSessionTable = MibTable((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3), )
if mibBuilder.loadTexts: matipSessionTable.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionTable.setDescription('A list of MATIP sessions.')
matipSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1), ).setIndexNames((0, "MATIP-MIB", "matipSessionIndex"))
if mibBuilder.loadTexts: matipSessionEntry.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionEntry.setDescription('An entry containing information applicable to a particular MATIP session.')
matipSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionIndex.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionIndex.setDescription('The identifier that can be used to locate this session.')
matipSessionClientServer = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("client", 1), ("server", 2), ("both", 3))).clone('client')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionClientServer.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionClientServer.setDescription("Flag defining the Client/Server nature of the product. 'both' is not supported by TIGER because 'client' serves as both client and server.")
matipSessionMuxMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("hlda1a2", 1), ("a1a2", 2), ("single", 3))).clone('hlda1a2')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionMuxMode.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionMuxMode.setDescription('Multiplexor Mode for this session defined as follows: HLD/A1/A2: 4 Byte ASCU definition A1/A2: 2 Byte ASCU definition Single: No multiplexing.')
matipSessionPresentationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("p1024b", 1), ("p1024c", 2), ("sna3270", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionPresentationMode.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionPresentationMode.setDescription('The type of presentation: p1024b p1024c sna3270 (not currently supported)')
matipSessionCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("paddedbaudot", 1), ("ipars", 2), ("ascii", 3), ("ebcdic", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionCoding.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionCoding.setDescription('Defines the coding or data that is associated with this entry: paddedbaudot: 5 bits, ipars: 6 bits, ascii: 7 bits, ebcdic: 8 bits')
matipSessionRestartTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionRestartTimer.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionRestartTimer.setDescription("The number of seconds that will be waited before the MATIP session will be restarted. A value of zero indicates that timing will not occur. The session restart timer is only used when matipSessionClientServer is set to 'client' and matipSessionDialOnDemand is 'disabled'.")
matipSessionDialOnDemand = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionDialOnDemand.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionDialOnDemand.setDescription('When dial on demand is enabled, the TCP session will only be started upon received data from the MATIP user.')
matipSessionActivityTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionActivityTimer.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionActivityTimer.setDescription('The number of seconds of inactivity before the TCP session will be disconnected.')
matipSessionQueueThresholdHi = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionQueueThresholdHi.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionQueueThresholdHi.setDescription('The queueing limit for traffic being sent to the AUTIF module. When this is reached, the software will push back against the MATIP users.')
matipSessionQueueThresholdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionQueueThresholdLow.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionQueueThresholdLow.setDescription('The level at which the user queues will be re-enabled.')
matipSessionConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionConnectTime.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionConnectTime.setDescription("The amount of time (in hundredths of a second) since this transport connection last entered the 'connected' state. A value of zero means this transport connection has never been established.")
matipSessionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sessionDown", 1), ("sessionActivated", 2), ("sessionConnected", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionStatus.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionStatus.setDescription("The state of this transport connection: 'sessionDown' - when this MATIP session is created by the configuration, or when the TCP connection fails. 'sessionActivated' - when the MATIP state machine has sent an SO command and is waiting for an OC response. 'sessionConnected' - when the MATIP session layer can begin Data Transfer.")
matipSessionDisconnects = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionDisconnects.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionDisconnects.setDescription('The Total number of MATIP session Disconnects.')
matipSessionSOSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionSOSent.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionSOSent.setDescription('The count of SO Commands sent.')
matipSessionSOReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionSOReceived.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionSOReceived.setDescription('The count of SO Commands received.')
matipSessionOCSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionOCSent.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionOCSent.setDescription('The count of OC Commands sent.')
matipSessionOCReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionOCReceived.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionOCReceived.setDescription('The count of OC Commands received.')
matipSessionSCSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionSCSent.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionSCSent.setDescription('The count of SC Commands sent.')
matipSessionSCReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionSCReceived.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionSCReceived.setDescription('The count of SC Commands received.')
matipSessionDataSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionDataSent.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionDataSent.setDescription('The count of data packets sent.')
matipSessionDataReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionDataReceived.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionDataReceived.setDescription('The count of data packets received.')
matipSessionStateChangeTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("partial", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: matipSessionStateChangeTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionStateChangeTrapEnable.setDescription("Indicates whether matipSessionStateChange traps should be generated for this interface. disabled - do not generate a trap enabled - generate trap when a session enters either the connected or disconnected state. or when any 'partner reject' occurs. partial - same as 'enabled' except only when the session is closed with busy.")
matipSessionTrapReason = MibTableColumn((1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: matipSessionTrapReason.setStatus('mandatory')
if mibBuilder.loadTexts: matipSessionTrapReason.setDescription("The reason that the matipSessionStateChange trap was generated: up - when the session enters 'connected' state. down - when the session enters 'disconnected' state.")
matipSessionStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 2) + (0,1)).setObjects(("MATIP-MIB", "matipSessionIndex"), ("MATIP-MIB", "matipSessionTrapReason"))
if mibBuilder.loadTexts: matipSessionStateChange.setDescription('This trap signifies that one of the sessions has changed state to/from connected/disconnected as given by matipSessionTrapReason.')
mibBuilder.exportSymbols("MATIP-MIB", matipSessionRestartTimer=matipSessionRestartTimer, matipSessionOCSent=matipSessionOCSent, matipSessionPresentationMode=matipSessionPresentationMode, matipSessionDialOnDemand=matipSessionDialOnDemand, matipUserMsgsIn=matipUserMsgsIn, matipSessionTrapReason=matipSessionTrapReason, matipMIB=matipMIB, matipUserHLD=matipUserHLD, tiger=tiger, matipSessionSCSent=matipSessionSCSent, matipSessionMuxMode=matipSessionMuxMode, matipSessionConnectTime=matipSessionConnectTime, matipSessionEntry=matipSessionEntry, matipUserQueueThresholdLow=matipUserQueueThresholdLow, matipUserStatus=matipUserStatus, matipUserCharIn=matipUserCharIn, matipUserStateChangeTrapEnable=matipUserStateChangeTrapEnable, matipSessionTable=matipSessionTable, matipSessionSCReceived=matipSessionSCReceived, matipUserStateTime=matipUserStateTime, matipSession=matipSession, ngcan=ngcan, matipUserA1=matipUserA1, matipUserCharOut=matipUserCharOut, matipSessionDisconnects=matipSessionDisconnects, matipUserCoding=matipUserCoding, matipSessionIndex=matipSessionIndex, matipSessionActivityTimer=matipSessionActivityTimer, matipSessionStateChange=matipSessionStateChange, matipSessionDataReceived=matipSessionDataReceived, matipUserQueueThresholdHi=matipUserQueueThresholdHi, matipUserTraps=matipUserTraps, matipUserA2=matipUserA2, matipUserSessionRef=matipUserSessionRef, matipUserIndex=matipUserIndex, matipSessionStateChangeTrapEnable=matipSessionStateChangeTrapEnable, matipSessionTraps=matipSessionTraps, matipSessionCoding=matipSessionCoding, matipSessionSOSent=matipSessionSOSent, matipSessionSOReceived=matipSessionSOReceived, matipUserStateChange=matipUserStateChange, matipSessionQueueThresholdHi=matipSessionQueueThresholdHi, matipUserMsgsOut=matipUserMsgsOut, matipUserDisconnects=matipUserDisconnects, matipUserTrapReason=matipUserTrapReason, matipUserPresentationMode=matipUserPresentationMode, matipTraps=matipTraps, matipSessionClientServer=matipSessionClientServer, matipSessionQueueThresholdLow=matipSessionQueueThresholdLow, matipUserTable=matipUserTable, matipNumUsers=matipNumUsers, matipSessionOCReceived=matipSessionOCReceived, matipSessionStatus=matipSessionStatus, matipSessionDataSent=matipSessionDataSent, matipUserEntry=matipUserEntry, matipUser=matipUser)
