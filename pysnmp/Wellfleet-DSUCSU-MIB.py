#
# PySNMP MIB module Wellfleet-DSUCSU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-DSUCSU-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:33:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, NotificationType, ModuleIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, Gauge32, NotificationType, MibIdentifier, ObjectIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "NotificationType", "ModuleIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "Gauge32", "NotificationType", "MibIdentifier", "ObjectIdentity", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfDsuCsuGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfDsuCsuGroup")
wfDsuCsuIfTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1), )
if mibBuilder.loadTexts: wfDsuCsuIfTable.setStatus('mandatory')
wfDsuCsuIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1), ).setIndexNames((0, "Wellfleet-DSUCSU-MIB", "wfDsuCsuIfSlot"), (0, "Wellfleet-DSUCSU-MIB", "wfDsuCsuIfConnector"))
if mibBuilder.loadTexts: wfDsuCsuIfEntry.setStatus('mandatory')
wfDsuCsuIfDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDsuCsuIfDelete.setStatus('mandatory')
wfDsuCsuIfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuIfSlot.setStatus('mandatory')
wfDsuCsuIfConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuIfConnector.setStatus('mandatory')
wfDsuCsuSoftRev = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuSoftRev.setStatus('mandatory')
wfDsuCsuHardRev = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuHardRev.setStatus('mandatory')
wfDsuCsuOpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dds156kbps", 1), ("cc64kbps", 2))).clone('dds156kbps')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDsuCsuOpMode.setStatus('mandatory')
wfDsuCsuTxClkSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("slave", 1), ("master", 2))).clone('slave')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDsuCsuTxClkSelect.setStatus('mandatory')
wfDsuCsuUnitReset = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetUnit", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDsuCsuUnitReset.setStatus('mandatory')
wfDsuCsu64KTxMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDsuCsu64KTxMonitor.setStatus('mandatory')
wfDsuCsuOpState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("normal", 1), ("localLpbk", 2), ("digitalLpbk", 3), ("remDigitalLpbk", 4), ("telcoLpbk", 5), ("remDigLpbkWPattern", 6), ("localAnlgLpbkWPattern", 7), ("pattern2047Gen", 8))).clone('normal')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuOpState.setStatus('mandatory')
wfDsuCsuServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5, 6))).clone(namedValues=NamedValues(("inService", 1), ("outOfService", 2), ("frameError", 3), ("lossOfLine", 5), ("telcoLpbk", 6))).clone('inService')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuServiceStatus.setStatus('mandatory')
wfDsuCsuV54Lpbk = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noLoop", 1), ("localAnlgLpbk", 2), ("localDigLpbk", 3), ("remDigLpbk", 4), ("remDigLpbkWPattern", 5), ("localAnlgLpbkWPattern", 6), ("pattern2047Gen", 7))).clone('noLoop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDsuCsuV54Lpbk.setStatus('mandatory')
wfDsuCsuV54Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDsuCsuV54Timer.setStatus('mandatory')
wfDsuCsuV54Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuV54Errors.setStatus('mandatory')
wfDsuCsuCqmsLaWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDsuCsuCqmsLaWindow.setStatus('mandatory')
wfDsuCsuCqmsLaErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuCqmsLaErrors.setStatus('mandatory')
wfDsuCsuCqmsLaPollRate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDsuCsuCqmsLaPollRate.setStatus('mandatory')
wfDsuCsuCqmsReset = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetCqms", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDsuCsuCqmsReset.setStatus('mandatory')
wfDsuCsuOOSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuOOSErrors.setStatus('mandatory')
wfDsuCsuFrameErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuFrameErrors.setStatus('mandatory')
wfDsuCsuLOLErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuLOLErrors.setStatus('mandatory')
wfDsuCsuInitState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("startup", 1), ("init", 2), ("monitor", 3), ("loopback", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDsuCsuInitState.setStatus('mandatory')
wfDsuCsuIfTrap = NotificationType((1, 3, 6, 1, 4, 1, 18, 3, 4, 30) + (0,1)).setObjects(("Wellfleet-DSUCSU-MIB", "wfDsuCsuServiceStatus"))
mibBuilder.exportSymbols("Wellfleet-DSUCSU-MIB", wfDsuCsuCqmsReset=wfDsuCsuCqmsReset, wfDsuCsuIfDelete=wfDsuCsuIfDelete, wfDsuCsuServiceStatus=wfDsuCsuServiceStatus, wfDsuCsuOpMode=wfDsuCsuOpMode, wfDsuCsuIfConnector=wfDsuCsuIfConnector, wfDsuCsuIfEntry=wfDsuCsuIfEntry, wfDsuCsuSoftRev=wfDsuCsuSoftRev, wfDsuCsuV54Timer=wfDsuCsuV54Timer, wfDsuCsuV54Lpbk=wfDsuCsuV54Lpbk, wfDsuCsuCqmsLaErrors=wfDsuCsuCqmsLaErrors, wfDsuCsuTxClkSelect=wfDsuCsuTxClkSelect, wfDsuCsuHardRev=wfDsuCsuHardRev, wfDsuCsuInitState=wfDsuCsuInitState, wfDsuCsuIfTable=wfDsuCsuIfTable, wfDsuCsuUnitReset=wfDsuCsuUnitReset, wfDsuCsuCqmsLaPollRate=wfDsuCsuCqmsLaPollRate, wfDsuCsuOpState=wfDsuCsuOpState, wfDsuCsuLOLErrors=wfDsuCsuLOLErrors, wfDsuCsuFrameErrors=wfDsuCsuFrameErrors, wfDsuCsuCqmsLaWindow=wfDsuCsuCqmsLaWindow, wfDsuCsuIfTrap=wfDsuCsuIfTrap, wfDsuCsuV54Errors=wfDsuCsuV54Errors, wfDsuCsu64KTxMonitor=wfDsuCsu64KTxMonitor, wfDsuCsuOOSErrors=wfDsuCsuOOSErrors, wfDsuCsuIfSlot=wfDsuCsuIfSlot)
