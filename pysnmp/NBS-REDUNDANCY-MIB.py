#
# PySNMP MIB module NBS-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBS-REDUNDANCY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:07:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbsCmmcSlotIndex, nbsCmmcChassisIndex, nbsCmmcPortIndex = mibBuilder.importSymbols("NBS-CMMC-MIB", "nbsCmmcSlotIndex", "nbsCmmcChassisIndex", "nbsCmmcPortIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, Counter64, Bits, MibIdentifier, Gauge32, NotificationType, TimeTicks, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter64", "Bits", "MibIdentifier", "Gauge32", "NotificationType", "TimeTicks", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "ObjectIdentity")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
nbsRedundancyMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 221))
if mibBuilder.loadTexts: nbsRedundancyMib.setLastUpdated('201505010000Z')
if mibBuilder.loadTexts: nbsRedundancyMib.setOrganization('NBS')
nbsRedundCfgGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 221, 1))
if mibBuilder.loadTexts: nbsRedundCfgGrp.setStatus('current')
nbsRedundEventGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 221, 100))
if mibBuilder.loadTexts: nbsRedundEventGrp.setStatus('current')
nbsYcableTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 221, 100, 0))
if mibBuilder.loadTexts: nbsYcableTraps.setStatus('current')
nbsRedundCfgTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 221, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundCfgTableSize.setStatus('current')
nbsRedundCfgTable = MibTable((1, 3, 6, 1, 4, 1, 629, 221, 1, 2), )
if mibBuilder.loadTexts: nbsRedundCfgTable.setStatus('current')
nbsRedundCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1), ).setIndexNames((0, "NBS-REDUNDANCY-MIB", "nbsRedundCfgNdx"))
if mibBuilder.loadTexts: nbsRedundCfgEntry.setStatus('current')
nbsRedundCfgNdx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsRedundCfgNdx.setStatus('current')
nbsRedundCfgPartnerNdxAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgPartnerNdxAdmin.setStatus('current')
nbsRedundCfgPartnerNdxOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundCfgPartnerNdxOper.setStatus('current')
nbsRedundCfgStatusAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("standby", 2), ("active", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgStatusAdmin.setStatus('current')
nbsRedundCfgStatusOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("standby", 2), ("active", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundCfgStatusOper.setStatus('current')
nbsRedundCfgPreferredAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("preferNot", 2), ("preferActive", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgPreferredAdmin.setStatus('current')
nbsRedundCfgStandbyTxAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("standbyCold", 2), ("standbyHot", 3))).clone('standbyHot')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgStandbyTxAdmin.setStatus('current')
nbsRedundCfgStandbyTxToggle = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("txOff", 2), ("txToggle", 3))).clone('txOff')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgStandbyTxToggle.setStatus('current')
nbsRedundCfgIfTypeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("access", 2), ("trunk", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgIfTypeAdmin.setStatus('current')
nbsRedundCfgIfTypeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 51), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("access", 2), ("trunk", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundCfgIfTypeOper.setStatus('current')
nbsRedundCfgGroupNumberAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 60), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgGroupNumberAdmin.setStatus('current')
nbsRedundCfgGroupNumberOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 61), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundCfgGroupNumberOper.setStatus('current')
nbsRedundGroupCfgTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 221, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundGroupCfgTableSize.setStatus('current')
nbsRedundGroupCfgTable = MibTable((1, 3, 6, 1, 4, 1, 629, 221, 1, 4), )
if mibBuilder.loadTexts: nbsRedundGroupCfgTable.setStatus('current')
nbsRedundGroupCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1), ).setIndexNames((0, "NBS-REDUNDANCY-MIB", "nbsRedundGroupCfgNdx"), (0, "NBS-REDUNDANCY-MIB", "nbsRedundGroupCfgNumber"))
if mibBuilder.loadTexts: nbsRedundGroupCfgEntry.setStatus('current')
nbsRedundGroupCfgNdx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsRedundGroupCfgNdx.setStatus('current')
nbsRedundGroupCfgNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: nbsRedundGroupCfgNumber.setStatus('current')
nbsRedundGroupCfgOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundGroupCfgOper.setStatus('current')
nbsRedundGroupCfgModeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("modeA", 2), ("modeB", 3))).clone('modeB')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRedundGroupCfgModeAdmin.setStatus('current')
nbsRedundGroupCfgModeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("modeA", 2), ("modeB", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundGroupCfgModeOper.setStatus('current')
nbsRedundGroupCfgYcableAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("disabled", 2), ("enabled", 3))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRedundGroupCfgYcableAdmin.setStatus('current')
nbsRedundGroupCfgYcableOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundGroupCfgYcableOper.setStatus('current')
nbsRedundGroupCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 50), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRedundGroupCfgRowStatus.setStatus('current')
nbsYcableTrapsStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 629, 221, 100, 0, 10)).setObjects(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"), ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"), ("NBS-CMMC-MIB", "nbsCmmcPortIndex"), ("NBS-REDUNDANCY-MIB", "nbsRedundCfgStatusOper"))
if mibBuilder.loadTexts: nbsYcableTrapsStatusChanged.setStatus('current')
mibBuilder.exportSymbols("NBS-REDUNDANCY-MIB", nbsRedundCfgGroupNumberOper=nbsRedundCfgGroupNumberOper, nbsRedundGroupCfgYcableAdmin=nbsRedundGroupCfgYcableAdmin, nbsRedundCfgPartnerNdxAdmin=nbsRedundCfgPartnerNdxAdmin, nbsRedundCfgStatusOper=nbsRedundCfgStatusOper, nbsRedundEventGrp=nbsRedundEventGrp, nbsRedundCfgNdx=nbsRedundCfgNdx, nbsRedundGroupCfgModeAdmin=nbsRedundGroupCfgModeAdmin, nbsRedundGroupCfgYcableOper=nbsRedundGroupCfgYcableOper, nbsRedundGroupCfgTableSize=nbsRedundGroupCfgTableSize, nbsRedundGroupCfgRowStatus=nbsRedundGroupCfgRowStatus, nbsYcableTrapsStatusChanged=nbsYcableTrapsStatusChanged, nbsRedundCfgEntry=nbsRedundCfgEntry, nbsRedundCfgGrp=nbsRedundCfgGrp, nbsRedundGroupCfgEntry=nbsRedundGroupCfgEntry, nbsRedundGroupCfgNumber=nbsRedundGroupCfgNumber, nbsRedundCfgStandbyTxAdmin=nbsRedundCfgStandbyTxAdmin, nbsRedundGroupCfgTable=nbsRedundGroupCfgTable, nbsYcableTraps=nbsYcableTraps, nbsRedundGroupCfgOper=nbsRedundGroupCfgOper, nbsRedundGroupCfgModeOper=nbsRedundGroupCfgModeOper, nbsRedundCfgTable=nbsRedundCfgTable, nbsRedundCfgGroupNumberAdmin=nbsRedundCfgGroupNumberAdmin, nbsRedundCfgPartnerNdxOper=nbsRedundCfgPartnerNdxOper, nbsRedundCfgStatusAdmin=nbsRedundCfgStatusAdmin, nbsRedundGroupCfgNdx=nbsRedundGroupCfgNdx, nbsRedundCfgIfTypeOper=nbsRedundCfgIfTypeOper, nbsRedundancyMib=nbsRedundancyMib, nbsRedundCfgStandbyTxToggle=nbsRedundCfgStandbyTxToggle, nbsRedundCfgIfTypeAdmin=nbsRedundCfgIfTypeAdmin, nbsRedundCfgPreferredAdmin=nbsRedundCfgPreferredAdmin, PYSNMP_MODULE_ID=nbsRedundancyMib, nbsRedundCfgTableSize=nbsRedundCfgTableSize)