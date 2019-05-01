#
# PySNMP MIB module LANADPTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANADPTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:05:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, enterprises, NotificationType, ModuleIdentity, ObjectIdentity, Bits, IpAddress, Counter64, Unsigned32, MibIdentifier, Counter32, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Bits", "IpAddress", "Counter64", "Unsigned32", "MibIdentifier", "Counter32", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

comet = MibIdentifier((1, 3, 6, 1, 4, 1, 22626))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1))
lanadapter = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1))
channels = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2))
channel1 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 1))
channel2 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 2))
channel3 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 3))
channel4 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 4))
channel5 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 5))
channel6 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 6))
messageString = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageString.setStatus('mandatory')
if mibBuilder.loadTexts: messageString.setDescription('Message giving more detailed information on alarms.')
channelAlarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: channelAlarm.setDescription('Alarm on Channel is Occured. 0 - No alarm, 1 - Alarm. ')
memmory90Full = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: memmory90Full.setStatus('mandatory')
if mibBuilder.loadTexts: memmory90Full.setDescription('Logger memmory is from 90% full. 0 - No alarm, 1 - Alarm.')
memmory100Full = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: memmory100Full.setStatus('mandatory')
if mibBuilder.loadTexts: memmory100Full.setDescription('Logger memmory is 100% full. 0 - No alarm, 1 - Alarm.')
vccLow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vccLow.setStatus('mandatory')
if mibBuilder.loadTexts: vccLow.setDescription('Vcc is low. 0 - No alarm, 1 - Alarm.')
batteryEnd = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: batteryEnd.setStatus('mandatory')
if mibBuilder.loadTexts: batteryEnd.setDescription('Calculated battery livetime is over. 0 - No alarm, 1 - Alarm.')
batteryLow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: batteryLow.setStatus('mandatory')
if mibBuilder.loadTexts: batteryLow.setDescription('Battery voltage is too low. 0 - No alarm, 1 - Alarm.')
communicationError = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: communicationError.setStatus('mandatory')
if mibBuilder.loadTexts: communicationError.setDescription('Communication with Logger failed. 0 - OK, 1 - Alarm.')
loggerOff = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loggerOff.setStatus('mandatory')
if mibBuilder.loadTexts: loggerOff.setDescription('Logger is Off. 0 - Logger is on; 1 - Logger is off')
ch1Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1Alarm.setStatus('mandatory')
if mibBuilder.loadTexts: ch1Alarm.setDescription('Alarm on channel 1; 0 - No alarm, 1 - Alarm.')
ch2Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch2Alarm.setStatus('mandatory')
if mibBuilder.loadTexts: ch2Alarm.setDescription('Alarm on channel 2; 0 - No alarm, 1 - Alarm.')
ch3Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch3Alarm.setStatus('mandatory')
if mibBuilder.loadTexts: ch3Alarm.setDescription('Alarm on channel 3; 0 - No alarm, 1 - Alarm.')
ch4Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch4Alarm.setStatus('mandatory')
if mibBuilder.loadTexts: ch4Alarm.setDescription('Alarm on channel 4; 0 - No alarm, 1 - Alarm.')
ch5Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch5Alarm.setStatus('mandatory')
if mibBuilder.loadTexts: ch5Alarm.setDescription('Alarm on channel 5; 0 - No alarm, 1 - Alarm.')
ch6Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch6Alarm.setStatus('mandatory')
if mibBuilder.loadTexts: ch6Alarm.setDescription('Alarm on channel 6; 0 - No alarm, 1 - Alarm.')
mibBuilder.exportSymbols("LANADPTER-MIB", traps=traps, loggerOff=loggerOff, channel3=channel3, channel2=channel2, channel6=channel6, ch3Alarm=ch3Alarm, products=products, channel5=channel5, communicationError=communicationError, ch5Alarm=ch5Alarm, ch1Alarm=ch1Alarm, ch6Alarm=ch6Alarm, messageString=messageString, channelAlarm=channelAlarm, channel4=channel4, memmory100Full=memmory100Full, ch4Alarm=ch4Alarm, batteryLow=batteryLow, memmory90Full=memmory90Full, DisplayString=DisplayString, comet=comet, vccLow=vccLow, ch2Alarm=ch2Alarm, lanadapter=lanadapter, channels=channels, batteryEnd=batteryEnd, channel1=channel1)
