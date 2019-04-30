#
# PySNMP MIB module PET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, ObjectIdentity, Bits, enterprises, Integer32, TimeTicks, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, iso, Counter64, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "ObjectIdentity", "Bits", "enterprises", "Integer32", "TimeTicks", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "iso", "Counter64", "ModuleIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wired_for_management = MibIdentifier((1, 3, 6, 1, 4, 1, 3183)).setLabel("wired-for-management")
pET = MibIdentifier((1, 3, 6, 1, 4, 1, 3183, 1))
pET_version_1 = MibIdentifier((1, 3, 6, 1, 4, 1, 3183, 1, 1)).setLabel("pET-version-1")
pETTrap = MibScalar((1, 3, 6, 1, 4, 1, 3183, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(110, 110)).setFixedLength(110)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pETTrap.setStatus('current')
pET_PresenceHeartbeat = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2584320)).setLabel("pET-PresenceHeartbeat")
pET_CoverTamper = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,356096)).setLabel("pET-CoverTamper")
pET_Voltage_Fan_Temperature = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552706)).setLabel("pET-Voltage-Fan-Temperature")
pET_LANLeash = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,356100)).setLabel("pET-LANLeash")
pET_Temperature = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,93952)).setLabel("pET-Temperature")
pET_ProcessorMissing = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,356099)).setLabel("pET-ProcessorMissing")
pET_ProcessorTemperature = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487169)).setLabel("pET-ProcessorTemperature")
pET_Watchdog = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1142534)).setLabel("pET-Watchdog")
pET_P_O_S_T = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1011456)).setLabel("pET-P-O-S-T")
pET_Voltage = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,159488)).setLabel("pET-Voltage")
pET_Fan = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,290560)).setLabel("pET-Fan")
pET_Fan_Temperature = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,683778)).setLabel("pET-Fan-Temperature")
pET_Undock = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,356101)).setLabel("pET-Undock")
pET_EventClear = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1076994)).setLabel("pET-EventClear")
pET_AlertOnLAN = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2277391)).setLabel("pET-AlertOnLAN")
mibBuilder.exportSymbols("PET-MIB", pET_Watchdog=pET_Watchdog, wired_for_management=wired_for_management, pET_Temperature=pET_Temperature, pET_P_O_S_T=pET_P_O_S_T, pET_ProcessorTemperature=pET_ProcessorTemperature, pET_EventClear=pET_EventClear, pET_Undock=pET_Undock, pET_Fan=pET_Fan, pETTrap=pETTrap, pET_Voltage=pET_Voltage, pET_Fan_Temperature=pET_Fan_Temperature, pET_CoverTamper=pET_CoverTamper, pET_Voltage_Fan_Temperature=pET_Voltage_Fan_Temperature, pET=pET, pET_LANLeash=pET_LANLeash, pET_AlertOnLAN=pET_AlertOnLAN, pET_ProcessorMissing=pET_ProcessorMissing, pET_version_1=pET_version_1, pET_PresenceHeartbeat=pET_PresenceHeartbeat)