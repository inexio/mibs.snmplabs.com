#
# PySNMP MIB module T7510-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/T7510-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:07:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, Counter64, MibIdentifier, NotificationType, Gauge32, IpAddress, enterprises, TimeTicks, Integer32, iso, ModuleIdentity, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Counter64", "MibIdentifier", "NotificationType", "Gauge32", "IpAddress", "enterprises", "TimeTicks", "Integer32", "iso", "ModuleIdentity", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

comet = MibIdentifier((1, 3, 6, 1, 4, 1, 22626))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1))
t7510 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2))
readings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1))
settings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2))
readingsint = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3))
settingsint = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5))
tables = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6))
temperature = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('mandatory')
humidity = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humidity.setStatus('mandatory')
computedValue = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: computedValue.setStatus('mandatory')
pressure = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pressure.setStatus('mandatory')
templow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: templow.setStatus('mandatory')
temphigh = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temphigh.setStatus('mandatory')
humiditylow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humiditylow.setStatus('mandatory')
humidityhigh = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humidityhigh.setStatus('mandatory')
cvlow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlow.setStatus('mandatory')
cvhigh = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvhigh.setStatus('mandatory')
temptime = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temptime.setStatus('mandatory')
humidityTime = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humidityTime.setStatus('mandatory')
cvTime = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvTime.setStatus('mandatory')
tempHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempHyst.setStatus('mandatory')
humidityHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humidityHyst.setStatus('mandatory')
cvHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHyst.setStatus('mandatory')
presslow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: presslow.setStatus('mandatory')
presshigh = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: presshigh.setStatus('mandatory')
presstime = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: presstime.setStatus('mandatory')
pressureHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pressureHyst.setStatus('mandatory')
temperaturei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperaturei.setStatus('mandatory')
humidityi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humidityi.setStatus('mandatory')
cvi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvi.setStatus('mandatory')
pressurei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pressurei.setStatus('mandatory')
templowi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: templowi.setStatus('mandatory')
temphighi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temphighi.setStatus('mandatory')
humiditylowi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humiditylowi.setStatus('mandatory')
humidityhighi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityhighi.setStatus('mandatory')
cvlowi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvlowi.setStatus('mandatory')
cvhighi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvhighi.setStatus('mandatory')
temptimei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temptimei.setStatus('mandatory')
humidityTimei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityTimei.setStatus('mandatory')
cvTimei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTimei.setStatus('mandatory')
tempHysti = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempHysti.setStatus('mandatory')
humidityHysti = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityHysti.setStatus('mandatory')
cvHysti = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvHysti.setStatus('mandatory')
presslowi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: presslowi.setStatus('mandatory')
presshighi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 11000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: presshighi.setStatus('mandatory')
presstimei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: presstimei.setStatus('mandatory')
pressHysti = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pressHysti.setStatus('mandatory')
messageString = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageString.setStatus('mandatory')
alarmTemperature = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmTemperature.setStatus('mandatory')
alarmhumidity = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmhumidity.setStatus('mandatory')
alarmCv = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmCv.setStatus('mandatory')
alarmPressure = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPressure.setStatus('mandatory')
historyTable = MibTable((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1), )
if mibBuilder.loadTexts: historyTable.setStatus('mandatory')
historyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1), ).setIndexNames((0, "T7510-MIB", "histtemperature"))
if mibBuilder.loadTexts: historyEntry.setStatus('optional')
histtemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histtemperature.setStatus('mandatory')
histhumidity = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histhumidity.setStatus('mandatory')
histcomputedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histcomputedValue.setStatus('mandatory')
histpressure = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histpressure.setStatus('mandatory')
mibBuilder.exportSymbols("T7510-MIB", products=products, temphigh=temphigh, humidityTimei=humidityTimei, presstimei=presstimei, presslow=presslow, presshighi=presshighi, cvHyst=cvHyst, histcomputedValue=histcomputedValue, pressHysti=pressHysti, cvlow=cvlow, temptime=temptime, presstime=presstime, cvTime=cvTime, humidityhigh=humidityhigh, cvlowi=cvlowi, humidityi=humidityi, pressurei=pressurei, alarmhumidity=alarmhumidity, humiditylow=humiditylow, cvhighi=cvhighi, alarmPressure=alarmPressure, presslowi=presslowi, cvhigh=cvhigh, humiditylowi=humiditylowi, templowi=templowi, humidityHysti=humidityHysti, humidityhighi=humidityhighi, histhumidity=histhumidity, templow=templow, computedValue=computedValue, tempHyst=tempHyst, humidityHyst=humidityHyst, humidity=humidity, cvHysti=cvHysti, histpressure=histpressure, settings=settings, DisplayString=DisplayString, humidityTime=humidityTime, temptimei=temptimei, alarmTemperature=alarmTemperature, historyTable=historyTable, temperature=temperature, cvTimei=cvTimei, tempHysti=tempHysti, pressure=pressure, traps=traps, readings=readings, tables=tables, cvi=cvi, alarmCv=alarmCv, t7510=t7510, historyEntry=historyEntry, presshigh=presshigh, pressureHyst=pressureHyst, comet=comet, settingsint=settingsint, readingsint=readingsint, temphighi=temphighi, messageString=messageString, temperaturei=temperaturei, histtemperature=histtemperature)