#
# PySNMP MIB module GUARDIAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GUARDIAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:20:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Unsigned32, Integer32, Counter64, NotificationType, MibIdentifier, ObjectIdentity, iso, enterprises, Gauge32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Unsigned32", "Integer32", "Counter64", "NotificationType", "MibIdentifier", "ObjectIdentity", "iso", "enterprises", "Gauge32", "IpAddress", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
westek = MibIdentifier((1, 3, 6, 1, 4, 1, 3166))
guardian = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1))
device = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2))
masks = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 4))
special = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 5))
devInput = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1))
devFan = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2))
devTemp = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3))
devISA = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4))
devDC = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5))
devInput1 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 1))
devInput2 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 2))
devInput3 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 3))
devInput4 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 4))
devFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1))
devFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2))
devFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3))
devFan4 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4))
devTemp1 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1))
devTemp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2))
devTemp3 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3))
devTemp4 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4))
devTemp5 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5))
devTemp6 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6))
devTemp7 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7))
devTemp8 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8))
devISAP12 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1))
devISAP5 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2))
devISAN5 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3))
devISAN12 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4))
devDCP12 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1))
devDCP5 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2))
guardianRev = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: guardianRev.setStatus('mandatory')
if mibBuilder.loadTexts: guardianRev.setDescription('The name and revision number of Guardian card. Revision = Major.Minor.Codeversion.')
control = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("reset", 1), ("updatenvr", 2), ("reset2nvr", 3), ("reset2fac", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: control.setStatus('mandatory')
if mibBuilder.loadTexts: control.setDescription('Guardian Control Functions 1=Reset Errors, 2=Write settings to NVRAM, 3=Reset to NVRAM, 4=Reset to factory defaults.')
devInpStat = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInpStat.setStatus('mandatory')
if mibBuilder.loadTexts: devInpStat.setDescription('Status bits for Inputs Bit 0-3 = Inputs 1-4')
devFanStat = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFanStat.setStatus('mandatory')
if mibBuilder.loadTexts: devFanStat.setDescription('Status bits for Fans Bit 0-3 = Fans 1-4')
devTempStat = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTempStat.setStatus('mandatory')
if mibBuilder.loadTexts: devTempStat.setDescription('Status bits for Temp probes Bit 0-7 = Temps 1-8')
devISAStat = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAStat.setStatus('mandatory')
if mibBuilder.loadTexts: devISAStat.setDescription('Status bits for ISA Voltages, Bits 0-3 = +12,+5,-5,-12')
devDCStat = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDCStat.setStatus('mandatory')
if mibBuilder.loadTexts: devDCStat.setDescription('Status bits for DC Voltages, Bits 0-1 = +12,+5')
devInp1Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp1Val.setStatus('mandatory')
if mibBuilder.loadTexts: devInp1Val.setDescription('Input Switch 1 current value, 1=Switched')
devInp1Pol = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp1Pol.setStatus('mandatory')
if mibBuilder.loadTexts: devInp1Pol.setDescription('Input Switch 1 Polarity, 1=Inverted')
devInp2Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp2Val.setStatus('mandatory')
if mibBuilder.loadTexts: devInp2Val.setDescription('Input Switch 2 current value, 1=Switched')
devInp2Pol = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp2Pol.setStatus('mandatory')
if mibBuilder.loadTexts: devInp2Pol.setDescription('Input Switch 2 Polarity, 1=Inverted')
devInp3Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp3Val.setStatus('mandatory')
if mibBuilder.loadTexts: devInp3Val.setDescription('Input Switch 3 current value, 1=Switched')
devInp3Pol = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp3Pol.setStatus('mandatory')
if mibBuilder.loadTexts: devInp3Pol.setDescription('Input Switch 3 Polarity, 1=Inverted')
devInp4Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp4Val.setStatus('mandatory')
if mibBuilder.loadTexts: devInp4Val.setDescription('Input Switch 4 current value, 1=Switched')
devInp4Pol = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp4Pol.setStatus('mandatory')
if mibBuilder.loadTexts: devInp4Pol.setDescription('Input Switch 4 Polarity, 1=Inverted')
devFan1Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devFan1Val.setStatus('mandatory')
if mibBuilder.loadTexts: devFan1Val.setDescription('Current Fan 1 Speed in RPM')
devFan1Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan1Min.setStatus('mandatory')
if mibBuilder.loadTexts: devFan1Min.setDescription('Fan 1 Minimum Speed in RPM')
devFan1Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan1Max.setStatus('mandatory')
if mibBuilder.loadTexts: devFan1Max.setDescription('Fan 1 Maximum Speed in RPM')
devFan2Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devFan2Val.setStatus('mandatory')
if mibBuilder.loadTexts: devFan2Val.setDescription('Current Fan 2 Speed in RPM')
devFan2Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan2Min.setStatus('mandatory')
if mibBuilder.loadTexts: devFan2Min.setDescription('Fan 2 Minimum Speed in RPM')
devFan2Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan2Max.setStatus('mandatory')
if mibBuilder.loadTexts: devFan2Max.setDescription('Fan 2 Maximum Speed in RPM')
devFan3Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devFan3Val.setStatus('mandatory')
if mibBuilder.loadTexts: devFan3Val.setDescription('Current Fan 3 Speed in RPM')
devFan3Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan3Min.setStatus('mandatory')
if mibBuilder.loadTexts: devFan3Min.setDescription('Fan 3 Minimum Speed in RPM')
devFan3Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan3Max.setStatus('mandatory')
if mibBuilder.loadTexts: devFan3Max.setDescription('Fan 3 Maximum Speed in RPM')
devFan4Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devFan4Val.setStatus('mandatory')
if mibBuilder.loadTexts: devFan4Val.setDescription('Current Fan 4 Speed in RPM')
devFan4Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan4Min.setStatus('mandatory')
if mibBuilder.loadTexts: devFan4Min.setDescription('Fan 4 Minimum Speed in RPM')
devFan4Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan4Max.setStatus('mandatory')
if mibBuilder.loadTexts: devFan4Max.setDescription('Fan 4 Maximum Speed in RPM')
devTemp1Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp1Val.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp1Val.setDescription('Current Probe 1 Temperature')
devTemp1Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp1Min.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp1Min.setDescription('Probe 1 Minimum Temperature')
devTemp1Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp1Max.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp1Max.setDescription('Probe 1 Maximum Temperature')
devTemp2Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp2Val.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp2Val.setDescription('Current Probe 2 Temperature')
devTemp2Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp2Min.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp2Min.setDescription('Probe 2 Minimum Temperature')
devTemp2Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp2Max.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp2Max.setDescription('Probe 2 Maximum Temperature')
devTemp3Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp3Val.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp3Val.setDescription('Current Probe 3 Temperature')
devTemp3Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp3Min.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp3Min.setDescription('Probe 3 Minimum Temperature')
devTemp3Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp3Max.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp3Max.setDescription('Probe 3 Maximum Temperature')
devTemp4Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp4Val.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp4Val.setDescription('Current Probe 4 Temperature')
devTemp4Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp4Min.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp4Min.setDescription('Probe 4 Minimum Temperature')
devTemp4Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp4Max.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp4Max.setDescription('Probe 4 Maximum Temperature')
devTemp5Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp5Val.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp5Val.setDescription('Current Probe 5 Temperature')
devTemp5Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp5Min.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp5Min.setDescription('Probe 5 Minimum Temperature')
devTemp5Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp5Max.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp5Max.setDescription('Probe 5 Maximum Temperature')
devTemp6Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp6Val.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp6Val.setDescription('Current Probe 6 Temperature')
devTemp6Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp6Min.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp6Min.setDescription('Probe 6 Minimum Temperature')
devTemp6Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp6Max.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp6Max.setDescription('Probe 6 Maximum Temperature')
devTemp7Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp7Val.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp7Val.setDescription('Current Probe 7 Temperature')
devTemp7Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp7Min.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp7Min.setDescription('Probe 7 Minimum Temperature')
devTemp7Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp7Max.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp7Max.setDescription('Probe 7 Maximum Temperature')
devTemp8Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp8Val.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp8Val.setDescription('Current Probe 8 Temperature')
devTemp8Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp8Min.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp8Min.setDescription('Probe 8 Minimum Temperature')
devTemp8Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp8Max.setStatus('mandatory')
if mibBuilder.loadTexts: devTemp8Max.setDescription('Probe 8 Maximum Temperature')
devISAP12Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devISAP12Val.setStatus('mandatory')
if mibBuilder.loadTexts: devISAP12Val.setDescription('Current ISA Bus +12V value (x100)')
devISAP12Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAP12Min.setStatus('mandatory')
if mibBuilder.loadTexts: devISAP12Min.setDescription('Minimum ISA Bus +12V value (x100)')
devISAP12Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAP12Max.setStatus('mandatory')
if mibBuilder.loadTexts: devISAP12Max.setDescription('Maximum ISA Bus +12V value (x100)')
devISAP5Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devISAP5Val.setStatus('mandatory')
if mibBuilder.loadTexts: devISAP5Val.setDescription('Current ISA Bus +5V value (x100)')
devISAP5Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAP5Min.setStatus('mandatory')
if mibBuilder.loadTexts: devISAP5Min.setDescription('Minimum ISA Bus +5V value (x100)')
devISAP5Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAP5Max.setStatus('mandatory')
if mibBuilder.loadTexts: devISAP5Max.setDescription('Maximum ISA Bus +5V value (x100)')
devISAN5Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devISAN5Val.setStatus('mandatory')
if mibBuilder.loadTexts: devISAN5Val.setDescription('Current ISA Bus -5V value (x100)')
devISAN5Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAN5Min.setStatus('mandatory')
if mibBuilder.loadTexts: devISAN5Min.setDescription('Minimum ISA Bus -5V value (x100)')
devISAN5Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAN5Max.setStatus('mandatory')
if mibBuilder.loadTexts: devISAN5Max.setDescription('Maximum ISA Bus -5V value (x100)')
devISAN12Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devISAN12Val.setStatus('mandatory')
if mibBuilder.loadTexts: devISAN12Val.setDescription('Current ISA Bus -12V value (x100)')
devISAN12Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAN12Min.setStatus('mandatory')
if mibBuilder.loadTexts: devISAN12Min.setDescription('Minimum ISA Bus -12V value (x100)')
devISAN12Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAN12Max.setStatus('mandatory')
if mibBuilder.loadTexts: devISAN12Max.setDescription('Maximum ISA Bus -12V value (x100)')
devDCP12Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDCP12Val.setStatus('mandatory')
if mibBuilder.loadTexts: devDCP12Val.setDescription('Current Drive Connector +12V value (x100)')
devDCP12Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDCP12Min.setStatus('mandatory')
if mibBuilder.loadTexts: devDCP12Min.setDescription('Minimum Drive Connector +12V value (x100)')
devDCP12Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDCP12Max.setStatus('mandatory')
if mibBuilder.loadTexts: devDCP12Max.setDescription('Maximum Drive Connector +12V value (x100)')
devDCP5Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDCP5Val.setStatus('mandatory')
if mibBuilder.loadTexts: devDCP5Val.setDescription('Current Drive Connector +5V value (x100)')
devDCP5Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDCP5Min.setStatus('mandatory')
if mibBuilder.loadTexts: devDCP5Min.setDescription('Minimum Drive Connector +5V value (x100)')
devDCP5Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDCP5Max.setStatus('mandatory')
if mibBuilder.loadTexts: devDCP5Max.setDescription('Maximum Drive Connector +5V value (x100)')
fanErrors = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fanErrors.setStatus('mandatory')
if mibBuilder.loadTexts: fanErrors.setDescription('BITMASK - Enable Fan Errors, Bit 0=Fan1')
tempErrors = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempErrors.setStatus('mandatory')
if mibBuilder.loadTexts: tempErrors.setDescription('BITMASK - Enable Temp Errors, Bit 0=Temp1')
isaErrors = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isaErrors.setStatus('mandatory')
if mibBuilder.loadTexts: isaErrors.setDescription('BITMASK - Enable ISA Bus Errors, Bit 0=+12v')
dcErrors = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dcErrors.setDescription('BITMASK - Enable Drive Connector Bus Errors, Bit 0=+12v, 1=+5v')
inputPSU = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inputPSU.setStatus('mandatory')
if mibBuilder.loadTexts: inputPSU.setDescription('BITMASK - Treat Input switches as PSU Errors, Bit 0-1=Input1=PSU Error')
inputTamper = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inputTamper.setStatus('mandatory')
if mibBuilder.loadTexts: inputTamper.setDescription('BITMASK - Treat Input switches as Tamper Errors, Bit 0-1=Input1=Tamper Error')
enOutput0 = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enOutput0.setStatus('mandatory')
if mibBuilder.loadTexts: enOutput0.setDescription("BITMASK - Enable Outputs/LED's on errors - Bit 0=Power,1=Fan,2=Temp,3=PSU,4=Tamper,5=Watchdog.")
enOutput1 = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enOutput1.setStatus('mandatory')
if mibBuilder.loadTexts: enOutput1.setDescription("BITMASK - Enable Outputs/LED's on errors - Bit 0=Power,1=Fan,2=Temp,3=PSU,4=Tamper,5=Watchdog.")
enOutput2 = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enOutput2.setStatus('mandatory')
if mibBuilder.loadTexts: enOutput2.setDescription("BITMASK - Enable Outputs/LED's on errors - Bit 0=Power,1=Fan,2=Temp,3=PSU,4=Tamper,5=Watchdog.")
enOutput3 = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enOutput3.setStatus('mandatory')
if mibBuilder.loadTexts: enOutput3.setDescription("BITMASK - Enable Outputs/LED's on errors - Bit 0=Power,1=Fan,2=Temp,3=PSU,4=Tamper,5=Watchdog.")
enBeeper = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enBeeper.setStatus('mandatory')
if mibBuilder.loadTexts: enBeeper.setDescription('BITMASK - Enable Beeper on errors - Bit 0=Power,1=Fan,2=Temp,3=PSU,4=Tamper,5=Watchdog.')
enRelay = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enRelay.setStatus('mandatory')
if mibBuilder.loadTexts: enRelay.setDescription('BITMASK - Enable Relay on errors - Bit 0=Power,1=Fan,2=Temp,3=PSU,4=Tamper,5=Watchdog.')
enReset = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enReset.setStatus('mandatory')
if mibBuilder.loadTexts: enReset.setDescription('BITMASK - Enable Reset on errors - Bit 0=Power,1=Fan,2=Temp,3=PSU,4=Tamper,5=Watchdog.')
watchdog = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: watchdog.setStatus('mandatory')
if mibBuilder.loadTexts: watchdog.setDescription('Current Watchdog timeout left in seconds, 0=Disabled')
inputsAlert = NotificationType((1, 3, 6, 1, 4, 1, 3166, 1) + (0,0))
if mibBuilder.loadTexts: inputsAlert.setDescription('Trap generated if any of the Inputs are activated')
fanAlert = NotificationType((1, 3, 6, 1, 4, 1, 3166, 1) + (0,1))
if mibBuilder.loadTexts: fanAlert.setDescription('Trap generated if any Fan speeds are outside limits')
tempAlert = NotificationType((1, 3, 6, 1, 4, 1, 3166, 1) + (0,2))
if mibBuilder.loadTexts: tempAlert.setDescription('Trap generated if temperature exceeds limits')
isaAlert = NotificationType((1, 3, 6, 1, 4, 1, 3166, 1) + (0,3))
if mibBuilder.loadTexts: isaAlert.setDescription('Trap generated if ISA Bus voltages exceed limits')
dcAlert = NotificationType((1, 3, 6, 1, 4, 1, 3166, 1) + (0,4))
if mibBuilder.loadTexts: dcAlert.setDescription('Trap generated if disk connector voltages exceed limits')
mibBuilder.exportSymbols("GUARDIAN-MIB", devFan3=devFan3, control=control, devFan4Max=devFan4Max, devISAN5Min=devISAN5Min, devInp3Pol=devInp3Pol, devDCP12Min=devDCP12Min, tempErrors=tempErrors, enOutput1=enOutput1, devTemp4Val=devTemp4Val, devFan2Val=devFan2Val, devFan=devFan, devTemp3Max=devTemp3Max, devTemp8Max=devTemp8Max, devDCP5Val=devDCP5Val, devTemp6Max=devTemp6Max, devISAN12Val=devISAN12Val, devISAP12Max=devISAP12Max, devFan3Min=devFan3Min, devDCP12Val=devDCP12Val, devTemp7Val=devTemp7Val, devISAP12=devISAP12, devTemp7Max=devTemp7Max, guardian=guardian, devISAP5Min=devISAP5Min, devTemp5Val=devTemp5Val, devInp3Val=devInp3Val, devTemp2=devTemp2, devTemp7=devTemp7, devDCP5=devDCP5, devTemp1Val=devTemp1Val, devDCP12=devDCP12, devInp2Pol=devInp2Pol, devISAN5Max=devISAN5Max, inputsAlert=inputsAlert, devFan4=devFan4, tempAlert=tempAlert, device=device, devInp4Pol=devInp4Pol, westek=westek, devISAN12Min=devISAN12Min, devISAP5=devISAP5, devTemp1=devTemp1, devTemp3Min=devTemp3Min, devISAN5=devISAN5, devFan1Max=devFan1Max, devISAN5Val=devISAN5Val, enOutput3=enOutput3, fanAlert=fanAlert, devTemp3=devTemp3, watchdog=watchdog, enRelay=enRelay, devInp1Val=devInp1Val, devDCP5Min=devDCP5Min, enOutput0=enOutput0, devTemp2Val=devTemp2Val, devISA=devISA, enOutput2=enOutput2, enReset=enReset, devTemp5=devTemp5, devInpStat=devInpStat, devFan2Max=devFan2Max, devTemp2Max=devTemp2Max, devInp4Val=devInp4Val, devISAP5Val=devISAP5Val, enBeeper=enBeeper, devFan3Val=devFan3Val, devInp2Val=devInp2Val, devTemp5Max=devTemp5Max, devFan2Min=devFan2Min, devInput4=devInput4, devISAP12Min=devISAP12Min, devTemp6Min=devTemp6Min, devTemp5Min=devTemp5Min, devDCP5Max=devDCP5Max, devInp1Pol=devInp1Pol, devTempStat=devTempStat, devTemp6=devTemp6, devDCStat=devDCStat, devTemp4=devTemp4, devFan3Max=devFan3Max, devISAP12Val=devISAP12Val, devFan1=devFan1, devISAStat=devISAStat, dcAlert=dcAlert, devFanStat=devFanStat, devTemp2Min=devTemp2Min, special=special, devDC=devDC, devTemp1Max=devTemp1Max, devTemp7Min=devTemp7Min, devFan1Min=devFan1Min, devFan1Val=devFan1Val, isaAlert=isaAlert, isaErrors=isaErrors, devTemp8Min=devTemp8Min, devInput3=devInput3, inputTamper=inputTamper, devInput2=devInput2, devTemp6Val=devTemp6Val, devTemp3Val=devTemp3Val, masks=masks, devTemp8=devTemp8, devFan4Val=devFan4Val, fanErrors=fanErrors, devInput=devInput, devDCP12Max=devDCP12Max, devTemp1Min=devTemp1Min, devISAN12Max=devISAN12Max, devTemp4Min=devTemp4Min, inputPSU=inputPSU, devTemp4Max=devTemp4Max, devTemp8Val=devTemp8Val, devISAN12=devISAN12, guardianRev=guardianRev, dcErrors=dcErrors, devFan2=devFan2, devISAP5Max=devISAP5Max, devTemp=devTemp, devFan4Min=devFan4Min, devInput1=devInput1)
