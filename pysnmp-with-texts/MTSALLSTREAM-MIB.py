#
# PySNMP MIB module MTSALLSTREAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MTSALLSTREAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:15:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, MibIdentifier, NotificationType, Counter64, iso, ObjectIdentity, Integer32, Unsigned32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "NotificationType", "Counter64", "iso", "ObjectIdentity", "Integer32", "Unsigned32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "enterprises", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mtsallstream = ModuleIdentity((1, 3, 6, 1, 4, 1, 23398))
if mibBuilder.loadTexts: mtsallstream.setLastUpdated('200505240000Z')
if mibBuilder.loadTexts: mtsallstream.setOrganization('MTS Allstream')
if mibBuilder.loadTexts: mtsallstream.setContactInfo(' Bogdan Moldoveanu Postal: Allstream 5160 Orbitor Drive Mississauga, ON L4W 5H2 Phone: +1-905-361-2189 Email: bogdan.moldoveanu@allstream.com')
if mibBuilder.loadTexts: mtsallstream.setDescription('The MIB Module for Allstream service notifications.')
allstreamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 1))
allstreamMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 2))
allstreamCICEventEntities = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 1, 1))
cicEventID = MibScalar((1, 3, 6, 1, 4, 1, 23398, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicEventID.setStatus('current')
if mibBuilder.loadTexts: cicEventID.setDescription('Cisco Info Center Event ID known by database as Server Serial.')
cicNode = MibScalar((1, 3, 6, 1, 4, 1, 23398, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicNode.setStatus('current')
if mibBuilder.loadTexts: cicNode.setDescription('Cisco Info Center Originator Node represents the real source of the event.')
cicEventMessage = MibScalar((1, 3, 6, 1, 4, 1, 23398, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicEventMessage.setStatus('current')
if mibBuilder.loadTexts: cicEventMessage.setDescription("Cisco Info Center event's message.")
cicEventSeverity = MibScalar((1, 3, 6, 1, 4, 1, 23398, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicEventSeverity.setStatus('current')
if mibBuilder.loadTexts: cicEventSeverity.setDescription('Cisco Info Center assigns this event severity.')
cicEventTrapReason = MibScalar((1, 3, 6, 1, 4, 1, 23398, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicEventTrapReason.setStatus('current')
if mibBuilder.loadTexts: cicEventTrapReason.setDescription('Another extra information about the forwarded event.')
allstreamNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 1, 20))
allstreamForwardCICEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 23398, 1, 20, 1)).setObjects(("MTSALLSTREAM-MIB", "cicEventID"), ("MTSALLSTREAM-MIB", "cicNode"), ("MTSALLSTREAM-MIB", "cicEventMessage"), ("MTSALLSTREAM-MIB", "cicEventSeverity"), ("MTSALLSTREAM-MIB", "cicEventTrapReason"))
if mibBuilder.loadTexts: allstreamForwardCICEventTrap.setStatus('current')
if mibBuilder.loadTexts: allstreamForwardCICEventTrap.setDescription('This notification is used to forward Cisco Info Center events southbound to another Network Management System / Event Manager.')
allstreamCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 2, 1))
allstreamGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 2, 2))
allstreamBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 23398, 2, 1, 1)).setObjects(("MTSALLSTREAM-MIB", "allstreamNotificationsGroup"), ("MTSALLSTREAM-MIB", "allstreamObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    allstreamBasicCompliance = allstreamBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: allstreamBasicCompliance.setDescription('The compliance statement for mtsallstream entities which implement this MIB.')
allstreamNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 23398, 2, 2, 1)).setObjects(("MTSALLSTREAM-MIB", "allstreamForwardCICEventTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    allstreamNotificationsGroup = allstreamNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: allstreamNotificationsGroup.setDescription('Allstream notifications group.')
allstreamObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 23398, 2, 2, 2)).setObjects(("MTSALLSTREAM-MIB", "cicEventID"), ("MTSALLSTREAM-MIB", "cicNode"), ("MTSALLSTREAM-MIB", "cicEventMessage"), ("MTSALLSTREAM-MIB", "cicEventSeverity"), ("MTSALLSTREAM-MIB", "cicEventTrapReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    allstreamObjectGroup = allstreamObjectGroup.setStatus('current')
if mibBuilder.loadTexts: allstreamObjectGroup.setDescription('A collection of objects providing basic instrumentation and control of mtsallstream entities.')
mibBuilder.exportSymbols("MTSALLSTREAM-MIB", allstreamCICEventEntities=allstreamCICEventEntities, PYSNMP_MODULE_ID=mtsallstream, allstreamNotificationsGroup=allstreamNotificationsGroup, cicEventTrapReason=cicEventTrapReason, mtsallstream=mtsallstream, cicEventID=cicEventID, cicEventSeverity=cicEventSeverity, allstreamObjectGroup=allstreamObjectGroup, allstreamForwardCICEventTrap=allstreamForwardCICEventTrap, allstreamBasicCompliance=allstreamBasicCompliance, cicEventMessage=cicEventMessage, cicNode=cicNode, allstreamCompliances=allstreamCompliances, allstreamMIBConformance=allstreamMIBConformance, allstreamNotifications=allstreamNotifications, allstreamObjects=allstreamObjects, allstreamGroups=allstreamGroups)
