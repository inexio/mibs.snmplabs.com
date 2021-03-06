#
# PySNMP MIB module NBS-FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBS-FAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:17:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NbsTcPartIndex, NbsTcStatusSimple, nbs = mibBuilder.importSymbols("NBS-MIB", "NbsTcPartIndex", "NbsTcStatusSimple", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Counter32, MibIdentifier, TimeTicks, Counter64, ObjectIdentity, iso, Unsigned32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Counter32", "MibIdentifier", "TimeTicks", "Counter64", "ObjectIdentity", "iso", "Unsigned32", "NotificationType", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsFanMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 226))
if mibBuilder.loadTexts: nbsFanMib.setLastUpdated('201306270000Z')
if mibBuilder.loadTexts: nbsFanMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsFanMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsFanMib.setDescription('For managing cooling systems')
nbsFanFanGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 226, 1))
if mibBuilder.loadTexts: nbsFanFanGrp.setStatus('current')
if mibBuilder.loadTexts: nbsFanFanGrp.setDescription('Fans in trays and power supplies')
nbsFanEventsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 226, 100))
if mibBuilder.loadTexts: nbsFanEventsGrp.setStatus('current')
if mibBuilder.loadTexts: nbsFanEventsGrp.setDescription('')
nbsFanEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 226, 100, 0))
if mibBuilder.loadTexts: nbsFanEvents.setStatus('current')
if mibBuilder.loadTexts: nbsFanEvents.setDescription('Event NOTIFICATIONS')
nbsFanFanTable = MibTable((1, 3, 6, 1, 4, 1, 629, 226, 1, 1), )
if mibBuilder.loadTexts: nbsFanFanTable.setStatus('current')
if mibBuilder.loadTexts: nbsFanFanTable.setDescription('Includes all fans in power supplies or fan trays')
nbsFanFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1), ).setIndexNames((0, "NBS-FAN-MIB", "nbsFanFanParentIfIndex"), (0, "NBS-FAN-MIB", "nbsFanFanParentPartIndex"), (0, "NBS-FAN-MIB", "nbsFanFanIndex"))
if mibBuilder.loadTexts: nbsFanFanEntry.setStatus('current')
if mibBuilder.loadTexts: nbsFanFanEntry.setDescription('A particular fan')
nbsFanFanParentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFanFanParentIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsFanFanParentIfIndex.setDescription('The ifIndex of the component where this fan is installed')
nbsFanFanParentPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 2), NbsTcPartIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFanFanParentPartIndex.setStatus('current')
if mibBuilder.loadTexts: nbsFanFanParentPartIndex.setDescription('The nbsPartHardPartIndex of the component where this fan is installed')
nbsFanFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFanFanIndex.setStatus('current')
if mibBuilder.loadTexts: nbsFanFanIndex.setDescription('The ordinal Id of this fan, unique within its parent part.')
nbsFanFanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFanFanDescription.setStatus('current')
if mibBuilder.loadTexts: nbsFanFanDescription.setDescription('The nbsPartHardDescription of this fan')
nbsFanFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 30), NbsTcStatusSimple()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFanFanStatus.setStatus('current')
if mibBuilder.loadTexts: nbsFanFanStatus.setDescription('The operational status of this fan')
nbsFanFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notSupported", 1), ("off", 2), ("low", 3), ("medium", 4), ("high", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFanFanSpeed.setStatus('current')
if mibBuilder.loadTexts: nbsFanFanSpeed.setDescription('The speed level of this fan')
nbsFanFanTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 226, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFanFanTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsFanFanTableSize.setDescription('The number of rows in nbsFanFanTable')
nbsFanTrapFanStatusBad = NotificationType((1, 3, 6, 1, 4, 1, 629, 226, 100, 0, 30)).setObjects(("NBS-FAN-MIB", "nbsFanFanParentIfIndex"), ("NBS-FAN-MIB", "nbsFanFanParentPartIndex"), ("NBS-FAN-MIB", "nbsFanFanIndex"), ("NBS-FAN-MIB", "nbsFanFanDescription"), ("NBS-FAN-MIB", "nbsFanFanStatus"))
if mibBuilder.loadTexts: nbsFanTrapFanStatusBad.setStatus('current')
if mibBuilder.loadTexts: nbsFanTrapFanStatusBad.setDescription("Sent when fan's nbsFanFanStatus changes to bad (2)")
nbsFanTrapFanStatusOk = NotificationType((1, 3, 6, 1, 4, 1, 629, 226, 100, 0, 31)).setObjects(("NBS-FAN-MIB", "nbsFanFanParentIfIndex"), ("NBS-FAN-MIB", "nbsFanFanParentPartIndex"), ("NBS-FAN-MIB", "nbsFanFanIndex"), ("NBS-FAN-MIB", "nbsFanFanDescription"), ("NBS-FAN-MIB", "nbsFanFanStatus"))
if mibBuilder.loadTexts: nbsFanTrapFanStatusOk.setStatus('current')
if mibBuilder.loadTexts: nbsFanTrapFanStatusOk.setDescription("Sent when fan's nbsFanFanStatus changes to good (3)")
nbsFanTrapFanSpeedChanged = NotificationType((1, 3, 6, 1, 4, 1, 629, 226, 100, 0, 40)).setObjects(("NBS-FAN-MIB", "nbsFanFanParentIfIndex"), ("NBS-FAN-MIB", "nbsFanFanParentPartIndex"), ("NBS-FAN-MIB", "nbsFanFanIndex"), ("NBS-FAN-MIB", "nbsFanFanDescription"), ("NBS-FAN-MIB", "nbsFanFanSpeed"))
if mibBuilder.loadTexts: nbsFanTrapFanSpeedChanged.setStatus('current')
if mibBuilder.loadTexts: nbsFanTrapFanSpeedChanged.setDescription("Sent when fan's nbsFanFanSpeed changes")
mibBuilder.exportSymbols("NBS-FAN-MIB", nbsFanFanSpeed=nbsFanFanSpeed, nbsFanMib=nbsFanMib, PYSNMP_MODULE_ID=nbsFanMib, nbsFanFanParentIfIndex=nbsFanFanParentIfIndex, nbsFanTrapFanStatusBad=nbsFanTrapFanStatusBad, nbsFanFanDescription=nbsFanFanDescription, nbsFanFanEntry=nbsFanFanEntry, nbsFanEvents=nbsFanEvents, nbsFanEventsGrp=nbsFanEventsGrp, nbsFanFanGrp=nbsFanFanGrp, nbsFanFanTable=nbsFanFanTable, nbsFanFanParentPartIndex=nbsFanFanParentPartIndex, nbsFanFanIndex=nbsFanFanIndex, nbsFanFanTableSize=nbsFanFanTableSize, nbsFanTrapFanSpeedChanged=nbsFanTrapFanSpeedChanged, nbsFanFanStatus=nbsFanFanStatus, nbsFanTrapFanStatusOk=nbsFanTrapFanStatusOk)
