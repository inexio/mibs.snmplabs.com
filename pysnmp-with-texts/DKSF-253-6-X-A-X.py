#
# PySNMP MIB module DKSF-253-6-X-A-X (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DKSF-253-6-X-A-X
# Produced by pysmi-0.3.4 at Wed May  1 12:47:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
MibIdentifier, Bits, Gauge32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, iso, Integer32, Unsigned32, ObjectIdentity, enterprises, Counter64, Counter32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "Gauge32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "iso", "Integer32", "Unsigned32", "ObjectIdentity", "enterprises", "Counter64", "Counter32", "TimeTicks", "NotificationType")
TimeStamp, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TruthValue", "TextualConvention", "DisplayString")
netPing = ModuleIdentity((1, 3, 6, 1, 4, 1, 25728, 253))
netPing.setRevisions(('2015-09-29 00:00', '2014-11-19 00:00', '2014-06-12 00:00', '2011-02-04 00:00', '2010-08-30 00:00', '2010-08-20 00:00', '2010-08-13 00:00', '2010-08-11 00:00', '2010-07-08 00:00', '2010-04-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netPing.setRevisionsDescriptions(('npIoLevelOut values changed, flip(-1) added npElecEnergy, npElecEnergy100 now can be writed and stored in EEPROM. Attention, stored values are distorted if npElecPulsesPerKWh is changed', 'npElecMeter branch updated', 'npIoSinglePulseDuration, npIoSinglePulseStart variables, npReboot branch added', 'Renamed to DKSF 253, 4th IO line is added', 'bugfix ioTrap variables', 'additional ioTrap variables', 'ioTrap variable definitions reordered for SNMPc compatibility', 'ioTrap definition added', 'ioLine pulse counter and npElecMeter branch added', 'SMIv2-style rewrite',))
if mibBuilder.loadTexts: netPing.setLastUpdated('201509290000Z')
if mibBuilder.loadTexts: netPing.setOrganization('Alentis Electronics')
if mibBuilder.loadTexts: netPing.setContactInfo('developers@netping.ru')
if mibBuilder.loadTexts: netPing.setDescription('MIB for NetPing remote sensing and control')
lightcom = MibIdentifier((1, 3, 6, 1, 4, 1, 25728))
npIo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900))
npIoTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8900, 1), )
if mibBuilder.loadTexts: npIoTable.setStatus('current')
if mibBuilder.loadTexts: npIoTable.setDescription('Digital Input/output Table')
npIoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1), ).setIndexNames((0, "DKSF-253-6-X-A-X", "npIoLineN"))
if mibBuilder.loadTexts: npIoEntry.setStatus('current')
if mibBuilder.loadTexts: npIoEntry.setDescription('Digital Input/output Table Row')
npIoLineN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoLineN.setStatus('current')
if mibBuilder.loadTexts: npIoLineN.setDescription('Number of IO line, from 1 to max supported')
npIoLevelIn = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoLevelIn.setStatus('current')
if mibBuilder.loadTexts: npIoLevelIn.setDescription('Input level, 0 or 1')
npIoLevelOut = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1))).clone(namedValues=NamedValues(("flip", -1), ("low", 0), ("high", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoLevelOut.setStatus('current')
if mibBuilder.loadTexts: npIoLevelOut.setDescription('Output level, 0 or 1. Write -1 to flip output.')
npIoMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoMemo.setStatus('current')
if mibBuilder.loadTexts: npIoMemo.setDescription('IO line memo')
npIoPulseCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoPulseCounter.setStatus('current')
if mibBuilder.loadTexts: npIoPulseCounter.setDescription('Pulse Counter (counts positive fronts) Write 0 to reset.')
npIoSinglePulseDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 25500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoSinglePulseDuration.setStatus('current')
if mibBuilder.loadTexts: npIoSinglePulseDuration.setDescription('Set duration of single pulse on IO output line, 100ms to 25500ms, min. step is 100ms')
npIoSinglePulseStart = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoSinglePulseStart.setStatus('current')
if mibBuilder.loadTexts: npIoSinglePulseStart.setDescription('Write 1 to start single pulse on IO output. Output will be inverted for time, specified by npIoSinglePulseDuration')
npIoTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900, 2))
npIoTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0))
npIoTrapLineN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLineN.setStatus('current')
if mibBuilder.loadTexts: npIoTrapLineN.setDescription('Trap data, Number of IO line')
npIoTrapLevelIn = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLevelIn.setStatus('current')
if mibBuilder.loadTexts: npIoTrapLevelIn.setDescription('Trap data, new Input level, 0 or 1')
npIoTrapMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapMemo.setStatus('current')
if mibBuilder.loadTexts: npIoTrapMemo.setDescription('Trap data, IO line memo')
npIoTrapLevelIn1 = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLevelIn1.setStatus('current')
if mibBuilder.loadTexts: npIoTrapLevelIn1.setDescription('Trap data, current Input level Line 1, value 0 or 1')
npIoTrapLevelIn2 = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLevelIn2.setStatus('current')
if mibBuilder.loadTexts: npIoTrapLevelIn2.setDescription('Trap data, current Input level Line 2, value 0 or 1')
npIoTrapLevelIn3 = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLevelIn3.setStatus('current')
if mibBuilder.loadTexts: npIoTrapLevelIn3.setDescription('Trap data, current Input level Line 3, value 0 or 1')
npIoTrapLevelIn4 = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLevelIn4.setStatus('current')
if mibBuilder.loadTexts: npIoTrapLevelIn4.setDescription('Trap data, current Input level Line 4, value 0 or 1')
npIoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0, 1)).setObjects(("DKSF-253-6-X-A-X", "npIoTrapLineN"), ("DKSF-253-6-X-A-X", "npIoTrapLevelIn"), ("DKSF-253-6-X-A-X", "npIoTrapMemo"), ("DKSF-253-6-X-A-X", "npIoTrapLevelIn1"), ("DKSF-253-6-X-A-X", "npIoTrapLevelIn2"), ("DKSF-253-6-X-A-X", "npIoTrapLevelIn3"), ("DKSF-253-6-X-A-X", "npIoTrapLevelIn4"))
if mibBuilder.loadTexts: npIoTrap.setStatus('current')
if mibBuilder.loadTexts: npIoTrap.setDescription('Input state of IO line is changed')
npElecMeter = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 9700))
npElecTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 9700, 1), )
if mibBuilder.loadTexts: npElecTable.setStatus('current')
if mibBuilder.loadTexts: npElecTable.setDescription('Electricity Meter Table')
npElecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1), ).setIndexNames((0, "DKSF-253-6-X-A-X", "npElecIndex"))
if mibBuilder.loadTexts: npElecEntry.setStatus('current')
if mibBuilder.loadTexts: npElecEntry.setDescription('Electricity Meter Table Table Row')
npElecIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npElecIndex.setStatus('current')
if mibBuilder.loadTexts: npElecIndex.setDescription('Number of elec.meter, associated with IO line')
npElecPulsesPerKwh = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npElecPulsesPerKwh.setStatus('current')
if mibBuilder.loadTexts: npElecPulsesPerKwh.setDescription('Pulses on IO line input per 1 kWh of consumed energy')
npElecPower = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npElecPower.setStatus('current')
if mibBuilder.loadTexts: npElecPower.setDescription('Power, Watts, based on pulse rate/interval, 5 minute average')
npElecEnergy = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npElecEnergy.setStatus('current')
if mibBuilder.loadTexts: npElecEnergy.setDescription('Energy counter, kWh, based on pulse count')
npElecEnergy100 = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npElecEnergy100.setStatus('current')
if mibBuilder.loadTexts: npElecEnergy100.setDescription('Energy counter, kWh*100, based on pulse count')
npReboot = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 911))
npSoftReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npSoftReboot.setStatus('current')
if mibBuilder.loadTexts: npSoftReboot.setDescription('Write 1 to reboot device after current operations completition')
npResetStack = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npResetStack.setStatus('current')
if mibBuilder.loadTexts: npResetStack.setDescription('Write 1 to re-initialize network stack')
npForcedReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npForcedReboot.setStatus('current')
if mibBuilder.loadTexts: npForcedReboot.setDescription('Write 1 to immediate forced reboot')
mibBuilder.exportSymbols("DKSF-253-6-X-A-X", npIoTraps=npIoTraps, npIoTrapLevelIn1=npIoTrapLevelIn1, npSoftReboot=npSoftReboot, npElecMeter=npElecMeter, npElecTable=npElecTable, npIoSinglePulseStart=npIoSinglePulseStart, lightcom=lightcom, npIoTrapLevelIn=npIoTrapLevelIn, npIoTrapLevelIn2=npIoTrapLevelIn2, npIoSinglePulseDuration=npIoSinglePulseDuration, npIoEntry=npIoEntry, PYSNMP_MODULE_ID=netPing, npIo=npIo, npIoTrap=npIoTrap, npElecIndex=npElecIndex, npForcedReboot=npForcedReboot, npElecEnergy100=npElecEnergy100, npReboot=npReboot, npIoLevelIn=npIoLevelIn, npElecEnergy=npElecEnergy, npIoTrapLevelIn3=npIoTrapLevelIn3, npElecEntry=npElecEntry, npIoPulseCounter=npIoPulseCounter, npIoTrapLevelIn4=npIoTrapLevelIn4, npIoLineN=npIoLineN, npElecPower=npElecPower, npIoTrapMemo=npIoTrapMemo, npIoTrapLineN=npIoTrapLineN, npIoTrapPrefix=npIoTrapPrefix, npIoLevelOut=npIoLevelOut, netPing=netPing, npElecPulsesPerKwh=npElecPulsesPerKwh, npResetStack=npResetStack, npIoMemo=npIoMemo, npIoTable=npIoTable)
