#
# PySNMP MIB module TIARA-HSSI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-HSSI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, TimeTicks, ModuleIdentity, NotificationType, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Bits, Counter32, ObjectIdentity, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "TimeTicks", "ModuleIdentity", "NotificationType", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Bits", "Counter32", "ObjectIdentity", "Gauge32", "Integer32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
tiaraInterfaces, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraInterfaces")
tiaraHssiMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2))
tiaraHssiMib.setRevisions(('1900-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tiaraHssiMib.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: tiaraHssiMib.setLastUpdated('0008180000Z')
if mibBuilder.loadTexts: tiaraHssiMib.setOrganization('Tiara Networks Inc.')
if mibBuilder.loadTexts: tiaraHssiMib.setContactInfo(' Tiara Networks Customer Support 525 Race Street, Suite 100, San Jose, CA 95126 USA Tel: +1 408-216-4700 Fax: +1 408-216-4701 Email: support@tiaranetworks.com')
if mibBuilder.loadTexts: tiaraHssiMib.setDescription(' MIB definitions for Tiara HSSI modules.')
hssiConfigTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1), )
if mibBuilder.loadTexts: hssiConfigTable.setStatus('current')
if mibBuilder.loadTexts: hssiConfigTable.setDescription('The HSSI interface configurable parameters are listed in this table.')
hssiConfigTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1), ).setIndexNames((0, "TIARA-HSSI-MIB", "hssiIfIndex"))
if mibBuilder.loadTexts: hssiConfigTableEntry.setStatus('current')
if mibBuilder.loadTexts: hssiConfigTableEntry.setDescription('HSSI table entry.')
hssiIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hssiIfIndex.setStatus('current')
if mibBuilder.loadTexts: hssiIfIndex.setDescription('An integer value that is an index in the entries of the ifTable (MIB-II) with a HSSI interface type.')
hssiConfigClockRate = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000000, 52000000)).clone(52000000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hssiConfigClockRate.setStatus('current')
if mibBuilder.loadTexts: hssiConfigClockRate.setDescription('Configures the clock rate (in Hertz) for the HSSI interface.')
hssiConfigClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internal", 1), ("line", 2))).clone('line')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hssiConfigClockSource.setStatus('current')
if mibBuilder.loadTexts: hssiConfigClockSource.setDescription('Configures the clock source for the HSSI interface to either internal or line.')
hssiConfigTxClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normalinternal", 1), ("normalterminal", 2), ("invertedinternal", 3), ("invertedterminal", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hssiConfigTxClockSource.setStatus('current')
if mibBuilder.loadTexts: hssiConfigTxClockSource.setDescription('Configures the transmit clock source for the HSSI interface to either internal or terminal. This variable is valid only for the HSSI interface on the USSI card.')
hssiConfigRxClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normalinternal", 1), ("normalterminal", 2), ("invertedinternal", 3), ("invertedterminal", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hssiConfigRxClockSource.setStatus('current')
if mibBuilder.loadTexts: hssiConfigRxClockSource.setDescription('Configures the receive clock source for the HSSI interface to either internal or terminal. This variable is valid only for the HSSI interface on the USSI card')
hssiConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dce", 1), ("dte", 2))).clone('dte')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hssiConfigMode.setStatus('current')
if mibBuilder.loadTexts: hssiConfigMode.setDescription('Configures the mode for the HSSI to either DCE or DTE.')
hssiConfigDataMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("inverted", 2))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hssiConfigDataMode.setStatus('current')
if mibBuilder.loadTexts: hssiConfigDataMode.setDescription('Configures the data mode for the HSSI interface. This variable is valid only for the HSSI interface on the USSI card.')
hssiConfigCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("crc16", 1), ("crc32", 2))).clone('crc32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hssiConfigCRC.setStatus('current')
if mibBuilder.loadTexts: hssiConfigCRC.setDescription('Configures the cyclic redundancy check for the HSSI interface to either 16 or 32 bits.')
hssiConfigProcessCtrlSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ignore", 1), ("process", 2))).clone('process')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hssiConfigProcessCtrlSignal.setStatus('current')
if mibBuilder.loadTexts: hssiConfigProcessCtrlSignal.setDescription('Configures the processing of control signals (CA/TA) for the HSSI interface. This variable is valid only for the HSSI interface on the USSI card.')
hssiDteLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hssiDteLoopback.setStatus('current')
if mibBuilder.loadTexts: hssiDteLoopback.setDescription('Configures the local DTE for loopback operation: TRUE : request local DTE to go into line loopback FALSE : request local DTE to abandon line loopback These commands are valid only if the HSSI adaptor is in DCE mode and connected to a local DTE. Since the local DTE has a greater loopback priority than the local DCE, a loopback request initiated by the DCE will be ignored if the DTE simultaneously requests the DCE to loopback. Similarly, the DTE will abort a loopback already initiated by the DCE when the DTE requests the DCE to loopback.')
hssiDceLoopbackTest = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noTest", 1), ("line", 2), ("cable", 3), ("remote", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hssiDceLoopbackTest.setStatus('current')
if mibBuilder.loadTexts: hssiDceLoopbackTest.setDescription('Configures the local/remote DCE for loopback operation. Three DCE loopback modes are available: line, cable, and remote. Use noTest to abandon any of the DCE loopbacks. If the DCE is already in any one of the loopback modes, then noTest must be issued to abort the current test before initiating another loopback request. These commands are valid only if the HSSI adaptor is in DTE mode and it connected to a DCE.')
hssiStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3), )
if mibBuilder.loadTexts: hssiStatsTable.setStatus('current')
if mibBuilder.loadTexts: hssiStatsTable.setDescription('The HSSI interface status parameters are listed in this table.')
hssiStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1), ).setIndexNames((0, "TIARA-HSSI-MIB", "hssiIfIndex"))
if mibBuilder.loadTexts: hssiStatsTableEntry.setStatus('current')
if mibBuilder.loadTexts: hssiStatsTableEntry.setDescription('HSSI Statistics table entry.')
hssiStatsAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 1), Bits().clone(namedValues=NamedValues(("hssi-no-alarms", 0), ("hssi-alarms-CA", 1), ("hssi-alarms-ST", 2), ("hssi-alarms-TM", 3), ("hssi-alarms-LC", 4), ("hssi-alarms-TA", 5), ("hssi-alarms-LALB", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hssiStatsAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: hssiStatsAlarmStatus.setDescription('Specifies the status of the HSSI alarm. If the particular bit is set, then it indicates that the alarm is in ON state. Alarm bits are mode dependent; they are interpreted as follows: hssi-alarms-CA - CA not received from DCE (HSSI is DTE) hssi-alarms-ST - HSSI adaptor driving ST (HSSI is DCE) hssi-alarms-TM - TM received from DCE (HSSI is DTE) hssi-alarms-LC - HSSI adaptor detects LC (HSSI is DTE) hssi-alarms-LC - HSSI adaptor driving LC (HSSI is DCE) hssi-alarms-TA - TA not received from DTE (HSSI is DCE) hssi-alarms-LALB - HSSI adaptor detects LA and/or LB (HSSI is DCE) hssi-alarms-LALB - HSSI adaptor driving LA and/or LB (HSSI is DTE) ')
hssiStatsFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hssiStatsFramesIn.setStatus('current')
if mibBuilder.loadTexts: hssiStatsFramesIn.setDescription('Specifies the number of incoming frames.')
hssiStatsFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hssiStatsFramesOut.setStatus('current')
if mibBuilder.loadTexts: hssiStatsFramesOut.setDescription('Specifies the number of outgoing frames.')
hssiStatsOctetsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hssiStatsOctetsIn.setStatus('current')
if mibBuilder.loadTexts: hssiStatsOctetsIn.setDescription('Specifies the number of incoming octets.')
hssiStatsOctetsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hssiStatsOctetsOut.setStatus('current')
if mibBuilder.loadTexts: hssiStatsOctetsOut.setDescription('Specifies the number of outgoing octets.')
hssiStatsCRCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hssiStatsCRCErrors.setStatus('current')
if mibBuilder.loadTexts: hssiStatsCRCErrors.setDescription('Specifies the number of CRC errors that have been identified.')
hssiTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 2))
hssiTrapVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 2, 1))
hssiAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("hssi-alarm-CA", 1), ("hssi-alarm-ST", 2), ("hssi-alarm-TM", 3), ("hssi-alarm-LC", 4), ("hssi-alarm-TA", 5), ("hssi-alarm-LALB", 6))))
if mibBuilder.loadTexts: hssiAlarmType.setStatus('current')
if mibBuilder.loadTexts: hssiAlarmType.setDescription('Specifies the type of alarm generated by the agent for the HSSI interface. Alarms are mode dependent; they are interpreted as follows: hssi-alarms-CA - CA not received from DCE (HSSI is DTE) hssi-alarms-ST - HSSI adaptor driving ST (HSSI is DCE) hssi-alarms-TM - TM received from DCE (HSSI is DTE) hssi-alarms-LC - HSSI adaptor detects LC (HSSI is DTE) hssi-alarms-LC - HSSI adaptor driving LC (HSSI is DCE) hssi-alarms-TA - TA not received from DTE (HSSI is DCE) hssi-alarms-LALB - HSSI adaptor detects LA and/or LB (HSSI is DCE) hssi-alarms-LALB - HSSI adaptor driving LA and/or LB (HSSI is DTE) ')
hssiAlarmOnTrap = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 2) + (0,1)).setObjects(("TIARA-HSSI-MIB", "hssiIfIndex"), ("TIARA-HSSI-MIB", "hssiAlarmType"))
if mibBuilder.loadTexts: hssiAlarmOnTrap.setDescription('HSSI alarm traps for the Alarm-On state.')
hssiAlarmOffTrap = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 2) + (0,2)).setObjects(("TIARA-HSSI-MIB", "hssiIfIndex"), ("TIARA-HSSI-MIB", "hssiAlarmType"))
if mibBuilder.loadTexts: hssiAlarmOffTrap.setDescription('HSSI alarm traps for the Alarm-Off state.')
mibBuilder.exportSymbols("TIARA-HSSI-MIB", hssiStatsFramesOut=hssiStatsFramesOut, hssiAlarmType=hssiAlarmType, hssiConfigRxClockSource=hssiConfigRxClockSource, hssiConfigTable=hssiConfigTable, hssiConfigMode=hssiConfigMode, hssiStatsOctetsIn=hssiStatsOctetsIn, PYSNMP_MODULE_ID=tiaraHssiMib, hssiConfigClockSource=hssiConfigClockSource, hssiAlarmOnTrap=hssiAlarmOnTrap, hssiStatsFramesIn=hssiStatsFramesIn, hssiConfigCRC=hssiConfigCRC, hssiTraps=hssiTraps, hssiConfigClockRate=hssiConfigClockRate, hssiStatsTableEntry=hssiStatsTableEntry, hssiDteLoopback=hssiDteLoopback, hssiTrapVariables=hssiTrapVariables, tiaraHssiMib=tiaraHssiMib, hssiConfigDataMode=hssiConfigDataMode, hssiDceLoopbackTest=hssiDceLoopbackTest, hssiIfIndex=hssiIfIndex, hssiConfigTableEntry=hssiConfigTableEntry, hssiStatsAlarmStatus=hssiStatsAlarmStatus, hssiStatsTable=hssiStatsTable, hssiStatsCRCErrors=hssiStatsCRCErrors, hssiStatsOctetsOut=hssiStatsOctetsOut, hssiAlarmOffTrap=hssiAlarmOffTrap, hssiConfigTxClockSource=hssiConfigTxClockSource, hssiConfigProcessCtrlSignal=hssiConfigProcessCtrlSignal)
