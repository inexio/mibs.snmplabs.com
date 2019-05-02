#
# PySNMP MIB module P8541-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/P8541-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:36:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, Counter64, MibIdentifier, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, enterprises, ObjectIdentity, iso, Counter32, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "Counter64", "MibIdentifier", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "enterprises", "ObjectIdentity", "iso", "Counter32", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

comet = MibIdentifier((1, 3, 6, 1, 4, 1, 22626))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1))
p8541 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5))
settings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 1))
channels = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2))
channel1 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1))
channel2 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2))
channel3 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3))
channel4 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 3))
tables = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 4))
sensorName = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorName.setStatus('mandatory')
if mibBuilder.loadTexts: sensorName.setDescription('Sensor name.')
ch1Name = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1Name.setStatus('mandatory')
if mibBuilder.loadTexts: ch1Name.setDescription('Channel 1 name.')
ch1Val = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1Val.setStatus('mandatory')
if mibBuilder.loadTexts: ch1Val.setDescription('Channel 1 temperature.')
ch1IntVal = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-550, 1250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1IntVal.setStatus('mandatory')
if mibBuilder.loadTexts: ch1IntVal.setDescription('Channel 1 temperature * 10 (12,5 dgr C = 125).')
ch1Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1Alarm.setStatus('mandatory')
if mibBuilder.loadTexts: ch1Alarm.setDescription('Alarm on channel 1; 0 - No alarm, 1 - Alarm Hi, 2- Alarm Lo.')
ch1LimHi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1LimHi.setStatus('mandatory')
if mibBuilder.loadTexts: ch1LimHi.setDescription('Channel 1 temperature upper alarm limit.')
ch1LimLo = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1LimLo.setStatus('mandatory')
if mibBuilder.loadTexts: ch1LimLo.setDescription('Channel 1 temperature low alarm limit.')
ch1LimHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1LimHyst.setStatus('mandatory')
if mibBuilder.loadTexts: ch1LimHyst.setDescription('Channel 1 temperature hysteressis.')
ch1Delay = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1Delay.setStatus('mandatory')
if mibBuilder.loadTexts: ch1Delay.setDescription('Channel 1 temperature alarm delay [s].')
ch2Name = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch2Name.setStatus('mandatory')
if mibBuilder.loadTexts: ch2Name.setDescription('Channel 2 name.')
ch2Val = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch2Val.setStatus('mandatory')
if mibBuilder.loadTexts: ch2Val.setDescription('Channel 2 temperature.')
ch2IntVal = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-550, 1250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch2IntVal.setStatus('mandatory')
if mibBuilder.loadTexts: ch2IntVal.setDescription('Channel 2 temperature * 10 (12,5 dgr C = 125).')
ch2Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch2Alarm.setStatus('mandatory')
if mibBuilder.loadTexts: ch2Alarm.setDescription('Alarm on channel 2; 0 - No alarm, 1 - Alarm Hi, 2- Alarm Lo.')
ch2LimHi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch2LimHi.setStatus('mandatory')
if mibBuilder.loadTexts: ch2LimHi.setDescription('Channel 2 temperature upper alarm limit.')
ch2LimLo = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch2LimLo.setStatus('mandatory')
if mibBuilder.loadTexts: ch2LimLo.setDescription('Channel 2 temperature low alarm limit.')
ch2LimHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch2LimHyst.setStatus('mandatory')
if mibBuilder.loadTexts: ch2LimHyst.setDescription('Channel 2 temperature hysteressis.')
ch2Delay = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch2Delay.setStatus('mandatory')
if mibBuilder.loadTexts: ch2Delay.setDescription('Channel 2 temperature alarm delay [s].')
ch3Name = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch3Name.setStatus('mandatory')
if mibBuilder.loadTexts: ch3Name.setDescription('Channel 3 name.')
ch3Val = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch3Val.setStatus('mandatory')
if mibBuilder.loadTexts: ch3Val.setDescription('Channel 3 temperature.')
ch3IntVal = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-550, 1250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch3IntVal.setStatus('mandatory')
if mibBuilder.loadTexts: ch3IntVal.setDescription('Channel 3 temperature * 10 (12,5 dgr C = 125).')
ch3Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch3Alarm.setStatus('mandatory')
if mibBuilder.loadTexts: ch3Alarm.setDescription('Alarm on channel 3; 0 - No alarm, 1 - Alarm Hi, 2- Alarm Lo.')
ch3LimHi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch3LimHi.setStatus('mandatory')
if mibBuilder.loadTexts: ch3LimHi.setDescription('Channel 3 temperature upper alarm limit.')
ch3LimLo = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch3LimLo.setStatus('mandatory')
if mibBuilder.loadTexts: ch3LimLo.setDescription('Channel 3 temperature low alarm limit.')
ch3LimHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch3LimHyst.setStatus('mandatory')
if mibBuilder.loadTexts: ch3LimHyst.setDescription('Channel 3 temperature hysteressis.')
ch3Delay = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch3Delay.setStatus('mandatory')
if mibBuilder.loadTexts: ch3Delay.setDescription('Channel 3 temperature alarm delay [s].')
ch4Name = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch4Name.setStatus('mandatory')
if mibBuilder.loadTexts: ch4Name.setDescription('Channel 4 name.')
ch4Val = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch4Val.setStatus('mandatory')
if mibBuilder.loadTexts: ch4Val.setDescription('Channel 4 temperature.')
ch4IntVal = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-550, 1250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch4IntVal.setStatus('mandatory')
if mibBuilder.loadTexts: ch4IntVal.setDescription('Channel 4 temperature * 10 (12,5 dgr C = 125).')
ch4Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch4Alarm.setStatus('mandatory')
if mibBuilder.loadTexts: ch4Alarm.setDescription('Alarm on channel 4; 0 - No alarm, 1 - Alarm Hi, 2- Alarm Lo.')
ch4LimHi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch4LimHi.setStatus('mandatory')
if mibBuilder.loadTexts: ch4LimHi.setDescription('Channel 4 temperature upper alarm limit.')
ch4LimLo = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch4LimLo.setStatus('mandatory')
if mibBuilder.loadTexts: ch4LimLo.setDescription('Channel 4 temperature low alarm limit.')
ch4LimHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch4LimHyst.setStatus('mandatory')
if mibBuilder.loadTexts: ch4LimHyst.setDescription('Channel 4 temperature hysteressis.')
ch4Delay = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch4Delay.setStatus('mandatory')
if mibBuilder.loadTexts: ch4Delay.setDescription('Channel 4 temperature alarm delay [s].')
messageString = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageString.setStatus('mandatory')
if mibBuilder.loadTexts: messageString.setDescription('Message giving more detailed information on alarms.')
historyTable = MibTable((1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1), )
if mibBuilder.loadTexts: historyTable.setStatus('mandatory')
if mibBuilder.loadTexts: historyTable.setDescription('Table of the history values.')
historyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1), ).setIndexNames((0, "P8541-MIB", "ch1temperature"))
if mibBuilder.loadTexts: historyEntry.setStatus('optional')
if mibBuilder.loadTexts: historyEntry.setDescription('History values entries.')
ch1temperature = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1temperature.setStatus('mandatory')
if mibBuilder.loadTexts: ch1temperature.setDescription('Temperature reading.')
ch2temperature = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch2temperature.setStatus('mandatory')
if mibBuilder.loadTexts: ch2temperature.setDescription('Humidity reading.')
ch3temperature = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch3temperature.setStatus('mandatory')
if mibBuilder.loadTexts: ch3temperature.setDescription('Computed value reading.')
ch4temperature = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch4temperature.setStatus('mandatory')
if mibBuilder.loadTexts: ch4temperature.setDescription('Pressure reading.')
mibBuilder.exportSymbols("P8541-MIB", DisplayString=DisplayString, ch1Val=ch1Val, ch2Name=ch2Name, ch2Delay=ch2Delay, ch3Val=ch3Val, channels=channels, channel2=channel2, ch4temperature=ch4temperature, ch4Alarm=ch4Alarm, ch2Alarm=ch2Alarm, ch4LimHyst=ch4LimHyst, ch1Alarm=ch1Alarm, ch1LimHyst=ch1LimHyst, ch3LimLo=ch3LimLo, ch1Name=ch1Name, historyEntry=historyEntry, ch4LimLo=ch4LimLo, ch3Alarm=ch3Alarm, ch3LimHi=ch3LimHi, ch4Delay=ch4Delay, ch3Name=ch3Name, channel4=channel4, historyTable=historyTable, messageString=messageString, tables=tables, channel1=channel1, settings=settings, ch4Val=ch4Val, ch2temperature=ch2temperature, comet=comet, p8541=p8541, ch1LimHi=ch1LimHi, ch2LimLo=ch2LimLo, ch1IntVal=ch1IntVal, ch4LimHi=ch4LimHi, ch2Val=ch2Val, sensorName=sensorName, products=products, ch1temperature=ch1temperature, ch4IntVal=ch4IntVal, ch3LimHyst=ch3LimHyst, ch3temperature=ch3temperature, ch1LimLo=ch1LimLo, ch3IntVal=ch3IntVal, ch4Name=ch4Name, ch2IntVal=ch2IntVal, ch2LimHi=ch2LimHi, channel3=channel3, ch1Delay=ch1Delay, ch3Delay=ch3Delay, ch2LimHyst=ch2LimHyst, traps=traps)