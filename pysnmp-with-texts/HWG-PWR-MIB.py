#
# PySNMP MIB module HWG-PWR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HWG-PWR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
NotificationType, Integer32, Counter32, Counter64, Unsigned32, NotificationType, IpAddress, MibIdentifier, Bits, enterprises, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter32", "Counter64", "Unsigned32", "NotificationType", "IpAddress", "MibIdentifier", "Bits", "enterprises", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Gauge32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Txt8(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 8)

class Txt16(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class SensorValue(Integer32):
    pass

class SensorID(Integer32):
    pass

class OpenClose(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("open", 0), ("close", 1))

class AlarmState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("invalid", 0), ("normal", 1), ("alarm", 2))

hwgroup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796))
x390 = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4))
hwgpwr = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 6))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 6, 70))
meters = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1))
input = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2))
infoAddressMAC = MibScalar((1, 3, 6, 1, 4, 1, 21796, 4, 6, 70, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: infoAddressMAC.setStatus('mandatory')
if mibBuilder.loadTexts: infoAddressMAC.setDescription('MAC address in text form. It is here to distinguish devices in trap messages.')
mtNumber = MibScalar((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtNumber.setStatus('mandatory')
if mibBuilder.loadTexts: mtNumber.setDescription('Pocet pripojenych M-BUS meridel')
mtTableMeters = MibTable((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2), )
if mibBuilder.loadTexts: mtTableMeters.setStatus('mandatory')
if mibBuilder.loadTexts: mtTableMeters.setDescription('A unique value for each meter.')
mtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1), ).setIndexNames((0, "HWG-PWR-MIB", "mtIndex"))
if mibBuilder.loadTexts: mtEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mtEntry.setDescription('An entry containing information applicable to a particular sensor.')
mtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mtIndex.setDescription('The sensor index.')
mtName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 2), Txt16()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtName.setStatus('mandatory')
if mibBuilder.loadTexts: mtName.setDescription('Jmeno merice.')
mtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 3), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtAddr.setStatus('mandatory')
if mibBuilder.loadTexts: mtAddr.setDescription('Primarni adresa.')
mtSecAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtSecAddr.setStatus('mandatory')
if mibBuilder.loadTexts: mtSecAddr.setDescription('Sekundarni adresa.')
mtValNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 5), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtValNumber.setStatus('mandatory')
if mibBuilder.loadTexts: mtValNumber.setDescription('Pocet merenych hodnot merice.')
mtvalTableValues = MibTable((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3), )
if mibBuilder.loadTexts: mtvalTableValues.setStatus('mandatory')
if mibBuilder.loadTexts: mtvalTableValues.setDescription('A unique value for each meter.')
mtvalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1), ).setIndexNames((0, "HWG-PWR-MIB", "mtvalIndex"))
if mibBuilder.loadTexts: mtvalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mtvalEntry.setDescription('An entry containing information applicable to a particular sensor.')
mtvalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtvalIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mtvalIndex.setDescription('The sensor index.')
mtvalName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 2), Txt16()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtvalName.setStatus('mandatory')
if mibBuilder.loadTexts: mtvalName.setDescription('Jmeno parametru.')
mtvalUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 3), Txt8()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtvalUnit.setStatus('mandatory')
if mibBuilder.loadTexts: mtvalUnit.setDescription('Jednotka parametru.')
mtvalTarif = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtvalTarif.setStatus('mandatory')
if mibBuilder.loadTexts: mtvalTarif.setDescription('Tarif parametru.')
mtvalExp = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 5), PositiveInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtvalExp.setStatus('mandatory')
if mibBuilder.loadTexts: mtvalExp.setDescription('Exponent parametru.')
mtvalMbusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 6), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtvalMbusValue.setStatus('mandatory')
if mibBuilder.loadTexts: mtvalMbusValue.setDescription('Aktualni hodnota prarametru v ciselnem formatu. Hodnota bez exponentu a ZeroOffsetu')
mtvalTxtValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 7), Txt8()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtvalTxtValue.setStatus('mandatory')
if mibBuilder.loadTexts: mtvalTxtValue.setDescription('Aktualni hodnota prarametru v textovem formatu. Hodnota se zapocitanym exponentm')
mtvalAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 8), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtvalAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: mtvalAlarmState.setDescription('Value Alarm State')
mtvalZeroOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtvalZeroOffset.setStatus('mandatory')
if mibBuilder.loadTexts: mtvalZeroOffset.setDescription('Value Zero Offset.')
inpNumber = MibScalar((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpNumber.setStatus('mandatory')
if mibBuilder.loadTexts: inpNumber.setDescription('Number of Input Dry Contacts')
inpTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2), )
if mibBuilder.loadTexts: inpTable.setStatus('mandatory')
if mibBuilder.loadTexts: inpTable.setDescription('A list of binary input entries.')
inpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1), ).setIndexNames((0, "HWG-PWR-MIB", "inpIndex"))
if mibBuilder.loadTexts: inpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: inpEntry.setDescription('An entry containing information applicable to a particular binary input.')
inpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpIndex.setStatus('mandatory')
if mibBuilder.loadTexts: inpIndex.setDescription('The binary input index.')
inpName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 2), Txt16()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inpName.setStatus('mandatory')
if mibBuilder.loadTexts: inpName.setDescription('The binary input name.')
inpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 3), OpenClose()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpValue.setStatus('mandatory')
if mibBuilder.loadTexts: inpValue.setDescription('The binary input value.')
inpValueName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 4), Txt8()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpValueName.setStatus('mandatory')
if mibBuilder.loadTexts: inpValueName.setDescription('The binary input name.')
inpAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 5), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: inpAlarmState.setDescription('The binary input alarm state.')
pwrStateToAlarm = NotificationType((1, 3, 6, 1, 4, 1, 21796, 4, 6) + (0,1)).setObjects(("HWG-PWR-MIB", "mtvalIndex"), ("HWG-PWR-MIB", "mtvalName"), ("HWG-PWR-MIB", "mtvalUnit"), ("HWG-PWR-MIB", "mtvalTarif"), ("HWG-PWR-MIB", "mtvalExp"), ("HWG-PWR-MIB", "mtvalValue"), ("HWG-PWR-MIB", "mtvalTxtValue"), ("HWG-PWR-MIB", "mtvalAlarmState"))
if mibBuilder.loadTexts: pwrStateToAlarm.setDescription('Value changed to Alarm state.')
pwrStateToNormal = NotificationType((1, 3, 6, 1, 4, 1, 21796, 4, 6) + (0,2)).setObjects(("HWG-PWR-MIB", "mtvalIndex"), ("HWG-PWR-MIB", "mtvalName"), ("HWG-PWR-MIB", "mtvalUnit"), ("HWG-PWR-MIB", "mtvalTarif"), ("HWG-PWR-MIB", "mtvalExp"), ("HWG-PWR-MIB", "mtvalValue"), ("HWG-PWR-MIB", "mtvalTxtValue"), ("HWG-PWR-MIB", "mtvalAlarmState"))
if mibBuilder.loadTexts: pwrStateToNormal.setDescription('Value changed to Normal state.')
inContactStateToAlarm = NotificationType((1, 3, 6, 1, 4, 1, 21796, 4, 6) + (0,3)).setObjects(("SNMPv2-MIB", "sysName"), ("HWG-PWR-MIB", "infoAddressMAC"), ("HWG-PWR-MIB", "inpIndex"), ("HWG-PWR-MIB", "inpName"), ("HWG-PWR-MIB", "inpValue"), ("HWG-PWR-MIB", "inpValueName"), ("HWG-PWR-MIB", "inpAlarmState"))
if mibBuilder.loadTexts: inContactStateToAlarm.setDescription('Input Dry Contact to Alarm state.')
inContactStateToNormal = NotificationType((1, 3, 6, 1, 4, 1, 21796, 4, 6) + (0,4)).setObjects(("SNMPv2-MIB", "sysName"), ("HWG-PWR-MIB", "infoAddressMAC"), ("HWG-PWR-MIB", "inpIndex"), ("HWG-PWR-MIB", "inpName"), ("HWG-PWR-MIB", "inpValue"), ("HWG-PWR-MIB", "inpValueName"), ("HWG-PWR-MIB", "inpAlarmState"))
if mibBuilder.loadTexts: inContactStateToNormal.setDescription('Input Dry Contact to Normal state.')
mibBuilder.exportSymbols("HWG-PWR-MIB", mtvalMbusValue=mtvalMbusValue, mtvalAlarmState=mtvalAlarmState, mtvalName=mtvalName, mtvalTxtValue=mtvalTxtValue, mtTableMeters=mtTableMeters, inpValueName=inpValueName, mtvalUnit=mtvalUnit, mtIndex=mtIndex, hwgroup=hwgroup, mtvalTableValues=mtvalTableValues, inpEntry=inpEntry, pwrStateToNormal=pwrStateToNormal, Txt8=Txt8, mtAddr=mtAddr, inpValue=inpValue, info=info, inpIndex=inpIndex, mtvalExp=mtvalExp, SensorID=SensorID, mtvalEntry=mtvalEntry, inpAlarmState=inpAlarmState, mtvalTarif=mtvalTarif, SensorValue=SensorValue, inpTable=inpTable, mtNumber=mtNumber, mtSecAddr=mtSecAddr, AlarmState=AlarmState, inContactStateToNormal=inContactStateToNormal, PositiveInteger=PositiveInteger, pwrStateToAlarm=pwrStateToAlarm, hwgpwr=hwgpwr, inpName=inpName, mtValNumber=mtValNumber, mtvalIndex=mtvalIndex, input=input, x390=x390, mtName=mtName, inpNumber=inpNumber, meters=meters, mtvalZeroOffset=mtvalZeroOffset, mtEntry=mtEntry, Txt16=Txt16, OpenClose=OpenClose, infoAddressMAC=infoAddressMAC, inContactStateToAlarm=inContactStateToAlarm)
