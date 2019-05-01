#
# PySNMP MIB module SM10-R2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SM10-R2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:07:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, Integer32, ObjectIdentity, MibIdentifier, IpAddress, NotificationType, TimeTicks, Unsigned32, enterprises, iso, Counter32, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Integer32", "ObjectIdentity", "MibIdentifier", "IpAddress", "NotificationType", "TimeTicks", "Unsigned32", "enterprises", "iso", "Counter32", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
engenio_information_technologies = MibIdentifier((1, 3, 6, 1, 4, 1, 1123)).setLabel("engenio-information-technologies")
wichita = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 1))
ftcollins = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 2))
cosprings = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 3))
austin = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 4))
tucson = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 5))
reston = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 6))
boulder = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 7))
sm10_R2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 4, 500)).setLabel("sm10-R2")
infoTable = MibTable((1, 3, 6, 1, 4, 1, 1123, 4, 500, 1), )
if mibBuilder.loadTexts: infoTable.setStatus('current')
if mibBuilder.loadTexts: infoTable.setDescription('Information for array traps.')
infoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1123, 4, 500, 1, 1), ).setIndexNames((0, "SM10-R2-MIB", "deviceHostIPType"))
if mibBuilder.loadTexts: infoEntry.setStatus('current')
if mibBuilder.loadTexts: infoEntry.setDescription('The data for array traps.')
deviceHostIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 4, 500, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHostIPType.setStatus('current')
if mibBuilder.loadTexts: deviceHostIPType.setDescription('Type of IP Address of the network-attached device or device host. 0 unknown, 1 ipv4, 2 ipv6')
deviceHostIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 4, 500, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHostIPAddr.setStatus('current')
if mibBuilder.loadTexts: deviceHostIPAddr.setDescription('IP Address of the network-attached device or device host.')
deviceHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 4, 500, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHostName.setStatus('current')
if mibBuilder.loadTexts: deviceHostName.setDescription('The user label for the host of the device being reported on.')
deviceUserLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 4, 500, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 29))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUserLabel.setStatus('current')
if mibBuilder.loadTexts: deviceUserLabel.setDescription('The user label for the device being reported on.')
deviceErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 4, 500, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceErrorCode.setStatus('current')
if mibBuilder.loadTexts: deviceErrorCode.setDescription('The error code as reported by the device or host.')
eventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 4, 500, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTime.setStatus('current')
if mibBuilder.loadTexts: eventTime.setDescription('The time at which the event happen on the device.')
trapDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 4, 500, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 69))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDescription.setStatus('current')
if mibBuilder.loadTexts: trapDescription.setDescription('A string to indicate the nature of the trap')
componentType = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 4, 500, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 59))).setMaxAccess("readonly")
if mibBuilder.loadTexts: componentType.setStatus('current')
if mibBuilder.loadTexts: componentType.setDescription('A string to identify the failing component type')
componentLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 4, 500, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readonly")
if mibBuilder.loadTexts: componentLocation.setStatus('current')
if mibBuilder.loadTexts: componentLocation.setDescription('A string to identify the location of the failing component')
storageArrayCritical = NotificationType((1, 3, 6, 1, 4, 1, 1123, 4, 500, 2)).setObjects(("SM10-R2-MIB", "deviceHostIPType"), ("SM10-R2-MIB", "deviceHostIPAddr"), ("SM10-R2-MIB", "deviceHostName"), ("SM10-R2-MIB", "deviceUserLabel"), ("SM10-R2-MIB", "deviceErrorCode"), ("SM10-R2-MIB", "eventTime"), ("SM10-R2-MIB", "trapDescription"), ("SM10-R2-MIB", "componentType"), ("SM10-R2-MIB", "componentLocation"))
if mibBuilder.loadTexts: storageArrayCritical.setStatus('current')
if mibBuilder.loadTexts: storageArrayCritical.setDescription('This trap indicates an event where user-interaction is required immediately. Some example events are component failures or critical errors.')
mibBuilder.exportSymbols("SM10-R2-MIB", tucson=tucson, eventTime=eventTime, deviceErrorCode=deviceErrorCode, deviceUserLabel=deviceUserLabel, sm10_R2=sm10_R2, deviceHostIPAddr=deviceHostIPAddr, reston=reston, storageArrayCritical=storageArrayCritical, infoEntry=infoEntry, austin=austin, deviceHostName=deviceHostName, cosprings=cosprings, engenio_information_technologies=engenio_information_technologies, trapDescription=trapDescription, infoTable=infoTable, ftcollins=ftcollins, componentType=componentType, wichita=wichita, boulder=boulder, componentLocation=componentLocation, deviceHostIPType=deviceHostIPType)
