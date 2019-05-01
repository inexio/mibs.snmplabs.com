#
# PySNMP MIB module TPLINK-ETHERNETOAMEVENTLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ETHERNETOAMEVENTLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, iso, ModuleIdentity, Bits, TimeTicks, Gauge32, ObjectIdentity, Counter32, IpAddress, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "iso", "ModuleIdentity", "Bits", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter32", "IpAddress", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ethernetOamEventLog, = mibBuilder.importSymbols("TPLINK-ETHERNETOAM-MIB", "ethernetOamEventLog")
ethernetOamEventLogStatTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1), )
if mibBuilder.loadTexts: ethernetOamEventLogStatTable.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatTable.setDescription('A table that contains the Ethernet OAM event log statistics of each port.')
ethernetOamEventLogStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetOamEventLogStatEntry.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatEntry.setDescription('An entry that contains the Ethernet OAM event log statistics of each port.')
ethernetOamEventLogStatPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatPort.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatPort.setDescription('Displays the port number.')
ethernetOamEventLogStatLocalSymbolPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalSymbolPeriod.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalSymbolPeriod.setDescription('Displays the number of error-symbol-period link events occurred on the local link.')
ethernetOamEventLogStatRemoteSymbolPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteSymbolPeriod.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteSymbolPeriod.setDescription('Displays the number of error-symbol-period link events occurred on the remote link.')
ethernetOamEventLogStatLocalFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalFrame.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalFrame.setDescription('Displays the number of error-frame link events occurred on the local link.')
ethernetOamEventLogStatRemoteFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteFrame.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteFrame.setDescription('Displays the number of error-frame link events occurred on the remote link.')
ethernetOamEventLogStatLocalFramePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalFramePeriod.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalFramePeriod.setDescription('Displays the number of error-frame-period link events occurred on the local link.')
ethernetOamEventLogStatRemoteFramePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteFramePeriod.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteFramePeriod.setDescription('Displays the number of error-frame-period link events occurred on the remote link.')
ethernetOamEventLogStatLocalFrameSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalFrameSeconds.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalFrameSeconds.setDescription('Displays the number of error-frame-seconds link events occurred on the local link or remote link.')
ethernetOamEventLogStatRemoteFrameSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteFrameSeconds.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteFrameSeconds.setDescription('Displays the number of error-frame-seconds link events occurred on the local link or remote link.')
ethernetOamEventLogStatLocalDyingGasp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalDyingGasp.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalDyingGasp.setDescription('Displays the number of Dying Gasp link events occurred on the local link.')
ethernetOamEventLogStatRemoteDyingGasp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteDyingGasp.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteDyingGasp.setDescription('Displays the number of Dying Gasp link events occurred on the remote link.')
ethernetOamEventLogStatLocalCriticalEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalCriticalEvent.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalCriticalEvent.setDescription('Displays the number of Critical Event link events occurred on the local link.')
ethernetOamEventLogStatRemoteCriticalEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteCriticalEvent.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteCriticalEvent.setDescription('Displays the number of Critical Event link events occurred on the remote link.')
ethernetOamEventLogTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2), )
if mibBuilder.loadTexts: ethernetOamEventLogTable.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogTable.setDescription('A table that contains the Ethernet OAM event log of each port.')
ethernetOamEventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TPLINK-ETHERNETOAMEVENTLOG-MIB", "ethernetOamEventLogSeq"))
if mibBuilder.loadTexts: ethernetOamEventLogEntry.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogEntry.setDescription('An entry that contains the Ethernet OAM event log of each port.')
ethernetOamEventLogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogPort.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogPort.setDescription('Displays the port number.')
ethernetOamEventLogSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogSeq.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogSeq.setDescription('Displays the sequence number.')
ethernetOamEventLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 16, 32, 48))).clone(namedValues=NamedValues(("symbol-period", 1), ("frame", 2), ("frame-period", 3), ("frame-seconds", 4), ("link-fault", 16), ("dying-gasp", 32), ("critical-event", 48)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogType.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogType.setDescription('Displays the type of the link event.')
ethernetOamEventLogLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("local", 0), ("remote", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogLocation.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogLocation.setDescription('Displays the location when the link event ocurred.')
ethernetOamEventLogTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogTimestamp.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogTimestamp.setDescription('Displays the timestamp when the link event ocurred.')
ethernetOamEventLogValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogValue.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogValue.setDescription('Displays the number of errors in the period.')
ethernetOamEventLogWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogWindow.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogWindow.setDescription('Displays the period of the link event.')
ethernetOamEventLogThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogThreshold.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogThreshold.setDescription('Displays the number of errors that is required to be equal to or greater than in order for the event to be generated.')
ethernetOamEventLogAccumulatedErr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogAccumulatedErr.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogAccumulatedErr.setDescription('Displays the number of errors that have been detected since the OAM sublayer was reset.')
ethernetOamEventLogClearTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 3), )
if mibBuilder.loadTexts: ethernetOamEventLogClearTable.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogClearTable.setDescription('You can clear both the statistics and log of link events of specified port in the table.')
ethernetOamEventLogClearEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetOamEventLogClearEntry.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogClearEntry.setDescription('You can clear both the statistics and log of link events of specified port in the entry.')
ethernetOamEventLogClearPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogClearPort.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogClearPort.setDescription('Displays the port number.')
ethernetOamEventLogClearAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("unchange", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamEventLogClearAction.setStatus('current')
if mibBuilder.loadTexts: ethernetOamEventLogClearAction.setDescription('Clear both the statistics and log of link events of specified port.')
mibBuilder.exportSymbols("TPLINK-ETHERNETOAMEVENTLOG-MIB", ethernetOamEventLogType=ethernetOamEventLogType, ethernetOamEventLogStatRemoteFramePeriod=ethernetOamEventLogStatRemoteFramePeriod, ethernetOamEventLogSeq=ethernetOamEventLogSeq, ethernetOamEventLogStatLocalFrameSeconds=ethernetOamEventLogStatLocalFrameSeconds, ethernetOamEventLogStatEntry=ethernetOamEventLogStatEntry, ethernetOamEventLogClearTable=ethernetOamEventLogClearTable, ethernetOamEventLogTimestamp=ethernetOamEventLogTimestamp, ethernetOamEventLogValue=ethernetOamEventLogValue, ethernetOamEventLogStatRemoteDyingGasp=ethernetOamEventLogStatRemoteDyingGasp, ethernetOamEventLogStatRemoteFrame=ethernetOamEventLogStatRemoteFrame, ethernetOamEventLogClearPort=ethernetOamEventLogClearPort, ethernetOamEventLogStatTable=ethernetOamEventLogStatTable, ethernetOamEventLogClearAction=ethernetOamEventLogClearAction, ethernetOamEventLogStatLocalDyingGasp=ethernetOamEventLogStatLocalDyingGasp, ethernetOamEventLogStatLocalSymbolPeriod=ethernetOamEventLogStatLocalSymbolPeriod, ethernetOamEventLogStatLocalCriticalEvent=ethernetOamEventLogStatLocalCriticalEvent, ethernetOamEventLogTable=ethernetOamEventLogTable, ethernetOamEventLogStatRemoteCriticalEvent=ethernetOamEventLogStatRemoteCriticalEvent, ethernetOamEventLogClearEntry=ethernetOamEventLogClearEntry, ethernetOamEventLogLocation=ethernetOamEventLogLocation, ethernetOamEventLogStatRemoteFrameSeconds=ethernetOamEventLogStatRemoteFrameSeconds, ethernetOamEventLogEntry=ethernetOamEventLogEntry, ethernetOamEventLogStatLocalFrame=ethernetOamEventLogStatLocalFrame, ethernetOamEventLogWindow=ethernetOamEventLogWindow, ethernetOamEventLogThreshold=ethernetOamEventLogThreshold, ethernetOamEventLogAccumulatedErr=ethernetOamEventLogAccumulatedErr, ethernetOamEventLogPort=ethernetOamEventLogPort, ethernetOamEventLogStatRemoteSymbolPeriod=ethernetOamEventLogStatRemoteSymbolPeriod, ethernetOamEventLogStatPort=ethernetOamEventLogStatPort, ethernetOamEventLogStatLocalFramePeriod=ethernetOamEventLogStatLocalFramePeriod)
