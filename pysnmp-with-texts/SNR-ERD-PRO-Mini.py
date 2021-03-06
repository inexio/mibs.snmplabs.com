#
# PySNMP MIB module SNR-ERD-PRO-Mini (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNR-ERD-PRO-Mini
# Produced by pysmi-0.3.4 at Wed May  1 15:08:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, IpAddress, Gauge32, Counter64, Integer32, Unsigned32, Counter32, Bits, MibIdentifier, ObjectIdentity, iso, TimeTicks, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "IpAddress", "Gauge32", "Counter64", "Integer32", "Unsigned32", "Counter32", "Bits", "MibIdentifier", "ObjectIdentity", "iso", "TimeTicks", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snr = ModuleIdentity((1, 3, 6, 1, 4, 1, 40418))
snr.setRevisions(('2015-04-29 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snr.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: snr.setLastUpdated('201504291200Z')
if mibBuilder.loadTexts: snr.setOrganization('NAG ')
if mibBuilder.loadTexts: snr.setContactInfo('erd@nag.ru')
if mibBuilder.loadTexts: snr.setDescription('The MIB module for SNR-ERD')
snr_erd = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2)).setLabel("snr-erd")
snr_erd_pro_mini = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5)).setLabel("snr-erd-pro-mini")
measurements = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1))
sensesstate = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 2))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 3))
counters = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 8))
options = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 10))
snrSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1))
temperatureSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1))
powerSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2))
alarmSensCnts = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 8, 2))
erdproMiniTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0))
voltageSensor = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageSensor.setStatus('current')
if mibBuilder.loadTexts: voltageSensor.setDescription('qwerty')
serialS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS1.setStatus('current')
if mibBuilder.loadTexts: serialS1.setDescription('qwerty')
serialS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS2.setStatus('current')
if mibBuilder.loadTexts: serialS2.setDescription('qwerty')
serialS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS3.setStatus('current')
if mibBuilder.loadTexts: serialS3.setDescription('qwerty')
serialS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS4.setStatus('current')
if mibBuilder.loadTexts: serialS4.setDescription('qwerty')
serialS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS5.setStatus('current')
if mibBuilder.loadTexts: serialS5.setDescription('qwerty')
serialS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 15), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS6.setStatus('current')
if mibBuilder.loadTexts: serialS6.setDescription('qwerty')
serialS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS7.setStatus('current')
if mibBuilder.loadTexts: serialS7.setDescription('qwerty')
serialS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 17), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS8.setStatus('current')
if mibBuilder.loadTexts: serialS8.setDescription('qwerty')
serialS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS9.setStatus('current')
if mibBuilder.loadTexts: serialS9.setDescription('qwerty')
serialS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS10.setStatus('current')
if mibBuilder.loadTexts: serialS10.setDescription('qwerty')
temperatureS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS1.setStatus('current')
if mibBuilder.loadTexts: temperatureS1.setDescription('qwerty')
temperatureS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS2.setStatus('current')
if mibBuilder.loadTexts: temperatureS2.setDescription('qwerty')
temperatureS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS3.setStatus('current')
if mibBuilder.loadTexts: temperatureS3.setDescription('qwerty')
temperatureS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS4.setStatus('current')
if mibBuilder.loadTexts: temperatureS4.setDescription('qwerty')
temperatureS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS5.setStatus('current')
if mibBuilder.loadTexts: temperatureS5.setDescription('qwerty')
temperatureS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS6.setStatus('current')
if mibBuilder.loadTexts: temperatureS6.setDescription('qwerty')
temperatureS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS7.setStatus('current')
if mibBuilder.loadTexts: temperatureS7.setDescription('qwerty')
temperatureS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS8.setStatus('current')
if mibBuilder.loadTexts: temperatureS8.setDescription('qwerty')
temperatureS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS9.setStatus('current')
if mibBuilder.loadTexts: temperatureS9.setDescription('qwerty')
temperatureS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS10.setStatus('current')
if mibBuilder.loadTexts: temperatureS10.setDescription('qwerty')
voltageS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS1.setStatus('current')
if mibBuilder.loadTexts: voltageS1.setDescription('qwerty')
currentS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS1.setStatus('current')
if mibBuilder.loadTexts: currentS1.setDescription('qwerty')
voltageS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS2.setStatus('current')
if mibBuilder.loadTexts: voltageS2.setDescription('qwerty')
currentS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS2.setStatus('current')
if mibBuilder.loadTexts: currentS2.setDescription('qwerty')
voltageS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS3.setStatus('current')
if mibBuilder.loadTexts: voltageS3.setDescription('qwerty')
currentS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS3.setStatus('current')
if mibBuilder.loadTexts: currentS3.setDescription('qwerty')
voltageS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS4.setStatus('current')
if mibBuilder.loadTexts: voltageS4.setDescription('qwerty')
currentS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS4.setStatus('current')
if mibBuilder.loadTexts: currentS4.setDescription('qwerty')
voltageS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS5.setStatus('current')
if mibBuilder.loadTexts: voltageS5.setDescription('qwerty')
currentS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS5.setStatus('current')
if mibBuilder.loadTexts: currentS5.setDescription('qwerty')
voltageS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS6.setStatus('current')
if mibBuilder.loadTexts: voltageS6.setDescription('qwerty')
currentS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS6.setStatus('current')
if mibBuilder.loadTexts: currentS6.setDescription('qwerty')
voltageS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS7.setStatus('current')
if mibBuilder.loadTexts: voltageS7.setDescription('qwerty')
currentS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS7.setStatus('current')
if mibBuilder.loadTexts: currentS7.setDescription('qwerty')
voltageS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS8.setStatus('current')
if mibBuilder.loadTexts: voltageS8.setDescription('qwerty')
currentS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS8.setStatus('current')
if mibBuilder.loadTexts: currentS8.setDescription('qwerty')
voltageS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS9.setStatus('current')
if mibBuilder.loadTexts: voltageS9.setDescription('qwerty')
currentS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS9.setStatus('current')
if mibBuilder.loadTexts: currentS9.setDescription('qwerty')
voltageS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS10.setStatus('current')
if mibBuilder.loadTexts: voltageS10.setDescription('qwerty')
currentS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS10.setStatus('current')
if mibBuilder.loadTexts: currentS10.setDescription('qwerty')
alarmSensor1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("high", 1), ("low", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSensor1.setStatus('current')
if mibBuilder.loadTexts: alarmSensor1.setDescription('qwerty')
alarmSensor2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("high", 1), ("low", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSensor2.setStatus('current')
if mibBuilder.loadTexts: alarmSensor2.setDescription('qwerty')
uSensor = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("no", 1), ("yes", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uSensor.setStatus('current')
if mibBuilder.loadTexts: uSensor.setDescription('qwerty')
smart1State = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 0), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart1State.setStatus('current')
if mibBuilder.loadTexts: smart1State.setDescription('qwerty')
smart2State = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 0), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart2State.setStatus('current')
if mibBuilder.loadTexts: smart2State.setDescription('qwerty')
smart1ResetTime = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 3, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart1ResetTime.setStatus('current')
if mibBuilder.loadTexts: smart1ResetTime.setDescription('qwerty')
smart2ResetTime = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 3, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart2ResetTime.setStatus('current')
if mibBuilder.loadTexts: smart2ResetTime.setDescription('qwerty')
alarmSensor1cnt = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 8, 2, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSensor1cnt.setStatus('current')
if mibBuilder.loadTexts: alarmSensor1cnt.setDescription('qwerty')
alarmSensor2cnt = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 8, 2, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSensor2cnt.setStatus('current')
if mibBuilder.loadTexts: alarmSensor2cnt.setDescription('qwerty')
dataType = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("integer", 0), ("float", 1), ("ufloat", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataType.setStatus('current')
if mibBuilder.loadTexts: dataType.setDescription('qwerty')
aSense1Alarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 1))
if mibBuilder.loadTexts: aSense1Alarm.setStatus('current')
if mibBuilder.loadTexts: aSense1Alarm.setDescription('Check the text of message')
aSense1Release = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 2))
if mibBuilder.loadTexts: aSense1Release.setStatus('current')
if mibBuilder.loadTexts: aSense1Release.setDescription('Check the text of message')
aSense2Alarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 3))
if mibBuilder.loadTexts: aSense2Alarm.setStatus('current')
if mibBuilder.loadTexts: aSense2Alarm.setDescription('Check the text of message')
aSense2Release = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 4))
if mibBuilder.loadTexts: aSense2Release.setStatus('current')
if mibBuilder.loadTexts: aSense2Release.setDescription('Check the text of message')
uSenseAlarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 9))
if mibBuilder.loadTexts: uSenseAlarm.setStatus('current')
if mibBuilder.loadTexts: uSenseAlarm.setDescription('Check the text of message')
uSenseRelease = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 10))
if mibBuilder.loadTexts: uSenseRelease.setStatus('current')
if mibBuilder.loadTexts: uSenseRelease.setDescription('Check the text of message')
smart1ThermoOn = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 13))
if mibBuilder.loadTexts: smart1ThermoOn.setStatus('current')
if mibBuilder.loadTexts: smart1ThermoOn.setDescription('Check the text of message')
smart1ThermoOff = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 14))
if mibBuilder.loadTexts: smart1ThermoOff.setStatus('current')
if mibBuilder.loadTexts: smart1ThermoOff.setDescription('Check the text of message')
smart2ThermoOn = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 15))
if mibBuilder.loadTexts: smart2ThermoOn.setStatus('current')
if mibBuilder.loadTexts: smart2ThermoOn.setDescription('Check the text of message')
smart2ThermoOff = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 16))
if mibBuilder.loadTexts: smart2ThermoOff.setStatus('current')
if mibBuilder.loadTexts: smart2ThermoOff.setDescription('Check the text of message')
tempSensorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 29))
if mibBuilder.loadTexts: tempSensorAlarm.setStatus('current')
if mibBuilder.loadTexts: tempSensorAlarm.setDescription('Check the text of message')
tempSensorRelease = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 30))
if mibBuilder.loadTexts: tempSensorRelease.setStatus('current')
if mibBuilder.loadTexts: tempSensorRelease.setDescription('Check the text of message')
voltSensorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 31))
if mibBuilder.loadTexts: voltSensorAlarm.setStatus('current')
if mibBuilder.loadTexts: voltSensorAlarm.setDescription('Check the text of message')
voltSensorRelease = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 32))
if mibBuilder.loadTexts: voltSensorRelease.setStatus('current')
if mibBuilder.loadTexts: voltSensorRelease.setDescription('Check the text of message')
task1Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 36))
if mibBuilder.loadTexts: task1Done.setStatus('current')
if mibBuilder.loadTexts: task1Done.setDescription('Check the text of message')
task2Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 37))
if mibBuilder.loadTexts: task2Done.setStatus('current')
if mibBuilder.loadTexts: task2Done.setDescription('Check the text of message')
task3Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 38))
if mibBuilder.loadTexts: task3Done.setStatus('current')
if mibBuilder.loadTexts: task3Done.setDescription('Check the text of message')
task4Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 39))
if mibBuilder.loadTexts: task4Done.setStatus('current')
if mibBuilder.loadTexts: task4Done.setDescription('Check the text of message')
pingLost = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 45))
if mibBuilder.loadTexts: pingLost.setStatus('current')
if mibBuilder.loadTexts: pingLost.setDescription('Check the text of message')
batteryChargeLow = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 47))
if mibBuilder.loadTexts: batteryChargeLow.setStatus('current')
if mibBuilder.loadTexts: batteryChargeLow.setDescription('Check the text of message')
erdProMiniTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 40418, 2, 5, 99)).setObjects(("SNR-ERD-PRO-Mini", "aSense1Alarm"), ("SNR-ERD-PRO-Mini", "aSense1Release"), ("SNR-ERD-PRO-Mini", "aSense2Alarm"), ("SNR-ERD-PRO-Mini", "aSense2Release"), ("SNR-ERD-PRO-Mini", "uSenseAlarm"), ("SNR-ERD-PRO-Mini", "uSenseRelease"), ("SNR-ERD-PRO-Mini", "smart1ThermoOn"), ("SNR-ERD-PRO-Mini", "smart1ThermoOff"), ("SNR-ERD-PRO-Mini", "smart2ThermoOn"), ("SNR-ERD-PRO-Mini", "smart2ThermoOff"), ("SNR-ERD-PRO-Mini", "tempSensorAlarm"), ("SNR-ERD-PRO-Mini", "tempSensorRelease"), ("SNR-ERD-PRO-Mini", "voltSensorAlarm"), ("SNR-ERD-PRO-Mini", "voltSensorRelease"), ("SNR-ERD-PRO-Mini", "task1Done"), ("SNR-ERD-PRO-Mini", "task2Done"), ("SNR-ERD-PRO-Mini", "task3Done"), ("SNR-ERD-PRO-Mini", "task4Done"), ("SNR-ERD-PRO-Mini", "pingLost"), ("SNR-ERD-PRO-Mini", "batteryChargeLow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    erdProMiniTrapGroup = erdProMiniTrapGroup.setStatus('current')
if mibBuilder.loadTexts: erdProMiniTrapGroup.setDescription(' ')
mibBuilder.exportSymbols("SNR-ERD-PRO-Mini", alarmSensor2=alarmSensor2, task1Done=task1Done, voltageS5=voltageS5, voltageS10=voltageS10, erdProMiniTrapGroup=erdProMiniTrapGroup, smart1ThermoOff=smart1ThermoOff, temperatureS6=temperatureS6, currentS3=currentS3, alarmSensCnts=alarmSensCnts, serialS3=serialS3, smart2State=smart2State, uSenseAlarm=uSenseAlarm, currentS8=currentS8, uSensor=uSensor, snr_erd_pro_mini=snr_erd_pro_mini, voltageSensor=voltageSensor, currentS2=currentS2, aSense1Release=aSense1Release, temperatureS7=temperatureS7, alarmSensor1=alarmSensor1, smart2ThermoOn=smart2ThermoOn, task2Done=task2Done, voltageS6=voltageS6, task4Done=task4Done, currentS4=currentS4, aSense2Release=aSense2Release, smart1ResetTime=smart1ResetTime, serialS7=serialS7, options=options, serialS8=serialS8, snr=snr, snrSensors=snrSensors, smart2ResetTime=smart2ResetTime, smart2ThermoOff=smart2ThermoOff, temperatureS2=temperatureS2, temperatureS5=temperatureS5, tempSensorRelease=tempSensorRelease, counters=counters, voltageS7=voltageS7, voltSensorAlarm=voltSensorAlarm, aSense1Alarm=aSense1Alarm, serialS1=serialS1, currentS5=currentS5, currentS10=currentS10, erdproMiniTraps=erdproMiniTraps, alarmSensor1cnt=alarmSensor1cnt, smart1State=smart1State, uSenseRelease=uSenseRelease, management=management, measurements=measurements, voltageS3=voltageS3, voltageS8=voltageS8, alarmSensor2cnt=alarmSensor2cnt, voltSensorRelease=voltSensorRelease, dataType=dataType, serialS5=serialS5, voltageS2=voltageS2, PYSNMP_MODULE_ID=snr, serialS6=serialS6, aSense2Alarm=aSense2Alarm, sensesstate=sensesstate, tempSensorAlarm=tempSensorAlarm, currentS1=currentS1, temperatureS9=temperatureS9, voltageS9=voltageS9, snr_erd=snr_erd, temperatureS1=temperatureS1, task3Done=task3Done, pingLost=pingLost, serialS10=serialS10, serialS4=serialS4, temperatureS3=temperatureS3, smart1ThermoOn=smart1ThermoOn, powerSensors=powerSensors, serialS9=serialS9, serialS2=serialS2, currentS7=currentS7, batteryChargeLow=batteryChargeLow, temperatureS4=temperatureS4, currentS6=currentS6, temperatureSensors=temperatureSensors, voltageS4=voltageS4, temperatureS10=temperatureS10, voltageS1=voltageS1, currentS9=currentS9, temperatureS8=temperatureS8)
