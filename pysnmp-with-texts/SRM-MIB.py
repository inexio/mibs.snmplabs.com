#
# PySNMP MIB module SRM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SRM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
cardSpecific, = mibBuilder.importSymbols("BASIS-MIB", "cardSpecific")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, TimeTicks, Bits, Counter32, MibIdentifier, Gauge32, IpAddress, ObjectIdentity, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "TimeTicks", "Bits", "Counter32", "MibIdentifier", "Gauge32", "IpAddress", "ObjectIdentity", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
srm3T3CnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 10))
srmeCnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 22))
srm3T3CnfGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1), )
if mibBuilder.loadTexts: srm3T3CnfGrpTable.setStatus('mandatory')
if mibBuilder.loadTexts: srm3T3CnfGrpTable.setDescription('The SRM 3T3 configuration table, it is the distribution of a T3 line. ')
srm3T3CnfGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1), ).setIndexNames((0, "SRM-MIB", "srmT3LineNum"), (0, "SRM-MIB", "srmStartT1LineNum"))
if mibBuilder.loadTexts: srm3T3CnfGrpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: srm3T3CnfGrpEntry.setDescription('an entry in the T3 configuration table ')
srmT3LineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srmT3LineNum.setStatus('mandatory')
if mibBuilder.loadTexts: srmT3LineNum.setDescription('Select T3 line number. There is no default value for this object.')
srmStartT1LineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 28))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srmStartT1LineNum.setStatus('mandatory')
if mibBuilder.loadTexts: srmStartT1LineNum.setDescription('The start T1 number to be affected. There is no default value for this object.')
srmT1RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("delete", 2), ("modify", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmT1RowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: srmT1RowStatus.setDescription('a command is used to add, delete, or modify one or more DS1 mapping. Default value is delete.')
srmTargetSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmTargetSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: srmTargetSlotNum.setDescription(' specify the target slot number to be linked. There is no default value for this object. For MGX8850: SRM01 services slots 1 - 6 and 9 - 14, SRM02 services slots 17 - 22 and 25 - 30 For MGX8220: SYNTAX INTEGER (5 ..14) ')
srmTargetSlotLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmTargetSlotLineNum.setStatus('mandatory')
if mibBuilder.loadTexts: srmTargetSlotLineNum.setDescription('0 means not assigned. There is no default value for this object.')
srmeCnfGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1), )
if mibBuilder.loadTexts: srmeCnfGrpTable.setStatus('mandatory')
if mibBuilder.loadTexts: srmeCnfGrpTable.setDescription('The SRME configuration table for bulk distribution of SRME lines.')
srmeCnfGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1), ).setIndexNames((0, "SRM-MIB", "srmeLineNum"), (0, "SRM-MIB", "srmeStartVtNum"))
if mibBuilder.loadTexts: srmeCnfGrpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: srmeCnfGrpEntry.setDescription('an entry in the SRME Distribution configuration table')
srmeLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srmeLineNum.setStatus('mandatory')
if mibBuilder.loadTexts: srmeLineNum.setDescription('Select SRME line number. For OC3/STM1: SYNTAX INTEGER 1 There is no default value for this object.')
srmeStartVtNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 84))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srmeStartVtNum.setStatus('mandatory')
if mibBuilder.loadTexts: srmeStartVtNum.setDescription('The start T1 or E1 number (virtual tributary) to be affected. For OC3 with T1 tributaries: SYNTAX INTEGER (1 .. 84) For STM1 with E1 tributaries: SYNTAX INTEGER (1 .. 63) There is no default value for this object.')
srmeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("delete", 2), ("modify", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmeRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: srmeRowStatus.setDescription('Command used to add, delete, or modify one or more T1 or E1 mappings. Only the srmeVtFramingType object can be modified once the distribution link is added. To modify all other objects, user should first delete the link and add it again. Default value is modify.')
srmeTargetSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmeTargetSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: srmeTargetSlotNum.setDescription(' specify the target slot number to be linked. There is no default value for this object. For MGX8x50: SRM01 services slots 1 - 6 and 9 - 14, SRM02 services slots 17 - 22 and 25 - 30 For MGX8x30: service slots 3-6 and 10-13 ')
srmeTargetSlotLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmeTargetSlotLineNum.setStatus('mandatory')
if mibBuilder.loadTexts: srmeTargetSlotLineNum.setDescription("Specify the target slot's line to be linked. 0 means not assigned. There is no default value for this object.")
srmeVtFramingType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("sf", 2), ("esf", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmeVtFramingType.setStatus('mandatory')
if mibBuilder.loadTexts: srmeVtFramingType.setDescription("Specifies the Framing Type of the target slot line. This is applicable only if the target module is a T1 Service Module and byte sync mapping is used on SRME. Not applicable to E1 Service Modules. sf: Superframe or D4 esf: Extended Superframe. Default is 'esf' if SRME lines are configured for byte-synchronous mapping, Else, the default is notApplicable. ")
mibBuilder.exportSymbols("SRM-MIB", srmeCnfGrpEntry=srmeCnfGrpEntry, srmeRowStatus=srmeRowStatus, srmT3LineNum=srmT3LineNum, srmT1RowStatus=srmT1RowStatus, srmStartT1LineNum=srmStartT1LineNum, srm3T3CnfGrpEntry=srm3T3CnfGrpEntry, srmTargetSlotNum=srmTargetSlotNum, srmeStartVtNum=srmeStartVtNum, srmeTargetSlotNum=srmeTargetSlotNum, srmeCnfGrp=srmeCnfGrp, srm3T3CnfGrp=srm3T3CnfGrp, srmeLineNum=srmeLineNum, srm3T3CnfGrpTable=srm3T3CnfGrpTable, srmTargetSlotLineNum=srmTargetSlotLineNum, srmeTargetSlotLineNum=srmeTargetSlotLineNum, srmeVtFramingType=srmeVtFramingType, srmeCnfGrpTable=srmeCnfGrpTable)
