#
# PySNMP MIB module MSSSERVER8260-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSSSERVER8260-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:05:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
proElsSubSysEventMsg, = mibBuilder.importSymbols("PROTEON-MIB", "proElsSubSysEventMsg")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, enterprises, NotificationType, Gauge32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, iso, Integer32, Unsigned32, Bits, ModuleIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "enterprises", "NotificationType", "Gauge32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "iso", "Integer32", "Unsigned32", "Bits", "ModuleIdentity", "Counter32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
nwaysMSS = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118))
mssServer8260 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 3))
mss8260Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 1))
mss8260PCAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2))
mss8260ResetFlag = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noreset", 1), ("reboot", 2))).clone('noreset')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mss8260ResetFlag.setStatus('mandatory')
mss8260DRAMinstalled = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8260DRAMinstalled.setStatus('mandatory')
mss8260NotifyStatus = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mss8260NotifyStatus.setStatus('mandatory')
mss8260TempThresholdStatus = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("shutdown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8260TempThresholdStatus.setStatus('mandatory')
mss8260PCAdapNumSlot = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8260PCAdapNumSlot.setStatus('mandatory')
mss8260PCAdapTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2, 2), )
if mibBuilder.loadTexts: mss8260PCAdapTable.setStatus('mandatory')
mss8260PCAdapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2, 2, 1), ).setIndexNames((0, "MSSSERVER8260-MIB", "mss8260PCAdapSlotNum"))
if mibBuilder.loadTexts: mss8260PCAdapEntry.setStatus('mandatory')
mss8260PCAdapSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8260PCAdapSlotNum.setStatus('mandatory')
mss8260PCAdapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("harddrive", 2), ("modem", 3), ("notPresent", 4), ("flashcard", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8260PCAdapType.setStatus('mandatory')
mssServer8260ELSTrapV2 = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 3) + (0,2)).setObjects(("PROTEON-MIB", "proElsSubSysEventMsg"))
mss8260PCAdapTypeChg = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 3) + (0,3)).setObjects(("MSSSERVER8260-MIB", "mss8260PCAdapType"))
mss8260TempThresholdChg = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 3) + (0,4)).setObjects(("MSSSERVER8260-MIB", "mss8260TempThresholdStatus"))
mibBuilder.exportSymbols("MSSSERVER8260-MIB", ibm=ibm, mss8260PCAdapTypeChg=mss8260PCAdapTypeChg, mssServer8260=mssServer8260, ibmProd=ibmProd, mss8260DRAMinstalled=mss8260DRAMinstalled, mss8260NotifyStatus=mss8260NotifyStatus, mss8260TempThresholdChg=mss8260TempThresholdChg, mssServer8260ELSTrapV2=mssServer8260ELSTrapV2, nwaysMSS=nwaysMSS, mss8260ResetFlag=mss8260ResetFlag, mss8260PCAdapter=mss8260PCAdapter, mss8260PCAdapTable=mss8260PCAdapTable, mss8260PCAdapNumSlot=mss8260PCAdapNumSlot, mss8260PCAdapEntry=mss8260PCAdapEntry, mss8260PCAdapSlotNum=mss8260PCAdapSlotNum, mss8260PCAdapType=mss8260PCAdapType, mss8260TempThresholdStatus=mss8260TempThresholdStatus, mss8260Prod=mss8260Prod)
