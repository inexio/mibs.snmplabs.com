#
# PySNMP MIB module VPIEVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VPIEVENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, Counter64, Unsigned32, TimeTicks, ObjectIdentity, IpAddress, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Bits, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Counter64", "Unsigned32", "TimeTicks", "ObjectIdentity", "IpAddress", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Bits", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
voiceprint, software = mibBuilder.importSymbols("VPI-MIB", "voiceprint", "software")
eventcenter = MibIdentifier((1, 3, 6, 1, 4, 1, 15191, 1, 1))
applicationId = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: applicationId.setStatus('mandatory')
if mibBuilder.loadTexts: applicationId.setDescription("This is the Application's Registered ID number.")
applicationName = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applicationName.setStatus('mandatory')
if mibBuilder.loadTexts: applicationName.setDescription("This is the Application's Registered Friendly Name.")
processName = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processName.setStatus('mandatory')
if mibBuilder.loadTexts: processName.setDescription("This is the Application's Registered Friendly Name for a SubProcess.")
logEventType = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logEventType.setStatus('mandatory')
if mibBuilder.loadTexts: logEventType.setDescription('This is the Application Specified Event Type for the Notification.')
logEventName = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logEventName.setStatus('mandatory')
if mibBuilder.loadTexts: logEventName.setDescription('This is the Application Specified Friendly Name for the Notification.')
logEventMessage = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: logEventMessage.setStatus('mandatory')
if mibBuilder.loadTexts: logEventMessage.setDescription('This is the Application Specified Message for the Notification.')
eventNotif = NotificationType((1, 3, 6, 1, 4, 1, 15191) + (0,0)).setObjects(("VPIEVENT-MIB", "applicationId"), ("VPIEVENT-MIB", "applicationName"), ("VPIEVENT-MIB", "processName"), ("VPIEVENT-MIB", "logEventType"), ("VPIEVENT-MIB", "logEventName"), ("VPIEVENT-MIB", "logEventMessage"))
if mibBuilder.loadTexts: eventNotif.setDescription('An Application Triggered Event Notification.')
mibBuilder.exportSymbols("VPIEVENT-MIB", logEventName=logEventName, processName=processName, logEventMessage=logEventMessage, applicationName=applicationName, logEventType=logEventType, eventcenter=eventcenter, applicationId=applicationId, eventNotif=eventNotif)
