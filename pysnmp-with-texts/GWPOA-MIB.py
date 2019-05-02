#
# PySNMP MIB module GWPOA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GWPOA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:20:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, Counter64, NotificationType, ModuleIdentity, Integer32, IpAddress, Gauge32, enterprises, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "Counter64", "NotificationType", "ModuleIdentity", "Integer32", "IpAddress", "Gauge32", "enterprises", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
mibDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
gwpoa = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 38))
poa = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 38, 1))
poaTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 38, 2))
poaTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 38, 3))
poaTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1), )
if mibBuilder.loadTexts: poaTable.setStatus('mandatory')
if mibBuilder.loadTexts: poaTable.setDescription('A table of POA objects')
poaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1), ).setIndexNames((0, "GWPOA-MIB", "poaIndex"))
if mibBuilder.loadTexts: poaEntry.setStatus('mandatory')
if mibBuilder.loadTexts: poaEntry.setDescription('An entry in the POA Table')
poaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaIndex.setStatus('mandatory')
if mibBuilder.loadTexts: poaIndex.setDescription('Index into the POA table')
poaPostOfficeName = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaPostOfficeName.setStatus('mandatory')
if mibBuilder.loadTexts: poaPostOfficeName.setDescription('The name of the Post Office this Agent is serving.')
poaTotalMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaTotalMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: poaTotalMsgs.setDescription('The number of total messages processed.')
poaProblemMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaProblemMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: poaProblemMsgs.setDescription('The number of problem messages.')
poaStatuses = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaStatuses.setStatus('mandatory')
if mibBuilder.loadTexts: poaStatuses.setDescription('The number of completed status messages.')
poaDeliveredUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaDeliveredUsers.setStatus('mandatory')
if mibBuilder.loadTexts: poaDeliveredUsers.setDescription('The number of users receiving messages.')
poaExecutedRules = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaExecutedRules.setStatus('mandatory')
if mibBuilder.loadTexts: poaExecutedRules.setDescription('The number of rules executed.')
poaUndeliverableMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaUndeliverableMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: poaUndeliverableMsgs.setDescription('The number of users not delivered to.')
poaPriorityQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaPriorityQueues.setStatus('mandatory')
if mibBuilder.loadTexts: poaPriorityQueues.setDescription('The number of priority messages waiting to be processed.')
poaNormalQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaNormalQueues.setStatus('mandatory')
if mibBuilder.loadTexts: poaNormalQueues.setDescription('The number of normal messages waiting to be processed.')
poaUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaUptime.setStatus('mandatory')
if mibBuilder.loadTexts: poaUptime.setDescription('Uptime of the Post Office Agent.')
poaCurrentLogFile = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCurrentLogFile.setStatus('mandatory')
if mibBuilder.loadTexts: poaCurrentLogFile.setDescription('Current log file.')
poaLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("verbose", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaLogLevel.setStatus('mandatory')
if mibBuilder.loadTexts: poaLogLevel.setDescription('Post Office Agent Log Level: Normal, Verbose')
poaFileLogging = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaFileLogging.setStatus('mandatory')
if mibBuilder.loadTexts: poaFileLogging.setDescription('Post Office Agent disk logging: YES or NO')
poaMaxLogFileAge = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaMaxLogFileAge.setStatus('mandatory')
if mibBuilder.loadTexts: poaMaxLogFileAge.setDescription('Maximum age for Post Office Agent log files.')
poaMaxLogDiskSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaMaxLogDiskSpace.setStatus('mandatory')
if mibBuilder.loadTexts: poaMaxLogDiskSpace.setDescription('Maximum disk space for Post Office Agent log files.')
poaCSRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCSRequests.setStatus('mandatory')
if mibBuilder.loadTexts: poaCSRequests.setDescription('The number of Client/Server requests')
poaCSRequestsPending = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCSRequestsPending.setStatus('mandatory')
if mibBuilder.loadTexts: poaCSRequestsPending.setDescription('The number of Client/Server requests pending')
poaCSUserTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCSUserTimeouts.setStatus('mandatory')
if mibBuilder.loadTexts: poaCSUserTimeouts.setDescription('The number of users that timed out')
poaCSFileQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCSFileQueues.setStatus('mandatory')
if mibBuilder.loadTexts: poaCSFileQueues.setDescription('The number of messages in the queues')
poaCSUsersConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCSUsersConnected.setStatus('mandatory')
if mibBuilder.loadTexts: poaCSUsersConnected.setDescription('The number of connected User Session')
poaGUID = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 36))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaGUID.setStatus('mandatory')
if mibBuilder.loadTexts: poaGUID.setDescription('Post Office Agent globally unique identifier.')
poaOS = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaOS.setStatus('mandatory')
if mibBuilder.loadTexts: poaOS.setDescription('Operating System name and version')
poaVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaVersion.setStatus('mandatory')
if mibBuilder.loadTexts: poaVersion.setDescription('Version and date this agent.')
poaAdmThreadStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmThreadStatus.setStatus('mandatory')
if mibBuilder.loadTexts: poaAdmThreadStatus.setDescription('Admin thread status: Running, Suspended, Unknown.')
poaAdmCompletedMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmCompletedMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: poaAdmCompletedMsgs.setDescription('Number of Admin messages processed since startup by this POA.')
poaAdmErrorMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmErrorMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: poaAdmErrorMsgs.setDescription('Number of Admin message errors since startup by this POA.')
poaAdmInQueueMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 28), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmInQueueMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: poaAdmInQueueMsgs.setDescription('Number of Admin messages waiting to be processed.')
poaAdmDBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmDBStatus.setStatus('mandatory')
if mibBuilder.loadTexts: poaAdmDBStatus.setDescription('Post Office database status: Normal, DB Error, Unknown.')
poaAdmDBSortLang = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmDBSortLang.setStatus('mandatory')
if mibBuilder.loadTexts: poaAdmDBSortLang.setDescription('Post Office database sort language.')
poaAdmDBRecoverCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmDBRecoverCnt.setStatus('mandatory')
if mibBuilder.loadTexts: poaAdmDBRecoverCnt.setDescription('Number of DB recoveries performed since startup by this POA.')
poaDN = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 32), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaDN.setStatus('mandatory')
if mibBuilder.loadTexts: poaDN.setDescription('Distinguished Name of POA agent.')
poaAvailDiskSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAvailDiskSpace.setStatus('mandatory')
if mibBuilder.loadTexts: poaAvailDiskSpace.setDescription('Number of MB of disk space available.')
poaHTTPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 34), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaHTTPPort.setStatus('mandatory')
if mibBuilder.loadTexts: poaHTTPPort.setDescription('HTTP used: 0 or port number')
poaAdmDBStatusNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("normal", 0), ("error", 1), ("recovering", 2), ("unknown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaAdmDBStatusNumber.setStatus('mandatory')
if mibBuilder.loadTexts: poaAdmDBStatusNumber.setDescription('Numeric Post Office database status')
poaMTPStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 0), ("closed", 1), ("open", 2), ("sendopen", 3), ("receiveopen", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaMTPStatus.setStatus('mandatory')
if mibBuilder.loadTexts: poaMTPStatus.setDescription('Status of the message transfer protocol')
poaUptimeInSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaUptimeInSeconds.setStatus('mandatory')
if mibBuilder.loadTexts: poaUptimeInSeconds.setDescription('Uptime of the Post Office Agent in seconds')
poaTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 38, 2, 1), Integer32())
if mibBuilder.loadTexts: poaTrapTime.setStatus('mandatory')
if mibBuilder.loadTexts: poaTrapTime.setDescription('The time the trap occurred. Seconds since Jan 1, 1970 (GMT)')
poaStartTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 38, 3) + (0,1)).setObjects(("GWPOA-MIB", "poaTrapTime"), ("GWPOA-MIB", "poaPostOfficeName"), ("GWPOA-MIB", "poaGUID"))
if mibBuilder.loadTexts: poaStartTrap.setDescription('GroupWise Post Office Agent (POA) has started.')
poaShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 38, 3) + (0,2)).setObjects(("GWPOA-MIB", "poaTrapTime"), ("GWPOA-MIB", "poaPostOfficeName"), ("GWPOA-MIB", "poaGUID"))
if mibBuilder.loadTexts: poaShutdownTrap.setDescription('GroupWise Post Office Agent (POA) has shut down.')
mibBuilder.exportSymbols("GWPOA-MIB", poaTable=poaTable, poaTrapInfo=poaTrapInfo, poaDeliveredUsers=poaDeliveredUsers, gwpoa=gwpoa, poaCSRequestsPending=poaCSRequestsPending, poaPostOfficeName=poaPostOfficeName, poaPriorityQueues=poaPriorityQueues, poaProblemMsgs=poaProblemMsgs, poaNormalQueues=poaNormalQueues, novell=novell, poaCSUsersConnected=poaCSUsersConnected, poaGUID=poaGUID, poaAdmCompletedMsgs=poaAdmCompletedMsgs, poaMTPStatus=poaMTPStatus, poaExecutedRules=poaExecutedRules, poaVersion=poaVersion, poaUndeliverableMsgs=poaUndeliverableMsgs, poaAdmDBRecoverCnt=poaAdmDBRecoverCnt, poaEntry=poaEntry, poaFileLogging=poaFileLogging, poaStartTrap=poaStartTrap, poaAdmDBStatusNumber=poaAdmDBStatusNumber, poaCSRequests=poaCSRequests, poaOS=poaOS, poaHTTPPort=poaHTTPPort, poaCSUserTimeouts=poaCSUserTimeouts, poaUptime=poaUptime, poaMaxLogDiskSpace=poaMaxLogDiskSpace, poaLogLevel=poaLogLevel, poaIndex=poaIndex, poaAdmThreadStatus=poaAdmThreadStatus, poaTrapTime=poaTrapTime, poaAdmDBStatus=poaAdmDBStatus, poa=poa, poaTotalMsgs=poaTotalMsgs, poaDN=poaDN, poaUptimeInSeconds=poaUptimeInSeconds, poaShutdownTrap=poaShutdownTrap, poaTraps=poaTraps, poaCurrentLogFile=poaCurrentLogFile, mibDoc=mibDoc, poaAdmDBSortLang=poaAdmDBSortLang, poaMaxLogFileAge=poaMaxLogFileAge, poaStatuses=poaStatuses, poaAvailDiskSpace=poaAvailDiskSpace, poaAdmInQueueMsgs=poaAdmInQueueMsgs, poaCSFileQueues=poaCSFileQueues, poaAdmErrorMsgs=poaAdmErrorMsgs)