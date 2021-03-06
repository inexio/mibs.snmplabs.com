#
# PySNMP MIB module WATCHGUARD-SYSTEM-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WATCHGUARD-SYSTEM-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:36:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, ObjectIdentity, iso, TimeTicks, ModuleIdentity, Unsigned32, Counter64, IpAddress, Counter32, Gauge32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "ObjectIdentity", "iso", "TimeTicks", "ModuleIdentity", "Unsigned32", "Counter64", "IpAddress", "Counter32", "Gauge32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
watchguard, = mibBuilder.importSymbols("WATCHGUARD-MIB", "watchguard")
wgSystemConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097, 2))
wgSystemConfigMIB.setRevisions(('2007-01-25 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wgSystemConfigMIB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: wgSystemConfigMIB.setLastUpdated('200701251200Z')
if mibBuilder.loadTexts: wgSystemConfigMIB.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: wgSystemConfigMIB.setContactInfo(' Ella Yu WatchGuard Technologies, Inc. 1841 Zanker Road San Jose, CA 95112 USA 408-519-4888 ella.yu@watchguard.com ')
if mibBuilder.loadTexts: wgSystemConfigMIB.setDescription('The MIB module to describe WatchGuard Firebox system configuration.')
wgSysTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 2, 3))
if mibBuilder.loadTexts: wgSysTraps.setStatus('current')
if mibBuilder.loadTexts: wgSysTraps.setDescription('This is the base object for system wide traps in this entity.')
wgSysTrapObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 2, 4))
if mibBuilder.loadTexts: wgSysTrapObjects.setStatus('current')
if mibBuilder.loadTexts: wgSysTrapObjects.setDescription('This is the base object for objects which are used as part of traps.')
wgSysTrapControl = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 2, 5))
if mibBuilder.loadTexts: wgSysTrapControl.setStatus('current')
if mibBuilder.loadTexts: wgSysTrapControl.setDescription('This is the base object identifier for all objects which are trap control for the entity.')
wgAlarmId = MibScalar((1, 3, 6, 1, 4, 1, 3097, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgAlarmId.setStatus('current')
if mibBuilder.loadTexts: wgAlarmId.setDescription('The id of the alarm that generates a trap.')
wgAlarmLabel = MibScalar((1, 3, 6, 1, 4, 1, 3097, 2, 4, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgAlarmLabel.setStatus('current')
if mibBuilder.loadTexts: wgAlarmLabel.setDescription('The name of the alarm that generates a trap.')
wgAlarmTime = MibScalar((1, 3, 6, 1, 4, 1, 3097, 2, 4, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgAlarmTime.setStatus('current')
if mibBuilder.loadTexts: wgAlarmTime.setDescription('The date and time of the alarm that generates a trap.')
wgAlarmLevel = MibScalar((1, 3, 6, 1, 4, 1, 3097, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 3, 2, 1))).clone(namedValues=NamedValues(("normal", 4), ("warning", 3), ("error", 2), ("critical", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgAlarmLevel.setStatus('current')
if mibBuilder.loadTexts: wgAlarmLevel.setDescription('The level of an alarm generated.')
wgAlarmHostname = MibScalar((1, 3, 6, 1, 4, 1, 3097, 2, 4, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgAlarmHostname.setStatus('current')
if mibBuilder.loadTexts: wgAlarmHostname.setDescription('The host name of the system where alarm occurred')
wgAlarmMsg = MibScalar((1, 3, 6, 1, 4, 1, 3097, 2, 4, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgAlarmMsg.setStatus('current')
if mibBuilder.loadTexts: wgAlarmMsg.setDescription('The message describing the nature of this alarm.')
wgAlarmTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 3097, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgAlarmTrapEnable.setStatus('current')
if mibBuilder.loadTexts: wgAlarmTrapEnable.setDescription('Indicates whether wgAlarmTrap trap should be generated.')
wgSysTrapsPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 2, 3, 0))
if mibBuilder.loadTexts: wgSysTrapsPrefix.setStatus('current')
if mibBuilder.loadTexts: wgSysTrapsPrefix.setDescription('')
wgAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 3097, 2, 3, 0, 1)).setObjects(("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmId"), ("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmLabel"), ("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmTime"), ("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmLevel"), ("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmHostname"), ("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmMsg"))
if mibBuilder.loadTexts: wgAlarmTrap.setStatus('current')
if mibBuilder.loadTexts: wgAlarmTrap.setDescription('An alarm was raised by Monitoring Agent of this WatchGuard entity.')
wgSnmpStart = NotificationType((1, 3, 6, 1, 4, 1, 3097, 2, 3, 0, 2))
if mibBuilder.loadTexts: wgSnmpStart.setStatus('current')
if mibBuilder.loadTexts: wgSnmpStart.setDescription('This trap is sent when the snmp starts.')
wgSnmpShutdown = NotificationType((1, 3, 6, 1, 4, 1, 3097, 2, 3, 0, 3))
if mibBuilder.loadTexts: wgSnmpShutdown.setStatus('current')
if mibBuilder.loadTexts: wgSnmpShutdown.setDescription('This trap is sent when the snmp terminates.')
mibBuilder.exportSymbols("WATCHGUARD-SYSTEM-CONFIG-MIB", wgSnmpStart=wgSnmpStart, wgSysTrapObjects=wgSysTrapObjects, wgAlarmMsg=wgAlarmMsg, wgAlarmLevel=wgAlarmLevel, wgAlarmTrap=wgAlarmTrap, wgAlarmTrapEnable=wgAlarmTrapEnable, wgAlarmTime=wgAlarmTime, wgSysTrapsPrefix=wgSysTrapsPrefix, PYSNMP_MODULE_ID=wgSystemConfigMIB, wgSysTraps=wgSysTraps, wgAlarmLabel=wgAlarmLabel, wgAlarmHostname=wgAlarmHostname, wgSnmpShutdown=wgSnmpShutdown, wgSysTrapControl=wgSysTrapControl, wgAlarmId=wgAlarmId, wgSystemConfigMIB=wgSystemConfigMIB)
