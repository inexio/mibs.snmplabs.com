#
# PySNMP MIB module INFORMANT-MBM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INFORMANT-MBM
# Produced by pysmi-0.3.4 at Wed May  1 13:53:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ObjectIdentity, iso, Bits, Counter64, TimeTicks, Unsigned32, MibIdentifier, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ObjectIdentity", "iso", "Bits", "Counter64", "TimeTicks", "Unsigned32", "MibIdentifier", "IpAddress", "Gauge32")
TruthValue, DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "DateAndTime", "TextualConvention")
WtcsDisplayString, informant = mibBuilder.importSymbols("WTCS", "WtcsDisplayString", "informant")
motherBoardMonitor = ModuleIdentity((1, 3, 6, 1, 4, 1, 9600, 1, 10))
motherBoardMonitor.setRevisions(('2004-06-23 20:39',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: motherBoardMonitor.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: motherBoardMonitor.setLastUpdated('200406232039Z')
if mibBuilder.loadTexts: motherBoardMonitor.setOrganization('Informant Systems, Inc.')
if mibBuilder.loadTexts: motherBoardMonitor.setContactInfo(' Garth Williams Tel: +1 780 433 7973 E-mail: garth.williams@wtcs.org')
if mibBuilder.loadTexts: motherBoardMonitor.setDescription('The MIB module for informant standard entities.')
mbmBusType = MibScalar((1, 3, 6, 1, 4, 1, 9600, 1, 10, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmBusType.setStatus('current')
if mibBuilder.loadTexts: mbmBusType.setDescription('None')
mbmPath = MibScalar((1, 3, 6, 1, 4, 1, 9600, 1, 10, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmPath.setStatus('current')
if mibBuilder.loadTexts: mbmPath.setDescription('MBM path')
mbmSmbName = MibScalar((1, 3, 6, 1, 4, 1, 9600, 1, 10, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSmbName.setStatus('current')
if mibBuilder.loadTexts: mbmSmbName.setDescription('Nice name for SMBus')
mbmSmbType = MibScalar((1, 3, 6, 1, 4, 1, 9600, 1, 10, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSmbType.setStatus('current')
if mibBuilder.loadTexts: mbmSmbType.setDescription('None')
mbmVersion = MibScalar((1, 3, 6, 1, 4, 1, 9600, 1, 10, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmVersion.setStatus('current')
if mibBuilder.loadTexts: mbmVersion.setDescription('MBM Version number')
mbmSensorTable = MibTable((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6), )
if mibBuilder.loadTexts: mbmSensorTable.setStatus('current')
if mibBuilder.loadTexts: mbmSensorTable.setDescription('The (conceptual) table listing all the MBM sensors.')
mbmSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1), ).setIndexNames((0, "INFORMANT-MBM", "mbmSensorIndex"))
if mibBuilder.loadTexts: mbmSensorEntry.setStatus('current')
if mibBuilder.loadTexts: mbmSensorEntry.setDescription('An entry (conceptual row) in the mbmSensorTable.')
mbmSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorIndex.setStatus('current')
if mibBuilder.loadTexts: mbmSensorIndex.setDescription('Index for this sensor')
mbmSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorName.setStatus('current')
if mibBuilder.loadTexts: mbmSensorName.setDescription('Name of sensor')
mbmSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("stUnknown", 0), ("stTemperature", 1), ("stVoltage", 2), ("stFan", 3), ("stMhz", 4), ("stPercentage", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorType.setStatus('current')
if mibBuilder.loadTexts: mbmSensorType.setDescription('Type of sensor')
mbmSensorReadout = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorReadout.setStatus('current')
if mibBuilder.loadTexts: mbmSensorReadout.setDescription('Total number of readout')
mbmSensorCurrentI = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorCurrentI.setStatus('current')
if mibBuilder.loadTexts: mbmSensorCurrentI.setDescription('Current value in integer form')
mbmSensorCurrentS = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorCurrentS.setStatus('current')
if mibBuilder.loadTexts: mbmSensorCurrentS.setDescription('Current value in string form')
mbmSensorLowI = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorLowI.setStatus('current')
if mibBuilder.loadTexts: mbmSensorLowI.setDescription('Lowest readout value in integer form')
mbmSensorLowS = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorLowS.setStatus('current')
if mibBuilder.loadTexts: mbmSensorLowS.setDescription('Lowest readout value in string form')
mbmSensorHighI = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorHighI.setStatus('current')
if mibBuilder.loadTexts: mbmSensorHighI.setDescription('Highest readout value in integer form')
mbmSensorHighS = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorHighS.setStatus('current')
if mibBuilder.loadTexts: mbmSensorHighS.setDescription('Highest readout value in string form')
mbmSensorAlarm1I = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorAlarm1I.setStatus('current')
if mibBuilder.loadTexts: mbmSensorAlarm1I.setDescription('temp & fan: low alarm; voltage: % off (integer form)')
mbmSensorAlarm1S = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorAlarm1S.setStatus('current')
if mibBuilder.loadTexts: mbmSensorAlarm1S.setDescription('temp & fan: low alarm; voltage: % off string form)')
mbmSensorAlarm2I = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorAlarm2I.setStatus('current')
if mibBuilder.loadTexts: mbmSensorAlarm2I.setDescription('temp: high alarm (integer form)')
mbmSensorAlarm2S = MibTableColumn((1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbmSensorAlarm2S.setStatus('current')
if mibBuilder.loadTexts: mbmSensorAlarm2S.setDescription('temp: high alarm (string form)')
mibBuilder.exportSymbols("INFORMANT-MBM", motherBoardMonitor=motherBoardMonitor, mbmSensorLowI=mbmSensorLowI, mbmSensorCurrentS=mbmSensorCurrentS, mbmSensorEntry=mbmSensorEntry, mbmSensorCurrentI=mbmSensorCurrentI, mbmSensorTable=mbmSensorTable, mbmSmbType=mbmSmbType, mbmSensorType=mbmSensorType, mbmSensorHighS=mbmSensorHighS, mbmSensorHighI=mbmSensorHighI, mbmSensorName=mbmSensorName, mbmSensorLowS=mbmSensorLowS, mbmSensorReadout=mbmSensorReadout, mbmSmbName=mbmSmbName, mbmVersion=mbmVersion, mbmSensorAlarm2S=mbmSensorAlarm2S, mbmPath=mbmPath, mbmSensorAlarm1I=mbmSensorAlarm1I, PYSNMP_MODULE_ID=motherBoardMonitor, mbmSensorIndex=mbmSensorIndex, mbmSensorAlarm2I=mbmSensorAlarm2I, mbmSensorAlarm1S=mbmSensorAlarm1S, mbmBusType=mbmBusType)
