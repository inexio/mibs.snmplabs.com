#
# PySNMP MIB module CXDataScope-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXDataScope-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
cxDataScope, = mibBuilder.importSymbols("CXProduct-SMI", "cxDataScope")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, Counter32, Unsigned32, TimeTicks, iso, Bits, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter32", "Unsigned32", "TimeTicks", "iso", "Bits", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dsControl = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1))
dsDataBaseVersion = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsDataBaseVersion.setStatus('mandatory')
if mibBuilder.loadTexts: dsDataBaseVersion.setDescription(' Version of the Database of Data Scope. Default Value: none')
dsDataBaseSize = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsDataBaseSize.setStatus('mandatory')
if mibBuilder.loadTexts: dsDataBaseSize.setDescription('The size of Database in Kbytes.')
dsDataBaseReady = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-ready", 1), ("ready", 2))).clone('not-ready')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsDataBaseReady.setStatus('mandatory')
if mibBuilder.loadTexts: dsDataBaseReady.setDescription('Status of Database. READY if Database has memory; NOT-READY if it failed to allocate memory.')
dsRTTYIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRTTYIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: dsRTTYIpAddress.setDescription(' The IP address of RTTY. For the time being, only ONE RTTY is supported.')
dsOutLostCounter1 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsOutLostCounter1.setStatus('mandatory')
if mibBuilder.loadTexts: dsOutLostCounter1.setDescription('The number of data records discarded when sent to Local Console.')
dsOutLostCounter2 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsOutLostCounter2.setStatus('mandatory')
if mibBuilder.loadTexts: dsOutLostCounter2.setDescription('The number of data records discarded when sent to RTTY.')
dsOutLostCounter3 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsOutLostCounter3.setStatus('mandatory')
if mibBuilder.loadTexts: dsOutLostCounter3.setDescription('The number of data records discarded when sent to PC.')
dsDataBase = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2))
dsOperationMode = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("stop-mode", 1), ("write-mode", 2), ("read-mode", 3))).clone('stop-mode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsOperationMode.setStatus('mandatory')
if mibBuilder.loadTexts: dsOperationMode.setDescription('Operational Mode of Database. No more data records can be saved to Database if the operational mode is in read-mode.')
dsTotalRecord = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsTotalRecord.setStatus('mandatory')
if mibBuilder.loadTexts: dsTotalRecord.setDescription('The total data records in the Database.')
dsOverwrittenRecord = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsOverwrittenRecord.setStatus('mandatory')
if mibBuilder.loadTexts: dsOverwrittenRecord.setDescription('The amount of data records overwritten since last deleting operation.')
dsReadNumberRecord = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsReadNumberRecord.setStatus('mandatory')
if mibBuilder.loadTexts: dsReadNumberRecord.setDescription('The number of data records that will be read per read operation.')
dsReadOutputDir = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("to-local-console", 1), ("to-RTTY-console", 2))).clone('to-local-console')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsReadOutputDir.setStatus('mandatory')
if mibBuilder.loadTexts: dsReadOutputDir.setDescription('Indicates where to send the data records when reading Database. When value is not equal to 1 or 2, output will be sent to local console.')
dsDBControl = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: dsDBControl.setStatus('mandatory')
if mibBuilder.loadTexts: dsDBControl.setDescription('Control of how to read/delete data resocrds in the Database: 1 - idle, no action, 2 - read dsReadNumberRecord number of Previous records and keep those records, 3 - read dsReadNumberRecord number of Previous records and erase those records, 4 - read dsReadNumberRecord number of Next-records, and keep those records, 5 - read dsReadNumberRecord number of Next-records, and erase those records, 6 - Erase All Records.')
dsReadFormat = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ascii-format", 1), ("binary-format", 2))).clone('ascii-format')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsReadFormat.setStatus('mandatory')
if mibBuilder.loadTexts: dsReadFormat.setDescription('The output data format for reading data records in Database.')
dsRegistryTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3), )
if mibBuilder.loadTexts: dsRegistryTable.setReference('Data Scope Design Description. Memotec internal document')
if mibBuilder.loadTexts: dsRegistryTable.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegistryTable.setDescription('Trace and Registry Control Table.')
dsRegistryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1), ).setIndexNames((0, "CXDataScope-MIB", "dsRegAppID"))
if mibBuilder.loadTexts: dsRegistryEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegistryEntry.setDescription('Trace and Registry Control Table Entry.')
dsRegAppID = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsRegAppID.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegAppID.setDescription('It is sap ID for driver tasks, or pre=defined application ID for other tasks.')
dsRegTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsRegTrafficType.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegTrafficType.setDescription('It is port type for driver tasks, or logical port type for other tasks.')
dsRegIFIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsRegIFIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegIFIndex.setDescription('It is the globalIndex in the ifTbl.')
dsRegDirFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tx-and-rx", 1), ("tx-only", 2), ("rx-only", 3))).clone('tx-and-rx')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDirFilter.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegDirFilter.setDescription('Filter on OsMessage Direction (Type).')
dsRegState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegState.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegState.setDescription('Indicating if Data Scope accepts data from the task registered at this entry.')
dsRegDfMask = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDfMask.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegDfMask.setDescription('Mask of the data filter. This mask will be ANDed with data chosen by dfOffset. The result is checked against dsRegDfValue.')
dsRegDfValue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDfValue.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegDfValue.setDescription('Value of the data filter.')
dsRegDfCriteria = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equal", 1), ("not-equal", 2))).clone('equal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDfCriteria.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegDfCriteria.setDescription('The criteria of comparing dfValue with the value obtained by ANDing dfMask with data.')
dsRegDfOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDfOffset.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegDfOffset.setDescription('The offset of data to be checked.')
dsRegStartMask = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStartMask.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegStartMask.setDescription('The mask of the data-match structure to trigger a start event.')
dsRegStartValue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 21), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStartValue.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegStartValue.setDescription('The value of the data-match structure to trigger a start event.')
dsRegStartCriteria = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equal", 1), ("not-equal", 2))).clone('equal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStartCriteria.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegStartCriteria.setDescription('The criteria of the data-match structure to trigger a start event.')
dsRegStartOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStartOffset.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegStartOffset.setDescription('The data offset of the data-match structure to trigger a start event.')
dsRegStopMask = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStopMask.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegStopMask.setDescription('The mask of the data-match structure to trigger a stop event.')
dsRegStopValue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 25), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStopValue.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegStopValue.setDescription('The value of the data-match structure to trigger a stop event.')
dsRegStopCriteria = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equal", 1), ("not-equal", 2))).clone('equal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStopCriteria.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegStopCriteria.setDescription('The criteria of the data-match structure to trigger a stop event. The values other than 1 and 2 mean the number of events that Data Scope will trace before a stop event is generated.')
dsRegStopOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 27), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStopOffset.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegStopOffset.setDescription('The data offset of the data-match structure to trigger a stop event.')
dsRegStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("non-recording", 1), ("recording", 2))).clone('non-recording')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsRegStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegStatus.setDescription('the state of this trace-registry entry, could be RECORDING or NON-RECORDING. When state is NON-RECORDING, a start event will change state to RECORDING; and a stop event will changes state from RECORDING to NON-RECORDING.')
dsRegDataLength = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 42), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDataLength.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegDataLength.setDescription('The maximum length of data that will be captured. Max. value is 65535.')
dsRegDataOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 43), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDataOffset.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegDataOffset.setDescription('The offset from where to start data capturing. Max. value is 65535.')
dsRegOutputDir = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 44), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegOutputDir.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegOutputDir.setDescription('a bitmap object indicating where to output the traced data. When Bit 0 set to 1: Output data to local console; When Bit 1 set to 1: Output data to RTTY; When Bit 2 set to 1: Output data to Database;')
dsRegOutputFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ascii-format", 1), ("binary-format", 2))).clone('ascii-format')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegOutputFormat.setStatus('mandatory')
if mibBuilder.loadTexts: dsRegOutputFormat.setDescription('indicats the format to be used to output the traced data.')
mibBuilder.exportSymbols("CXDataScope-MIB", dsReadFormat=dsReadFormat, dsTotalRecord=dsTotalRecord, dsRegDfOffset=dsRegDfOffset, dsRegStartOffset=dsRegStartOffset, dsOutLostCounter3=dsOutLostCounter3, dsReadNumberRecord=dsReadNumberRecord, dsRegAppID=dsRegAppID, dsRTTYIpAddress=dsRTTYIpAddress, dsRegStartValue=dsRegStartValue, dsRegStopOffset=dsRegStopOffset, dsRegDfValue=dsRegDfValue, dsRegStartCriteria=dsRegStartCriteria, dsDataBaseVersion=dsDataBaseVersion, dsDataBase=dsDataBase, dsDBControl=dsDBControl, dsRegIFIndex=dsRegIFIndex, dsRegStopValue=dsRegStopValue, dsRegDfMask=dsRegDfMask, dsRegState=dsRegState, dsRegDirFilter=dsRegDirFilter, dsOperationMode=dsOperationMode, dsDataBaseSize=dsDataBaseSize, dsOutLostCounter2=dsOutLostCounter2, dsReadOutputDir=dsReadOutputDir, dsRegOutputDir=dsRegOutputDir, dsOverwrittenRecord=dsOverwrittenRecord, dsRegStatus=dsRegStatus, dsRegTrafficType=dsRegTrafficType, dsRegStopMask=dsRegStopMask, dsControl=dsControl, dsRegOutputFormat=dsRegOutputFormat, dsRegStopCriteria=dsRegStopCriteria, dsRegStartMask=dsRegStartMask, dsOutLostCounter1=dsOutLostCounter1, dsRegDataOffset=dsRegDataOffset, dsDataBaseReady=dsDataBaseReady, dsRegistryEntry=dsRegistryEntry, dsRegDataLength=dsRegDataLength, dsRegDfCriteria=dsRegDfCriteria, dsRegistryTable=dsRegistryTable)
